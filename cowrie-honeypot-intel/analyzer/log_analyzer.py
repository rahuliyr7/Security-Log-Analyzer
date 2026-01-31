""" 
Log Analyzer Script to analyze logs from my honeypot and future tools and services

Rahul Iyer 
New Jersey Institute of Technology
Program B.S. Information Technology Infromation and Network Security ...    **(Minor: Artificial Intelligence --> soon to be declared)**
"""

import json
import pandas as pd # type: ignore
from datetime import datetime


def parse_logs(log_file):
    """
    Parse through honeypot JSON logs line by line and extract login attempts (login attempts only for now) info and analyze.
    Returns a pandas dataframe with organized attack data.
    """
    #Empty list used to store login attempts. List chosen for efficient appending of new login_attempt(s).
    login_attempts = []

    #File open using "with" as opposed to f=open('','') since f = open requires closing, 
    #using "with" python automatically closes when done even when theres an error.
    #r read mode out of rwa (read write append).
    #(log_file) is the parameter or input to the function variable to hold filename that gets passed in as function is called.
    #f is our 'opened' file object a connection to the open file that lets you read from it so 
    #ex log_file is the title of the book and 'f' is the actual open book you can read from.
    with open(log_file, 'r') as f:

       
        #Loop through each line in f.
        for line in f:

             #Attempt to parse give line as JSON try used due to possibility of corrupted lines.
             #Convert JSON to text in Python dictionary.
            try:
                entry = json.loads(line)

                #Filter put in place so we only get login events, as honepot logs many different events.
                if entry.get('eventid') in ['cowrie.login.failed', 'cowrie.login.success']:
                
                    #Extract neccesary fields from given login attempt.
                    #Used .get() as opposed to [] to avoid missing file key error.
                    login_attempt = {
                        'time': entry.get('timestamp'),
                         'attacker_ip': entry.get('src_ip'),
                          'user_attempt': entry.get('username'),
                           'pass_attempt': entry.get('password'),
                           #True if login succesful false if failed in reference to ('login result').
                            'login_result': entry.get('eventid') == 'cowrie.login.success'
                    }
                    #Add attempt to login_attempts list.
                    login_attempts.append(login_attempt)

             #If line cannot be parsed as JSON skip line and continue.
             #This prevents on bad line from crashing the anaysis.
             #End of function returns Data frame of login_attempts with newly appended login_attempt.
            except json.JSONDecodeError:
                continue

    #Convert to DataFrame.
    df = pd.DataFrame(login_attempts)

    #Adding columns organized based on time for temporal analysis.
    if not df.empty and 'time' in df.columns:
            df['time'] = pd.to_datetime(df['time'])
            df['hour'] = df['time'].dt.hour
            df['day_of_week'] = df['time'].dt.day_name()
            df['date'] = df['time'].dt.date

    return df
     


def analyze_attempts(df):
    """
    Analyze login attempt data from honepoty and print a comprehensive report.

    Displays which usernames and passwords attackers attempt to use, 
    
    where said attacks are originating from, when they have occured, and identifies brute force patterns.
    """
    #Print header section with formatting.
    print("\n" + "="*60)

    print("Honeypot Attack Analysis")

    print("="*60)

    #Printing base statistics.
    #nunique() function used to make sure we gather different ips usernames and passwords no repeats.

    print("\n[Attack Summary]")

    #len(df) counts the total rows so total login attempts.
    print(f"Total # Login Attempts: {len(df)}")

    print(f"Different Attacker IP Addresses: {df['attacker_ip'].nunique()}")

    print(f"Different usernames attempted: {df['user_attempt'].nunique()}")

    print(f"Different passwords attempted: {df['pass_attempt'].nunique()}")
    #sum() counts True values in the login_result colimn 
    #True = 1 False = 0 so sum provides a count of succesful logins
    print(f"Succesful logins: {df['login_result'].sum()}")

    #Top 10 attempted usernames.
    #Tells us most targeted usernames.
    #Tells us what accounts attackers believe may exist.
    print("\n[Top 10 Usernames]")

    #value_counts() keeps a count of occurences for username in this case
    #head(10) provides only the 10 most common usernames in this case.
    #enumerate adds ranking numbers.
    for rank, (username , count) in enumerate(df['user_attempt'].value_counts().head(10).items(), 1):

        print(f"{rank}. '{username}' - {count} attempts")


    #Top 10 attempted passwords.
    #Shows us most commonn passwords attempted.
    print("\n[Top 10 Passwords]")

    for rank, (password , count) in enumerate(df['pass_attempt'].value_counts().head(10).items(), 1):

        print(f"{rank}. '{password}' - {count} attempts")


    #Top 10 attempt(s) source IP addresses.
    #Identifies most frequent attackers by IP address.
    #IPs with many attempts are likely brute force attempts.
    print("\n[Top 10  most frequent IP addresses]")

    #Counts attempts per IP and provides the top 10 IPs.
    for rank, (ip , count) in enumerate(df['attacker_ip'].value_counts().head(10).items(), 1):

        print(f"{rank}. '{ip}' - {count} attempts")


    #Displaying the timing.
    #Shows what hour attacks occured in of the day, and can help us see if attacks may be automated.
    if 'hour' in df.columns:
            print("\n[Attack Times]")

            #value_counts() counts attempts per hour.
            #sort_index() sorts by hour from 0 NOT BY COUNT.
            #This provides us with a hourly distribution in chornological order.
            for hour , count in df['hour'].value_counts().sort_index().items():
                #{hour:02d} formats the hour with 2 digits for example 08:00 rather than 8:00
                print(f"{hour:02d}:00 = {count} attempts")

    #Printing the closing statments
    print("\n" + "="*60)
    print("Analysis Complete.")
    print("="*60)


#Main Execution block
#This block only runs when the script is executed directly from python log_analyzer.py.
#This block doesnt run whe imported as a module in another script.
if __name__ == "__main__":

    #Printing program header.
    print ("="*60)

    print("Cowrie Honeypot Threat Intelligence Analyzer")

    print("="*60)

    #Parsing the log file.
    print("\nParsing JSON logs...")

    #Calls the parse_logs function to read the cowrie.json file.
    #Returns a pandas DataFrame with all the login attempts.
    df = parse_logs('cowrie.json')

    #Checking to see if any data was found.
    if df.empty:

        #If DataFrame is empty this tells us theres no login attempts in the file.
        print("No login attempts found in file at the moment ")

    else:
        #Else executing means we have data and lets proceed with analysis.
        #Show how many attempts were found using len(df) gives # of rows which is equivalent to # of login attempts.
        print(f"Found {len(df)} login attempts in file\n")

        #Run the comprehensive analysis.
        #Prints the detailed report to the screen.
        analyze_attempts(df)
            
        #Save the raw data to a CSV file.
        #index = False is in place so row numbers are excluded in the CSV.
        #This allows the data to be used in other tools such as Excel
        df.to_csv('attack_data.csv', index = False)

        #Confirming the file was saved.
        print(f"\nRaw data saved to: attack_data.csv")



  




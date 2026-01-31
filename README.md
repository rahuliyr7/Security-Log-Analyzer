# SSH Honeypot Threat Intelligence Platform

Rahul Iyer  
NJIT Information Technology Network and Infomration Security Student  
Expected Graduation: May 2027

## Overview

This project documents the setup of a Cowrie SSH honeypot on a Raspberry Pi 5 and a custom Python-based analyzer used to examine SSH login attempts. The goal is to understand how attackers attempt to access systems by analyzing usernames, passwords, source IPs, and timing patterns.

The project was created to gain hands-on experience with real-world attack behavior beyond classroom material.

## What I Built

- A Cowrie SSH honeypot configured to simulate a vulnerable SSH server
- A Python script to parse and analyze Cowrie JSON login logs
- A network configuration separating attacker access from administrative access

## System Setup

Hardware:
- Raspberry Pi 5

Honeypot Software:
- Cowrie 2.6.1

Custom Code:
- Python-based log analyzer using pandas

The honeypot records SSH authentication attempts including attempted usernames, passwords, source IP addresses, and timestamps. The configuration is designed to appear realistic rather than immediately blocking all login attempts.

## Network Configuration

- Administrative SSH access runs on port 22222
- Honeypot SSH service runs on port 2222
- External port 22 is forwarded to the honeypot SSH port

This setup ensures attackers interact only with the honeypot while legitimate administrative access remains separate.

## Authentication Method

- HoneyPotAuthRandom is used to randomly allow login after a number of failed attempts
- This approach makes the honeypot appear like a poorly secured real system

UserDB authentication was tested but resulted in SSH prompting only for a password instead of a username and password combination. This issue is still under investigation and may be related to Cowrie’s SSH handling.

## The Analyzer

The Python analyzer performs the following tasks:

- Reads Cowrie JSON logs line by line to handle large files efficiently
- Filters log entries to include only SSH login attempts
- Extracts timestamps, source IP addresses, usernames, and passwords
- Counts and summarizes repeated login attempts
- Performs basic temporal analysis by hour and day
- Exports parsed data to CSV for further inspection

Design choices focused on clarity, simplicity, and scalability.

## Sample Output

Cowrie Honeypot Threat Intelligence Analyzer  
Developed by Rahul Iyer

Attack Summary
- Total login attempts: 4
- Unique attacker IPs: 1
- Unique usernames attempted: 2
- Unique passwords attempted: 4
- Successful logins: 1

Top Usernames
- fakeuser3: 3 attempts
- fakeuser4: 1 attempt

Top Passwords
- attempt 1
- attempt 2
- attempt 3
- why

Top IP Address
- 192.168.1.163: 4 attempts

Attack Timing
- 12:00: 4 attempts

Sample output is based on sanitized test data. Real honeypot logs are intentionally excluded from this repository.

## Problems Solved

SSH Port Conflicts  
Running both the honeypot and administrative SSH on the same port caused conflicts. This was resolved by separating the services onto different ports.

File Permission Issues  
Cowrie initially could not write log files due to directory ownership. This was fixed by correcting file permissions.

Configuration Changes Not Applying  
Changes to the Cowrie configuration did not take effect until the service was restarted.

UserDB Authentication Issue  
SSH prompting behavior did not match expectations when using UserDB authentication. This issue is still being investigated.

## Running the Analyzer

cd analyzer  
pip install -r requirements.txt  
python log_analyzer_mine.py  

The script prints a summary report and saves parsed login data to a CSV file.

## What I Learned

- Attackers commonly attempt default accounts such as root and admin
- Password guessing follows predictable patterns
- Automated attacks can be identified by repeated and consistent timing patterns

## Repository Structure

analyzer/  
- log_analyzer_mine.py  
- requirements.txt  

docs/  
- Cowrie_Honeypot_Setup.pdf  

configs/  
- cowrie.cfg.local.example  

README.md

## Skills Used

- Linux system administration
- Python scripting and data analysis
- Basic networking concepts
- Honeypots and attack pattern analysis
- Troubleshooting and debugging

## Why This Project

This project was built to gain practical cybersecurity experience by working directly with attack data. Observing real login attempts provided insight into attacker behavior that cannot be learned through theory alone.

## Contact

Rahul Iyer  
rti@njit.edu  
New Jersey Institute of Technology – Information Technology Network and Infomration Security
Educational project deployed in an isolated environment for learning purposes only.

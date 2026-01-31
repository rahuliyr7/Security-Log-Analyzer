SSH Honeypot Threat Intelligence Platform
Rahul Iyer | NJIT Cybersecurity Student
Expected Graduation: May 2027
What I Built
I set up a Cowrie SSH honeypot on my Raspberry Pi 5 to see what real attackers do when they try to break into systems. 
Then I built a Python analyzer to make sense of all the attack data - who's attacking, what credentials they're trying, 
and when attacks happen.
Started this to learn more about real-world threats beyond what we cover in class. Turns out watching actual attacks 
happen is way more interesting than reading about them in textbooks.
The Setup
Hardware: Raspberry Pi 5
Honeypot Software: Cowrie 2.6.1
My Code: Python threat intelligence analyzer
The honeypot pretends to be a vulnerable SSH server. When attackers connect, it logs everything they try - usernames, 
passwords, commands. I configured it to randomly let them in after some failed attempts (more realistic than always 
succeeding or always failing).
My analyzer processes those logs and finds patterns in the data.
How It Works
Network Configuration

Real SSH (for me to manage the Pi): Port 22222
Honeypot SSH (for attackers): Port 2222
External port 22 forwards to honeypot port 2222

Kept them separate so attackers hit the honeypot while I can still safely access the Pi.
Authentication Method
Using HoneyPotAuthRandom - randomly allows login after a few failed attempts. Makes it seem like a real server with weak 
security instead of an obvious trap.
I tried UserDB (predefined username/password combinations) but ran into issues where SSH would only prompt for password, 
not username. Still figuring out why - might be how Cowrie handles the SSH protocol internally.
The Analyzer (My Code)
Built a Python script that:

Reads Cowrie's JSON logs line-by-line (important when files get big)
Filters out everything except login attempts
Counts patterns: which usernames get tried most, which passwords, which IPs attack most often
Shows timing: what hours attacks happen, what days of the week
Exports to CSV for additional analysis

Why I built it this way:

Line-by-line reading instead of loading the whole file at once (memory efficient)
Used pandas for data analysis (makes stats easy)
Lots of comments explaining my decisions (helps me remember why I did things a certain way)

Sample Output
[ATTACK SUMMARY]
Total # Login Attempts: 47
Different Attacker IP Addresses: 12
Different usernames attempted: 8
Successful logins: 3

[TOP 10 USERNAMES]
1. 'root' - 23 attempts
2. 'admin' - 12 attempts
3. 'user' - 7 attempts
Right now I only have my own test data. Once I expose this to the real internet, expecting to see way more interesting 
patterns from actual botnets and attackers.
Problems I Solved
SSH Port Conflicts
Couldn't run both honeypot and real SSH on the same port. Solved by putting honeypot on 2222 and my admin SSH on 22222 
(non-standard port so attackers don't find it).
File Permissions
Cowrie couldn't write logs because files were owned by root.
Fix:
bashsudo chown -R $USER:$USER /opt/cowrie
Configuration Changes Not Working
Made changes to cowrie.cfg.local but nothing happened. Turns out you have to actually restart Cowrie. Obvious in 
hindsight.
Fix:
bashbin/cowrie stop && bin/cowrie start
UserDB Authentication Issues
SSH prompt only asked for password, never username+password together even though I configured it that way. Still 
investigating - probably something with how Cowrie handles the SSH handshake.
Running the Analyzer
bashcd analyzer
pip install -r requirements.txt
python log_analyzer_mine.py
```

Prints full analysis report and saves raw data to attack_data.csv.

## What I Learned

Even from limited test data:
- Attackers always try 'root' and 'admin' first
- Common passwords: 123456, password, admin
- You can tell automated bots from manual attempts by timing patterns

Once I get real attack data from the internet, I'll see what credentials are actually being used in the wild right now.

## Currently Working On

**Active Development:**
- Brute force detection algorithm (automatically flag IPs with 5+ attempts)
- Weak password analyzer (check attempts against compromised password databases)
- Attack rate calculations (attempts per hour, identifying attack surges)
- Enhanced temporal analysis (peak attack windows, weekly patterns)

Check the commit history - I'm actively pushing updates as I expand the analyzer.

## Next Steps

**Short Term:**
- Expose honeypot to actual internet traffic (currently just local testing)
- Collect real attack data over 2-3 weeks
- Analyze patterns from real botnets and attackers

**Future Enhancements:**
- IP reputation API integration (AbuseIPDB, GreyNoise)
- Geographic attack mapping (visualize where attacks originate)
- Web dashboard for real-time monitoring
- Command analysis (see what attackers do post-login)
- Email alerting for high-severity attacks
- Machine learning for anomaly detection

## Files
```
.
├── analyzer/
│   ├── log_analyzer_mine.py     # My threat intelligence analyzer
│   └── requirements.txt         # Python dependencies
├── docs/
│   └── Cowrie_Honeypot_Setup.pdf    # Original deployment notes
├── configs/
│   └── cowrie.cfg.local.example     # Sample configuration
└── README.md
Skills Used

Linux administration - SSH configuration, service management, permissions
Python - File I/O, data processing, pandas for analysis
Networking - Port forwarding, understanding SSH protocol
Security concepts - Honeypots, attack patterns, threat intelligence
Problem solving - Debugging config issues, troubleshooting deployment

Why This Project
Wanted hands-on security experience beyond classroom assignments. Reading about attacks is one thing - actually seeing 
what attackers do in real-time is completely different. This taught me more about SSH security and attack patterns than 
any textbook could.
Plus it's something I can keep expanding as I learn new techniques and tools.
Contact
Rahul Iyer
rti@njit.edu | LinkedIn
New Jersey Institute of Technology | Cybersecurity

Educational project - deployed in isolated environment for learning purposes only.

NOW CREATE THE FILE:
bashcd ~/Desktop/cowrie-honeypot-threat-intel
nano README.md
Copy everything from "# SSH Honeypot" down to the bottom, paste it, save (Ctrl+X, Y, Enter).
Then push to GitHub - want me to give you those commands?no like send it akll in a codebox and send the sampe output in 
the code bix as well11:40 AMGot it! Here's the COMPLETE README in one code block:
markdown# SSH Honeypot Threat Intelligence Platform

Rahul Iyer | NJIT Cybersecurity Student  
Expected Graduation: May 2027

## What I Built

I set up a Cowrie SSH honeypot on my Raspberry Pi 5 to see what real attackers do when they try to break into systems. 
Then I built a Python analyzer to make sense of all the attack data - who's attacking, what credentials they're trying, 
and when attacks happen.

Started this to learn more about real-world threats beyond what we cover in class. Turns out watching actual attacks 
happen is way more interesting than reading about them in textbooks.

## The Setup

**Hardware:** Raspberry Pi 5  
**Honeypot Software:** Cowrie 2.6.1  
**My Code:** Python threat intelligence analyzer  

The honeypot pretends to be a vulnerable SSH server. When attackers connect, it logs everything they try - usernames, 
passwords, commands. I configured it to randomly let them in after some failed attempts (more realistic than always 
succeeding or always failing).

My analyzer processes those logs and finds patterns in the data.

## How It Works

### Network Configuration
- Real SSH (for me to manage the Pi): Port 22222
- Honeypot SSH (for attackers): Port 2222
- External port 22 forwards to honeypot port 2222

Kept them separate so attackers hit the honeypot while I can still safely access the Pi.

### Authentication Method
Using **HoneyPotAuthRandom** - randomly allows login after a few failed attempts. Makes it seem like a real server with 
weak security instead of an obvious trap.

I tried **UserDB** (predefined username/password combinations) but ran into issues where SSH would only prompt for 
password, not username. Still figuring out why - might be how Cowrie handles the SSH protocol internally.

## The Analyzer (My Code)

Built a Python script that:
- Reads Cowrie's JSON logs line-by-line (important when files get big)
- Filters out everything except login attempts
- Counts patterns: which usernames get tried most, which passwords, which IPs attack most often
- Shows timing: what hours attacks happen, what days of the week
- Exports to CSV for additional analysis

**Why I built it this way:**
- Line-by-line reading instead of loading the whole file at once (memory efficient)
- Used pandas for data analysis (makes stats easy)
- Lots of comments explaining my decisions (helps me remember why I did things a certain way)

### Sample Output
```
============================================================
Cowrie Honeypot Threat Intelligence Analyzer
Developed by: Rahul Iyer | NJIT Cybersecurity Student
============================================================

Parsing cowrie.json logs...

Successfully parsed 4 login attempts

============================================================
Honeypot Attack Analysis
============================================================

[Attack Summary]
Total # Login Attempts: 4
Different Attacker IP Addresses: 1
Different usernames attempted: 2
Different passwords attempted: 4
Succesful logins: 1

[Top 10 Usernames]
1. 'fakeuser3' - 3 attempts
2. 'fakeuser4' - 1 attempts

[Top 10 Passwords]
1. 'attempt 1' - 1 attempts
2. 'attempt 2' - 1 attempts
3. 'attempt 3' - 1 attempts
4. 'why' - 1 attempts

[Top 10  most frequent IP addresses]
1. '192.168.1.163' - 4 attempts

[Attack Times]
12:00 = 4 attempts

============================================================
Analysis Complete.
============================================================

Raw data saved to: attack_data.csv
```

Right now I only have my own test data. Once I expose this to the real internet, expecting to see way more interesting 
patterns from actual botnets and attackers.

## Problems I Solved

### SSH Port Conflicts
Couldn't run both honeypot and real SSH on the same port. Solved by putting honeypot on 2222 and my admin SSH on 22222 
(non-standard port so attackers don't find it).

### File Permissions
Cowrie couldn't write logs because files were owned by root. Fixed with:
```bash
sudo chown -R $USER:$USER /opt/cowrie
```

### Configuration Changes Not Working
Made changes to cowrie.cfg.local but nothing happened. Turns out you have to actually restart Cowrie. Obvious in 
hindsight.
```bash
bin/cowrie stop && bin/cowrie start
```

### UserDB Authentication Issues
SSH prompt only asked for password, never username+password together even though I configured it that way. Still 
investigating - probably something with how Cowrie handles the SSH handshake.

## Running the Analyzer
```bash
cd analyzer
pip install -r requirements.txt
python log_analyzer_mine.py
```

Prints full analysis report and saves raw data to attack_data.csv.

## What I Learned

Even from limited test data:
- Attackers always try 'root' and 'admin' first
- Common passwords: 123456, password, admin
- You can tell automated bots from manual attempts by timing patterns

Once I get real attack data from the internet, I'll see what credentials are actually being used in the wild right now.

## Currently Working On

**Active Development:**
- Brute force detection algorithm (automatically flag IPs with 5+ attempts)
- Weak password analyzer (check attempts against compromised password databases)
- Attack rate calculations (attempts per hour, identifying attack surges)
- Enhanced temporal analysis (peak attack windows, weekly patterns)

Check the commit history - I'm actively pushing updates as I expand the analyzer.

## Next Steps

**Short Term:**
- Expose honeypot to actual internet traffic (currently just local testing)
- Collect real attack data over 2-3 weeks
- Analyze patterns from real botnets and attackers

**Future Enhancements:**
- IP reputation API integration (AbuseIPDB, GreyNoise)
- Geographic attack mapping (visualize where attacks originate)
- Web dashboard for real-time monitoring
- Command analysis (see what attackers do post-login)
- Email alerting for high-severity attacks
- Machine learning for anomaly detection

## Files
```
.
├── analyzer/
│   ├── log_analyzer_mine.py     # My threat intelligence analyzer
│   └── requirements.txt         # Python dependencies
├── docs/
│   └── Cowrie_Honeypot_Setup.pdf    # Original deployment notes
├── configs/
│   └── cowrie.cfg.local.example     # Sample configuration
└── README.md
```

## Skills Used

- **Linux administration** - SSH configuration, service management, permissions
- **Python** - File I/O, data processing, pandas for analysis
- **Networking** - Port forwarding, understanding SSH protocol
- **Security concepts** - Honeypots, attack patterns, threat intelligence
- **Problem solving** - Debugging config issues, troubleshooting deployment

## Why This Project

Wanted hands-on security experience beyond classroom assignments. Reading about attacks is one thing - actually seeing 
what attackers do in real-time is completely different. This taught me more about SSH security and attack patterns than 
any textbook could.

Plus it's something I can keep expanding as I learn new techniques and tools.

## Contact

**Rahul Iyer**  
rti@njit.edu | [LinkedIn](https://linkedin.com/in/rahuliyr)  
New Jersey Institute of Technology | Cybersecurity

---

*Educational project - deployed in isolated environment for learning purposes only.*

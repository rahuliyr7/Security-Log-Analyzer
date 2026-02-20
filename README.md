# SSH Honeypot Threat Intelligence Platform
**Rahul Iyer** | NJIT Information Technology & Network Security | Expected Graduation: May 2027

## Overview
A Cowrie SSH honeypot deployed on a Raspberry Pi 5 to capture and analyze real-world SSH intrusion attempts. Built to go beyond classroom material and work with actual attack data.

## What I Built
- Cowrie SSH honeypot configured to simulate a vulnerable server and capture attacker behavior
- Python log analyzer to parse Cowrie JSON logs and surface patterns in credentials, IPs, and timing
- Isolated network setup separating honeypot traffic from administrative access

## Network Configuration
- Port 22 (external) → forwarded to honeypot on port 2222
- Administrative SSH runs on port 22222
- Configured with `HoneyPotAuthAlways` to accept all login attempts and capture post-auth commands

## The Analyzer
`analyzer/log_analyzer.py` parses Cowrie JSON logs and outputs:
- Top usernames and passwords attempted
- Most active attacker IPs
- Attack frequency by hour and day
- CSV export for further analysis

## Usage
```bash
cd analyzer
python log_analyzer.py
```

## What I Learned
Real attack traffic follows predictable patterns — default credentials dominate, and automated scanners reveal themselves through timing consistency. Seeing this firsthand made concepts like threat detection and log analysis click in a way textbooks don't.

## Repository Structure
- `analyzer/` — Python log analyzer
- `configs/` — Example Cowrie configuration
- `docs/` — Honeypot setup documentation

## Skills
Linux administration · Python · Network configuration · Honeypots · Log analysis · Threat intelligence

---
*Deployed in an isolated environment for educational purposes. Real honeypot logs are excluded from this repository.*

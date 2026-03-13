# JWT Token Attack Lab

## Overview

The JWT Token Attack Lab is a practical cybersecurity research project designed to demonstrate how misconfigured JSON Web Token (JWT) implementations can lead to severe authentication vulnerabilities.

This lab simulates both secure and insecure authentication systems, allowing controlled experimentation with token forgery, signature bypass techniques, and improper verification logic.

The project highlights how small mistakes in authentication design can result in full privilege escalation and unauthorized access.

It provides a realistic learning environment resembling modern web application security testing workflows.

## Objectives

This lab was developed to:
* Demonstrate real-world JWT authentication weaknesses
* Explore signature verification flaws
* Simulate privilege escalation through forged tokens
* Compare secure vs vulnerable authentication logic
* Build hands-on offensive and defensive security skills

The project bridges theoretical security knowledge with practical implementation.


## Key Features

* JWT token generation with user payload and expiration logic
* Configurable signature verification mechanism
* Demonstration of signature bypass vulnerability
* Forged token generation simulation
* Simple CLI authentication workflow
* Login and registration simulation with JSON storage
* Security event logging system
* Separation between secure and vulnerable configurations
* Modular project structure for experimentation


## Project Architecture

```
jwt-token-attack-lab/
│
├── access_secure.py          # Secure token verification logic
├── access_vulnerable.py      # Vulnerable verification implementation
├── config_secure.py          # Secure configuration
├── config_vulnerable.py      # Weak configuration scenario
├── login.py                  # User authentication workflow
├── register.py               # User registration simulation
├── forge_token.py            # Token forgery demonstration
├── database.py               # JSON-based user storage
├── logger.py                 # Security event logging
├── users.json                # Simulated user database
├── security_log.txt          # Recorded suspicious events
```


## How the Vulnerability Works

The lab demonstrates a scenario where:

* Signature verification may be disabled or improperly enforced
* Attackers can craft forged JWT tokens
* Tokens may be accepted without validating the signing algorithm
* Unauthorized access can occur due to flawed authentication logic

This reflects real application security risks such as:

* Algorithm confusion attacks
* “None” algorithm exploitation
* Improper secret handling
* Missing verification enforcement


## Example Workflow

### Register User
```
$ python register.py
Username: emma
Password: pass123
User registered successfully.
```

### Login and Generate Token
```
$ python login.py
Username: emma
Password: pass123

Token:
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

### Access Secure Endpoint
```
$ python access_secure.py --token <token>
Access granted. Welcome emma
```

### Forge Token (Attack Simulation)
```
$ python forge_token.py
Forged Token:
eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0...
```

### Access Vulnerable Endpoint
```
$ python access_vulnerable.py --token <forged_token>
Access granted. Welcome attacker
```

### Security Log Example
```
2026-03-04 20:13:38 — Invalid token attempt detected
```


## Security Concepts Demonstrated

This system showcases several important cybersecurity principles:

* Stateless authentication mechanisms
* Token-based identity management
* Signature verification enforcement
* Authentication bypass attack logic
* Secure configuration vs insecure configuration design
* Logging of suspicious authentication attempts

It reflects common vulnerabilities documented in modern security standards such as OWASP.

## Learning Outcomes

By completing this project, the following competencies are demonstrated:

* Practical application security testing
* Understanding of authentication attack vectors
* Secure system design comparison skills
* Defensive coding and configuration awareness
* Cybersecurity research methodology
* Modular Python security tool development

These skills are directly relevant to penetration testing, secure development, and security analysis roles.


## Responsible Usage Notice

This laboratory environment is intended strictly for:

* Educational experimentation
* Ethical security research
* Controlled vulnerability analysis

It must only be used in authorized environments and never against live systems without permission.

## Author

Developed as part of an applied cybersecurity learning initiative focused on authentication security, vulnerability analysis, and defensive engineering.

## License

This project is provided for educational and research purposes.
Users are responsible for ensuring ethical and lawful use.

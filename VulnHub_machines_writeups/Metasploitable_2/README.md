# Metasploitable 2 — Initial Enumeration & Privilege Escalation

## Objective

The goal of this lab was to perform reconnaissance, identify exposed services, gain initial access, enumerate the system, and escalate privileges to root on the Metasploitable 2 virtual machine.

---

### 1. Environment Setup

#### Attacker Machine
- Kali Linux VM
- VirtualBox
- Host-only Adapter

#### Target Machine
- Metasploitable 2
- Vulnerable Linux VM intentionally designed for security training

---

### 2. Network Discovery

#### Command
```bash
sudo netdiscover
```

#### Purpose

Used ARP-based discovery to identify active hosts on the local virtual network.

#### Key Learning
- ARP is used for IP-to-MAC resolution
- Helps identify live machines in LAN environments
- Useful during internal network reconnaissance

### 3. Target Identification
#### Command
```bash
ifconfig
```

#### Purpose

Identify IP address of the Metasploitable machine.

#### Observation
- Kali IP: 192.168.xx.xx
- Target IP: 192.168.xx.xx

### 4. Port Scanning

#### Basic Scan
```bash
nmap <target-ip>
```

#### Advanced Scan
```bash
nmap -sC -sV <target-ip>
```

#### Explanation
`-sC`

Runs default NSE (Nmap Scripting Engine) scripts.

`-sV`

Performs service version detection.

### 5. Open Services Identified
| Port | Service | Observation |
|------|---------|-------------|
| 21 | FTP | Anonymous login enabled |
| 23 |	Telnet |	Weak credentials accepted |
| 80 |	HTTP |	Web service exposed |
| 22 |	SSH	 | Remote administration |
| 3306 | MySQL |	Database service |

### 6. FTP Enumeration

#### Command
```bash
ftp <target-ip>
```

#### Credentials Used
```
Username: anonymous
Password: anonymous
```

#### Findings

- Anonymous authentication was enabled
- Misconfiguration allowed unauthorized access

#### Security Impact

Attackers may:

- access sensitive files
- upload malicious content
- gather internal information

### 7. Telnet Access

#### Command
```bash
telnet <target-ip>
```

#### Credentials Used
```
Username: msfadmin
Password: msfadmin
```

#### Key Learning

Telnet transmits credentials in plaintext and is considered insecure.

### 8. Enumeration After Access

#### Commands Used
```bash
whoami
uname -a
uname -r
id
history
sudo -l
```

### 9. Important Discovery

#### Command
```bash
sudo -l
```

#### Result
```
(ALL) ALL
```

#### Meaning

The msfadmin user was allowed to execute any command as root.

### 10. Privilege Escalation
#### Command
```bash
sudo su
```

#### Result

Obtained root shell access.

#### Verification
```bash
whoami
```

Output:
```
root
```

### 11. Key Security Weaknesses
- Weak/default credentials
- Telnet enabled
- Excessive sudo permissions
- Anonymous FTP access
- Outdated kernel version

### 12. Remediation Recommendations

#### Disable Telnet

Replace with SSH.

#### Enforce Strong Password Policy

Prevent default credential usage.

#### Restrict sudo Permissions

Apply principle of least privilege.

#### Disable Anonymous FTP

Require authenticated access only.

#### Patch System

Upgrade outdated Linux kernel and services.

### 13. Key Concepts Learned
- Reconnaissance
- Service Enumeration
- Authentication Weaknesses
- Linux Enumeration
- Privilege Escalation
- Security Misconfiguration
# 🧙 Fantasy CTF - Writeup
---
## 🧩 Challenge Overview
**The challenge description:**
> "Play this short game to get familiar with the terminal applications and some of the most important rules in scope for picoCTF."

After launching the challenge instance, a Netcat (`nc`) command was provided to connect to the remote service.
---

## 🔗 Connecting to the Challenge
The provided command was:
```bash
nc <host> <port>
```
After executing it, an interactive terminal-based game started.

## 🔍 Analysis
The challenge was not a traditional exploitation problem.
Instead, it focused on:
- Interacting with a remote CLI application
- Reading prompts carefully
- Selecting appropriate options
- Understanding picoCTF scope rules
The program presented multiple choices, and selecting the correct options allowed progression through the game.

Eventually, the correct sequence of decisions resulted in the flag being displayed.

## 🛠 Approach
- Launched the challenge instance.
- Connected using Netcat.
- Carefully read each prompt.
- Selected the logical options to progress.
- Retrieved the flag when the correct path was chosen.

## 🧠 Concepts Reinforced
- Basic terminal interaction
- Using Netcat (nc) to connect to remote services
- Reading and interpreting CLI prompts
- Understanding CTF scope and rules

## 🎯 Key Takeaway
This challenge reinforced foundational skills required for many CTF categories:
- Comfort with terminal-based applications
- Attention to detail when reading prompts
- Proper interaction with remote services
While simple, these skills are critical for more advanced challenges in reverse engineering, cryptography, and binary exploitation.
---
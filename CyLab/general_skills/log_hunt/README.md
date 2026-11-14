# Challenge: Log Analysis (picoCTF)

### 1. The Problem
A server log file (`server.log`) was leaking flag fragments across thousands of entries. The data was "noisy," meaning flag pieces were repeated many times and scattered amongst standard server warnings and errors. Manual extraction was inefficient due to the volume of redundant data.

### 2. The Solution
I used Linux CLI tools (`grep`, `sort`, `uniq`) to initially identify the unique fragments. To ensure accuracy, I developed a Python automation script that parses the log file, extracts fragments based on their timestamps, and reassembles them in chronological order. This eliminated the "noise" and provided the correct sequence: `picoCTF{us3_y0urlinux_skills_cedfa5fb}`.

### 3. The Lesson (SDE Perspective)
This challenge highlights the risk of **Verbose Logging** in production environments. Developers should implement log-level management (e.g., ensuring DEBUG or INFO levels don't leak sensitive variables). Additionally, this exercise demonstrates the power of **Stream Processing**—using scripts to transform unstructured log data into actionable information.
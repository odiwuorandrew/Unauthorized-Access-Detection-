# Unauthorized-Access-Detection-
Unauthorized Access Detection Script 🚨

## 📌 Overview
This Python script **monitors failed login attempts** in real time, alerting users of **unauthorized access** attempts on a Windows system using **Event Viewer logs**.

## 🛠 Features
🔥**Live monitoring** – Refreshes automatically every **30 seconds**.
🔥**Uses WMI (Windows Management Instrumentation)** for event logs.
🔥**Shows last 5 unauthorized login attempts**.
🔥**Simple & lightweight** – Works without extra dependencies!

## 🚀 Requirements
- Windows OS
- Python 3+
- Administrator privileges(to access security logs)

## 🔧 Installation & Setup
💫 Install Python from [Python’s official website](https://www.python.org/downloads/).
💫Install WMI module:
     bash
     pip install wmi
   
  💫Run the script:
     bash
     python detect_unauthorized_access.py
   

🎯 Usage
🔹 The script automatically checks for failed login attempts every 30 seconds.
🔹 If suspicious activity is found, it displays the last 5 unauthorized access attempts.
🔹 To stop monitoring, simply *press CTRL+C* in the terminal.

*📌 Example Output*
```
🔍 Live Monitoring for Unauthorized Access... (2025-06-05 10:30:00)
🚨 Unauthorized Access Attempts Detected! 🚨
[2025-06-05 10:29:45] Failed Login Attempt: User=Admin
[2025-06-05 10:28:12] Failed Login Attempt: User=Guest
[2025-06-05 10:27:34] Failed Login Attempt: User=Unknown
🔄 Waiting for new login attempts... (Refreshing in 30 sec)
```

*⚠️⚠️ Disclaimer⚠️⚠️*
🚨 *This script is for educational and security purposes only!* 🚨
Please ensure you have *proper authorization* before monitoring system logs.

*🛠 Future Improvements*
✔ *Log unauthorized attempts in a database*.
✔ *Send email alerts for repeated failed logins*.
✔ *Enhance filtering with specific user targets*.

*📌 Contributions*
Want to *improve the script*? Feel free to submit a *pull request* or raise issues on GitHub!

---
©2025 by:Odiwuor| https://github.com/odiwuorandrew

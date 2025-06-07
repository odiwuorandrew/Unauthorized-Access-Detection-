import win32evtlog
import datetime
import time

Configurable settings
LOG_TYPE = 'Security'
EVENT_ID = 4625  # Failed logon
THRESHOLD = 5  # Max failed attempts before alert
TIME_WINDOW = 300  # Look back this many seconds (5 minutes)
CHECK_INTERVAL = 15  # Check every 15 seconds
LOG_FILE = 'unauthorized_access_log.txt'

def get_failed_logins():
    server = 'localhost'
    log_type = LOG_TYPE
    hand = win32evtlog.OpenEventLog(server, log_type)
    flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
    now = datetime.datetime.now()
    events = []

    try:
        while True:
            records = win32evtlog.ReadEventLog(hand, flags, 0)
            if not records:
                break
            for event in records:
                if event.EventID == EVENT_ID:
                    event_time = event.TimeGenerated
[07/06, 13:13] ChatGPT: if (now - event_time).total_seconds() <= TIME_WINDOW:
                        events.append(event)
            break  # Check only most recent batch
    except Exception as e:
        print(f"[!] Error reading event log: {e}")
    return events

def log_alert(events):
    with open(LOG_FILE, 'a') as f:
        f.write(f"\n[{datetime.datetime.now()}] ALERT: {len(events)} failed login attempts detected.\n")
        for event in events:
            f.write(f"Time: {event.TimeGenerated}, Source: {event.SourceName}, Event ID: {event.EventID}\n")

def monitor():
    print("[*] Unauthorized Access Monitor started.")
    while True:
        failed_logins = get_failed_logins()
        if len(failed_logins) >= THRESHOLD:
            print(f"[!] ALERT: {len(failed_logins)} failed login attempts detected!")
            log_alert(failed_logins)
        time.sleep(CHECK_INTERVAL)

if _name_ == "_main_":
    monitor()

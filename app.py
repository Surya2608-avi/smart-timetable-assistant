import streamlit as st
from datetime import datetime, date
import sqlite3
from calendar_service import get_calendar_service
from datetime import datetime, timedelta

st.set_page_config(page_title="Smart Timetable Assistant", layout="centered")

st.title("Smart Timetable Assistant")
st.write("Manage your schedule with conflict detection and free slot finder.")

service = get_calendar_service()

conn = sqlite3.connect("tasks.db", check_same_thread=False)
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS tasks
             (name TEXT, deadline TEXT, priority TEXT)''')

# ---------------- SHOW EVENTS ----------------

st.markdown("---")
st.subheader(" Upcoming Events")

if st.button("Show Upcoming Events"):
    events_result = service.events().list(
        calendarId='primary',
        maxResults=10,
        singleEvents=True,
        orderBy='startTime'
    ).execute()

    events = events_result.get('items', [])

    if not events:
        st.write("No upcoming events found.")
    else:
        for event in events:
            st.write("•", event['summary'])
st.markdown("---")
st.subheader("🔔 Reminders")

c.execute("SELECT * FROM tasks")
tasks = c.fetchall()

today = date.today()

for t in tasks:
    task_name = t[0]
    deadline = datetime.strptime(t[1], "%Y-%m-%d").date()

    days_left = (deadline - today).days

    if days_left == 0:
        st.error(f"🚨 Reminder: {task_name} is due TODAY!")
    elif days_left == 1:
        st.warning(f"⚠️ Reminder: {task_name} is due TOMORROW!")

# ---------------- CONFLICT FUNCTION ----------------

def check_conflict(service, start, end):
    events_result = service.events().list(
        calendarId='primary',
        timeMin=start,
        timeMax=end,
        singleEvents=True
    ).execute()

    events = events_result.get('items', [])
    return len(events) > 0

# ---------------- ADD EVENT ----------------

st.markdown("---")
st.subheader("Add New Event")

title = st.text_input("Event Title")
date = st.date_input("Date")
start_time = st.time_input("Start Time")
end_time = st.time_input("End Time")

if st.button("Show Tasks", key="show_tasks_btn"):
    c.execute("SELECT * FROM tasks")
    tasks = c.fetchall()

    if not tasks:
        st.write("No tasks found.")
    else:
        today = date.today()

        for t in tasks:
            task_name = t[0]
            deadline_str = t[1]
            priority = t[2]

            deadline_date = datetime.strptime(deadline_str, "%Y-%m-%d").date()
            days_left = (deadline_date - today).days

            if days_left <= 2:
                st.error(f"⚠️ {task_name} | Due: {deadline_str} | URGENT!")

                # 👇 NEW: Study Suggestion
                st.info(f"📖 Suggestion: Study '{task_name}' today!")

            elif days_left <= 5:
                st.warning(f"⏳ {task_name} | Due: {deadline_str} | Moderate")

                st.info(f"📖 Suggestion: Plan study for '{task_name}' soon.")

            else:
                st.success(f"✅ {task_name} | Due: {deadline_str} | Safe")
# ---------------- FREE SLOT FINDER ----------------

st.markdown("---")
st.subheader(" Find Free Slots")

free_date = st.date_input("Select Date", key="free_date")

if st.button("Find Free Time"):

    start_of_day = datetime.combine(free_date, datetime.strptime("08:00", "%H:%M").time())
    end_of_day = datetime.combine(free_date, datetime.strptime("22:00", "%H:%M").time())

    start_iso = start_of_day.isoformat() + "+05:30"
    end_iso = end_of_day.isoformat() + "+05:30"

    events_result = service.events().list(
        calendarId='primary',
        timeMin=start_iso,
        timeMax=end_iso,
        singleEvents=True,
        orderBy='startTime'
    ).execute()

    events = events_result.get('items', [])

    busy = []

    for event in events:
        if 'dateTime' in event['start']:
            s = datetime.fromisoformat(event['start']['dateTime'].replace("Z", "+00:00"))
            e = datetime.fromisoformat(event['end']['dateTime'].replace("Z", "+00:00"))
            busy.append((s, e))

    busy.sort()

    current = start_of_day
    free_slots = []

    for s, e in busy:
        if current < s:
            free_slots.append((current, s))
        current = max(current, e)

    if current < end_of_day:
        free_slots.append((current, end_of_day))

    if not free_slots:
        st.write("No free slots available.")
    else:
        for s, e in free_slots:
            st.write(f"Free from {s.time()} to {e.time()}")
st.markdown("---")
st.subheader("📚 Assignment Tracker")

task_name = st.text_input("Task Name", key="task_name")
deadline = st.date_input("Deadline", key="task_deadline")
priority = st.selectbox("Priority", ["High", "Medium", "Low"])

if st.button("Add Task"):
    if not task_name:
        st.error("Enter task name")
    else:
        c.execute("INSERT INTO tasks VALUES (?, ?, ?)",
                  (task_name, str(deadline), priority))
        conn.commit()
        st.success("Task added successfully!")
if st.button("Show Tasks", key="btn2"):
    c.execute("SELECT * FROM tasks")
    tasks = c.fetchall()

    if not tasks:
        st.write("No tasks found.")
    else:
        for t in tasks:
            st.write(f"📌 {t[0]} | Due: {t[1]} | Priority: {t[2]}")
import re
from datetime import timedelta

st.markdown("---")
st.subheader("🤖 AI Scheduler")

user_input = st.text_input("Enter your request", key="ai_input")

if st.button("Run AI Scheduler", key="ai_btn"):

    if not user_input:
        st.error("Enter a request")
        st.stop()

    text = user_input.lower()

    # Extract title
    if "schedule" in text:
        title = text.replace("schedule", "").split("tomorrow")[0].strip()
    else:
        title = "Event"

    # Date
    if "tomorrow" in text:
        event_date = datetime.today().date() + timedelta(days=1)
    else:
        st.error("Use 'tomorrow' in request")
        st.stop()

    # Time extraction
    pattern = r'(\d{1,2})\s*pm\s*to\s*(\d{1,2})\s*pm'
    match = re.search(pattern, text)

    if not match:
        st.error("Use format like '4pm to 6pm'")
        st.stop()

    start_hour = int(match.group(1)) + 12
    end_hour = int(match.group(2)) + 12

    start_time = datetime.strptime(f"{start_hour}:00", "%H:%M").time()
    end_time = datetime.strptime(f"{end_hour}:00", "%H:%M").time()

    start_dt = datetime.combine(event_date, start_time).isoformat() + "+05:30"
    end_dt = datetime.combine(event_date, end_time).isoformat() + "+05:30"

    conflict = check_conflict(service, start_dt, end_dt)

    if conflict:
        st.error("⚠️ Conflict detected!")
    else:
        event = {
            'summary': title,
            'start': {'dateTime': start_dt, 'timeZone': 'Asia/Kolkata'},
            'end': {'dateTime': end_dt, 'timeZone': 'Asia/Kolkata'},
        }

        service.events().insert(calendarId='primary', body=event).execute()
        st.success("✅ Event scheduled!")
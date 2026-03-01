import streamlit as st
from calendar_service import get_calendar_service
from datetime import datetime, timedelta

st.set_page_config(page_title="Smart Timetable Assistant", layout="centered")

st.title("📅 Smart Timetable Assistant")
st.write("Manage your schedule with conflict detection and free slot finder.")

service = get_calendar_service()

# ---------------- SHOW EVENTS ----------------

st.markdown("---")
st.subheader("📌 Upcoming Events")

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
st.subheader("➕ Add New Event")

title = st.text_input("Event Title")
date = st.date_input("Date")
start_time = st.time_input("Start Time")
end_time = st.time_input("End Time")

if st.button("Create Event"):

    if not title:
        st.error("Please enter event title.")
        st.stop()

    if start_time >= end_time:
        st.error("End time must be after start time.")
        st.stop()

    start_datetime = datetime.combine(date, start_time).isoformat() + "+05:30"
    end_datetime = datetime.combine(date, end_time).isoformat() + "+05:30"

    conflict = check_conflict(service, start_datetime, end_datetime)

    if conflict:
        st.error("❌ Time conflict detected!")
    else:
        event = {
            'summary': title,
            'start': {
                'dateTime': start_datetime,
                'timeZone': 'Asia/Kolkata',
            },
            'end': {
                'dateTime': end_datetime,
                'timeZone': 'Asia/Kolkata',
            },
        }

        service.events().insert(calendarId='primary', body=event).execute()
        st.success("✅ Event created successfully!")

# ---------------- FREE SLOT FINDER ----------------

st.markdown("---")
st.subheader("🧠 Find Free Slots")

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
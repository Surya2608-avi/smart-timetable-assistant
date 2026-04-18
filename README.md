# Smart Timetable Assistant

## 📌 Project Overview

Smart Timetable Assistant is a conversational scheduling and academic planning system built using Python, Streamlit, SQLite, and Google Calendar API.

The application helps users manage daily schedules efficiently by supporting event creation, conflict detection, free slot finding, assignment tracking, reminders, and intelligent study planning. It acts as a personal academic assistant by improving productivity and time management.

---

## 🚀 Features

### 📅 Calendar Management

* View upcoming Google Calendar events
* Create new events directly from the app
* Detect scheduling conflicts for overlapping events
* Find free time slots for better planning

### 🤖 Natural Language Scheduling

* Schedule events using simple text commands
* Example: `schedule dsa study tomorrow 4pm to 6pm`

### 📚 Assignment Tracker

* Add assignments with deadlines and priorities
* Track urgent, moderate, and safe tasks
* Deadline-based study suggestions

### 🔔 Reminder System

* Automatic reminders for upcoming deadlines
* Alerts for tasks due today or tomorrow

### 📖 Smart Study Planner

* Intelligent study session scheduling
* Subject-wise time allocation
* Break and rest optimization
* Weekly study plan generation
* Progress tracking with smart recommendations

---

## 🛠️ Technologies Used

* Python
* Streamlit
* SQLite
* Google Calendar API
* Google OAuth Authentication
* Git & GitHub

---

## 📂 Project Structure

smart-timetable-assistant/
│
├── app.py
├── calendar_service.py
├── requirements.txt
├── README.md
├── .gitignore
├── tasks.db
├── token.json (local only)
├── credentials.json (local only)
└── venv/

---

## ⚙️ Installation & Setup

### Step 1: Clone Repository

```bash
git clone https://github.com/Surya2608-avi/smart-timetable-assistant.git
cd smart-timetable-assistant
```

### Step 2: Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Add Google Calendar Credentials

Download `credentials.json` from Google Cloud Console and place it inside the project folder.

### Step 5: Run the Application

```bash
streamlit run app.py
```



## 🔗 GitHub Repository

Repository Link:
https://github.com/Surya2608-avi/smart-timetable-assistant

---

## 🎯 Final Outcome

This project successfully transforms a basic scheduling system into a smart academic planner capable of managing events, tracking assignments, and generating intelligent study plans.

It demonstrates practical use of APIs, databases, automation, and conversational scheduling in a real-world productivity application.

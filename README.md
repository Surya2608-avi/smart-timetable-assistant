# Smart Timetable Assistant

## 📌 Project Overview

Smart Timetable Assistant is a production-ready academic scheduling and study planning application built using Python, Streamlit, SQLite, and Google Calendar API.

The system helps students manage academic schedules efficiently by combining calendar management, assignment tracking, intelligent study planning, and progress monitoring into a single platform. It supports event scheduling, conflict detection, free slot finding, deadline reminders, study plan generation, and subject-wise planning.

This project transforms a simple timetable system into a smart academic assistant for productivity and time management.

---

## 🚀 Core Features

---

## 📅 Calendar Management

### Google Calendar Integration

* Connects securely using Google OAuth Authentication
* Fetches upcoming events from Google Calendar
* Real-time event synchronization

### Event Scheduling

* Create new academic and personal events
* Automatic validation for title, date, and time

### Conflict Detection

* Detects overlapping events before scheduling
* Suggests alternate time slots for conflict resolution

### Free Slot Finder

* Finds available time slots for efficient planning

---

## 📚 Assignment Tracker

* Add assignments with deadlines and priority levels
* Deadline-based urgency detection:

  * Urgent
  * Moderate
  * Safe
* Assignment deadline notifications
* Smart reminders for tasks due today or tomorrow

---

## 🤖 Smart Study Planner

### Intelligent Study Session Scheduling

* Automatically recommends study sessions based on deadlines

### Subject-wise Time Allocation

* Allocate study hours for each subject separately

### Break & Rest Optimization

* Suggests breaks after long study sessions

### Weekly Study Plan Generator

* Automatically creates weekly study schedules

### Export Functionality

* Download weekly study plans as text files

### Progress Tracking

* Mark study progress as Completed / Pending

### Smart Recommendations

* Suggests subjects needing more focus

---

## 📊 Professional Dashboard

The application includes a dashboard with:

* Total Tasks
* Subjects Planned
* Progress Entries
* Upcoming deadlines
* Study recommendations

This gives the project a production-ready interface.

---

## 🛠️ Technologies Used

| Technology          | Purpose                 |
| ------------------- | ----------------------- |
| Python              | Backend Logic           |
| Streamlit           | Web Interface           |
| SQLite              | Local Database          |
| Google Calendar API | Calendar Integration    |
| Google OAuth        | Secure Authentication   |
| Git & GitHub        | Version Control         |
| VS Code             | Development Environment |

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

---

## Step 1 — Clone Repository

```bash id="lrcxy4"
git clone https://github.com/Surya2608-avi/smart-timetable-assistant.git
cd smart-timetable-assistant
```

---

## Step 2 — Create Virtual Environment

```bash id="s6hixh"
python -m venv venv
venv\Scripts\activate
```

You should see:

```text id="ry7vti"
(venv)
```

---

## Step 3 — Install Required Packages

```bash id="d0d80p"
pip install -r requirements.txt
```

---

## Step 4 — Configure Google Calendar API

### Create Google Cloud Project

1. Open Google Cloud Console
2. Create a new project
3. Enable **Google Calendar API**
4. Go to **APIs & Services → Credentials**
5. Create **OAuth Client ID**
6. Download the file

Rename the downloaded file as:

```text id="jpwv66"
credentials.json
```

Place it inside the project folder.

---

## Step 5 — Run the Application

```bash id="bcpvdr"
streamlit run app.py
```

The app will open in your browser:

```text id="j0lyi1"
http://localhost:8501
```

---

## 🔐 Important Security Note

The following files should NEVER be uploaded to GitHub:

* credentials.json
* token.json
* tasks.db
* venv/
* **pycache**/

These are protected using `.gitignore`.

This ensures secure handling of Google OAuth credentials.

---

## 📤 Export Feature

Users can export:

* Weekly Study Plans
* Academic scheduling reports

This improves offline usability and documentation.

---

## 🎥 Demo Video

Demo Video Link:
(Add your Google Drive video link here)

---

## 🔗 GitHub Repository

Repository Link:

https://github.com/Surya2608-avi/smart-timetable-assistant

---

## 🎯 Final Milestone

### Production-Ready Academic Scheduling Application

This project successfully satisfies all Track A milestones:

✔ Calendar scheduling
✔ Conflict detection
✔ Assignment tracking
✔ Intelligent study planning
✔ Progress recommendations
✔ Export functionality
✔ Professional dashboard
✔ Production-ready UI

---

## 📌 Future Improvements

Possible future enhancements:

* Email / SMS reminders
* Monthly planner view
* Mobile application version
* AI-powered scheduling optimization
* Faculty timetable integration

---

## 👨‍💻 Author

### Surya Avinash

B.Tech CSE
Smart Timetable Assistant Project

# Playto-Community-Feed
🏗️ Playto Community Feed – Engineering Challenge
📌 Overview

This project is a Community Feed system built as part of the Playto Engineering Challenge.
It supports posts, threaded discussions, likes with karma rewards, and a dynamic leaderboard based on recent activity.

The focus of this project is backend correctness, performance, and data integrity, with a minimal frontend to demonstrate functionality.


# Features
# 📰 Community Feed
-Users can create text posts

-Posts display author information

-Threaded comments (nested replies like Reddit)


# ❤️ Likes & Karma System


Like on a Post → +5 Karma to the post author

Like on a Comment → +1 Karma to the comment author

Users cannot like the same post/comment twice

Likes are concurrency-safe


# 🏆 Leaderboard (Last 24 Hours)

Displays Top 5 users

Ranked by karma earned in the last 24 hours only

Karma is calculated dynamically from transaction history

No cached or stored “daily karma” fields

# 🛠️ Tech Stack

# Backend

Django

Django REST Framework (DRF)

SQLite (development database)

django-cors-headers


# Frontend

React (Vite)

Tailwind CSS

Axios


# ⚙️ Architecture Highlights

# Karma as Transactions

Karma is stored as immutable KarmaTransaction records

Ensures:

Accurate aggregation

No stale counters

Easy auditing


# Performance

Efficient fetching of nested comment trees

Avoids N+1 query problem

Optimized aggregation queries for leaderboard


# API-Driven Design

Frontend communicates only via REST APIs

Clear separation of concerns


# 📂 Project Structure
<img width="307" height="420" alt="image" src="https://github.com/user-attachments/assets/48a91ad6-8c15-42d4-9d2c-b00f303e0d37" />




# ▶️ How to Run the Project

# 1️⃣ Backend Setup
cd backend

venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver



# Backend runs at:

http://localhost:8000



# 2️⃣ Frontend Setup
cd frontend

npm install

npm run dev




# Frontend runs at:

http://localhost:5173


# 🔌 API Endpoints
<img width="861" height="277" alt="image" src="https://github.com/user-attachments/assets/d1d5e36e-92f6-4fdb-adbc-794a2d6f126c" />


# 🧪 Testing Notes

Posts and comments can be created via Django Admin

Likes can be triggered from the frontend UI

Leaderboard updates dynamically based on recent likes

# 🧠 Design Decisions

No authentication layer: Out of scope for this challenge

Tailwind v3: Used for stability and compatibility

CORS enabled: To support local frontend–backend communication

Minimal UI: Focused on backend logic and correctness

🎤 

“I modeled karma as immutable transactions and compute the leaderboard dynamically using time-bounded aggregation queries. This avoids stale data, handles concurrency safely, and keeps the system scalable.”

# ✅ Project Status

✔ All challenge requirements completed
✔ Backend logic validated
✔ Frontend integrated
✔ Ready for review and submission

# 🎉 Event Booking System
username: Admin
password: Singtan@123

A full-stack Event Booking System built using:

- 🔥 Django (Backend)
- ⚛️ React (Frontend)
- 🔐 JWT Authentication

---

## 🚀 Features

- User Login (JWT आधारित authentication)
- View Events
- Book Events
- View My Bookings
- Admin Panel
- Create / Delete Events

---

## 🖥️ Tech Stack

### Frontend:
- React
- Axios
- React Router

### Backend:
- Django
- Django REST Framework
- Simple JWT

---

## ⚙️ Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/Mr-rajkmar/Final-Project-Event-Booking-system.git
cd Final-Project-Event-Booking-system
# 📘 Event Booking System – Project Manual

## 🔄 System Flow

### 1. User Login
- User enters username and password
- Backend verifies credentials
- JWT token is generated
- Token is stored in frontend (localStorage)

---

### 2. View Events
- Frontend sends GET request to `/api/events/`
- Backend returns list of events
- Events are displayed on screen

---

### 3. Book Event
- User clicks "Book Now"
- Frontend sends POST request to `/api/bookings/`
- Booking is saved in database

---

### 4. View My Bookings
- Frontend sends GET request to `/api/bookings/`
- Backend returns user's bookings
- Displayed in UI

---

### 5. Admin Panel
- Admin can:
  - Create events
  - Delete events
- Changes reflect instantly in frontend

---

## 🧠 Working Summary

- React handles UI
- Django REST handles backend APIs
- JWT secures communication
- Axios connects frontend with backend

---

## ✅ Conclusion

The system successfully demonstrates a full-stack application with authentication, API handling, and real-world booking functionality.

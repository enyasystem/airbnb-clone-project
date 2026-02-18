# StayBackend: Airbnb Clone Project

## ▶️ Quick Start (Run Locally)

This repository now includes a minimal runnable Django backend scaffold.

### 1) Create and activate a virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2) Install dependencies
```bash
pip install -r requirements.txt
```

### 3) Apply migrations
```bash
python manage.py migrate
```

### 4) Run the development server
```bash
python manage.py runserver 0.0.0.0:8000
```

### 5) Verify the service
Open: `http://127.0.0.1:8000/api/health/`

Expected response:
```json
{"status":"ok","service":"staybackend"}
```

🏡💻 A backend-focused blueprint of an Airbnb-like booking platform. This project simulates real-world full-stack development with a focus on database design, API development, and secure backend architecture.  🚀🔐🧠

# 🚀 Project Goals
Build a scalable, real-world booking app backend

Apply backend principles with Django & MySQL

Practice secure API development and CI/CD integration

Collaborate via GitHub and document effectively

# 🛠️ Tech Stack
Backend Framework: Django

Database: MySQL

API: REST / GraphQL

Version Control: Git & GitHub

CI/CD: GitHub Actions / Docker

# 👥 Team Roles
Role	Responsibility
Backend Developer	Designs APIs, business logic, and ensures backend performance
Database Admin	Structures, optimizes, and secures the database schema
DevOps Engineer	Sets up CI/CD pipelines, containerization, and deployment workflow
Project Coordinator	Manages timelines, documentation, and team task alignment

# 🧰 Technology Stack
Technology	Purpose
Django	A powerful Python web framework used to build robust RESTful APIs and manage backend logic.
MySQL	A relational database system for storing user data, listings, and bookings securely and efficiently.
GraphQL	An API query language that allows clients to request exactly the data they need, improving performance and flexibility.
Docker	Containerization tool to ensure consistent development and deployment environments.
Git & GitHub	Version control and collaboration tools for managing project code and tracking changes.
GitHub Actions	Automates testing, building, and deployment processes for continuous integration and delivery (CI/CD).

# 🗃️ Database Design
Below is an overview of the key entities and their relationships in the StayBackend project:

# 🧑‍💼 Users
Stores information about platform users.

id: unique identifier

name: full name

email: unique email address

password: hashed password

role: host or guest

Relationship:
A user can list multiple properties and make multiple bookings.

# 🏠 Properties
Details of homes listed on the platform.

id: unique identifier

owner_id: references user (host)

title: name of the property

description: brief details

location: address or coordinates

Relationship:
A property belongs to a user (host) and can have many bookings and reviews.

# 📅 Bookings
Tracks reservations made by users.

id: unique identifier

property_id: references the booked property

user_id: references the guest

check_in: booking start date

check_out: booking end date

Relationship:
Each booking is made by one user for one property.

# ✍️ Reviews
Captures user feedback.

id: unique identifier

user_id: reviewer

property_id: reviewed property

rating: numeric rating

comment: optional text feedback

Relationship:
A user can review many properties; a property can have many reviews.

# 💳 Payments
Manages transactions for bookings.

id: unique identifier

booking_id: references the related booking

amount: amount paid

status: success, failed, pending

payment_date: timestamp of transaction

Relationship:
Each payment is tied to one booking.

# 🧩 Feature Breakdown
👤 User Management
Allows users to register, log in, and manage their profiles securely. It handles authentication, role-based access (host or guest), and password protection to ensure data privacy.

# 🏘️ Property Management
Hosts can list, update, and delete properties with relevant details like title, location, and description. This feature enables users to showcase their accommodations to potential guests.

# 📅 Booking System
Guests can book available properties for specific dates. This module ensures date availability, prevents double-bookings, and allows both users and hosts to track booking history.

# 💳 Payment Integration
Securely handles payment processing for bookings. It tracks transactions, manages payment statuses, and ensures a smooth financial flow between guests and hosts.

# ✍️ Reviews & Ratings
Guests can leave feedback and rate properties after their stay. This feature helps maintain trust and transparency in the platform by giving future guests insight into past experiences.


# 🔐 API Security
Securing the backend is essential to protect sensitive user information, payment data, and the integrity of the platform. The following measures are implemented:

# ✅ Authentication
Token-based authentication (e.g., JWT) ensures that only registered users can access protected endpoints. This prevents unauthorized access to user accounts and private data.

# 🔒 Authorization
Role-based access control restricts what different users (e.g., host vs guest) can do. It ensures that users only perform actions allowed by their role — like only hosts managing listings.

# 🚫 Rate Limiting
Limits the number of API requests per user over a time period to prevent abuse or denial-of-service (DoS) attacks. It helps maintain server performance and security.

# 🔐 Data Encryption
All sensitive data, especially passwords and payment information, is encrypted at rest and in transit. This protects against data breaches and information leaks.

# 🛡️ Input Validation & Sanitization
All user inputs are validated and sanitized to prevent injection attacks (e.g., SQL, XSS). This maintains the reliability and integrity of the database.

# ⚙️ CI/CD Pipeline
CI/CD (Continuous Integration and Continuous Deployment) pipelines automate the process of testing, building, and deploying code. This ensures that every change made to the codebase is automatically verified and deployed without manual intervention.

In this project, CI/CD helps maintain code quality, catch bugs early, and ensure fast and reliable deployments.

# 🛠 Tools Used
GitHub Actions: Automates tasks such as testing, linting, and deployment.

Docker: Provides a consistent containerized environment for development, testing, and deployment.

GitHub: Triggers pipelines when code is pushed or pull requests are made.

With CI/CD, the team can ship updates faster and more confidently, reducing downtime and human errors.

# StayBackend: Airbnb Clone Project
🏡💻 A backend-focused blueprint of an Airbnb-like booking platform. This project simulates real-world full-stack development with a focus on database design, API development, and secure backend architecture.  🚀🔐🧠

🚀 Project Goals
Build a scalable, real-world booking app backend

Apply backend principles with Django & MySQL

Practice secure API development and CI/CD integration

Collaborate via GitHub and document effectively

🛠️ Tech Stack
Backend Framework: Django

Database: MySQL

API: REST / GraphQL

Version Control: Git & GitHub

CI/CD: GitHub Actions / Docker

👥 Team Roles
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

🧑‍💼 Users
Stores information about platform users.

id: unique identifier

name: full name

email: unique email address

password: hashed password

role: host or guest

Relationship:
A user can list multiple properties and make multiple bookings.

🏠 Properties
Details of homes listed on the platform.

id: unique identifier

owner_id: references user (host)

title: name of the property

description: brief details

location: address or coordinates

Relationship:
A property belongs to a user (host) and can have many bookings and reviews.

📅 Bookings
Tracks reservations made by users.

id: unique identifier

property_id: references the booked property

user_id: references the guest

check_in: booking start date

check_out: booking end date

Relationship:
Each booking is made by one user for one property.

✍️ Reviews
Captures user feedback.

id: unique identifier

user_id: reviewer

property_id: reviewed property

rating: numeric rating

comment: optional text feedback

Relationship:
A user can review many properties; a property can have many reviews.

💳 Payments
Manages transactions for bookings.

id: unique identifier

booking_id: references the related booking

amount: amount paid

status: success, failed, pending

payment_date: timestamp of transaction

Relationship:
Each payment is tied to one booking.

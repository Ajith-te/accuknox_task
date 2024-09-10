# Django REST API

## Overview

This project is a Django REST API designed for [brief description of your project]. It includes functionalities for user login/signup, search, friend requests, and listing friends.

## Features

- User authentication and authorization
- Search functionality
- Friend requests
- List friends

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.x
- Django
- Django REST Framework
- Docker (for containerization)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Ajith-te/accuknox_task.git
   cd accuknox_task


2. **Create a virtual environment and activate it**
    python -m venv venv
    source venv/bin/activate  # On Windows `venv\Scripts\activate`


3. **Install the required packages**
    pip install -r requirements.txt


4. **Run migrations**
    python manage.py migrate

   
5. **Create a superuser**
    python manage.py createsuperuser


6. **Start the development server:**
    python manage.py runserver


### Docker Setup

1. **Build the Docker image**
    docker build -t your-image-name .


2. **Run the Docker container**
    docker run -p 8000:8000 your-image-name


### API Endpoints

 - User Signup: POST /api/signup/
 - User Login: POST /api/login/
 - Search Users: GET /api/search/
 - Send Friend Request: POST /api/friend-request/
 - List Friends: GET /api/friends/
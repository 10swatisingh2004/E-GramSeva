# E Gram Seva 

## Overview

**E Gram Seva** is a digital platform designed to connect citizens with the government services offered by the Gram Panchayat. It allows citizens to apply for various services, track the status of their applications, and interact with the Panchayat officials. The platform also facilitates officers and staff to manage and update the applications and services. 

This project is developed using **Django** as the backend framework and focuses on offering different views and functionalities for users with different roles such as *officer*, *staff*, and *user*.

## Features

- **User Registration & Login**: Allows users to register and log in to the platform.
- **Service Listing**: Displays a list of services offered by the Gram Panchayat.
- **Service Application**: Registered users can apply for various services.
- **Application Tracking**: Users can view the status of their applications.
- **Admin and Officer Functions**: Officers can create, update, and delete services.
- **Staff Management**: Staff and officers can update the status of applications.

## Technologies Used

- **Django**: Backend web framework.
- **HTML/CSS**: For front-end design.
- **SQLite**: For local database storage.
- **JavaScript**: For handling dynamic content.

## Installation

### Prerequisites

- Python 3.x
- Django

### Steps to Set Up Locally

1. **Clone the Repository**

   First, clone the repository to your local machine:

   ```bash
   git clone https://github.com/10swatisingh2004/E-GramSeva.git
   cd e-gramseva

   ```
2. **Install Dependencies**
   Install the necessary dependencies using pip:
   ```bash
   pip install -r requirements.txt
   ```
3. **Set Up the Database**
   Run migrations to set up the database schema:
   ```bash
   python manage.py migrate
   ```
4. **Create Superuser (Optional)**
   If you want to create a superuser (admin) for managing the application, run:
   ```bash
   python manage.py createsuperuser
   ```
5. **Run the Development Server**
   Start the Django development server:
   ```bash
   python manage.py runserver
   ```
6. **Access the Application**
   Open a browser and go to http://127.0.0.1:8000/ to access the E Gram Seva platform.
   
## Features and Functionalities
**Home Page:**
- The landing page (home) allows users to navigate to different sections of the platform.
**User Registration & Login:**
- Users can register with a username, password, and role. There are three roles: user, officer, and staff.
**Service Management**
- Officers can create, update, and delete services.
- Users can view and apply for available services.
**Application Management**
- Users can view the status of their applications.
- Staff and officers can update the status of applications, e.g., approved, rejected, or pending.
**Officer and Staff Management**
- Officers can manage services and applications.
- Staff can assist with application status updates.

## Folder Structure
- *app/*: The core application folder containing models, views, and templates.
- *templates/*: HTML files for rendering views.
- *static/*: Folder for static files (CSS, JS).
- *urls.py*: Defines the URLs for the views in the application.
- *models.py*: Contains the models for user roles, services, and applications.

## License
This project is licensed under the MIT License.

## Author
- **Swati Singh** - *Developer*

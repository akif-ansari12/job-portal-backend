# Job Portal Backend API

A backend REST API for a Job & Recruitment Management System built with **Python, Django, Django REST Framework, MySQL, and JWT Authentication**.

The API supports role-based access for **Candidates** and **Recruiters**, job management, job applications, application status management, search, filtering, pagination, file validation, automated testing, and GitHub Actions CI.

## Tech Stack

* Python
* Django
* Django REST Framework
* MySQL
* Django ORM
* JWT Authentication
* Git & GitHub
* GitHub Actions

## Features

### Authentication

* User registration
* JWT login
* JWT authentication
* Authenticated profile endpoint

### Role-Based Access Control

Two user roles are supported:

* **Candidate**

  * View jobs
  * Apply for jobs
  * View own applications
  * Filter own applications by status

* **Recruiter**

  * Create jobs
  * Update own jobs
  * Delete own jobs
  * View applications for own jobs
  * Update application status

### Job Management

* Create job
* List jobs
* Retrieve job details
* Update job
* Delete job
* Recruiter ownership validation
* Search jobs
* Filter by location
* Filter by job type
* Pagination

### Job Applications

* Candidate can apply for jobs
* Prevent duplicate applications
* Candidate can view own applications
* Recruiter can view applications for their jobs
* Application status workflow:

  * Applied
  * Shortlisted
  * Rejected
  * Hired

### Resume Validation

* PDF, DOC and DOCX files supported
* Maximum resume size: 5 MB

### Testing & CI

* Django REST API automated tests
* Application API test coverage
* Duplicate application validation
* Role permission testing
* Application status update testing
* GitHub Actions CI
* MySQL service used during CI testing

## API Endpoints

### Accounts

| Method | Endpoint                  | Description               |
| ------ | ------------------------- | ------------------------- |
| POST   | `/api/accounts/register/` | Register user             |
| POST   | `/api/accounts/login/`    | Login and obtain JWT      |
| GET    | `/api/accounts/profile/`  | Get authenticated profile |

### Jobs

| Method    | Endpoint          | Description |
| --------- | ----------------- | ----------- |
| GET       | `/api/jobs/`      | List jobs   |
| POST      | `/api/jobs/`      | Create job  |
| GET       | `/api/jobs/<id>/` | Job details |
| PUT/PATCH | `/api/jobs/<id>/` | Update job  |
| DELETE    | `/api/jobs/<id>/` | Delete job  |

### Applications

| Method | Endpoint                             | Description               |
| ------ | ------------------------------------ | ------------------------- |
| POST   | `/api/applications/apply/`           | Apply for a job           |
| GET    | `/api/applications/my-applications/` | Candidate applications    |
| GET    | `/api/applications/recruiter/`       | Recruiter applications    |
| PATCH  | `/api/applications/<id>/status/`     | Update application status |

## Search & Filtering

Jobs can be searched and filtered using query parameters.

Examples:

```text
/api/jobs/?search=python
/api/jobs/?location=Noida
/api/jobs/?job_type=Full%20Time
/api/jobs/?search=python&location=Noida
```

Applications can be filtered by status:

```text
/api/applications/my-applications/?status=Applied
/api/applications/recruiter/?status=Shortlisted
```

## Pagination

The API uses Django REST Framework pagination.

Default page size:

```text
5 results per page
```

Example:

```text
/api/jobs/?page=2
```

## Project Structure

```text
job-portal-backend/
│
├── accounts/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── permissions.py
│   └── urls.py
│
├── jobs/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── permissions.py
│   └── urls.py
│
├── applications/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── tests.py
│   └── urls.py
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── .github/
│   └── workflows/
│       └── django.yml
│
├── manage.py
├── .gitignore
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/akif-ansari12/job-portal-backend.git
cd job-portal-backend
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
venv\Scripts\activate
```

Install dependencies:

```bash
pip install django djangorestframework mysqlclient djangorestframework-simplejwt
```

## Database Configuration

The project uses MySQL.

Configure the following environment variables:

```text
DB_NAME
DB_USER
DB_PASSWORD
DB_HOST
DB_PORT
```

Run migrations:

```bash
python manage.py migrate
```

Create a superuser if required:

```bash
python manage.py createsuperuser
```

Start the development server:

```bash
python manage.py runserver
```

The API will be available at:

```text
http://127.0.0.1:8000/
```

## Running Tests

Run all Django tests:

```bash
python manage.py test
```

Application tests:

```bash
python manage.py test applications
```

Current application test suite covers:

* Candidate application
* Duplicate application prevention
* Recruiter application restriction
* Candidate status-update restriction
* Recruiter status update

## CI/CD

GitHub Actions is configured to automatically:

1. Checkout the repository
2. Set up Python
3. Install dependencies
4. Start MySQL
5. Run Django migrations
6. Run automated tests

This ensures that changes are tested automatically before deployment.

## Future Improvements

Planned improvements include:

* Docker & Docker Compose
* Production deployment
* Gunicorn
* Nginx
* AWS deployment
* API documentation with Swagger/OpenAPI
* Celery & Redis for background tasks

## Author

**Akif Ansari**

Python Backend Developer | Django | Django REST Framework | MySQL | REST APIs

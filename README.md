# Django Todo Board Backend Readme

Welcome to the Django Todo Board Backend! This backend application provides the necessary API endpoints for managing tasks on your Todo board.

## Prerequisites

Before you start, ensure you have the following installed:

- **Python**: Make sure you have Python 3 installed on your system. You can download it from [python.org](https://www.python.org/).

- **Docker**: If you plan to run the app using Docker, make sure you have Docker installed. You can download it from [docker.com](https://www.docker.com).

## Getting Started

Follow the steps below to set up and run the Django Todo Board Backend using a virtual environment.

### Setting Up a Virtual Environment

1. Clone the repository: `git clone https://github.com/salman1204/todo-board-django`
2. Navigate to the project directory: `cd todo-board-django`
3. Create a virtual environment: `python3 -m venv venv`
4. Activate the virtual environment:
   - On macOS and Linux: `source venv/bin/activate`
   - On Windows: `venv\Scripts\activate`

### Running the Application

1. Install project dependencies: `pip install -r requirements.txt`
2. Apply database migrations: `python manage.py migrate`
3. Start the development server: `python manage.py runserver`
4. Open your browser and go to `http://localhost:8000` to access the API.

### Running with Docker

1. Clone the repository: `git clone hhttps://github.com/salman1204/todo-board-django`
2. Navigate to the project directory: `cd todo-board-django`
3. Build the Docker image: `docker-compose build`
4. Run the Docker container: `docker-compose up`
5. Open your browser and go to `http://localhost:8000` to access the API.

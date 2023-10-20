# Project: findme

"findme" is a web application that provides a modern and efficient way to connect users with information. The project is divided into two main components: the frontend and the backend.

## Frontend
- **Tech Stack**:
  - [Vite](https://vitejs.dev/) for a fast development environment
  - [Vue 3](https://v3.vuejs.org/) for building user interfaces
  - [Apollo Client](https://www.apollographql.com/docs/react/) for GraphQL communication

## Backend

The backend is powered by Django, GraphQL, Graphene, and PostgreSQL. This robust combination allows for flexible data management and efficient queries, making it an ideal choice for handling the application's data and logic.

- **Tech Stack**:
  
  - [Django](https://www.djangoproject.com/) for web framework
  - [GraphQL](https://graphql.org/) for flexible API queries
  - [Graphene](https://graphene-python.org/) for connecting Django and GraphQL
  - [PostgreSQL](https://www.postgresql.org/) for the database

## Containerization:
This project includes Docker and Docker-Compose configurations to facilitate easy deployment and containerization. With these tools, you can easily set up the project environment and scale it as needed.

  - Docker: For creating, deploying, and running applications in containers.
  - Docker Compose: For defining and running multi-container Docker applications.

## Deployment:
  - Gunicorn: A Python Web Server Gateway Interface (WSGI) HTTP server.
  - Nginx: A high-performance web server and reverse proxy server.


## Installation
1. Clone the repository: `git clone https://github.com/moriire/findme.git`
2. Frontend Setup:
   - Navigate to the frontend directory: `cd findme/frontend`
   - Install dependencies: `yarn install`
   - Start the development server: `yarn dev`
3. Backend Setup:
   - Navigate to the backend directory: `cd findme/backend`
   - Install Python dependencies: `pip install -r requirements.txt`
   - Apply database migrations: `python manage.py migrate`
   - Start the Django development server: `python manage.py runserver`
4. Docker Compose (Production):
   - From the project root, run: `docker-compose up -d`

## Usage
- Frontend: Access the frontend in your browser at `http://localhost:3000`.
- Backend: Access the backend at `http://localhost:8000/graphql`.
- Production Deployment: Configure Nginx to serve the application on a domain of your choice.

## Contribution
- We welcome contributions! Feel free to submit pull requests and open issues.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

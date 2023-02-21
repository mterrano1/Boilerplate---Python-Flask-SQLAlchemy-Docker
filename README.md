# Case Tracker API


## Full project

https://www.youtube.com/watch?v=cONFD37A6y8

https://github.com/mterrano1/Case-Tracker-Final-Project


## Description

This is the Flask API for the Case Tracker project. The API is used to handle comments for the project.


## Technologies Used

- Flask - a micro web framework for Python.
- SQLAlchemy - an Object-Relational Mapping (ORM) library for Python.
- Flask-Migrate - a Flask extension that handles database migrations.
- Flask-CORS - a Flask extension for handling Cross-Origin Resource Sharing (CORS).
- PyJWT - a Python library for JSON Web Tokens (JWTs).
- dotenv - a Python library for loading environment variables from a .env file.


## Getting Started


### Prerequisites

To run the API, you'll need to have Docker installed on your machine.


### Installation

1. Clone the repository:
```console
$ git clone https://github.com/mterrano1/case-tracker-flask
```

2. Build the Docker image:
```console
$ docker build -t case-tracker-flask .
```

3. Run the Docker container:
```console
$ docker run -p 5000:5000 flask
```


## Usage

Once the container is running, you can use the following endpoints to interact with the API:

- `GET /comments/<case_id>` - Retrieves all comments for a specific case.
- `POST /comments` - Adds a new comment to the database.


### Example Requests

#### Retrieve Comments
```console
$ curl http://localhost:5000/comments/1
```

#### Add Comment
```console
$ curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer <token>"
-d '{"case_id": 1, "comment": "This is a test comment.", "first_name": "John", "last_name": "Doe"}'
http://localhost:5000/comments
```
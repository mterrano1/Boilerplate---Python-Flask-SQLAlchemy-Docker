# Case-Tracker Comment API

This is a Flask API that handles comments for the Case-Tracker project. It allows authenticated users to retrieve and add comments for a specific case.

Installation
Clone the repository to your local machine.
Create a virtual environment for the project using virtualenv or conda.
Activate the virtual environment.
Install the required packages using pip install -r requirements.txt.
Create a PostgreSQL database and add the database URI to a .env file as DATABASE_URL.
Add a secret key for JWT authentication to the .env file as JWT_SECRET.
Run the database migrations using flask db upgrade.
Start the application using flask run.
Endpoints
GET /comments/:case_id
Returns a list of comments for a specific case.

Request Parameters:

case_id (int) - the ID of the case to retrieve comments for.
Response:

200 OK - list of comments as JSON.
401 Unauthorized - if user is not authenticated.
POST /comments/:case_id
Adds a new comment for a specific case.

Request Parameters:

case_id (int) - the ID of the case to add the comment to.
Request Body:

comment (string) - the comment text.
first_name (string) - the first name of the user who added the comment.
last_name (string) - the last name of the user who added the comment.
Response:

201 Created - if comment is added successfully.
400 Bad Request - if comment text is missing or empty.
401 Unauthorized - if user is not authenticated.
Authentication
This API uses JWT authentication to verify user identities. To make authenticated requests, clients must include a valid JWT token in the Authorization header of the request. If the token is missing or invalid, the server will respond with a 401 Unauthorized error.

Technologies Used
Flask - a micro web framework for Python.
SQLAlchemy - an Object-Relational Mapping (ORM) library for Python.
Flask-Migrate - a Flask extension that handles database migrations.
Flask-CORS - a Flask extension for handling Cross-Origin Resource Sharing (CORS).
PyJWT - a Python library for JSON Web Tokens (JWTs).
dotenv - a Python library for loading environment variables from a .env file.
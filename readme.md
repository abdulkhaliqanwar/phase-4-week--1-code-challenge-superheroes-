# Phase-4 Week-1 Code Challenge: Superheroes

## Description
This project is a Flask-based API for managing superheroes and their powers. It allows users to retrieve information about superheroes, their abilities, and assign powers to them. The API follows RESTful principles and provides endpoints for fetching and updating data.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Installation
Follow these steps to set up and run the project locally:

```sh
# Clone the repository
git clone https://github.com:abdulkhaliqanwar/phase-4-week--1-code-challenge.git

# Navigate to the project directory
cd superheroes

# Create a virtual environment
pipenv install && pipenv shell


# Run database migrations
flask db upgrade

# Seed the database
python seed.py

# Start the Flask server
flask run or python app.py
```

## Usage
Once the server is running, you can interact with the API using Postman or curl.

Example:
```sh
# Fetch all superheroes
curl http://127.0.0.1:5000/heroes
```

## Features
- Retrieve a list of superheroes
- Fetch details about individual superheroes
- View available superpowers
- Assign superpowers to superheroes

## API Endpoints
### Get all superheroes
```
GET /heroes
```
Response:
```json
[
  {"id": 1, "name": "Superman", "city": "Metropolis"},
  {"id": 2, "name": "Batman", "city": "Gotham"}
]
```

### Get a superhero by ID
```
GET /heroes/<id>
```
Response:
```json
{"id": 1, "name": "Superman", "city": "Metropolis", "powers": ["Flight", "Super Strength"]}
```

### Get all powers
```
GET /powers
```
Response:
```json
[
  {"id": 1, "name": "Flight", "description": "Ability to fly"},
  {"id": 2, "name": "Invisibility", "description": "Can become invisible"}
]
```

### Assign a power to a hero
```
POST /hero_powers
```
Request Body:
```json
{
  "hero_id": 1,
  "power_id": 2
}
```
Response:
```json
{"message": "Power assigned successfully"}
```

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Open a Pull Request

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


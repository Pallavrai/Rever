# Rever

Rever is an AI-based solution designed to recommend users Data Structures and Algorithms (DSA) questions for practice.

## Features

- AI-based recommendation system for DSA questions
- Built with Django
- Easy setup with Poetry
- Docker support for containerization

## Setup

### Prerequisites

- Python 3.8+ 
- Poetry
- Docker

### Installation

1. Fork this repo then clone it :

    ```bash
    git clone https://github.com/yourusername/rever.git
    cd rever
    ```

2. Install dependencies using Poetry:

    ```bash
    poetry install
    ```

3. Rename the environment file:

    ```bash
    mv django.env.example django.env
    ```

4. Run the application:

    ```bash
    poetry run python manage.py runserver
    ```

### Using Docker

1. Build the Docker image:

    ```bash
    docker build -t rever .
    ```

2. Run the Docker container:

    ```bash
    docker run -d -p 8000:8000 --env-file=django.env --name rever_container rever
    ```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
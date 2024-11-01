# Nyaya API

This Nyaya application provides legal advice based on the Indian Penal Code (IPC) sections. By leveraging the Groq client for natural language processing, the API retrieves relevant legal information and offers advice based on user queries.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [License](#license)

## Features

- Provides legal advice based on IPC sections.
- Simple and intuitive API design with endpoints for different legal advice use cases.
- Automatically generated API documentation accessible at /docs when the application is running.

## Requirements

- Docker (if using Docker)
- Python 3.6 or higher (if running locally)
- An active Groq API key for using the Groq client.

## Installation

### Using Docker
1. **Install Docker**: Follow the instructions on the [official Docker website](https://www.docker.com/get-started) to install Docker on your machine.
2. **Clone the Repository**:'
   
   ```
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
   ```  
4. **Build the Docker Image**:
   
   ```
   docker build -t my-fastapi-app .
   ```
6. **Run the Docker Container**:
   
   ```
   docker run -d -p 8000:8000 my-fastapi-app
   ```
      
### Running Locally (Without Docker)
1. **Install Python**: Download Python from [official Python website](https://www.python.org/downloads/) to install Python on your machine.
2. **Clone the Repository**:
   
   ```
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
   ```
4. **Set Up a Virtual Environment (optional)**:
   
   ```
   python -m venv venv
   ```
6. **Activate the virtual environment***:
   - On Windows:
     
     ```
      venv\Scripts\activate
     ```
   - On macOS/Linux:
     
     ```
      source venv/bin/activate
     ```
7. **Install Dependencies**:
   
   ```
   pip install -r requirements.txt
   ```
9. **Run the Application**:
    
    ```
   uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
    ```

## Usage

After the application is running, you can access the API at [http://localhost:8000](http://localhost:8000).

## API Endpoints

### Get Legal Advice: 
- **Endpoint**: /get_legal_advice/
- **Method**: POST
- **Request Body**:
  
   json
   ```
   {
     "query": "Explain IPC section 131."
   }
   ```
- **Response**: Legal advice related to the IPC section.
  
### Get IPC Sections:
- **Endpoint**: /ipc_sections/
- **Method**: GET
- **Response**: List of IPC sections.

## Testing

You can test the API using tools like Postman or cURL. Here’s an example of a cURL command to get legal advice:

```
curl -X POST "http://localhost:8000/get_legal_advice/" -H "Content-Type: application/json" -d '{"query": "Explain IPC section 131."}'
```

## License

<<<<<<< HEAD
This project is licensed under the MIT License - see the [LICENSE file](/LICENSE.txt) for details.
=======
This project is licensed under the MIT License - see the [LICENSE file](/LICENSE.txt) for details.
>>>>>>> 39058b8e2b703c9edfa1e4cf99386bbf87a9bf18

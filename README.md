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
- Automatically generated API documentation accessible at `/docs` when the application is running.

## Requirements

- Python 3.6 or higher.
- An active Groq API key for using the Groq client.

## Installation

### Running Locally (Without Docker)
1. **Install Python**: Follow the instructions on the [official Python website](https://www.python.org/downloads/) to install Python on your machine.
2. **Clone the Repository**:
   
   `git clone https://github.com/yourusername/your-repo.git`  
   `cd your-repo`

3. **Set Up a Virtual Environment (optional)**:
   
   `python -m venv venv`

4. **Activate the Virtual Environment**:
   - On Windows:
     `venv\Scripts\activate`
   - On macOS/Linux:
     `source venv/bin/activate`

5. **Install Dependencies**:
   
   `pip install -r requirements.txt`

6. **Run the Application**:
    
   `uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload`

## Usage

After the application is running, you can access the API at [https://nyayaapi.onrender.com](https://nyayaapi.onrender.com).

## API Endpoints

### Get Legal Advice: 
- **Endpoint**: /get_legal_advice/
- **Method**: POST
- **Request Body**:
  
   ```json
   {
     "query": "instigates any person to do that thing"
   }

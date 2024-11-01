FastAPI Legal Advice API
This FastAPI application provides legal advice based on the Indian Penal Code (IPC) sections. By leveraging the Groq client for natural language processing, the API can retrieve relevant legal information and give advice based on user queries.

Table of Contents
Features
Requirements
Installation
Using Docker
Running Locally (Without Docker)
Usage
API Endpoints
Get Legal Advice
Get IPC Sections
Testing
License
Features
Provides legal advice based on IPC sections.
Simple and intuitive API design with endpoints for different legal advice use cases.
Automatically generated API documentation accessible at /docs when the application is running.
Requirements
Docker (if using Docker)
Python 3.6 or higher (if running locally)
An active Groq API key for using the Groq client.
Installation
Using Docker
Install Docker: Follow the official Docker installation guide to install Docker on your machine.
Clone the Repository:
bash
Copy code
git clone https://github.com/yourusername/your-repo.git
cd your-repo
Build the Docker Image:
bash
Copy code
docker build -t my-fastapi-app .
Run the Docker Container:
bash
Copy code
docker run -d -p 8000:8000 my-fastapi-app
Running Locally (Without Docker)
Install Python: Download Python from python.org.
Clone the Repository:
bash
Copy code
git clone https://github.com/yourusername/your-repo.git
cd your-repo
Set Up a Virtual Environment (optional):
bash
Copy code
python -m venv venv
Activate the virtual environment:
On Windows:
bash
Copy code
venv\Scripts\activate
On macOS/Linux:
bash
Copy code
source venv/bin/activate
Install Dependencies:
bash
Copy code
pip install -r requirements.txt
Run the Application:
bash
Copy code
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
Usage
After the application is running, you can access the API at http://localhost:8000. The documentation is available at http://localhost:8000/docs.

API Endpoints
Get Legal Advice
Endpoint: /get_legal_advice/
Method: POST
Request Body:
json
Copy code
{
  "query": "Explain IPC section 131."
}
Response: Returns legal advice related to the specified IPC section.
Get IPC Sections
Endpoint: /ipc_sections/
Method: GET
Response: Returns a list of IPC sections.
Testing
You can test the API using tools like Postman or cURL. Below is an example of a cURL command to get legal advice:

bash
Copy code
curl -X POST "http://localhost:8000/get_legal_advice/" -H "Content-Type: application/json" -d '{"query": "Explain IPC section 131."}'
License
This project is licensed under the MIT License - see the LICENSE file for details.
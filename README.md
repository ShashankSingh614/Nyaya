# Nyaya API

This Nyaya application provides legal advice based on the Indian Penal Code (IPC) sections. By leveraging the Groq client for natural language processing, the API retrieves relevant legal information and offers advice based on user queries.

## Table of Contents

- [Features](#features)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [License](#license)

## Features

- Provides legal advice based on IPC sections.
- Simple and intuitive API design with endpoints for different legal advice use cases.
- Automatically generated API documentation accessible at `/docs` when the application is running.

## Usage

You can access the API at [https://nyayaapi.onrender.com](https://nyayaapi.onrender.com).

## API Endpoints

**Get Legal Advice**:
   - **Endpoint**: /get_legal_advice/
   - **Method**: POST
   - **Request Body**:
        ```json
        {
          "query": "what is the legal punishment for raping a minor"
        }
        ```
   - **Response**:
        ```json
        {
          "Section_Number": 61,
          "Title": "Criminal conspiracy.",
          "Content": "2) Whoever is a party to a criminal conspiracy,–– (a) to commit an offence punishable with death, imprisonment for life or rigorous imprisonment for a term of two years or upwards, shall, where no express provision is made in this Sanhita for the punishment of such a conspiracy, be punished in the same manner as if he had abetted such offence; (b) other than a criminal conspiracy to commit an offence punishable as aforesaid shall be punished with imprisonment of either description for a term not exceeding six months, or with fine or with both.",
          "Punishment": "The punishment for criminal conspiracy under Section 61 of the Bharatiya Nyaya Sanhita (BNS) depends on the seriousness of the offense being conspired to commit: Serious offenses- If the conspiracy is to commit an offense punishable by death, life imprisonment, or rigorous imprisonment for at least two years, the punishment is the same as if the conspirator had attempted the offense. Lesser offenses- If the conspiracy is to commit an offense punishable by imprisonment for up to two years, the punishment is imprisonment for up to six months, a fine, or both.",
          "Explanation": "Section 61(2) of the BNS provides a framework for punishing individuals involved in criminal conspiracies. The punishment is based on the seriousness of the offense being conspired to commit, ensuring that the punishment is appropriate.",
          "Illustrations": "."
        }
        ```
## License

This project is licensed under the MIT License. See the [LICENSE file](/LICENSE.txt) file for details.
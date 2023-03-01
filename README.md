# Django REST framework Email API

This is a Django-based RESTful API for sending emails. It allows you to send emails by making POST requests to the API with the required data in JSON format.

## Prerequisites

* Docker
* Docker Compose

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com//django-email-api.git
    cd django-email-api
    ```
<!-- 
2. Create a virtual environment and activate it:

    ```bash
    python3 -m venv env
    source env/bin/activate
    ```

3. Install the required packages:

    ```bash

    ``` -->

2. Add these settings in the projects settings.py file:

    ```bash

    ```
**Note**: Replace EMAIL_HOST_USER and EMAIL_HOST_PASSWORD with your own email credentials.

3. Run the Docker containers:

    ```bash

    ```

4. Test the API by sending a POST request to http://localhost:8000/email/ with the required data in JSON format. For example:

    ```bash

    ```
<!-- 
7. You can now send a POST request to the /email/ endpoint with the email details in JSON format:

    ```bash

    ``` -->




## API Endpoints

### POST /email/
This endpoint sends an email with the provided data in JSON format. Required fields: to, subject, body, from.

## Response

On success, the API returns a 200 OK response with the message "Email sent successfully".

On failure, the API returns a 400 Bad Request response with the error message "Email sending failed".


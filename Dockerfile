#what image we want to base our container on
FROM python:3.10.8

# Setting Environment Variables to dont write python byte code and 
# setting output to terminal without buffering
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory to /EmailAPI
WORKDIR /EmailAPI

# Copying requirements.txt to the directory on our container
COPY requirements.txt /EmailAPI/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /EmailAPI
COPY . /EmailAPI/


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

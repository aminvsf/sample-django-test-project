# Pull base image
FROM python:3.8

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /sample

# Install dependencies
COPY requirements.txt /sample/
RUN pip install -r requirements.txt

# Copy project
COPY . /sample

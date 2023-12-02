FROM python:3.8.3-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip 

# copy project
COPY . /usr/src/app

EXPOSE 8000


CMD [".", "./.venv/Scripts/activate","python", "manage.py", "runserver", "0.0.0.0:8000"]
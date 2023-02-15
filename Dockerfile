#Base Image
FROM python:3

#setup environment variable
ENV PYTHONUNBUFFERED=1


#where your code lives
WORKDIR /riade/OneDrive/Desktop/universty_system_django

#copy whole project to your docker home directory
COPY requirements.txt ./

#run this command to install all dependencies
RUN pip install -r requirements.txt

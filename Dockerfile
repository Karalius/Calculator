# set the base image
FROM python:3.9-slim-buster

# set the working directory
WORKDIR /usr/src/app

# requirements
COPY requirements.txt ./

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# install python package
RUN pip install calc

CMD ["python"]

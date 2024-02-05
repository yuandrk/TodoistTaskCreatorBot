# argument from makefile to set type of arch
ARG ARCH

FROM ${ARCH}/python:3.13-rc-slim

# Set the working directory in the container
WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables
ARG TODOIST_TOKEN
ARG TELE_TOKEN

ENV TODOIST_TOKEN=${TODOIST_TOKEN:-default_value}
ENV TELE_TOKEN=${TELE_TOKEN:-default_value}

# Run app.py when the container launches
CMD ["python", "./main.py"]

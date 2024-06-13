# Telegram Bot + Todoist App Integration

This project integrates a Telegram bot with the Todoist app to manage tasks efficiently.

## Setup

### Environment Variables

Set the following environment variables with your Telegram and Todoist tokens:

```sh
    export TELE_TOKEN=your_telegram_token
    export TODOIST_TOKEN=your_todoist_token
```

To run the application using Docker, use the following command:

```sh
docker run -it -e TODOIST_TOKEN -e TELE_TOKEN <docker_image>
```

### Manual Build

To manually build the Docker container, use the following command:

```sh
docker build --build-arg ARCH=arm64 -t <name_of_container> .
```

### Local Installation

To set up the project locally, follow these steps:

1. **Create a virtual environment:**

   ```sh
   python3 -m venv teledoist_env
   ```

2. **Activate the virtual environment:**

   ```sh
   source teledoist_env/bin/activate
   ```

3. **Install the required packages:**

   ```sh
   pip install -r requirements.txt
   ```

## Usage

### Create Task

Use the Telegram bot to create tasks in your Todoist app.

### Documentation

Refer to the project documentation for detailed instructions and examples.

## Labels

* OpenIA: ?
* Label: ?

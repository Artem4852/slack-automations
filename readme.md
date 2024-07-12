# Arcade Sessions Automation

This project provides a set of tools to interact with and automate Slack Arcade sessions without directly using the Slack interface. It includes a graphical user interface (GUI) and an API for programmatic interaction.

## Features

- Start, pause, and resume Arcade sessions
- Send messages to session threads
- Automate session management tasks
- User-friendly GUI for easy interaction

## Components

### 1. ArcadeApi (arcadeApi.py)

A Python class that interacts with the Arcade channel in Slack. It provides methods to:

- Start a new session
- Load an existing session
- Pause and resume sessions
- Get remaining time in a session
- Post replies to session threads

### 2. SlackApi (api.py)

An unofficial implementation of the Slack API, providing methods to:

- Search for messages
- Get channel messages and conversation replies
- Post messages and commands
- Execute actions on messages

### 3. GUI (ui.py) - doesn't work very well (please don't use this)

A PyQt5-based graphical user interface that allows users to:

- Start new Arcade sessions
- Pause and resume sessions
- Send messages to session threads
- Set working directory for sessions

## Setup

1. Clone the repository
2. Install the required dependencies (PyQt5, requests, python-dotenv)
3. Set up your environment variables:
   - Create a `.env` file in the project root
   - Add your Slack cookie and token ([where to find those?](#slack-api-credentials))
     ```
     cookie=your_slack_cookie_here
     token=your_slack_token_here
     ```

## Slack API credentials

To get your Slack API credentials, follow these steps:

1. Open Slack in your web browser
2. Open the developer console (F12)
3. Go to the "Network" tab
4. Reload the page
5. Click on any XHR request
6. Find the "cookie" in the "Request Headers" section and "token" in the "Request Payload" section

## Usage

### GUI (if you still decide to use it)

Run the `ui.py` script to launch the graphical interface:

```
python ui.py
```

### API

You can also use the `ArcadeApi` and `SlackApi` classes programmatically in your Python scripts:

```python
from arcadeApi import ArcadeApi

api = ArcadeApi(user_id="your_user_id", save=True, debug=False)

# Start a new session
api.start_session("My Arcade Session")

# Pause the session
api.pause_session()

# Resume the session
api.resume_session()

# Post a reply to the session thread
api.post_reply("Hello, Arcade!")
```

## Notes

- This project uses unofficial Slack API endpoints and may break if Slack changes their internal API structure.
- Make sure to handle your Slack credentials securely and do not share them publicly.

## License

This project is open source and available under the MIT License.

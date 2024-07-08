from shared import urls, forms, headers, save_json, channels, actions
import requests, time
import os, dotenv

dotenv.load_dotenv()

class SlackApi:
    """
    Unofficial implementation of the Slack API
    
    Args:
        save (bool, optional): Save the JSON response to a file. Defaults to False.
        debug (bool, optional): Print the JSON response. Defaults to False."""
    def __init__(self, save=False, debug=False) -> None:
        self.debug = debug
        self.save = save
        self.session = requests.Session()
        headers["cookie"] = os.getenv("cookie")
        self.session.headers = headers
        self.token = os.getenv("token")

    def search(self, query) -> dict:
        """
        Search for messages in Slack
        
        Args:
            query (str): The search query"""
        url = urls["search"]
        form = forms["search"]
        form["token"] = self.token
        form["query"] = query
        response = self.session.post(url, headers=headers, data=form)
        data = response.json()

        if self.save: save_json(data, "json/search.json")
        if self.debug: print(data)

        return data

    def get_channel_messages(self, channel) -> dict:
        """
        Get the messages in the arcade channel"""
        url = urls["get_channel_messages"]
        form = forms["get_channel_messages"]
        form["token"] = self.token
        form["channel"] = channels[channel]
        response = self.session.post(url, headers=headers, data=form)
        
        data = response.json()
        if self.save: save_json(data, "json/messages.json")
        if self.debug: print(data)

        return data

    def get_conversation_replies(self, channel, ts) -> dict:
        """
        Get the replies to a message in a conversation

        Args:
            channel (str): The channel ID
            ts (str): The timestamp of the message"""
        url = urls["get_conversation_replies"]
        form = forms["get_conversation_replies"]
        form["token"] = self.token
        form["channel"] = channel
        form["ts"] = ts
        response = self.session.post(url, headers=headers, data=form)
        data = response.json()

        if self.save: save_json(data, "json/replies.json")
        if self.debug: print(data)

        return data

    def post_message(self, channel, text) -> dict:
        """
        Post a message in a channel
        
        Args:
            channel (str): The channel ID
            text (str): The message text"""
        url = urls["post_message"]
        form = forms["post_message"]
        form["token"] = self.token
        form["channel"] = channel
        form["blocks"] = form["blocks"].format(text=text)
        response = self.session.post(url, headers=headers, data=form)
        data = response.json()

        if self.save: save_json(data, "json/post_message.json")
        if self.debug: print(data)

        return data

    def post_command(self, channel, command, text=None) -> dict:
        """
        Post a command in a channel
        
        Args:
            channel (str): The channel ID
            command (str): The command
            text (str): The command params (optional)"""
        url = urls["post_command"]
        form = forms["post_command"]
        form["token"] = self.token
        form["channel"] = channel
        form["command"] = "/"+command
        form["disp"] = "/"+command
        form["blocks"] = form["blocks"].format(text=text if text else "")
        response = self.session.post(url, headers=headers, data=form)
        data = response.json()

        if self.save: save_json(data, "json/post_command.json")
        if self.debug: print(data)

        return data

    def post_action(self, channel, ts, action) -> dict:
        """
        Execute an action
        
        Args:
            channel (str): The ID of channel where message is
            ts (str): The timestamp of the message
            action (str): The action to execute"""
        url = urls["post_action"]
        form = forms["post_action"]
        form["token"] = self.token
        form["actions"] = actions[action]
        form["container"] = form["container"].format(ts=ts, channel=channels[channel])
        response = self.session.post(url, headers=headers, data=form)
        data = response.json()

        if self.save: save_json(data, "json/post_action.json")
        if self.debug: print(data)

        return data

    def reply_to_thread(self, channel, ts, text) -> dict:
        """
        Reply to a thread
        
        Args:
            channel (str): The ID of channel where thread is
            ts (str): The timestamp of the message initiating the thread
            text (str): The reply text"""
        url = urls["post_message"]
        form = forms["post_message"]
        form["token"] = self.token
        form["channel"] = channel
        form["thread_ts"] = ts
        form["blocks"] = form["blocks"].format(text=text)
        response = self.session.post(url, headers=headers, data=form)
        data = response.json()

        if self.save: save_json(data, "json/reply_to_thread.json")
        if self.debug: print(data)

        return data
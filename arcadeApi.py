from shared import urls, forms, headers, save_json, channels, actions
import requests, time
from datetime import datetime

from api import SlackApi

class ArcadeApi:
    """
    A class to interact with the arcade channel in Slack"""
    def __init__(self, save=False, debug=False):
        self.api = SlackApi(save=save, debug=debug)
        self.current_session_ts = None
        self.paused = False
    
    def start_session(self, title):
        """
        Start a new arcade session

        Args:
            title (str): The title of the arcade session"""
        if self.current_session_ts: raise Exception("Session is already in progress. Finish the current session first.")
        self.api.post_command(channels["arcade"], "arcade", title)
        self.current_session_ts = self.get_latest_session_ts()

    def load_session(self, ts) -> None:
        """
        Load an existing arcade session
        
        Args:
            ts (str): The timestamp of the arcade session to load"""
        self.current_session_ts = ts
        self.api.get_conversation_replies(channels["arcade"], ts)
    
    def get_latest_session_ts(self) -> str:
        """
        Get the timestamp of the latest arcade session

        Returns:
            str: The timestamp of the latest arcade session"""
        ts = self.api.search("from:@hakkuun <@U078W0AP3FZ> in:#arcade \"minutes\"")["items"][0]["messages"][0]["ts"]
        return ts
    
    def pause_session(self) -> None:
        """
        Pause the current arcade session"""
        if self.paused: raise Exception("Session is already paused")
        self.api.post_action("arcade", self.current_session_ts, "pause")
        self.paused = True
    
    def resume_session(self) -> None:
        """
        Resume the current arcade session"""
        if not self.paused: raise Exception("Session is not paused")
        self.api.post_action("arcade", self.current_session_ts, "resume")
        self.paused = False

    def end_session(self) -> None:
        """
        End the current arcade session"""
        self.api.post_command(channels["arcade"], "arcade", "end")
        self.current_session_ts = None

    def get_time_left(self) -> int:
        """
        Get the time left (in minutes) in the current arcade session

        Returns:
            int: The time left in the current arcade session"""
        # start = datetime.fromtimestamp(float(self.current_session_ts))
        # now = datetime.now()
        # left = 60 - (now - start).seconds // 60
        # return left
        messages = self.api.get_conversation_replies(channels["arcade"], self.current_session_ts)["messages"]
        left = messages[0]["text"].replace("Time Remaining: ", "")
        left = int(left[:left.find(" ")])
        return left
    
    def post_reply(self, message) -> None:
        """
        Post a reply to the current arcade session

        Args:
            message (str): The message to post"""
        self.api.reply_to_thread(channels["arcade"], self.current_session_ts, message)
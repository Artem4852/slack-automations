from shared import urls, forms, headers, save_json, channels, actions
import requests, time
from datetime import datetime

from api import SlackApi

class ArcadeApi:
    """
    A class to interact with the arcade channel in Slack"""
    def __init__(self, user_id, save=False, debug=False):
        self.api = SlackApi(save=save, debug=debug)
        self.current_session_ts = None
        self.paused = False
        self.user_id = user_id
    
    def start_session(self, title):
        """
        Start a new arcade session

        Args:
            title (str): The title of the arcade session"""
        if self.current_session_ts: raise Exception("Session is already in progress. Finish the current session first.")
        self.api.post_command(channels["arcade"], "arcade", title)
        time.sleep(10)
        self.current_session_ts = self.get_latest_session_ts(True)

    def load_session(self, ts=None) -> None:
        """
        Load an existing arcade session
        
        Args:
            ts (str): The timestamp of the arcade session to load"""
        if ts: self.current_session_ts = ts
        else: self.current_session_ts = self.get_latest_session_ts()
        messages = self.api.get_conversation_replies(channels["arcade"], ts)["messages"]
        self.paused = not "until the session is ended early." in messages[0]["text"]
    
    def get_latest_session_ts(self, start=False) -> str:
        """
        Get the timestamp of the latest arcade session

        Returns:
            str: The timestamp of the latest arcade session"""
        try: 
            ts = self.api.search(f"from:@hakkuun <@{self.user_id}> in:#arcade " + ("\"minutes\"" if not start else "60 minutes"))["items"][0]["messages"][0]["ts"]
            return ts
        except:
            return None
    
    def pause_session(self) -> None:
        """
        Pause the current arcade session"""
        if not self.current_session_ts: raise Exception("No active session")
        elif self.paused: raise Exception("Session is already paused")
        # self.current_session_ts = self.get_latest_session_ts()
        print(self.current_session_ts)
        print(self.api.post_action("arcade", self.current_session_ts, "pause"))
        self.paused = True
        print(self.paused)
    
    def resume_session(self) -> None:
        """
        Resume the current arcade session"""
        if not self.current_session_ts: raise Exception("No active session")
        elif not self.paused: raise Exception("Session is not paused")
        # self.current_session_ts = self.get_latest_session_ts()
        self.api.post_action("arcade", self.current_session_ts, "resume")
        self.paused = False

    def get_time_left(self) -> int:
        """
        Get the time left (in minutes) in the current arcade session

        Returns:
            int: The time left in the current arcade session"""
        messages = self.api.get_conversation_replies(channels["arcade"], self.current_session_ts)["messages"]
        left = messages[0]["text"]
        left = int(left[:left.index(" minutes")].split(" ")[-1])
        return left
    
    def post_reply(self, message) -> None:
        """
        Post a reply to the current arcade session

        Args:
            message (str): The message to post"""
        self.api.reply_to_thread(channels["arcade"], self.current_session_ts, message)
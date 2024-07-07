from shared import urls, forms, headers, save_json, channels, actions
from arcadeApi import ArcadeApi
import requests, time

api = ArcadeApi(save=True, debug=False)

# print(reply_to_thread(channels["arcade"], "1720266789.748599", "Test"))
# unreplied = get_channel_messages()
# print(unreplied)
# for message in unreplied:
#     reply_to_thread(channels["arcade"], message["ts"], "Test")

# print(post_command(channels["arcade"], "arcade", "test"))
# print(post_action("arcade", "1720345345.827299", "pause"))
# print(get_conversation_replies(channels["arcade"], "1720345345.827299"))

api.current_session_ts = "1720357828.912929"
# api.pause_session()
# api.load_session("1720357828.912929")
print(api.get_time_left())
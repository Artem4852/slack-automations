from shared import urls, forms, headers, save_json, channels, actions
import requests

def get_channel_messages():
    url = urls["get_channel_messages"]
    form = forms["get_channel_messages"]
    form["channel"] = channels["arcade"]
    response = requests.post(url, headers=headers, data=form)
    data = response.json()
    save_json(data, "messages.json")

    unreplied = []

    for message in data["history"]["messages"]:
        if not "reply_count" in message:
            unreplied.append(message)
            print(message["text"], message["ts"])
    return unreplied

def get_conversation_replies(channel, ts):
    url = urls["get_conversation_replies"]
    form = forms["get_conversation_replies"]
    form["channel"] = channel
    form["ts"] = ts
    response = requests.post(url, headers=headers, data=form)
    data = response.json()
    save_json(data, "replies.json")
    return data

def post_message(channel, text):
    url = urls["post_message"]
    form = forms["post_message"]
    form["channel"] = channel
    form["blocks"] = form["blocks"].format(text=text)
    response = requests.post(url, headers=headers, data=form)
    print(response.json())

def post_command(channel, command, text):
    url = urls["post_command"]
    form = forms["post_command"]
    form["channel"] = channel
    form["command"] = "/"+command
    form["disp"] = "/"+command
    form["blocks"] = form["blocks"].format(text=text)
    response = requests.post(url, headers=headers, data=form)
    print(response.json())

def post_action(channel, ts, action):
    url = urls["post_action"]
    form = forms["post_action"]
    form["actions"] = actions[action]
    form["container"] = form["container"].format(ts=ts, channel=channels[channel])
    response = requests.post(url, headers=headers, data=form)
    print(response.json())

def reply_to_thread(channel, ts, text):
    url = urls["post_message"]
    form = forms["post_message"]
    form["channel"] = channel
    form["thread_ts"] = ts
    form["blocks"] = form["blocks"].format(text=text)
    response = requests.post(url, headers=headers, data=form)
    print(response.json())

if __name__ == "__main__":
    # print(reply_to_thread(channels["arcade"], "1720266789.748599", "Test"))
    # unreplied = get_channel_messages()
    # print(unreplied)
    # for message in unreplied:
    #     reply_to_thread(channels["arcade"], message["ts"], "Test")

    print(post_command(channels["arcade"], "arcade", "test"))
    # print(post_action("arcade", "1720345345.827299", "pause"))
    # print(get_conversation_replies(channels["arcade"], "1720345345.827299"))
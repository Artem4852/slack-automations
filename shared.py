import dotenv, os, json

dotenv.load_dotenv()

headers = {
    "cookie": os.getenv("cookie"),
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}

urls = {
    "get_channel_messages": "https://hackclub.slack.com/api/conversations.view",
    "get_conversation_replies": "https://hackclub.slack.com/api/conversations.replies",
    "post_message": 'https://hackclub.slack.com/api/chat.postMessage',
    "post_command": "https://hackclub.slack.com/api/chat.command",
    "post_action": "https://hackclub.slack.com/api/blocks.actions",
    "submit_action": "https://hackclub.slack.com/api/views.submit"
}

channels = {
    "arcade": "C06SBHMQU8G",
    "arcade-help": "C077TSWKER0",
}

actions = {
    "pause": "[{\"action_id\":\"pause\",\"block_id\":\"panel\",\"text\":{\"type\":\"plain_text\",\"text\":\"Pause\",\"emoji\":true},\"value\":\"gf8epwufiarkmz701ckm2c28\",\"type\":\"button\"}]",
    "resume": "[{\"action_id\":\"resume\",\"block_id\":\"panel\",\"text\":{\"type\":\"plain_text\",\"text\":\"Resume\",\"emoji\":true},\"value\":\"gf8epwufiarkmz701ckm2c28\",\"type\":\"button\"}]"
}

forms = {
    "get_channel_messages": {
        "token": os.getenv("token"),
        "count": "28",
        "channel": "",
        "no_members": "true",
        "ignore_replies": "true"
    },
    "get_conversation_replies": {
        "token": os.getenv("token"),
        "channel": "",
        "ts": "",
        "inclusive": "true",
        "limit": "28"
    },
    "post_message": {
        "token": os.getenv("token"),
        "channel": "",
        "ts": "",
        "type": "message",
        "blocks": "[{{\"type\": \"rich_text\", \"elements\": [{{\"type\": \"rich_text_section\",\"elements\":[{{\"type\":\"text\",\"text\": \"{text}\"}}]}}]}}]"
    },
    "post_command": {
        "token": os.getenv("token"),
        "command": "",
        "disp": "",
        "blocks": "[{{\"type\": \"rich_text\", \"elements\": [{{\"type\": \"rich_text_section\",\"elements\":[{{\"type\":\"text\",\"text\": \"{text}\"}}]}}]}}]",
        "channel": ""
    },
    "post_action": {
        "token": os.getenv("token"),
        "actions": "",
        "container": "{{\"type\":\"message\",\"message_ts\":\"{ts}\",\"channel_id\":\"{channel}\",\"is_ephemeral\":false}}",
        "service_id": "B077ZPZ3RB7",
        "client_token": "web-1720344935585"
    }
}

def save_json(data, filename="data.json"):
    with open(filename, "w") as f: json.dump(data, f)
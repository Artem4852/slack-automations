import dotenv, os, json

dotenv.load_dotenv()

headers = {
    "cookie": os.getenv("cookie"),
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}

queries = {
    "full_hour": "in:#arcade from:@hakkuun has::tada:",
    "end_early": "in:#arcade from:@hakkuun has::exit:",
    "approved": "in:#arcade from:@hakkuun \"approved\"",
    "rejected": "in:#arcade from:@hakkuun \"rejected\"",
    "new_users": "from:@hakkuun \"welcome to your first\"",
    "on_day": " before:{end_date} after:{start_date}"
}

urls = {
    "get_channel_messages": "https://hackclub.slack.com/api/conversations.view",
    "get_conversation_replies": "https://hackclub.slack.com/api/conversations.replies",
    "post_message": 'https://hackclub.slack.com/api/chat.postMessage',
    "post_command": "https://hackclub.slack.com/api/chat.command",
    "post_action": "https://hackclub.slack.com/api/blocks.actions",
    "submit_view": "https://hackclub.slack.com/api/views.submit",
    "search": "https://hackclub.slack.com/api/search.modules.messages",
}

channels = {
    "arcade": "C06SBHMQU8G",
    "arcade-help": "C077TSWKER0",
}

actions = {
    "pause": "[{\"action_id\":\"pause\",\"block_id\":\"panel\",\"text\":{\"type\":\"plain_text\",\"text\":\"Pause\",\"emoji\":true},\"value\":\"gf8epwufiarkmz701ckm2c28\",\"type\":\"button\"}]",
    "resume": "[{\"action_id\":\"resume\",\"block_id\":\"panel\",\"text\":{\"type\":\"plain_text\",\"text\":\"Resume\",\"emoji\":true},\"value\":\"gf8epwufiarkmz701ckm2c28\",\"type\":\"button\"}]",
    "opengoal": "[{\"action_id\":\"opengoal\",\"block_id\":\"panel\",\"text\":{\"type\":\"plain_text\",\"text\":\"Change Goal\",\"emoji\":true},\"type\":\"button\"}]",
    "end": "[{\"action_id\":\"cancel\",\"block_id\":\"panel\",\"text\":{\"type\":\"plain_text\",\"text\":\"End Early\",\"emoji\":true},\"type\":\"button\"}]",
}

forms = {
    "get_channel_messages": {
        "token": "",
        "count": "28",
        "channel": "",
        "no_members": "true",
        "ignore_replies": "true"
    },
    "get_conversation_replies": {
        "token": "",
        "channel": "",
        "ts": "",
        "inclusive": "true",
        "limit": "28"
    },
    "post_message": {
        "token": "",
        "channel": "",
        "ts": "",
        "type": "message",
        "blocks": "[{{\"type\": \"rich_text\", \"elements\": [{{\"type\": \"rich_text_section\",\"elements\":[{{\"type\":\"text\",\"text\": \"{text}\"}}]}}]}}]"
    },
    "post_command": {
        "token": "",
        "command": "",
        "disp": "",
        "blocks": "[{{\"type\": \"rich_text\", \"elements\": [{{\"type\": \"rich_text_section\",\"elements\":[{{\"type\":\"text\",\"text\": \"{text}\"}}]}}]}}]",
        "channel": ""
    },
    "post_action": {
        "token": "",
        "actions": "",
        "container": '{{"type":"message","message_ts":"{ts}","channel_id":"{channel}","is_ephemeral":false}}',
        "service_id": "B077ZPZ3RB7",
        "client_token": "web-1720510987040"
    },
    "search": {
        "token": "",
        "module": "messages",
    }
}

def save_json(data, filename="data.json"):
    with open(filename, "w") as f: json.dump(data, f)
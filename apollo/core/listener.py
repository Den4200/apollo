from apollo.core.client import client, messages


def listen(updater, *_) -> None:
    msgs = client.get_new_msgs()

    if msgs:
        for msg_id, msg in msgs.items():
            messages.contents[msg_id] = msg
            updater(
                 f'[color=dd2020]{msg["from_user"]["username"]}[/color] > {msg["message"]}'
            )

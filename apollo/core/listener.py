from .client import messages


def listen(client, *_) -> None:
    msgs = client.get_new_msgs()

    if msgs:
        for msg_id, msg in msgs:
            messages.contents[msg_id] = msg

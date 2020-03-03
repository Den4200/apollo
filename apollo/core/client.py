from dataclasses import dataclass

from frost import FrostClient


@dataclass
class MessagesData:
    contents = dict()


# Store client & messages in memory globally
messages = MessagesData()
client = FrostClient()


def listen(_) -> None:
    msgs = client.get_new_msgs()

    if msgs:
        for msg_id, msg in msgs:
            messages.contents[msg_id] = msg

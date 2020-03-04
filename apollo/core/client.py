from dataclasses import dataclass

from frost import FrostClient


@dataclass
class MessagesData:
    contents = dict()


# Store client & messages in memory globally
messages = MessagesData()
client = FrostClient()

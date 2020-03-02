from typing import Any
from dataclasses import dataclass

from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout


Builder.load_file('apollo/core/messages.kv')


@dataclass
class MessagesData:
    contents = dict()


class MessagesScreen(Screen):

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class Messages(GridLayout):

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

    def send_message(self):
        msg = self.message_prompt.text
        print(f'Sending "{msg}"')
        self.message_prompt.text = ''

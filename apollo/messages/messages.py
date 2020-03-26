from typing import Any

from kivy.clock import Clock
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout

from apollo.rooms import Members, Rooms  # NOQA: F401
from apollo.messages.history import MessageHistory  # NOQA: F401
from apollo.core.client import client


Builder.load_file('apollo/messages/messages.kv')


class MessagesScreen(Screen):

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class Messages(GridLayout):

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

        Window.bind(on_key_down=self._on_key_down)
        self.bind(size=self._adjust_fields)

    def send_message(self):
        msg = self.message_prompt.text

        if msg:
            client.send_msg(1, msg)  # TODO: get current room id

        self.message_prompt.text = ''
        Clock.schedule_once(self._focus_text_input, 0.1)

    def _focus_text_input(self, _):
        self.message_prompt.focus = True

    def _on_key_down(self, instance, kb, keycode, text, modifiers):
        if keycode == 40:
            self.send_message()

    def _adjust_fields(self, *_):
        """
        Adjust all fields when window is resized.
        """
        # Chat history height - 90%, but at least 50px for bottom new message/send button part
        if Window.size[1] * 0.1 < 50:
            new_height = Window.size[1] - 50
        else:
            new_height = Window.size[1] * 0.9

        self.message_history.height = new_height

        # Message prompt width - 80%, but at least 160px for send button
        if Window.size[0] * 0.2 < 160:
            new_width = Window.size[0] - 160
        else:
            new_width = Window.size[0] * 0.8

        self.message_prompt.width = new_width

        Clock.schedule_once(self.message_history._update_chat_history_layout, 0.01)

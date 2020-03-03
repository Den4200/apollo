from typing import Any

from kivy.clock import Clock
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout

from .history import ScrollableLabel  # NOQA: F401


Builder.load_file('apollo/messages/messages.kv')


class MessagesScreen(Screen):

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class Messages(GridLayout):

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        Window.bind(on_key_down=self._on_key_down)

    def send_message(self):
        msg = self.message_prompt.text

        if msg:
            self.message_history.update_chat_history(f'[color=dd2020]f1re[/color] > {msg}')

        self.message_prompt.text = ''
        Clock.schedule_once(self._focus_text_input, 0.1)

    def _focus_text_input(self, _):
        self.message_prompt.focus = True

    def _on_key_down(self, instance, kb, keycode, text, modifiers):
        if keycode == 40:
            self.send_message()

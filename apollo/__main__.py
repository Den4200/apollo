from typing import Any

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from .core.login import LoginScreen
from .core.messages import MessagesScreen


class Manager(ScreenManager):

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.add_widget(LoginScreen(name='login_screen'))
        self.add_widget(MessagesScreen(name='messages_screen'))


class Apollo(App):

    def build(self):
        return Manager()


if __name__ == "__main__":
    Apollo().run()

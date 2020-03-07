from typing import Any

from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager

from apollo.core.login import LoginScreen  # NOQA: F401
from apollo.core.register import RegisterScreen  # NOQA: F401
from apollo.messages import MessagesScreen  # NOQA: F401


Builder.load_file('apollo/core/screen_manager.kv')


class Manager(ScreenManager):

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

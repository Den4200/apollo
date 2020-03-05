from functools import partial

from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.screenmanager import Screen

from ..listener import listen
from ..client import client, messages

Builder.load_file('apollo/core/login/login.kv')


class LoginScreen(Screen):

    def login(self, username, password):
        client.login(username, password)

        # Display previous chat messages
        msgs = client.get_all_msgs()
        for msg_id, msg in msgs.items():
            messages.contents[msg_id] = msg

            self.manager.messages_screen.messages.message_history.update_chat_history(
                f'[color=dd2020]{msg["from_user"]["username"]}[/color] > {msg["message"]}'
            )

        Clock.schedule_interval(partial(
            listen,
            self.manager.messages_screen.messages.message_history.update_chat_history
        ), 0.25)

        self.manager.current = 'messages_screen'

    def reset_form(self):
        self.ids['username'].text = ''
        self.ids['password'].text = ''

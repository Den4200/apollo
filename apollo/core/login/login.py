from functools import partial

from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen

from frost.client import Status

from apollo.core.listener import listen
from apollo.core.client import client, messages

Builder.load_file('apollo/core/login/login.kv')


class LoginScreen(Screen):

    def login(self, username, password):
        status = client.login(username, password)

        if status == Status.SUCCESS.value:
            # Display previous chat messages
            msgs = client.get_all_msgs()
            updater = self.manager.messages_screen.messages.message_history.update_chat_history
            for msg_id, msg in msgs.items():
                messages.contents[msg_id] = msg

                updater(
                    f'[color=dd2020]{msg["from_user"]["username"]}[/color] > {msg["message"]}'
                )

            Clock.schedule_interval(partial(listen, updater), 0.25)

            self.manager.current = 'messages_screen'

        else:
            LoginFailure().open()

        self.reset_form()

    def reset_form(self):
        self.ids['username'].text = ''
        self.ids['password'].text = ''


class LoginFailure(Popup):
    pass

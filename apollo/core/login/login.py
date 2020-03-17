from functools import partial

from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen

from frost.client import Status
from frost.client.events import login_status

from apollo.core.listener import listen
from apollo.core.client import client

Builder.load_file('apollo/core/login/login.kv')


class LoginScreen(Screen):

    def login(self, username, password):
        client.login(username, password)

        status = None
        while status is None:
            status = login_status.get_status()

        if status == Status.SUCCESS.value:
            updater = self.manager.messages_screen.messages.message_history.update_chat_history
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

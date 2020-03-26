from functools import partial

from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen

from frost.client import Status

from apollo.utils import get_status
from apollo.core.listener import listen
from apollo.core.client import client

Builder.load_file('apollo/core/login/login.kv')


class LoginScreen(Screen):

    def login(self, username, password):
        client.login(username, password)

        status = get_status('login')
        if status == Status.SUCCESS.value:
            self.manager.messages_screen.rooms.update()
            Clock.schedule_interval(partial(listen, self.manager), 0.25)
            self.manager.current = 'messages_screen'

        else:
            LoginFailure().open()

        self.reset_form()

    def reset_form(self):
        self.ids['username'].text = ''
        self.ids['password'].text = ''


class LoginFailure(Popup):
    pass

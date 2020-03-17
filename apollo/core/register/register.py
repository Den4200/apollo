from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen

from frost.client import Status
from frost.client.events import register_status

from apollo.core.client import client


Builder.load_file('apollo/core/register/register.kv')


class RegisterScreen(Screen):

    def register(self, username, password):
        client.register(username, password)

        status = None
        while status is None:
            status = register_status.get_status()

        if status == Status.SUCCESS.value:
            self.manager.current = 'login_screen'

        else:
            RegistrationFailure().open()

        self.reset_form()

    def reset_form(self):
        self.ids['username'].text = ''
        self.ids['password'].text = ''


class RegistrationFailure(Popup):
    pass

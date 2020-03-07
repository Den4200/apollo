from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

from apollo.core.client import client


Builder.load_file('apollo/core/register/register.kv')


class RegisterScreen(Screen):

    def register(self, username, password):
        client.register(username, password)
        self.manager.current = 'login_screen'

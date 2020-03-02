from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

Builder.load_file('apollo/core/login/login.kv')


class LoginScreen(Screen):

    def login(self, username, password):
        self.manager.current = 'messages_screen'

    def reset_form(self):
        self.ids['username'].text = ''
        self.ids['password'].text = ''

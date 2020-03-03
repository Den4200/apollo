from kivy.app import App

from .core import client
from .core import Manager


class Apollo(App):

    def build(self):
        client.connect()
        return Manager()


if __name__ == "__main__":
    try:
        Apollo().run()

    finally:
        client.close()

from typing import Any

from kivy.lang import Builder
from kivy.uix.scrollview import ScrollView


Builder.load_file('apollo/messages/history.kv')


class ScrollableLabel(ScrollView):

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

    def update_chat_history(self, message):
        # Adds new line & new message
        self.chat_history.text += f'\n{message}'

        # Set layout height to whatever height of chat history text is + 15 pixels
        # Set chat history label to whatever height of chat history text is
        # Set width of chat history text to 98 of the label width (adds small margins)
        self.layout.height = self.chat_history.texture_size[1] + 15
        self.chat_history.height = self.chat_history.texture_size[1]
        self.chat_history.text_size = (self.chat_history.width * 0.98, None)

        # Auto scroll down to the latest message
        self.scroll_to(self.scroll_to_point)

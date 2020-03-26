from typing import Any

from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.recycleview import RecycleView
from kivy.properties import (
    NumericProperty,
    ObjectProperty,
    StringProperty
)
from frost.client import Memory

from apollo.utils import get_status
from apollo.core.client import client


Builder.load_file('apollo/rooms/rooms.kv')


class Rooms(RecycleView):

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

        self.currently_highlighted = None
        self.prev_highlighted = None
        self.data = list()

    def update(self):
        client.get_joined_rooms()

        # wait until we receive the joined rooms
        get_status('get_joined_rooms')

        rooms = Memory.rooms.values()
        self.data = [
            {
                'ctx': self,
                'alpha': 0,
                'name': room.name,
                'id': room.id
            } for room in rooms
        ]

    def highlight(self, room):
        if self.prev_highlighted is not None:
            self.prev_highlighted.alpha = 0

        room.alpha = 0.5
        self.currently_highlighted = room


class Room(Label):
    ctx = ObjectProperty()
    alpha = NumericProperty()
    name = StringProperty()
    id = NumericProperty()

    def on_mouse_pos(self, window, pos):
        if self.collide_point(*pos):
            self.ctx.highlight(self)

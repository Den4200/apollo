from typing import Any

from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.recycleview import RecycleView
from kivy.properties import (
    NumericProperty,
    ObjectProperty,
    StringProperty
)
from frost.client import Memory, Status

from apollo.utils import get_status
from apollo.core.client import client


Builder.load_file('apollo/rooms/members.kv')


class Members(RecycleView):

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

        self.currently_highlighted = None
        self.data = list()

    def update(self):
        room_id = 1  # TODO: get currently selected room id
        client.get_room_members(room_id)

        status = get_status('get_room_members')
        if status == Status.SUCCESS.value:
            print(Memory.get_room_member_changes())


class Member(Label):
    ctx = ObjectProperty()
    alpha = NumericProperty()

    username = StringProperty()
    id = NumericProperty()

    def on_mouse_pos(self, window, pos):
        if self.collide_point(*pos):
            self.ctx.highlight(self)

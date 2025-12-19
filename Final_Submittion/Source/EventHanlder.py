import flet as ft
from Controls.InputControl import InputControl


class EventHandler:
    def __init__(self, page: ft.Page):
        self.page = page
        self.input_control = InputControl(page)

    def get_user_input(self):
        return (self.input_control.
                get_input())

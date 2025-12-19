import flet as ft
from OutputControl import OutputControl
from InputControl import InputControl


class EventHandler:
    def __init__(self, page: ft.Page):
        self.page = page
        self.output_control = OutputControl(page)
        self.input_control = InputControl(page)

    def display_output(self, output):
        self.output_control.update_output(output)

    def get_user_input(self):
        return (self.input_control.
                get_input())

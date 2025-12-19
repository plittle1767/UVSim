import flet as ft
from Controls.OutputControl import OutputControl
from Controls.InputControl import InputControl


class EventHandler:
    def __init__(self, page: ft.Page):
        self.page = page
        self.output_control = OutputControl(page)
        self.input_control = InputControl(page)

    def display_output(self, output):
        self.output_control.display_output(output)

    def get_user_input(self):
        return (self.input_control.
                get_input())

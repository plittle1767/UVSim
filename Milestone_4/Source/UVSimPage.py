import flet as ft
from OutputControl import OutputControl
from InputControl import InputControl
from FileHandler import FileHandler


class UVSimPage(ft.Row):

    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.output_buttons = OutputControl(page)
        self.input_buttons = InputControl(page)
        self.page.update()

    def build(self):
        return ft.Column(
            [
                self.output_buttons.build(),
                self.program_layout()
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,

        )

    def run_button_result(self, e):
        FileHandler(self.page).operation.execute()

    def stop_button_result(self, e):
        FileHandler(self.page).operation.stop_execution()

    def program_layout(self):
        return ft.Column(
            [
                ft.Row(
                    [self.run_button(), self.stop_button()],
                    spacing=10,
                    alignment=ft.MainAxisAlignment.CENTER,
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )

    def run_button(self):
        return ft.ElevatedButton(
            content=ft.Container(
                content=ft.Row(
                    [
                        ft.Icon(ft.icons.START_ROUNDED, size=50),
                        ft.Text("Run", size=50),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                ),
            ),
            on_click=self.run_button_result,

        )

    def stop_button(self):
        return ft.ElevatedButton(
            content=ft.Container(
                content=ft.Row(
                    [
                        ft.Icon(ft.icons.STOP, size=50),
                        ft.Text("Stop", size=50),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                ),
                on_click=self.stop_button_result,
            ),
        )

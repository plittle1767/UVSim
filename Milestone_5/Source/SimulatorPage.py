import flet as ft
from Controls.FileHandler import FileHandler
from Controls.OutputControl import OutputControl
from Controls.InputControl import InputControl


class SimulatorPage(ft.Row):

    def __init__(self, page: ft.Page, sim_id, file_path):
        super().__init__()
        self.page = page
        self.sim_id = sim_id
        self.output_buttons = OutputControl(page)
        self.input_buttons = InputControl(page)
        self.file_handler = FileHandler(page, file_path)
        self.page.scroll = True
        self.controls = [
            ft.Row(
                [
                    ft.Column(
                        [
                            self.buttons_layout(),
                            self.output_buttons,
                        ],
                        # alignment=ft.MainAxisAlignment.START,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,

                    ),
                    self.file_handler.build(),
                ],
                spacing=50,
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                vertical_alignment=ft.CrossAxisAlignment.START,
            )
        ]

    def set_sim_id(self, sim_id):
        self.sim_id = sim_id
        self.page.update()

    def run_button_result(self, e):
        self.file_handler.load_file_into_register(self.file_handler.text_file_path)
        self.file_handler.operation.execute()

    def stop_button_result(self, e):
        self.file_handler.operation.stop_execution()

    def buttons_layout(self):
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


import flet as ft


class OutputControl(ft.Row):
    output_text = ft.Ref[ft.TextField]()

    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.display = ft.Column(
            [
                ft.Row(
                    [
                        ft.Container(
                            content=ft.Text("Output", size=50),
                            alignment=ft.alignment.center,
                            width=500,
                            height=75,
                            border_radius=15,
                            bgcolor=ft.colors.TERTIARY,
                            margin=15,
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
        self._active_view: ft.Control = self.display
        self.controls = [self.active_view]

    @property
    def active_view(self):
        return self._active_view

    @active_view.setter
    def active_view(self, value):
        self._active_view = value
        self.controls.append(self._active_view)
        self.update()

    # def display_output_title(self):
    #     return ft.Column(
    #         [
    #             ft.Card(
    #                 content=ft.Container(
    #                     content=ft.Text("Output", size=50, color="white"),
    #                     alignment=ft.alignment.center,
    #                     width=200,
    #                     height=100,
    #                     border_radius=15,
    #                 )
    #             ),
    #
    #         ],
    #         alignment=ft.MainAxisAlignment.CENTER,
    #     )

    def display_output(self, output):
        self.display.controls.append(ft.Row(
            [
                ft.Card(
                    content=ft.Container(
                        content=ft.Text(output, size=25),
                        alignment=ft.alignment.center,
                        width=200,
                        height=60,
                        border_radius=15,
                    )
                ),

            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ))
        self.page.update()
        # self.output_text.current.value = output
        # self.page.update()

    # def build(self):
    #     self.page.update()
    #     return ft.Row(
    #         [
    #             self.display_output_title(),
    #         ],
    #         alignment=ft.MainAxisAlignment.CENTER,
    #     )

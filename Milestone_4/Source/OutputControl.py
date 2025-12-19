import flet as ft


class OutputControl(ft.Row):
    output_text = ft.Ref[ft.TextField]()

    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

    def display_output(self):
        return ft.Column(
            [
                ft.Card(
                    content=ft.Container(
                        content=ft.Text("Output", size=50, color="white"),
                        alignment=ft.alignment.center,
                        width=200,
                        height=100,
                        border_radius=15,
                    )
                ),
                ft.TextField(ref=self.output_text,
                             read_only=True,
                             # on_change=self.update_output,
                             bgcolor="grey",
                             width=200,
                             height=100,
                             border_radius=15,
                             )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )

    def update_output(self, output):
        self.output_text.current.value = output
        self.page.update()

    def build(self):
        self.page.update()
        return ft.Row(
            [
                self.display_output(),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
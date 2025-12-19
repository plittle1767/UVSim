import flet as ft
from UVSim import Operations


def main(page: ft.Page):
    files = ft.Ref[ft.Column]()
    start_button = ft.Ref[ft.ElevatedButton]()
    operation = Operations(page)

    page.title = "UVSim"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def file_picker_result(e: ft.FilePickerResultEvent):
        start_button.current.disabled = True if e.files is None else False
        files.value = (
            ", ".join(map(lambda f: f.name, e.files)) if e.files else "Cancelled!"
        )
        if e.files is not None:
            for f in e.files:
                operation.read_file(str(f.path))

        page.update()

    def run_button_result(e):
        operation.execute()

    file_picker = ft.FilePicker(on_result=file_picker_result)
    page.overlay.append(file_picker)

    def display_select_file_button():
        return ft.ElevatedButton(
            content=ft.Container(
                content=ft.Row(
                    [
                        ft.Icon(ft.icons.FOLDER_OPEN, size=50),
                        ft.Text("Select files", size=50),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                ),
                on_click=lambda _: file_picker.pick_files(allow_multiple=False),
            ),
        )

    def program_layout():
        return ft.Column(
            [
                ft.Row(
                    [display_select_file_button(), run_button(), stop_button()],
                    spacing=10,
                    alignment=ft.MainAxisAlignment.CENTER,
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )

    def run_button():
        return ft.ElevatedButton(
            ref=start_button,
            content=ft.Container(
                content=ft.Row(
                    [
                        ft.Icon(ft.icons.START_ROUNDED, size=50),
                        ft.Text("Run", size=50),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                ),
            ),
            on_click=run_button_result,
            disabled=True
        )

    def stop_button():
        return ft.ElevatedButton(
            content=ft.Container(
                content=ft.Row(
                    [
                        ft.Icon(ft.icons.STOP, size=50),
                        ft.Text("Stop", size=50),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                ),
                on_click=lambda _: operation.stop_execution()
            ),
        )

    def display_layout():
        display = ft.Column(
            [
                ft.Row(
                    [
                        display_output()],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
        return display

    def display_output():
        output_text = operation.get_output()
        return ft.Column(
            [
                ft.Container(
                    content=ft.Text("Output", size=50),
                    alignment=ft.alignment.center,
                    bgcolor="green200",
                    width=200,
                    height=100,
                    border_radius=15,
                ),
                ft.Container(
                    content=ft.Text(output_text, size=50),
                    alignment=ft.alignment.center,
                    bgcolor="grey",
                    width=200,
                    height=100,
                    border_radius=15,
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )

    page.add(
        display_layout(),
        program_layout(),
    )


ft.app(target=main)

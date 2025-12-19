import flet as ft
from Operations import Operations


class FileEditor(ft.Row):

    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.operation = Operations(page)
        self.file_picker = ft.FilePicker(on_result=self.file_picker_result)
        self.save_file_dialog = ft.FilePicker(on_result=self.save_file_result)
        self.page.overlay.extend([self.file_picker, self.save_file_dialog])
        self.textfield = ft.TextField(multiline=True,
                                      autofocus=True,
                                      border=ft.InputBorder.OUTLINE,
                                      bgcolor=ft.colors.YELLOW_50,
                                      border_color=ft.colors.BLACK,
                                      min_lines=0,
                                      max_lines=100,
                                      content_padding=50,
                                      cursor_color=ft.colors.BLACK, )
        self.text_file_path = None
        self.menubar = ft.MenuBar(
            style=ft.MenuStyle(
                alignment=ft.alignment.top_left,
                mouse_cursor={ft.MaterialState.HOVERED: ft.MouseCursor.WAIT,
                              ft.MaterialState.DEFAULT: ft.MouseCursor.ZOOM_OUT},
            ),
            controls=[
                ft.SubmenuButton(
                    content=ft.Text("File", color="white"),
                    controls=[
                        ft.MenuItemButton(
                            content=ft.Text("Open New file", color="white"),
                            leading=ft.Icon(ft.icons.FOLDER_OPEN, color="white"),
                            on_click=lambda _: self.file_picker.pick_files(allow_multiple=False)
                        ),
                        ft.MenuItemButton(
                            content=ft.Text("Save", color="white"),
                            leading=ft.Icon(ft.icons.SAVE, color="white"),
                            on_click=lambda _: self.save_file_dialog.save_file(),
                        ),

                    ]
                ),
                ft.MenuItemButton(
                    content=ft.Text("Load File", color="white"),
                    on_click=self.go_to_UVSim

                ),
            ]
        )

        self.page.update()

    def build(self):
        self.textfield.value = self.get_text_field_value()
        return ft.Column(
            [
                ft.Row([self.menubar]),
                self.textfield
            ],
            horizontal_alignment=ft.CrossAxisAlignment.START,
        )

    def go_to_UVSim(self, e):
        self.operation.read_file(self.text_file_path)

    def file_picker_result(self, e: ft.FilePickerResultEvent):
        if e.files is not None:
            self.text_file_path = str(e.files[0].path)
            self.textfield.value = self.open_file(self.text_file_path)
            self.page.update()

    def save_file_result(self, e: ft.FilePickerResultEvent):
        save_file_path = e.path
        if save_file_path:
            try:
                self.save_text(save_file_path, self.textfield.value)
            except FileNotFoundError:
                self.textfield.hint_text = "File not found"

    def save_text(self, path, value):
        with open(path, "w") as file:
            file.write(value)

    def open_file(self, user_file):
        try:
            with open(user_file, "r") as file:
                return file.read()
        except FileNotFoundError:
            self.textfield.hint_text = "File not found"

    def get_text_field_value(self):
        if self.text_file_path is not None:
            self.textfield.value = self.open_file(self.text_file_path)
        else:
            self.textfield.value = "Edit file here..."
            self.textfield.color = "black"
            self.textfield.bgcolor = "white"
        return self.textfield.value

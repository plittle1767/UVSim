import flet as ft
from Operations import Operations


class FileHandler(ft.Row):

    def __init__(self, page: ft.Page, file_path):
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
                                      border_radius=15,
                                      min_lines=0,
                                      max_lines=100,
                                      content_padding=50,
                                      cursor_color=ft.colors.BLACK,
                                      input_filter=ft.InputFilter(allow=True, regex_string=r"[0-9\+\-\n]")
                                      )
        self.text_file_path = file_path
        self.menubar = ft.MenuBar(
            style=ft.MenuStyle(
                alignment=ft.alignment.top_left,
                mouse_cursor={ft.MaterialState.HOVERED: ft.MouseCursor.WAIT,
                              ft.MaterialState.DEFAULT: ft.MouseCursor.ZOOM_OUT},
            ),
            controls=[
                ft.SubmenuButton(
                    content=ft.Text("File"),
                    controls=[
                        ft.MenuItemButton(
                            content=ft.Text("Open New file"),
                            leading=ft.Icon(ft.icons.FOLDER_OPEN),
                            on_click=lambda _: self.file_picker.pick_files(allow_multiple=False)
                        ),

                    ]
                ),
                ft.MenuItemButton(
                    content=ft.Text("Save and Load File"),
                    on_click=self.save_load_file

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

    def save_load_file(self, e):
        if self.text_file_path is None:
            self.save_file_dialog.save_file()
        else:
            self.operation.read_file(self.text_file_path)

    def file_picker_result(self, e: ft.FilePickerResultEvent):
        if e.files is not None:
            self.text_file_path = str(e.files[0].path)
            self.textfield.value = self.open_file(self.text_file_path)
            self.page.update()

    def save_file_result(self, e: ft.FilePickerResultEvent):
        save_file_path = e.path
        self.text_file_path = save_file_path
        if save_file_path:
            try:
                self.save_text(save_file_path, self.textfield.value)
                self.operation.read_file(save_file_path)
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
            self.textfield.hint_text = "Add BasicML instructions here or upload a new file..."
        return self.textfield.value

    def load_file_into_register(self, file_path):
        self.operation.read_file(file_path)

    def run_program(self):
        self.operation.execute()

    def stop_program(self):
        self.operation.stop_execution()

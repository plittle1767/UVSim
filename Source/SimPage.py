import flet as ft
from Operations import Operations


class SimPage(ft.Row):
    def __init__(self, page: ft.Page, app_layout, file_path, file_name):
        super().__init__()
        self.page = page
        self.app_layout = app_layout
        self.operation = Operations(page, self)
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
                                      max_lines=249,
                                      content_padding=10,
                                      cursor_color=ft.colors.BLACK,
                                      input_filter=ft.InputFilter(allow=True, regex_string=r"[0-9\+\-\n]")
                                      )
        self.output_textfield = ft.TextField(multiline=True,
                                             autofocus=True,
                                             border=ft.InputBorder.OUTLINE,
                                             bgcolor=ft.colors.SECONDARY_CONTAINER,
                                             border_color=ft.colors.BLACK,
                                             border_radius=15,
                                             min_lines=0,
                                             content_padding=50,
                                             read_only=True,
                                             )
        self.output_list = []
        self.text_file_path = file_path
        self.file_name = file_name
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
                ft.MenuItemButton(
                    content=ft.Text("Run"),
                    leading=ft.Icon(ft.icons.START_ROUNDED),
                    on_click=self.run_button_result,
                )
            ]
        )
        self.controls = [self.build()]
        self.page.update()

    def build(self):
        self.textfield.value = self.get_text_field_value()
        self.output_textfield.value = self.update_text_field()
        return ft.Column(
            [
                ft.Row([
                    self.menubar,
                    ft.Container(
                        content=ft.Text("Output", size=50),
                        width=500,
                        border_radius=15,
                        alignment=ft.alignment.center,
                        bgcolor=ft.colors.TERTIARY,
                    )
                ]),
                ft.Row([
                    self.textfield,
                    self.output_textfield
                ],
                    vertical_alignment=ft.CrossAxisAlignment.START,
                    expand=True),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.START,
            spacing=30
        )

    def save_load_file(self, e):
        if self.text_file_path is None:
            self.save_file_dialog.save_file()
        else:
            with open(self.text_file_path, "w") as file:
                file.write(self.textfield.value)
            self.operation.read_file(self.text_file_path)

    def file_picker_result(self, e: ft.FilePickerResultEvent):
        if e.files is not None:
            self.text_file_path = str(e.files[0].path)
            self.textfield.value = self.open_file(self.text_file_path)
            self.app_layout.sim_pages[e.files[0].name] = self
            del self.app_layout.sim_pages[self.file_name]
            self.app_layout.sidebar.sync_sim_destinations()
            self.page.go(f"/simulator/{e.files[0].name}")

        self.output_textfield.value = self.update_text_field()
        self.page.update()

    def save_file_result(self, e: ft.FilePickerResultEvent):
        save_file_path = e.path
        self.text_file_path = save_file_path
        if save_file_path:
            try:
                with open(save_file_path, "w") as file:
                    file.write(self.textfield.value)
                self.operation.read_file(save_file_path)
            except FileNotFoundError:
                self.textfield.hint_text = "File not found"

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

    def update_text_field(self):
        if self.output_list is not None:
            self.output_textfield.value = "\n".join(self.output_list)
        return self.output_textfield.value

    def run_button_result(self, e):
        self.operation.read_file(self.text_file_path)
        self.operation.execute()

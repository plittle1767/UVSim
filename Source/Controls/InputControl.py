import flet as ft


class InputControl(ft.AlertDialog):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.got_input = False

    def build(self):
        return self.get_input()

    def get_input(self):
        def close_dlg(e):
            self.got_input = True
            dialog.open = False
            self.page.update()

        def textfield_change(e):
            if user_input.value == "":
                send_button.disabled = True
            else:
                send_button.disabled = False
            self.page.update()

        user_input = ft.TextField(label="Input Here", text_size=50, on_change=textfield_change)
        send_button = ft.ElevatedButton(text="Send", on_click=close_dlg, disabled=True)
        dialog = ft.AlertDialog(
            modal=False,
            title=ft.Text("Insert a Value", size=50),
            actions=[
                ft.Column(
                    [
                        user_input,
                        send_button,
                    ]
                ),
            ],
        )
        self.page.dialog = dialog
        dialog.open = True
        self.page.update()
        user_input.focus()
        while not self.got_input:
            pass
        self.got_input = False
        return user_input.value

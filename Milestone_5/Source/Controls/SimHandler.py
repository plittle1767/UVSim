# import flet as ft
# from Controls.OutputControl import OutputControl
# from Controls.InputControl import InputControl
# from Controls.FileHandler import FileHandler
#
#
# class SimHandler(ft.Row):
#
#     def __init__(self, page: ft.Page):
#         super().__init__()
#         self.page = page
#         self.output_buttons = OutputControl(page)
#         self.input_buttons = InputControl(page)
#         self.page.update()
#
#     def build(self):
#         return ft.Column(
#             [
#                 self.output_buttons.build(),
#                 self.buttons_layout(),
#             ],
#             alignment=ft.MainAxisAlignment.START,
#             horizontal_alignment=ft.CrossAxisAlignment.CENTER,
#
#         )
#
#     def run_button_result(self, e):
#         FileHandler(self.page).operation.execute()
#
#     def stop_button_result(self, e):
#         FileHandler(self.page).operation.stop_execution()
#
#     def buttons_layout(self):
#         return ft.Column(
#             [
#                 ft.Row(
#                     [self.run_button(), self.stop_button()],
#                     spacing=10,
#                     alignment=ft.MainAxisAlignment.CENTER,
#                 )
#             ],
#             horizontal_alignment=ft.CrossAxisAlignment.CENTER,
#         )
#
#     def run_button(self):
#         return ft.ElevatedButton(
#             content=ft.Container(
#                 content=ft.Row(
#                     [
#                         ft.Icon(ft.icons.START_ROUNDED, size=50),
#                         ft.Text("Run", size=50),
#                     ],
#                     alignment=ft.MainAxisAlignment.SPACE_AROUND,
#                 ),
#             ),
#             on_click=self.run_button_result,
#
#         )
#
#     def stop_button(self):
#         return ft.ElevatedButton(
#             content=ft.Container(
#                 content=ft.Row(
#                     [
#                         ft.Icon(ft.icons.STOP, size=50),
#                         ft.Text("Stop", size=50),
#                     ],
#                     alignment=ft.MainAxisAlignment.SPACE_AROUND,
#                 ),
#                 on_click=self.stop_button_result,
#             ),
#         )

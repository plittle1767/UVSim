import flet as ft
from UVSimPage import UVSimPage
from Topbar import Topbar
from FileHandler import FileHandler


def main(page: ft.Page):
    page.title = "UVSim"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.scroll = True
    page.appbar = Topbar(page).build()
    page.add(
        ft.Row(
            [
                UVSimPage(page).build(),
                FileHandler(page).build(),
            ],
            spacing=10,
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            vertical_alignment=ft.CrossAxisAlignment.START,
        ),
    )
    page.update()


ft.app(target=main)

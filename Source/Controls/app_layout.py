import flet as ft

from Controls.Sidebar import Sidebar
from SimPage import SimPage


class AppLayout(ft.Row):
    sim_pages = {}

    def __init__(self, page: ft.Page, topbar, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page = page
        self.topbar = topbar
        self.page.on_resize = self.page_resize
        self.file_picker = ft.FilePicker(on_result=self.file_picker_result)
        self.page.overlay.append(self.file_picker)
        self.toggle_nav_rail_button = ft.IconButton(
            icon=ft.icons.ARROW_CIRCLE_LEFT,
            selected=False,
            selected_icon=ft.icons.ARROW_CIRCLE_RIGHT,
            on_click=self.toggle_nav_rail,
        )
        self.sidebar = Sidebar(self, page, self.sim_pages)
        self.home_view = self.home_page_view()
        self._active_view: ft.Control = self.home_view
        self.controls = [self.sidebar,
                         self.toggle_nav_rail_button,
                         self.active_view]

    def home_page_view(self):
        return ft.Column(
            [
                ft.Row(
                    [
                        ft.Container(
                            ft.Text("Welcome to UVSim", theme_style=ft.TextThemeStyle.HEADLINE_LARGE),
                            expand=True,
                            padding=ft.padding.only(top=15)
                        ),
                        ft.Container(
                            content=ft.ElevatedButton(
                                "Add new simulator",
                                icon=ft.icons.ADD,
                                on_click=lambda _: self.file_picker.pick_files(allow_multiple=True),
                            ),
                            padding=ft.padding.only(right=50, top=15)
                        ),
                    ]
                ),
                ft.Row([ft.Text("No Simulator Available")])
            ],
            expand=True,
        )

    @property
    def active_view(self):
        return self._active_view

    @active_view.setter
    def active_view(self, value):
        self._active_view = value
        self.controls[-1] = self._active_view
        self.sidebar.sync_sim_destinations()
        self.update()

    def set_sim_view(self, file_name):
        index = 0
        for f in self.sim_pages:
            if f == file_name:
                break
            index += 1
        self.active_view = self.sim_pages[file_name]
        self.sidebar.top_nav_rail.selected_index = None
        self.sidebar.bottom_nav_rail.selected_index = index
        self.sidebar.update()
        self.page.update()
        self.page_resize()

    def set_all_sim_view(self):
        self.active_view = self.home_view
        self.hydrate_all_sim_view()
        self.sidebar.top_nav_rail.selected_index = 0
        self.sidebar.bottom_nav_rail.selected_index = None
        self.sidebar.update()
        self.page.update()

    def page_resize(self, e=None):
        if self.active_view in self.sim_pages:
            self.active_view.resize(
                self.sidebar.visible, self.page.width, self.page.height
            )
        self.page.update()

    def hydrate_all_sim_view(self):
        self.home_view.controls[-1] = ft.Row(
            [
                ft.Container(
                    content=ft.Row(
                        [
                            ft.Container(
                                content=ft.Text(value=s, theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
                                data=s,
                                expand=True,
                                on_click=self.go_to_simulator,
                            ),
                            ft.Container(
                                content=ft.PopupMenuButton(
                                    items=[
                                        ft.PopupMenuItem(
                                            content=ft.Text(
                                                value="Delete",
                                            ),
                                            data=s,
                                            on_click=self.delete_sim_link,
                                        )
                                    ]
                                ),
                                padding=ft.padding.only(right=-10),
                                border_radius=ft.border_radius.all(3),
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    border=ft.border.all(1),
                    border_radius=ft.border_radius.all(5),
                    bgcolor=ft.colors.SECONDARY_CONTAINER,
                    padding=ft.padding.all(10),
                    width=250,
                    data=s,
                )
                for s in self.sim_pages
            ],
            wrap=True,
        )
        self.sidebar.sync_sim_destinations()

    def file_picker_result(self, e: ft.FilePickerResultEvent):
        for file in e.files:
            self.sim_pages.update({
                file.name: SimPage(self.page, self, file.path, file.name)
            })

        self.hydrate_all_sim_view()
        self.page.update()

    def go_to_simulator(self, e):
        self.page.go(f"/simulator/{e.control.data}")

    def toggle_nav_rail(self, e):
        self.sidebar.visible = not self.sidebar.visible
        self.toggle_nav_rail_button.selected = not self.toggle_nav_rail_button.selected
        self.page_resize()
        self.page.update()

    def delete_sim_link(self, e):
        del self.sim_pages[e.control.data]
        self.set_all_sim_view()

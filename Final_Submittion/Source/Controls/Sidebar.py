import flet as ft


class Sidebar(ft.UserControl):

    def __init__(self, app_layout, page, sim_pages):
        super().__init__()
        self.app_layout = app_layout
        self.page = page
        self.sim_pages = sim_pages
        self.view = None
        self.nav_rail_visible = True
        self.top_nav_items = [
            ft.NavigationRailDestination(
                label_content=ft.Text("All Simulations"),
                label="Simulations",
                icon=ft.icons.MONITOR,
                selected_icon=ft.icons.MONITOR_OUTLINED,
            ),

        ]
        self.top_nav_rail = ft.NavigationRail(
            selected_index=None,
            label_type=ft.NavigationRailLabelType.ALL,
            on_change=self.top_nav_change,
            destinations=self.top_nav_items,
            extended=True,
            height=110,
            bgcolor=ft.colors.SECONDARY_CONTAINER,
        )
        self.bottom_nav_rail = ft.NavigationRail(
            selected_index=None,
            label_type=ft.NavigationRailLabelType.ALL,
            on_change=self.bottom_nav_change,
            extended=True,
            expand=True,
            bgcolor=ft.colors.SECONDARY_CONTAINER,
        )
        self.toggle_nav_rail_button = ft.IconButton(ft.icons.ARROW_BACK)

    def build(self):
        self.view = ft.Container(
            content=ft.Column([
                ft.Row([
                    ft.Text("Workspace"),
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                # divider
                ft.Container(
                    bgcolor=ft.colors.TERTIARY,
                    border_radius=ft.border_radius.all(30),
                    height=1,
                    alignment=ft.alignment.center_right,
                    width=220
                ),
                self.top_nav_rail,
                # divider
                ft.Container(
                    bgcolor=ft.colors.TERTIARY,
                    border_radius=ft.border_radius.all(30),
                    height=1,
                    alignment=ft.alignment.center_right,
                    width=220
                ),
                self.bottom_nav_rail
            ], tight=True),
            padding=ft.padding.all(15),
            margin=ft.margin.all(0),
            width=250,
            expand=True,
            bgcolor=ft.colors.SECONDARY_CONTAINER,
            visible=self.nav_rail_visible,
        )
        return self.view

    def sync_sim_destinations(self):
        self.bottom_nav_rail.destinations = []
        for file_name in self.sim_pages:
            self.bottom_nav_rail.destinations.append(
                ft.NavigationRailDestination(
                    label_content=ft.Text(file_name, data=file_name),
                    label=file_name,
                    selected_icon=ft.icons.CHEVRON_RIGHT_ROUNDED,
                    icon=ft.icons.CHEVRON_RIGHT_OUTLINED,
                )
            )
        self.view.update()
        self.page.update()

    def toggle_nav_rail(self, e):
        self.view.visible = not self.view.visible
        self.view.update()
        self.page.update()

    def top_nav_change(self, e):
        index = e if (type(e) == int) else e.control.selected_index
        self.bottom_nav_rail.selected_index = None
        self.top_nav_rail.selected_index = index
        self.view.update()
        if index == 0:
            self.page.route = "/all_sim"
        self.page.update()

    def bottom_nav_change(self, e):
        index = e if (type(e) == int) else e.control.selected_index
        self.bottom_nav_rail.selected_index = index
        self.top_nav_rail.selected_index = None
        self.page.route = f"/simulator/{self.bottom_nav_rail.destinations[index].label}"
        self.view.update()
        self.page.update()

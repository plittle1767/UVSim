import flet as ft
from Controls.Topbar import Topbar
from Controls.app_layout import AppLayout


def main(page: ft.Page):
    page.title = "UVSim"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.scroll = True
    topbar = Topbar(page)
    layout = AppLayout(page,
                       topbar=topbar,
                       tight=True,
                       expand=True,
                       vertical_alignment="start",
                       )

    def route_change(e):
        troute = ft.TemplateRoute(page.route)
        # if troute.match("/"):
        #     page.go("/all_sim")
        if troute.match("/all_sim"):
            layout.set_all_sim_view()
        elif troute.match("/simulator/:id"):
            layout.set_sim_view(troute.id)

        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.views.clear()
    page.views.append(
        ft.View(
            "/",
            [topbar.build(), layout],
            padding=ft.padding.all(0),

        )
    )
    page.update()
    # if not layout.sim_pages:
    #     layout.sim_pages.update({"No File": SimulatorPage(page, topbar, "No File", "No File")})
    # page.go("/")

    page.on_route_change = route_change
    page.on_view_pop = view_pop


ft.app(target=main)

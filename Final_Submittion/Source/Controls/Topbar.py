import flet as ft
import re


class Topbar(ft.AppBar):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.green_theme(None)
        self.appbar_items = ft.PopupMenuButton(
            content=ft.Row([
                ft.Icon(ft.icons.PALETTE, color=ft.colors.PRIMARY_CONTAINER),
                ft.Text("Themes", theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
            ]),
            items=[
                ft.PopupMenuItem(
                    content=ft.Row(
                        [
                            ft.Icon(ft.icons.PALETTE, color=ft.colors.GREEN),
                            ft.Text("Green", color=ft.colors.GREEN)
                        ]
                    ),
                    on_click=self.green_theme,
                ),
                ft.PopupMenuItem(
                    content=ft.Row(
                        [
                            ft.Icon(ft.icons.PALETTE, color=ft.colors.LIGHT_BLUE),
                            ft.Text("Blue", color=ft.colors.LIGHT_BLUE)
                        ]
                    ),
                    on_click=self.blue_theme,

                ),
                ft.PopupMenuItem(
                    content=ft.Row(
                        [
                            ft.Icon(ft.icons.PALETTE, color=ft.colors.TEAL),
                            ft.Text("Teal", color=ft.colors.TEAL)
                        ]
                    ),
                    on_click=self.Teal_theme,
                ),
                ft.PopupMenuItem(
                    content=ft.Row(
                        [
                            ft.Icon(ft.icons.PALETTE, color=ft.colors.PURPLE),
                            ft.Text("Purple", color=ft.colors.PURPLE)
                        ]
                    ),
                    on_click=self.purple_theme,
                ),
                ft.PopupMenuItem(
                    content=ft.Row(
                        [
                            ft.Icon(ft.icons.PALETTE),
                            ft.Text("Custom"),
                        ]
                    ),
                    on_click=self.custom_theme,
                ),
            ],
        )
        self.create_appbar = ft.AppBar(
            title=ft.Text("UVSim", theme_style=ft.TextThemeStyle.DISPLAY_LARGE, text_align=ft.TextAlign.START, color="white"),
            center_title=False,
            bgcolor=ft.colors.PRIMARY,
            toolbar_height=75,
            actions=[
                ft.Container(
                    content=self.appbar_items,
                    margin=ft.margin.only(left=50, right=25),
                )
            ],
        )
        self.page.appbar = self.create_appbar
        self.page.update()

    def build(self):
        return self.create_appbar

    def green_theme(self, e):
        self.page.theme = ft.Theme(
            color_scheme=ft.ColorScheme(
                primary="#436814",
                on_primary="0xFFFFFFFF",
                primary_container="0xFFC3F18C",
                on_primary_container="0xFF102000",
                secondary="0xFF586249",
                on_secondary="0xFFFFFFFF",
                secondary_container="0xFFDBE7C8",
                on_secondary_container="0xFF151E0B",
                tertiary="0xFF386663",
                on_tertiary="0xFFFFFFFF",
                tertiary_container="0xFFBBECE8",
                on_tertiary_container="0xFF00201E",
                error="0xFFBA1A1A",
                error_container="0xFFFFDAD6",
                on_error="0xFFFFFFFF",
                on_error_container="0xFF410002",
                background="0xFFFDFCF5",
                on_background="0xFF1B1C18",
                surface="#fdfcf5",
                on_surface="#1b1c18",
                surface_variant="#e1e4d5",
                on_surface_variant="#44483d",
                outline="0xFF75796C",
                on_inverse_surface="0xFFF2F1E9",
                inverse_surface="0xFF30312C",
                inverse_primary="0xFFA8D473",
                shadow="0xFF000000",
                surface_tint="0xFF436814",
                outline_variant="0xFFC5C8BA",
                scrim="0xFF000000",
            )
        )
        self.page.update()

    def blue_theme(self, e):
        self.page.theme = ft.Theme(
            color_scheme=ft.ColorScheme(
                primary="#006399",
                on_primary="#ffffff",
                primary_container="#cde5ff",
                on_primary_container="#001d32",
                secondary="#51606f",
                on_secondary="#ffffff",
                secondary_container="#d4e4f6",
                on_secondary_container="#0d1d2a",
                tertiary="#67587a",
                on_tertiary="#ffffff",
                tertiary_container="#eddcff",
                on_tertiary_container="#221533",
                error="#ba1a1a",
                error_container="#ffdad6",
                on_error="0xFFFFFFFF",
                on_error_container="#ffdad6",
                background="#fcfcff",
                on_background="#1a1c1e",
                surface="#fcfcff",
                on_surface="#1a1c1e",
                surface_variant="#dee3eb",
                on_surface_variant="#42474e",
                outline="#72787e",
                on_inverse_surface="0xFFF2F1E9",
                inverse_surface="0xFF30312C",
                inverse_primary="0xFFA8D473",
                shadow="0xFF000000",
                surface_tint="0xFF436814",
                outline_variant="0xFFC5C8BA",
                scrim="0xFF000000",
            )
        )
        self.page.update()

    def Teal_theme(self, e):
        self.page.theme = ft.Theme(
            color_scheme=ft.ColorScheme(
                primary="#006971",
                on_primary="#ffffff",
                primary_container="#86f3ff",
                on_primary_container="#002023",
                secondary="#4a6366",
                on_secondary="0xFFFFFFFF",
                secondary_container="#cde7eb",
                on_secondary_container="#051f22",
                tertiary="#505e7d",
                on_tertiary="0xFFFFFFFF",
                tertiary_container="#d8e2ff",
                on_tertiary_container="#0b1b36",
                error="0xFFBA1A1A",
                error_container="0xFFFFDAD6",
                on_error="0xFFFFFFFF",
                on_error_container="0xFF410002",
                background="0xFFFDFCF5",
                on_background="0xFF1B1C18",
                surface="#fafdfd",
                on_surface="#191c1d",
                surface_variant="#dae4e5",
                on_surface_variant="#3f484a",
                outline="#6f797a",
                on_inverse_surface="0xFFF2F1E9",
                inverse_surface="0xFF30312C",
                inverse_primary="0xFFA8D473",
                shadow="0xFF000000",
                surface_tint="0xFF436814",
                outline_variant="0xFFC5C8BA",
                scrim="0xFF000000",
            )
        )
        self.page.update()

    def purple_theme(self, e):
        self.page.theme = ft.Theme(
            color_scheme=ft.ColorScheme(
                primary="#714c9f",
                on_primary="0xFFFFFFFF",
                primary_container="#eedbff",
                on_primary_container="#2a0054",
                secondary="#655a6f",
                on_secondary="0xFFFFFFFF",
                secondary_container="#ecddf7",
                on_secondary_container="#20182a",
                tertiary="#80515a",
                on_tertiary="#ffffff",
                tertiary_container="#ffd9de",
                on_tertiary_container="#321018",
                error="0xFFBA1A1A",
                error_container="0xFFFFDAD6",
                on_error="0xFFFFFFFF",
                on_error_container="0xFF410002",
                background="0xFFFDFCF5",
                on_background="0xFF1B1C18",
                surface="#fffbff",
                on_surface="0xFF1B1C18",
                surface_variant="0xFFE1E4D5",
                on_surface_variant="0xFF44483D",
                outline="0xFF75796C",
                on_inverse_surface="0xFFF2F1E9",
                inverse_surface="0xFF30312C",
                inverse_primary="0xFFA8D473",
                shadow="0xFF000000",
                surface_tint="0xFF436814",
                outline_variant="0xFFC5C8BA",
                scrim="0xFF000000",
            )
        )
        self.page.update()

    def is_hex_color(self, s):
        return bool(re.match("^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$", s))

    def custom_theme(self, e):
        def apply_custom_theme(e):
            if not self.is_hex_color(text_color.value):
                print("Invalid Color")
            elif not self.is_hex_color(primary_color.value):
                print("Invalid Color")
            elif not self.is_hex_color(secondary_color.value):
                print("Invalid Color")
            elif not self.is_hex_color(tertiary_color.value):
                print("Invalid Color")
            else:
                self.page.theme = ft.Theme(
                    color_scheme=ft.ColorScheme(
                        primary=primary_color.value,
                        on_primary="0xFFFFFFFF",
                        primary_container=primary_color.value,
                        on_primary_container=primary_color.value,
                        secondary=secondary_color.value,
                        on_secondary="0xFFFFFFFF",
                        secondary_container=secondary_color.value,
                        on_secondary_container=secondary_color.value,
                        tertiary=tertiary_color.value,
                        on_tertiary="0xFFFFFFFF",
                        tertiary_container=tertiary_color.value,
                        on_tertiary_container=tertiary_color.value,
                        error="0xFFBA1A1A",
                        error_container="0xFFFFDAD6",
                        on_error="0xFFFFFFFF",
                        on_error_container="0xFF410002",
                        background="0xFFFDFCF5",
                        on_background="0xFF1B1C18",
                        surface=text_color.value,
                        on_surface="0xFF1B1C18",
                        surface_variant="0xFFE1E4D5",
                        on_surface_variant="0xFF44483D",
                        outline="0xFF75796C",
                        on_inverse_surface="0xFFF2F1E9",
                        inverse_surface="0xFF30312C",
                        inverse_primary="0xFFA8D473",
                        shadow="0xFF000000",
                        surface_tint="0xFF436814",
                        outline_variant="0xFFC5C8BA",
                        scrim="0xFF000000",
                    )
                )

            custom_theme_dlg.open = False
            self.page.update()

        def textfield_change(e):
            if (text_color.value and
                    primary_color.value and
                    secondary_color.value and
                    tertiary_color.value != ""):
                apply_button.disabled = False
            else:
                apply_button.disabled = True
            self.page.update()

        text_color = ft.TextField(label="Text Color", text_size=10, on_change=textfield_change, hint_text= "e.g., #FFFFFFFF")
        primary_color = ft.TextField(label="Primary Color", text_size=10, on_change=textfield_change, hint_text= "e.g., #FFFFFFFF")
        secondary_color = ft.TextField(label="Secondary Color", text_size=10, on_change=textfield_change, hint_text= "e.g., #FFFFFFFF")
        tertiary_color = ft.TextField(label="Tertiary Color", text_size=10, on_change=textfield_change, hint_text= "#e.g., #FFFFFFFF")
        apply_button = ft.ElevatedButton(text="Apply Theme", on_click=apply_custom_theme, disabled=True)

        custom_theme_dlg = ft.AlertDialog(
            title=ft.Text("Custom Theme", size=50),
            actions=[
                ft.Column(
                    [
                        text_color,
                        primary_color,
                        secondary_color,
                        tertiary_color,
                        apply_button,
                    ]
                ),
            ],
            on_dismiss=lambda e: print("Dismissed"),
        )

        self.page.dialog = custom_theme_dlg
        custom_theme_dlg.open = True
        self.page.update()

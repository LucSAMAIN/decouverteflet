import flet as ft

def homeView(page: ft.Page):
    return ft.View(
        route="/home",
        controls=[
            ft.Container(
                content=ft.Column(
                    [
                        ft.Text("Home !!"),
                        ft.ElevatedButton("Go log in page", on_click=lambda _: page.go("/login")),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                alignment=ft.alignment.center,
                expand=True,
            )
        ]
    )

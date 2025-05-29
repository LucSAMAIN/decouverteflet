import flet as ft

def logInView(page : ft.Page):
    
    return ft.View(
        route="/login",
        controls=[
            ft.Text("Log in !!"),
            ft.ElevatedButton("Go home page", on_click=lambda _ : page.go("/home"))
        ]
    )
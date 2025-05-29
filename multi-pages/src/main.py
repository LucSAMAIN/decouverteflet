import flet as ft

# import pages:
from pages.home import homeView
from pages.login import logInView


def main(page: ft.Page):
    page.title = "muti pages app test"
    
    def route_change(e : ft.RouteChangeEvent):
        page.views.clear()
        if page.route == "/home":
            page.views.append(homeView(page))
        elif page.route == "/login":
            page.views.append(logInView(page))
        
        page.update()
        
    
    page.on_route_change = route_change
    page.go("/home")


ft.app(main, assets_dir="src/assets")

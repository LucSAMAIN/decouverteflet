import flet as ft


def main(page: ft.Page):
    page.title = "Hello Flet!" # le nom de l'onglet
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    counter = ft.Text("Luc c'est moi ?", color="blue")

    # widget:
    # page.controls.append(counter)
    # page.update()
    # =
    page.add(counter)
    
    # containers:
    page.add(
    ft.Row(controls=[
        ft.Text("A"),
        ft.Text("B"),
        ft.Text("C")
    ])
    )
    
    # onclick event:
    field = ft.TextField(label="Your name")
    answer_field = ft.Text(f"Your name is : {field.value}", visible=False)
    
    def field_button_on_click_func(e):
        answer_field.value = f"Your name is : {field.value}"
        answer_field.visible = True
        page.update()
    field_button = ft.ElevatedButton(text="Say my name!", on_click=field_button_on_click_func)
    
    page.add(
        ft.Row(controls=[
            field,
            field_button,
            answer_field
        ])
    )
    
    btn = ft.ElevatedButton("Click me!")
    page.add(btn)


ft.app(main)
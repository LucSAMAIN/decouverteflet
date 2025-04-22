import flet as ft


def main(page : ft.Page):
    
    """
    =====================================================================================================
    ========================================== PAGE SETTINGS ============================================
    =====================================================================================================
    """
    
    #Title:
    page.title = "Ma calculatrice en Flet"
    
    #Vertical / horizontal alignment:
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    #Fonts:
    page.fonts = {
        "RobotoSlab": "https://github.com/google/fonts/raw/main/apache/robotoslab/RobotoSlab%5Bwght%5D.ttf"
    }
    
    """
    GLOBAL VARIABLES
    """    
    COMPUTATION_STRING = ""
    
    """
    =====================================================================================================
    ========================================= EVENTS HANDLING ===========================================
    =====================================================================================================
    """
        
        
    def update_display_on_click(e):
        nonlocal COMPUTATION_STRING
        COMPUTATION_STRING += e.control.text
        display_panel.value = COMPUTATION_STRING
        page.update()
        

    def equal_button_on_click_func(e):
        nonlocal COMPUTATION_STRING
        i = 0
        stackComputation = [] # (operator, operandLeft, operantRight), ...
        while (i<len(COMPUTATION_STRING)):
            c = COMPUTATION_STRING[i]
            if c == "=":
                update_display("SYNTAX ERROR")
            elif c == "+":
                pass
            i+=1

                
        
    """
    =====================================================================================================
    ======================================== OTHERS FUNCTIONS ===========================================
    =====================================================================================================
    """
    
    def update_display(display_string):
        display_panel.value = display_string
        page.update()
    
    """
    =====================================================================================================
    ======================================== WIDGETS CREATION ===========================================
    =====================================================================================================
    """
  
    
    #Display panel:
    display_panel = ft.Text(
        COMPUTATION_STRING,
        font_family = "RobotoSlab"
    )
    
    #Calculator:
        #Operators row (+ - *)
    add_button = ft.ElevatedButton(text="+", on_click=update_display_on_click)
    minus_button = ft.ElevatedButton(text="-", on_click=update_display_on_click)
    times_button = ft.ElevatedButton(text="*", on_click=update_display_on_click)
    
    calculation_row = ft.Row(
        controls=[
            add_button,
            minus_button,
            times_button],
        alignment=ft.MainAxisAlignment.CENTER
    )
    
        #Numeric keypad(1, 2, ..., 0)
    one_button = ft.ElevatedButton(text="1", on_click=update_display_on_click)
    two_button = ft.ElevatedButton(text="2", on_click=update_display_on_click)
    three_button = ft.ElevatedButton(text="3", on_click=update_display_on_click)
    keypad_123_row = ft.Row(
        controls=[
            one_button,
            two_button,
            three_button],
        alignment=ft.MainAxisAlignment.CENTER,
    )
    
    four_button = ft.ElevatedButton(text="4", on_click=update_display_on_click)
    five_button = ft.ElevatedButton(text="5", on_click=update_display_on_click)
    six_button = ft.ElevatedButton(text="6", on_click=update_display_on_click)
    keypad_456_row = ft.Row(
        controls=[
            four_button,
            five_button,
            six_button],
        alignment=ft.MainAxisAlignment.CENTER,
    )
    
    seven_button = ft.ElevatedButton(text="7", on_click=update_display_on_click)
    eight_button = ft.ElevatedButton(text="8", on_click=update_display_on_click)
    nine_button = ft.ElevatedButton(text="9", on_click=update_display_on_click)
    keypad_789_row = ft.Row(
        controls=[
            seven_button,
            eight_button,
            nine_button],
        alignment=ft.MainAxisAlignment.CENTER
    )
    
    zero_button = ft.ElevatedButton(text="0", on_click=update_display_on_click)
    equal_button = ft.ElevatedButton(text="=", on_click=equal_button_on_click_func)
    keypad_0_row = ft.Row(controls=[zero_button, equal_button], alignment=ft.MainAxisAlignment.CENTER)

    main_content = ft.Column(
        controls=[
            display_panel,
            calculation_row,
            keypad_123_row,
            keypad_456_row,
            keypad_789_row,
            keypad_0_row
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    """
    =====================================================================================================
    ========================================= ADDING WIDGETS ============================================
    =====================================================================================================
    """
    
    page.add(
        main_content
    )
    
    
ft.app(target=main)
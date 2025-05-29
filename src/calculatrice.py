import flet as ft


def calc(page : ft.Page):
    """
    =====================================================================================================
    ==========================================GLOBAL VARIABLES ==========================================
    =====================================================================================================
    """   
    
    VIOLET = "#f6d4fa"
    HARD_RED = "#ff6b6b"
    CYAN = "#bbfaf6"
    COMPUTATION_STRING = ""
    
    
    """
    =====================================================================================================
    ========================================== PAGE SETTINGS ============================================
    =====================================================================================================
    """
    page.title = "Ma calculatrice en Flet"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = VIOLET
    
    
    page.fonts = {
        "RobotoSlab": "https://github.com/google/fonts/raw/main/apache/robotoslab/RobotoSlab%5Bwght%5D.ttf"
    }
    
    """
    =====================================================================================================
    ========================================= EVENTS HANDLING ===========================================
    =====================================================================================================
    """
        
        
    def update_display_on_click(e):
        nonlocal COMPUTATION_STRING
        if COMPUTATION_STRING == "Err":
            COMPUTATION_STRING = ""
        COMPUTATION_STRING += e.control.text
        display_panel.content.value = COMPUTATION_STRING
        page.update()
        

    def equal_button_on_click_func(e):
        nonlocal COMPUTATION_STRING
        try:
            COMPUTATION_STRING = str(eval(COMPUTATION_STRING))
        except Exception:
            COMPUTATION_STRING = "Err"
        display_panel.content.value = COMPUTATION_STRING
        page.update()
        
    def clear_button_on_click_func(e):
        nonlocal COMPUTATION_STRING
        COMPUTATION_STRING = ""
        display_panel.content.value = COMPUTATION_STRING
        page.update()

                
        
    """
    =====================================================================================================
    ======================================== OTHERS FUNCTIONS ===========================================
    =====================================================================================================
    """
    
        
    
    """
    =====================================================================================================
    ======================================== WIDGETS CREATION ===========================================
    =====================================================================================================
    """
  
    
    #Display panel:
    display_panel = ft.Container(
        content = ft.Text(COMPUTATION_STRING, font_family = "RobotoSlab"),
        border = ft.border.all(4, HARD_RED),
        alignment=ft.alignment.center,
        border_radius = 10,
        margin=ft.margin.only(bottom=10),
        width = 300,
        shadow = ft.BoxShadow(blur_radius=50, color=CYAN)
    )
    
    #Calculator:
        #Operators row (+ - *)
    add_button = ft.ElevatedButton(text="+", on_click=update_display_on_click)
    minus_button = ft.ElevatedButton(text="-", on_click=update_display_on_click)
    times_button = ft.ElevatedButton(text="*", on_click=update_display_on_click)
    divide_button = ft.ElevatedButton(text="/", on_click=update_display_on_click)
    
    
    calculation_row = ft.Row(
        controls=[
            add_button,
            minus_button,
            times_button,
            divide_button],
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
    clear_button = ft.ElevatedButton(text="CE", on_click=clear_button_on_click_func)
    keypad_0_row = ft.Row(controls=[zero_button, 
                                    equal_button,
                                    clear_button], 
                          alignment=ft.MainAxisAlignment.CENTER)

    main_content = ft.Container(
            ft.Column(
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
        ),
            
        width=320,
        shadow = ft.BoxShadow(blur_radius=100, spread_radius=10, color=CYAN),
        border = ft.border.all(4, HARD_RED),
        border_radius = 20,
        padding = 20
    )

    """
    =====================================================================================================
    ========================================= ADDING WIDGETS ============================================
    =====================================================================================================
    """
    
    luc_text = ft.Text(
        value= "C'est ma Calculatrice euhh", 
        color= ft.Paint(
            gradient=ft.PaintLinearGradient(
                (0, 10), 
                (0, 100), 
                colors=[ft.Colors.BLUE, ft.Colors.YELLOW]
                ),
            )
        )
    
    page.add(
        luc_text,
        main_content
    )
    

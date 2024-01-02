import flet as ft 

async def main(page: ft.Page):
    page.window_width = 720
    page.window_height = 1280
    page.window_resizable = False
    page.padding = 0

    boton_azul = ft.Stack([
        ft.Container(width=80, height=80, bgcolor=ft.colors.WHITE, border_radius=50),
        ft.Container(width=70, height=70, left=5, top=5, bgcolor=ft.colors.BLUE, border_radius=50)
    ])


    items_superior = {
        ft.Container(boton_azul, width=80, height=80),
        ft.Container(width=40, height=40, bgcolor=ft.colors.RED_200, border_radius=50),
        ft.Container(width=40, height=40, bgcolor=ft.colors.YELLOW, border_radius=50),
        ft.Container(width=40, height=40, bgcolor=ft.colors.GREEN, border_radius=50),
    }


    superior = ft.Container(content=ft.Row(items_superior),width=600, height=80, margin=ft.margin.only(top=40))
    centro = ft.Container(width=600, height=400, margin=ft.margin.only(top=40), border=ft.border.all())
    inferior = ft.Container(width=600, height=400, margin=ft.margin.only(top=40), border=ft.border.all())


    col = ft.Column(spacing=0, controls=[
        superior,
        centro,
        inferior,
    ])

    contenedor = ft.Container(col, width=720, height=1280, bgcolor=ft.colors.RED, alignment=ft.alignment.top_center)

    await page.add_async(contenedor)
 
ft.app(target=main)
import flet as ft
from models.usuario import crear_tabla

def main(page: ft.Page):

    crear_tabla()

    page.add(ft.Text("Todo funcionando 😎"))

ft.app(target=main)
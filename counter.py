import flet
from flet import *

def main(page: Page):
    page.title ="Counter"
    page.vertical_alignment ="center"

    text_field= TextField(value= 0, width=100, text_align="right")
    def minus_clicked(e):
        text_field.value = int(text_field.value) - 1
        page.update()
    def plus_clicked(e):
        text_field.value = int(text_field.value) + 1
        page.update()

    page.add(
        Row(
            [IconButton(icons.REMOVE, on_click=minus_clicked),
            text_field,
            IconButton(icons.ADD, on_click=plus_clicked),
            ],
            alignment="center",
        )
    )
flet.app(target=main)           
            
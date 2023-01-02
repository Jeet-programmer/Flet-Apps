import flet
from flet import Page, TextField
from flet import ElevatedButton, Page, Row, Text

def main(page: Page):
    def calc(e):
        result.size=30
        result.value="Your Bmi is :" + str ("%.2f" %(  int(weight.value)/(int(height.value)*0.01)**2))
        page.update()
        
    page.title="BMI calculator"
    result=Text("Find what Your Bmi")
    weight=TextField(label="Weight",hint_text="Weight in kg")
    height=TextField(label="Height",hint_text="Height in cm")
    b=ElevatedButton(text="Calculate",on_click=calc)
    page.add(result,weight,height,b)

flet.app(target=main)
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button


class KnisterApp(App):
    def build(self):
        layout = GridLayout(cols=5, rows=5)

        for i in range(1, 26):
            b = Button(text=f"{i}")
            layout.add_widget(b)

        return layout


if __name__ == '__main__':
    KnisterApp().run()

import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

from main import Knister


class KnisterGrid(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(cols=5, rows=5, **kwargs)

        self.current_number = None
        self.knister = Knister()

        for idx in range(25):
            b = Button(text="", font_size='40sp')
            b.bind(on_press=lambda btn, i=idx: self.set_num(btn, i))
            self.add_widget(b)

    def set_num(self, button, idx):
        if button.text == "" and self.knister.field[idx // 5][idx % 5] == 0:
            button.text = str(self.current_number)
            self.knister.field[idx // 5][idx % 5] = self.current_number
            self.knister.show()
            self.current_number = self.knister.roll()

    def start(self):
        self.current_number = self.knister.roll()
        print("Current:", self.current_number)


class KnisterApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical")

        self.next_num = Label(text="0", font_size='40sp', size_hint=(1.0, 1.0))
        layout.add_widget(self.next_num)

        self.knister_grid = KnisterGrid(size_hint=(1.0, 5.0))
        layout.add_widget(self.knister_grid)

        start_button = Button(
            text="Start", font_size='40sp', size_hint=(1.0, 1.0))
        start_button.bind(on_press=self.start_game)
        layout.add_widget(start_button)

        return layout

    def start_game(self, instance):
        self.knister_grid.start()


if __name__ == '__main__':
    KnisterApp().run()

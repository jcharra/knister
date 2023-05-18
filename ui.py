from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.properties import NumericProperty

from main import Knister


class KnisterGrid(GridLayout):
    def __init__(self, on_change, **kwargs):
        super().__init__(cols=5, rows=5, **kwargs)

        self.on_change = on_change
        self.current_number = None
        self.knister = Knister()

        for idx in range(25):
            b = Button(text="", font_size='40sp')
            b.bind(on_press=lambda btn, i=idx: self.set_num(btn, i))
            self.add_widget(b)

    def set_num(self, button, idx):
        if self.current_number and button.text == "" and self.knister.field[idx // 5][idx % 5] == 0:
            button.text = str(self.current_number)
            self.knister.field[idx // 5][idx % 5] = self.current_number or 0
            self.knister.show()
            self.current_number = self.knister.roll()
            self.on_change()

    def start(self):
        self.current_number = self.knister.roll()
        self.on_change()


class TopBar(BoxLayout):
    score = NumericProperty(0)
    nextNum = NumericProperty(0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.next_widget = Label(text=f"", font_size='40sp')
        self.add_widget(self.next_widget)

        self.score_widget = Label(text="Score: 0", font_size='40sp')
        self.add_widget(self.score_widget)

    def on_score(self, instance, value):
        self.score_widget.text = f"Score: {self.score}"

    def on_nextNum(self, instance, value):
        self.next_widget.text = f"Next: {self.nextNum}"


class KnisterApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical")

        self.top_bar = TopBar()
        layout.add_widget(self.top_bar)

        self.knister_grid = KnisterGrid(
            size_hint=(1.0, 5.0), on_change=self.update)
        layout.add_widget(self.knister_grid)

        start_button = Button(
            text="Start", font_size='40sp', size_hint=(1.0, 1.0))
        start_button.bind(on_press=self.start_game)
        layout.add_widget(start_button)

        return layout

    def start_game(self, instance):
        self.knister_grid.start()

    def update(self):
        self.top_bar.nextNum = self.knister_grid.current_number
        self.top_bar.score = self.knister_grid.knister.evaluate()


if __name__ == '__main__':
    KnisterApp().run()

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.modalview import ModalView
from kivy.properties import NumericProperty
from dialog import AbortGameDialogContent, GameOverDialogContent

from model import Knister


class KnisterGrid(GridLayout):
    def __init__(self, notify_parent, **kwargs):
        super().__init__(cols=5, rows=5, **kwargs)

        self.notify_parent = notify_parent
        self.buttons = []
        self.knister = Knister()
        self.current_number = None

        for row in range(5):
            row_buttons = []
            for col in range(5):
                b = Button(text="", font_size='40sp')
                b.bind(on_press=lambda btn, r=row,
                       c=col: self.set_num(r, c))
                self.add_widget(b)
                row_buttons.append(b)
            self.buttons.append(row_buttons)

    def set_num(self, row, col):
        if self.current_number and self.knister.field[row][col] == 0:
            self.knister.field[row][col] = self.current_number or 0
            self.current_number = self.knister.roll()
            self.sync()
            self.check_finished()

    def new_game(self):
        self.knister = Knister()
        self.current_number = self.knister.roll()
        self.sync()

    def sync(self):
        for row in range(5):
            for col in range(5):
                self.buttons[row][col].text = str(
                    self.knister.field[row][col] or "")
        self.notify_parent()

    def check_finished(self):
        if self.knister.is_finished():
            view = ModalView(size_hint=(None, None), size=(400, 400))
            view.add_widget(GameOverDialogContent(
                score=self.knister.evaluate(), dismiss=view.dismiss))
            view.open()


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
            size_hint=(1.0, 5.0), notify_parent=self.update)
        layout.add_widget(self.knister_grid)

        start_button = Button(
            text="New game", font_size='40sp', size_hint=(1.0, 1.0))
        start_button.bind(on_press=self.start_game)
        layout.add_widget(start_button)

        return layout

    def start_game(self, instance):
        if self.knister_grid.knister.evaluate() > 0 and not self.knister_grid.knister.is_finished():
            view = ModalView(size_hint=(None, None), size=(400, 400))
            view.add_widget(AbortGameDialogContent(
                on_confirm=self.knister_grid.new_game, dismiss=view.dismiss))
            view.open()
        else:
            self.knister_grid.new_game()

    def update(self):
        self.top_bar.nextNum = self.knister_grid.current_number
        self.top_bar.score = self.knister_grid.knister.evaluate()


if __name__ == '__main__':
    KnisterApp().run()

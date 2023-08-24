from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

GAME_FONT_SIZE = '60'
DIALOG_FONT_SIZE = '26sp'
DIALOG_DIMENSIONS = 600, 400


class AbortGameDialogContent(GridLayout):
    def __init__(self, on_confirm, dismiss, **kwargs):
        super().__init__(cols=1, rows=3, **kwargs)

        self.on_confirm = on_confirm
        self.dismiss = dismiss

        self.add_widget(
            Label(text='Abort current game?', font_size=DIALOG_FONT_SIZE, size_hint=(1.0, 2.0)))

        abort_button = Button(text="Yes, start new game",
                              font_size=DIALOG_FONT_SIZE)
        abort_button.bind(on_press=self.confirm)
        self.add_widget(abort_button)

        continue_button = Button(
            text="No, continue", font_size=DIALOG_FONT_SIZE)
        continue_button.bind(on_press=self.dismiss)
        self.add_widget(continue_button)

    def confirm(self, instance):
        self.dismiss()
        self.on_confirm()


class GameOverDialogContent(GridLayout):
    def __init__(self, score, dismiss, **kwargs):
        super().__init__(cols=1, rows=3, **kwargs)

        self.add_widget(
            Label(text=f"Game over", font_size=DIALOG_FONT_SIZE, size_hint=(1.0, 3.0)))
        self.add_widget(
            Label(text=f"Your score: {score}", font_size=DIALOG_FONT_SIZE, size_hint=(1.0, 3.0), bold=True, color=(0, 1, 0)))
        ok_button = Button(
            text="OK", font_size=DIALOG_FONT_SIZE, size_hint=(1.0, 2.0))
        ok_button.bind(on_press=dismiss)
        self.add_widget(ok_button)

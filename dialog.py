from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class AbortGameDialogContent(GridLayout):
    def __init__(self, on_confirm, dismiss, **kwargs):
        super().__init__(cols=1, rows=3, **kwargs)

        self.on_confirm = on_confirm
        self.dismiss = dismiss

        self.add_widget(
            Label(text='Abort current game?', size_hint=(1.0, 2.0)))

        abort_button = Button(text="Yes, start new game")
        abort_button.bind(on_press=self.confirm)
        self.add_widget(abort_button)

        continue_button = Button(text="No, continue")
        continue_button.bind(on_press=self.dismiss)
        self.add_widget(continue_button)

    def confirm(self, instance):
        self.dismiss()
        self.on_confirm()


class GameOverDialogContent(GridLayout):
    def __init__(self, score, dismiss, **kwargs):
        super().__init__(cols=1, rows=3, **kwargs)

        self.add_widget(Label(text=f"Game over", size_hint=(1.0, 3.0)))
        self.add_widget(
            Label(text=f"Your score: {score}", size_hint=(1.0, 3.0)))
        ok_button = Button(text="OK")
        ok_button.bind(on_press=dismiss)
        self.add_widget(ok_button)

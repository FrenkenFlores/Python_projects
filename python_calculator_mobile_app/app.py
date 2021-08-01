from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

class MainApp(App):
    def on_button_press(self, instance):
        console = self.solution.text
        button_text = instance.text

        if button_text == 'C':
            self.solution.text = str()
        else:
            # If an operator comes after another operator, ignore it
            if console and (self.last_was_operator and button_text in self.operators):
                return
            # If operator comes without a number before it, ignore it
            elif not console and button_text in self.operators:
                return
            # Else add the number or operator to the console
            else:
                self.solution.text = console + button_text
        self.last_pressed_button = button_text
        self.last_was_operator = self.last_pressed_button in self.operators

    def on_equal_press(self, instance):
        # If number after the operator was missing
        if self.last_was_operator:
            return
        eq = self.solution.text
        if eq:
            self.solution.text = str(eval(eq))

    def build(self):
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['.', '0', 'C', '+']
        ]
        self.operators = ['+', '-', '*', '/']
        self.last_pressed_button = None
        self.last_was_operator = None

        main_layout = BoxLayout(orientation='vertical')
        self.solution = TextInput(readonly=True, multiline=False)
        main_layout.add_widget(self.solution)
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(text=label)
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)
        equal_button = Button(text='=')
        equal_button.bind(on_press=self.on_equal_press)
        main_layout.add_widget(equal_button)
        return main_layout

if __name__ == '__main__':
    app = MainApp()
    app.run()
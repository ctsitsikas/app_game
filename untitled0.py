import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class WordleGame(App):
    def __init__(self, **kwargs):
        super(WordleGame, self).__init__(**kwargs)
        self.secret_word = self.choose_secret_word()
        self.guesses_left = 6
        self.current_guess = ['_' for _ in self.secret_word]

    def build(self):
        # Create a BoxLayout with vertical orientation
        layout = BoxLayout(orientation='vertical', spacing=10, padding=40)

        # Add a Label for the secret word display
        self.secret_word_label = Label(text=self.display_word(), font_size=20)
        layout.add_widget(self.secret_word_label)

        # Add a TextInput for the user to enter their guess
        self.user_input = TextInput(multiline=False, font_size=20, padding_y=(0, 20))
        layout.add_widget(self.user_input)

        # Add a Button to trigger the guess
        btn_guess = Button(text='Make Guess', font_size=20)
        btn_guess.bind(on_press=self.make_guess)  # Directly bind the on_press event
        layout.add_widget(btn_guess)

        # Add a Label for the remaining guesses
        self.guesses_label = Label(text=f'Guesses left: {self.guesses_left}', font_size=20)
        layout.add_widget(self.guesses_label)

        # Bind the close event to the on_close method
        self.bind(on_stop=self.on_close)  # Use on_stop instead of on_close

        return layout

    def choose_secret_word(self):
        # You can modify this to load a word from a file or use an API for more words
        word_list = ['pesto']
        return random.choice(word_list)

    def display_word(self):
        return " ".join(self.current_guess)

    def make_guess(self, instance):
        guess = self.user_input.text.lower()
        if len(guess) == 1 and guess.isalpha():
            if guess in self.secret_word and guess not in self.current_guess:
                for i, char in enumerate(self.secret_word):
                    if char == guess:
                        self.current_guess[i] = guess
            else:
                self.guesses_left -= 1
            self.guesses_label.text = f'Guesses left: {self.guesses_left}'
            self.secret_word_label.text = self.display_word()
            self.user_input.text = ''  # Clear the TextInput after a guess

            if '_' not in self.current_guess or self.guesses_left == 0:
                self.game_over()  # Handle game over scenario

    def game_over(self):
        self.stop()  # Close the Kivy application when the game is over

    def on_close(self, *args):
        self.stop()  # Close the Kivy application when the close button is clicked

if __name__ == "__main__":
    WordleGame().run()

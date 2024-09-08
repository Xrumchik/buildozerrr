from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from random import shuffle

class WordGameApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        self.word_label = Label(text='', font_size=24)
        self.input_field = TextInput(multiline=False, font_size=24)
        self.button = Button(text='Ответить', font_size=24, background_color=(0, 1, 0, 1), background_normal='', border=(30, 30, 30, 30))
        self.button.bind(on_press=self.check_answer)
        self.result_label = Label(text='', font_size=24)
        self.restart_button = Button(text='Перезапустить игру', font_size=24, background_color=(0, 1, 0, 1), background_normal='', border=(30, 30, 30, 30))
        self.restart_button.bind(on_press=self.restart_game)
        self.restart_button.disabled = True
        self.layout.add_widget(self.word_label)
        self.layout.add_widget(self.input_field)
        self.layout.add_widget(self.button)
        self.layout.add_widget(self.result_label)
        self.layout.add_widget(self.restart_button)
        self.s_ful = {
            'квартал': 2, 'километр': 3, 'кремень': 2, 'кремня': 2, 'лыжня': 2, 'локтя': 1, 'локтей': 2, 'ногтя': 1, 'ногтей': 2, 'создав': 2, 
            'прибыв': 2, 'намерение': 2, 'нарост': 2, 'недруг': 1, 'недуг': 2, 'ненависть': 1, 'новостей': 3, 'отрочество': 1, 'поручни': 1, 'приданое': 2, 
            'призыв': 2, 'свекла': 1, 'сироты': 2, 'созыв': 2, 'сосредоточение': 4,
            'статуя': 1, 'столяр': 2, 'таможня': 2, 'цемент': 2, 'центнер': 1, 'цепочка': 2, 'верна': 2, 'ловка': 2, 'значимый': 1, 'кухонный': 1, 'мозаичный': 3, 
            'оптовый': 2, 'прозорливый': 3, 'прозорлива': 3, 'сливовый': 1, 'довезенный': 3, 'заселенный': 3, 'заселена': 4, 'низведенный': 3, 'облегченный': 3, 'ободренный': 3, 
            'обостренный': 3, 'отключенный': 3, 'повторенный': 3, 'поделенный': 3
        }
        self.keys = list(self.s_ful.keys())
        shuffle(self.keys)
        self.current_word = self.keys.pop(0)
        self.word_label.text = self.current_word
        return self.layout

    def check_answer(self, instance):
        try:
            answer = int(self.input_field.text)
            if answer == self.s_ful[self.current_word]:
                self.result_label.text = 'Правильно!'
            else:
                self.result_label.text = f'Неверно. Правильный ответ: {self.s_ful[self.current_word]}'
            self.input_field.text = ''
            if self.keys:
                self.current_word = self.keys.pop(0)
                self.word_label.text = self.current_word
            else:
                self.word_label.text = 'Игра окончена!'
                self.button.disabled = True
                self.restart_button.disabled = False
        except ValueError:
            self.result_label.text = 'Неправильный формат ответа!'

    def restart_game(self, instance):
        self.keys = list(self.s_ful.keys())
        shuffle(self.keys)
        self.current_word = self.keys.pop(0)
        self.word_label.text = self.current_word
        self.input_field.text = ''
        self.result_label.text = ''
        self.button.disabled = False
        self.restart_button.disabled = True

if __name__ == '__main__':
    WordGameApp().run()

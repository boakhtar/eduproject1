import random
word_list = ['человек', 'работа', 'вопрос', 'сторона', 'страна', 'случай', 'голова', 'ребенок', 'система',
             'отношение', 'женщина', 'деньги', 'машина', 'проблема', 'решение', 'история', 'власть', 'тысяча',
             'возможность', 'результат', 'область', 'статья', 'компания', 'группа', 'развитие', 'процесс', 'условие',
             'средство', 'начало', 'уровень', 'минута', 'качество', 'дорога', 'действие', 'государство', 'любовь',
             'взгляд', 'общество', 'деятельность', 'организация', 'президент', 'комната', 'порядок', 'момент',
             'письмо', 'помощь', 'ситуация', 'состояние', 'квартира', 'внимание', 'смерть', 'программа', 'задача',
             'предприятие', 'разговор', 'правительство', 'производство', 'информация', 'положение', 'интерес',
             'федерация', 'правило', 'управление', 'мужчина', 'партия', 'сердце', 'движение', 'материал', 'неделя',
             'чувство', 'газета', 'причина', 'основа', 'товарищ', 'культура', 'данные', 'мнение', 'документ',
             'институт', 'проект', 'встреча', 'директор', 'служба', 'судьба', 'девушка', 'очередь', 'состав',
             'количество', 'событие', 'объект', 'создание', 'значение', 'период', 'искусство', 'структура', 'пример',
             'исследование', 'гражданин', 'начальник', 'принцип', 'воздух', 'характер']
def get_word(word_list):
    return random.choice(word_list).upper()

def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]


def play(word):
    word_completion = '_' * len(word)
    guessed_letters = []
    guessed_words = []
    tries = 6

    print('Давайте играть в угадайку слов!')
    print(display_hangman(tries))
    print(f'Слово из {len(word)} букв: {word_completion}')

    while True:
        letter = input('Введите букву или слово: \n').upper()
        if letter == 'ВЫХОД':
            print('Спасибо за игру!')
            break

        if len(letter) > 1:
            if letter in guessed_words:
                print('Слово уже было введено!')
                continue
            else:
                guessed_words.append(letter)
                if letter == word:
                    print(f'Поздравляю, вы угадали слово {word}!')
                    break
                else:
                    print(f'Слово {letter} не подходит(')
                    tries -= 1
                    print(display_hangman(tries))
                    print(word_completion)
                    if tries == 0:
                        print(f'Вы проиграли, загаданное слово - {word}')
                        break
                    continue

        elif len(letter) == 1:
            if letter in guessed_letters:
                print('Буква уже была введена!')
                continue
            else:
                guessed_letters.append(letter)
                if letter in word:
                    print(f'Поздравляю, вы угадали букву {letter}!')
                    word_completion = list(word_completion)
                    for i in range(len(word)):
                        if word[i] == letter:
                            word_completion[i] = letter
                    word_completion = ''.join(word_completion)
                    print(display_hangman(tries))
                    print(word_completion)

                    if '_' not in word_completion:
                        print(f'Поздравляю, вы угадали слово {word}!')
                        break
                else:
                    print(f'Буквы {letter} нет в слове')
                    tries -= 1
                    print(display_hangman(tries))
                    print(word_completion)
                    if tries == 0:
                        print(f'Вы проиграли, загаданное слово - {word}')
                        break
                    continue
        else:
            print('Введите одну букву или целое слово!')
            continue

    again = input('Ходите сыграть еще? (да/д/нет/н)').lower()
    if again == 'да' or again == 'д':
        word = get_word(word_list)
        play(word)

word = get_word(word_list)
play(word)
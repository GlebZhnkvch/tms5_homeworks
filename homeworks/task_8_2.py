dict_ = {'uppercase_letters': '',
         'lowercase_letters': '',
         }
list_of_uppercase_letters = []
list_of_lowercase_letters = []


def uppercase_and_lowercase_letters(string):
    try:
        for letter in string:
            if letter.isupper():
                list_of_uppercase_letters.append(letter)
                str_of_uppercase_letters = ', '.join(list_of_uppercase_letters)
                dict_['uppercase_letters'] = str_of_uppercase_letters
            elif letter.islower():
                list_of_lowercase_letters.append(letter)
                str_of_lowercase_letters = ', '.join(list_of_lowercase_letters)
                dict_['lowercase_letters'] = str_of_lowercase_letters
        return dict_
    except (TypeError, AttributeError):
        return f'You passed: {string} as argument, please pass the: string'

print(uppercase_and_lowercase_letters('KOkoKowefmewo'))
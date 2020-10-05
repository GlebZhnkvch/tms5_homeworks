def function_for_detecting_palindromes(*words):
    try:
        for word in words:
            word_len = int(len(word) / 2)
            inverted_word = word[::-1]
            if inverted_word[0: word_len] == word[0:word_len]:
                print(f'{word} is palindrom')
            else:
                print (f'{word} is not palindrom')
    except (TypeError, AttributeError):
        return f'Please, pass the string to detecting, you passed: {words}'
print(function_for_detecting_palindromes('oko', 'woiefjwe', 'ololo', 'gregre'))

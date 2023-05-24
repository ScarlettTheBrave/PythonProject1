def caesar_cipher():
    # Запитуємо у користувача рядок, який треба зашифрувати
    cipher = input('Enter your cryptogram: ')

    shift = None
    # Просимо користувача ввести значення зсуву і перевіряємо його на коректність
    while shift is None:
        try:
            shift = int(input('Enter shift value (1-25): '))
            if not 1 <= shift <= 25:
                raise ValueError
        except ValueError:
            print('Invalid shift value. Please enter an integer between 1 and 25.')
            shift = None

    text = ''
    # Проходимося по кожному символу в рядку
    for char in cipher:
        # Якщо символ не є літерою, додаємо його до вихідного рядку без змін
        if not char.isalpha():
            text += char
        else:
            # Визначаємо, чи є символ великою чи малою літерою
            is_upper = char.isupper()
            char = char.upper()
            # Зсуваємо код символу на задане значення
            code = ord(char) + shift
            if code > ord('Z'):
                code -= 26
            # Додаємо закодований символ до вихідного рядку зберігаючи регістр літер
            text += chr(code).upper() if is_upper else chr(code).lower()

    # Друкуємо закодований текст
    print('Encrypted text:', text)


caesar_cipher()
```
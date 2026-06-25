def censor_vowels(text):
    vowels = "аоиеуяыэюёАОИЕУЯЫЭЮЁ"
    result = ""

    for letter in text:
        if letter in vowels:
            result += "*"
        else:
            result += letter

    return result

print(censor_vowels("Привет, как дела?"))


# The present script deals with the translation of normal text into morse-code.
# It is also capable of translating from an encripted morse-code into a normal text.

morse_dic = {
    # Alphabet
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....", "I": "..",
    "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
    "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": ".--", "Y": "-.--", "Z": "--..",
    # Numbers
    "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..",
    "9": "----.", "0": "-----",
    # Punctuation
    ".": ".-.-.-", ",": "--.--", ":": "---...", "?": "..--..", "!": ".---.", "-": "-....-", "/": "-..-.",
    "(": "-*--*-", ")": "-*--*-", "'": ".-..-.", '"': ".-..-.",
    # Special
    " ": " / "
    }


continue_translation = True

while continue_translation:

    text_style = input("Is the input a normal text? Yes/No --> ")

    # Normal Text -> Morse code
    if text_style.title() == "Yes":
        text = input("Please insert the text: ")
        text_into_morse_list = []

        for ch in text:
            if ch.title() in morse_dic:
                text_into_morse_list.append(morse_dic[ch.title()])
            else:
                text_into_morse_list.append(ch)

        print(*text_into_morse_list, sep=" ")

    # Morse code -> Normal Text
    elif text_style.title() == "No":
        morse = input("Please insert the morse-code text: ")
        morse_into_text_list = []

        for word in morse.split(" / "):
            translated_word = ""
            for ch in word.split(" "):
                if ch in morse_dic.values():
                    found_key = ([k for k, v in morse_dic.items() if v == ch])
                    translated_word += "".join(found_key)
                else:
                    translated_word += ch
            morse_into_text_list.append(translated_word)
        print(" ".join(morse_into_text_list), end="\n")

    else:
        print(f"Your answer ({text_style}) is not compatible with the available options")

    new_translating = input("Do you want to translate a new text? Yes/No --> ")
    if new_translating.title() == "No":
        continue_translation = False

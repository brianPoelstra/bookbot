def main():
    file_contents=""
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    return file_contents

def word_count(book_text):
    token=book_text.replace("\n", " ")
    token=token.split()
    return len(token)

def character_count(book_text):
    book_text=book_text.lower()
    dict = {"a": 0,
    "b": 0,
    "c": 0,
    "d": 0,
    "e": 0,
    "f": 0,
    "g": 0,
    "h": 0,
    "i": 0,
    "j": 0,
    "k": 0,
    "l": 0,
    "m": 0,
    "n": 0,
    "o": 0,
    "p": 0,
    "q": 0,
    "r": 0,
    "s": 0,
    "t": 0,
    "u": 0,
    "v": 0,
    "w": 0,
    "x": 0,
    "y": 0,
    "z": 0}

    for char in book_text:
        if char in dict:
            dict[char]+=1
    return dict

def report(word_count, character_count):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    for key in character_count:
        print(f"The '{key}' character was found {character_count[key]} times")
    print("--- End report ---")
    



report(word_count(main()), character_count(main()))
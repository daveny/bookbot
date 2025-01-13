def main():
    print("--- Begin report of books/frankenstein.txt ---")

    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")

    print("")

    char_count = get_char_count(text)
    char_count_list = sorted(char_count.items(), key=sort_on, reverse=True)
    for char in char_count_list:
        print(f"The '{char[0]}' character was found {char[1]} times")
    
    print("--- End of report ---")

def get_char_count(text):
    chars = {}
    for char in text.lower():
        if char.isalpha():
            chars[char] = chars.get(char, 0) + 1
    return chars

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def sort_on(dict):
    return dict[1]


def get_char_count(text):
    chars = {}
    for char in text.lower():
        if char.isalpha():
            chars[char] = chars.get(char, 0) + 1
    return chars


main()

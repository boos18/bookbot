def main():
    book_path = "books/frankenstein.txt"
    book_contents = get_book_contents(book_path)
    print(str(count_words(book_contents)))
    char_count = count_characters(book_contents)
    print(char_count)

def get_book_contents(path):
    with open(path) as f:
        return f.read()
    
    
def count_words(text):
    words = text.split()
    amount_of_words = len(words)
    return amount_of_words


def count_characters(text):
    characters = {}
    for char in text:
        lowered = char.lower()
        if lowered in characters:
            characters[lowered] += 1
        else:
            characters[lowered] = 1
    return characters
    
main()

def main():
    book_path = "books/frankenstein.txt"
    book_contents = get_book_contents(book_path)
    word_count = count_words(book_contents)
    char_count_dict = count_characters(book_contents)
    char_count_dict_list = clean_count_characters(char_count_dict)
    report = create_report(book_path,word_count,char_count_dict_list)
    print_report(report)

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
        if lowered.isalpha():
            if lowered in characters:
                characters[lowered] += 1
            else:
                characters[lowered] = 1
    return characters

def clean_count_characters(characters):
    sorted_character_count = []
    for char in characters:
        detailed_dict = {"Character": char, "num": characters[char]}
        sorted_character_count.append(detailed_dict)
    sorted_character_count.sort(reverse=True, key=sort_on)
    return sorted_character_count
    #print(sorted_character_count)

def sort_on(dict):
    return dict["num"]

def create_report(path, word_count, character_dict_list):
    report_lines = []
    report_lines.append(f"--- Begin report of {path}")
    report_lines.append(f"{word_count} words found in the document")
    
    for dict in character_dict_list:
        line = "The " + dict["Character"] + " character was found " + str(dict["num"]) + " times"
        report_lines.append(line)
    return report_lines


def print_report(report):
    print(report[0])    
    print(report[1])
    print("\n")
    for x in range(len(report)):
        if x > 1:
            print(report[x])
    print("--- End report ---")

main()

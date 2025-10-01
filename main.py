import sys
from stats import count_words, count_characters, sort_chars

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

relative_path = sys.argv[1]

def main(relative_path):
    relative_path = "books/frankenstein.txt"
    text = get_book_text(relative_path)
    num_words = count_words(text)
    char_dict = count_characters(text)
    sorted_chars = sort_chars(char_dict)
    print_report(relative_path, num_words, sorted_chars)

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def print_report(relative_path, num_words, sorted_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {relative_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        char = item["char"]
        count = item["num"]
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")

main(relative_path)
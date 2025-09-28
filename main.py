from stats import count_words, count_characters

def main():
    relative_path = "books/frankenstein.txt"
    text = get_book_text(relative_path)
    num_words = count_words(text)
    num_ea_char = count_characters(text)
    print(f"Found {num_words} total words")
    print(num_ea_char)

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

main()
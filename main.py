import sys
from stats import get_num_words, get_chars_dict, sort_on


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars = get_chars_dict(text)
    sorted_chars = sort_on(chars)
    print(f"Found {num_words} total words")
    for letter in sorted_chars:
        print(f"{letter['char']}: {letter['num']}")


def get_book_text(path):
    with open(path) as f:
        return f.read()



main()
import sys
def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
        return file_content

from stats import count_words
from stats import count_characters
from stats import sort_char_counts


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text_to_print = get_book_text(sys.argv[1])
    num_words = count_words(text_to_print)
    char_counts = count_characters(text_to_print)
    sorted_char_counts = sort_char_counts(char_counts)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_char_counts:
    # item is a dictionary like {"char": "a", "num": 123}
        character = item["char"]
        count = item["num"]
    # Check if it's an alphabetical character
        if character.isalpha():
            print(f"{character}: {count}")
    print("============= END ===============")






main()

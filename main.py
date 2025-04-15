from stats import count_words
from stats import get_book_text
from stats import count_characters
from stats import sort_char_count
import sys

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    num_words = count_words(get_book_text(sys.argv[1]))
    char_count = count_characters(get_book_text(sys.argv[1]))
    sort_chars = sort_char_count(char_count)

    print("============ BOOKBOT ============\n"
       f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------\n"
          f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for dict in sort_chars:
        if dict["character"].isalpha() == True:
            print(f"{dict["character"]}: {dict["count"]}")

    print("============= END ===============")

main()
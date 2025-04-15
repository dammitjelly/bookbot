from stats import count_words
from stats import get_book_text
from stats import count_characters
from stats import sort_char_count

def main():
    num_words = count_words(get_book_text("books/frankenstein.txt"))
    char_count = count_characters(get_book_text("books/frankenstein.txt"))
    sort_chars = sort_char_count(char_count)

    print("============ BOOKBOT ============\n"
        "Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------\n"
          f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for dict in sort_chars:
        if dict["character"].isalpha() == True:
            print(f"{dict["character"]}: {dict["count"]}")

    print("============= END ===============")

main()
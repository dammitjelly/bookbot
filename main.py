from stats import count_words
from stats import get_book_text
from stats import count_characters

def main():
    num_words = count_words(get_book_text("books/frankenstein.txt"))
    char_count = count_characters(get_book_text("books/frankenstein.txt"))
    print(f"{num_words} words found in the document")
    print(char_count)

main()
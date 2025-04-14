def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def count_words(text):
    words_list = text.split()
    return len(words_list)

def count_characters(text):
    lower_string = text.lower()
    char_dict = {}
    for char in lower_string:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict


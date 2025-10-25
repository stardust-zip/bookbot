def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def count_words(book_text):
    return len(book_text.split())


def count_characters(book_text):
    char_dict = {}
    for character in book_text.lower():
        if character not in char_dict:
            char_dict[character] = 1
        else:
            char_dict[character] += 1
    return char_dict


def count_specific_word(book_text, word_to_find):
    count = 0
    for word in book_text.lower().split():
        if word_to_find == word:
            count += 1
    return count


def sort_on(items):
    return items["num"]


def sorted_dict(char_dict):
    dict_list = []
    for char, amount in char_dict.items():
        dict_list.append({"char": char, "num": amount})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list


def useless_function():
    return "You are a failure"

def count_words(text):
    num_words = len(text.split())
    return num_words

def count_characters(text):
    sanitised_text = text.lower()
    chars = {}
    for char in sanitised_text:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return(chars)

def sort_chars(chars):
    list_of_dicts = []
    for char, count in chars.items():
        individual_dict = {
            "char": char,
            "num": count
        }
        list_of_dicts.append(individual_dict)
    list_of_dicts.sort(reverse=True, key=sort_keys)
    return list_of_dicts

def sort_keys(chars):
    return chars["num"]


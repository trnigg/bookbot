def count_words(text):
    num_words = len(text.split())
    return num_words

def count_characters(text):
    sanitised_text = text.lower()
    counts = {}
    for char in sanitised_text:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return(counts)
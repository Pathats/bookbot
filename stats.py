def get_num_words(text):
    words = text.split()
    return len(words)



def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower() 
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort(item):
    return item["num"]


def sort_on(chars):
    value_list = []
    for key, value in chars.items():
        if key.isalpha():
            value_list.append({"char": key, "num": value}) 
    value_list.sort(reverse=True, key=sort)
    return value_list 

    
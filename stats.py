def count_words(text):
    spliced = text.split()
    return len(spliced)


def count_characters(text):
    chars = list(text)
    char_count = {}
    for c in chars:
        c = c.lower()
        if c in char_count:
            char_count[c]+=1
        else:
            if c == " " or (c.isalpha() == False):
                continue
            char_count[c] = 1

    return char_count


def sort_helper(x):
    return x["num"]


def sort_list(list):
    the_list = [{"char":k, "num":v} for k,v in list.items()]
    the_list.sort(reverse=True, key=sort_helper)
    return the_list


def get_num_words(content):
    return len(content.split())


def get_letters_appearance(content):
    # i did it that way before because i'm stupid
    # words = content.split()
    # letters_total_count = {}
    # for word in words:
    #     for letter in word:
    #         if letter.lower() in letters_total_count:
    #             # print(letter.lower() in letters_total_count)
    #             letters_total_count[letter.lower()] += 1
    #         else:
    #             letters_total_count[letter.lower()] = 1
    # # print(letters_total_count)

    # return letters_total_count
    # -----------------------------

    letters_total_count = {}
    for letter in content:
        if letter.lower() in letters_total_count:
            letters_total_count[letter.lower()] += 1
        else:
            letters_total_count[letter.lower()] = 1
    return letters_total_count


def sort_on(items):
    return items["num"]


def sort_dictionaries(dictionaries):
    dictionaries_with_keys = []

    for dictionary in dictionaries:
        dictionaries_with_keys.append(
            {"char": dictionary, "num": dictionaries[dictionary]}
        )

    dictionaries_with_keys.sort(key=sort_on, reverse=True)
    return dictionaries_with_keys

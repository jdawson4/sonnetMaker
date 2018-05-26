import nltk
from nltk.tokenize import RegexpTokenizer
#okay so nothing was bloody working, I had to canabalize some other code
#this code in particular comes from "kevin-brown" on github:
#https://github.com/kevin-brown/rhyme-detect/blob/master/rhyme_detect/rhymes.py
#thanks kevin!

def syllables(word):
    phones_list = possible_phones(word)

    if not phones_list:
        return []

    phones = phones_list[0]

    syllables = []
    syllable = ""

    for phone in phones:
        if phone[-1].isdigit():
            syllable += phone[:-1].lower()
            syllables.append(syllable)
            syllable = ""
        else:
            syllable += phone.lower()

    if syllable:
        syllables.append(syllable)

    return syllables


def get_nth_word(line, position):
    tokenizer = RegexpTokenizer(r"\w+")
    words = tokenizer.tokenize(line)

    if not words:
        raise ValueError("The given line must not be empty")

    return words[position]


def last_word(line):
    return get_nth_word(line, -1)


def possible_phones(word):
    phone_dictionary = nltk.corpus.cmudict.dict()

    if word not in phone_dictionary:
        return []

    return phone_dictionary[word]


def line_similarity(first_line, second_line):
    first_compare = last_word(first_line)
    second_compare = last_word(second_line)

    return word_similarity(first_compare, second_compare)

def word_similarity(first_word, second_word, start_phone=None, end_phone=None):
    first_phones = possible_phones(first_word)
    second_phones = possible_phones(second_word)

    if not first_phones or not second_phones:
        return 0

    first_phones = first_phones[0]
    second_phones = second_phones[0]

    first_range = first_phones[start_phone:end_phone]
    second_range = second_phones[start_phone:end_phone]

    first_range = first_range[::-1]
    second_range = second_range[::-1]

    if len(first_range) > len(second_range):
        first_range, second_range = second_range, first_range

    hits = 0
    total = len(first_range)

    for idx, phone in enumerate(first_range):
        other_phone = second_range[idx]

        if phone == other_phone:
            hits += 1

            # Phones with emphasis are better matches, weight them more
            if phone[-1].isdigit():
                hits += 1
                total += 1

    #print(hits)
    #print(total)
    return hits#| total

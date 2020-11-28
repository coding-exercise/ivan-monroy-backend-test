alphabet = [
    's',
    'x',
    'o',
    'c',
    'q',
    'n',
    'm',
    'w',
    'p',
    'f',
    'y',
    'h',
    'e',
    'l',
    'j',
    'r',
    'd',
    'g',
    'u',
    'i']
foo_letters = ['u', 'd', 'x', 's', 'm', 'p', 'f']
bar_letters = [letter for letter in alphabet if letter not in foo_letters]


def is_preposition(word):
    return len(word) == 6 and 'u' not in word and word[-1] in foo_letters


def is_verb(word):
    return 6 <= len(word) and word[-1] in bar_letters


def is_subjunctive_verb(word):
    return is_verb(word) and word[0] in bar_letters


def to_decimal(number):
    decimal_value = 0
    for i in range(len(number)):
        decimal_value = decimal_value + ((20 ** i) * alphabet.index(number[i]))
    return decimal_value


def is_pretty_number(number):
    decimal_value = to_decimal(number)
    return 81827 <= decimal_value and decimal_value % 3 == 0


def build_statistics_dictionary(text_split):
    statistics = {
        'prepositions': 0,
        'verbs': 0,
        'subjunctive_verbs': 0,
        'pretty_numbers': 0}
    pretty_numbers = []
    for word in text_split:
        if is_preposition(word):
            statistics['prepositions'] += 1
        if is_verb(word):
            statistics['verbs'] += 1
        if is_subjunctive_verb(word):
            statistics['subjunctive_verbs'] += 1
        if is_pretty_number(word):
            if word in pretty_numbers:
                pass
            else:
                statistics['pretty_numbers'] += 1
                pretty_numbers.append(word)
    return statistics


def vocabulary_list(text_split):
    return sorted(
        list(
            set(text_split)),
        key=lambda word: [
            alphabet.index(c) for c in word])

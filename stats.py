def count_words(text):
    words_list = text.split()
    return len(words_list)
def count_characters(text):
    lowercase_text = text.lower()
    all_characters = list(lowercase_text)
    all_unique_characters = set(all_characters)
    num_of_each = {}
    for unique_character in all_unique_characters:
        num_of_each[unique_character] = 0
        for character in all_characters:
            if character == unique_character:
                num_of_each[unique_character] += 1
    return num_of_each
def sort_on(items):
    return items["num"]
def sort_greatest_to_least(dictionary):
    sorted_characters_list = []
    for character in dictionary:
        if character.isalpha():
            sorted_characters_list.append({"char": character, "num": dictionary[character]})
    sorted_characters_list.sort(reverse=True, key=sort_on)
    return sorted_characters_list
from stats import sort_on
from main import get_book_text
def count_number_of_words(text):
    all_words = text.split()
    num_of_each = {}
    for word in all_words:
        if word in num_of_each:
            num_of_each[word] += 1
        else:
            num_of_each[word] = 1
    return num_of_each
def sort_greatest_to_least(dictionary):
    sorted_words_list = []
    for word in dictionary:
        sorted_words_list.append({"word": word, "num": dictionary[word]})
    sorted_words_list.sort(reverse=True, key=sort_on)
    return sorted_words_list
book_text = get_book_text("books/An Enegmatic Encounter.txt")
unsorted_words_dictionary = count_number_of_words(book_text)
sorted_words_dictionary = sort_greatest_to_least(unsorted_words_dictionary)
for dict in sorted_words_dictionary:
    print(f"{dict["word"]}: {dict["num"]}")
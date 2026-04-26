import sys
from stats import count_words, count_characters, sort_greatest_to_least
def main():
    if len(sys.argv) == 2:
        book_text = get_book_text(sys.argv[1])
        words_count = count_words(book_text)
        sorted_characters_count = sort_greatest_to_least(count_characters(book_text))
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {words_count} total words")
        print("----------- Character Count ----------")
        for dict in sorted_characters_count:
            print(f"{dict["char"]}: {dict["num"]}")
        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
    return text
if __name__ == "__main__":
    main()
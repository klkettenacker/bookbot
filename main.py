from stats import count_words, count_characters, sort_list
import sys


def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()
    


def main():
    print(len(sys.argv))

    if (len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
        book_text = get_book_text(book_path)

        word_count = count_words(book_text)
        char_count = sort_list(count_characters(book_text))
        #num_chars = count_characters(book_text)
        #print(f'{num_chars}')

        print("============ BOOKBOT ============")
        print(f'Analyzing book found at {book_path}')
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        print("----------- Character Count ----------")
        for char in char_count:
            print(f'{char["char"]}: {char["num"]}')
        print("============= END ===============")
    
    
    



main()
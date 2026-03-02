# Counts the number of times a word appears in a text(book)
def count_words(book):
    counts = {}
    for line in book:
        line = line.split()
        for word in line:
            # Character strip for all words
            word = word.strip(",.!¡¿?:;[]'\"()")
            # Converts word to lowercase
            word = word.lower()
            counts[word] = counts.get(word, 0) + 1
    return counts

# Returns a list of the words that appear just one time
def hapax_legomenon(counts):
    hapax_list = []
    for word in counts:
        if counts[word] == 1:
            hapax_list.append(word)
    return hapax_list

# Initialize the program, gets the user input (file name) and executes
if __name__ == "__main__":
    book_name = input("Enter the book name: ")
    book = open(book_name, encoding='utf-8')
    # print(count_words(book))
    print("Hapax Legomenon words:", hapax_legomenon(count_words(book)))
    book.close()
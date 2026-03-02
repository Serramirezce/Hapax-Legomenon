# Counts the number of times a word appears in a file
def count_words(book):
    counts = {}
    for line in book:
        line = line.split()
        for word in line:
            # Character strip for all words
            word = word.strip(",.!¡¿?:;[]'\"()")
            # Converts word to lowercase
            word = word.lower()
            # Update the count for this word
            counts[word] = counts.get(word, 0) + 1
    return counts

# Returns a list of the words that appear just once in the text
def hapax_legomenon(counts):
    hapax_list = []
    for word in counts:
        if counts[word] == 1:
            hapax_list.append(word)
    return hapax_list


# Main program: Gets the user input (file name) and displays results
if __name__ == "__main__":
    # Prompts the input
    book_name = input("Enter the book name: ")

    # Opens file:
    with open(book_name, encoding='utf-8') as book:
        word_counts = count_words(book)
    
    # Display list of Hapax Legomenon
    print("Hapax Legomenon words:", hapax_legomenon(word_counts))

    # Sorted list by frequency (ascending)
    sorted_words = sorted(word_counts.items(), key=lambda item: item[1])

    # Display the 10 most frequent words
    print("\n10 most frequent words: \nWord: Times that word appears")
    for word, freq in sorted_words[-10:]:
        print(f"{word}: {freq}")
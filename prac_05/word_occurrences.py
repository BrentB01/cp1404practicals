def main():
    def count_words(string):
        word_counts = {}
        words = string.split()

        for word in words:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1

        return word_counts

    user_input = input("Enter a string: ")
    word_counts = count_words(user_input)

    max_word_length = max(len(word) for word in word_counts.keys())

    print("Text:", user_input)
    for word, count in sorted(word_counts.items()):
        print(f"{word:{max_word_length}} : {count}")


main()


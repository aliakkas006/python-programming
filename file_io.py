with open("about_python.txt", mode="r") as read_file:
    words_all = []
    for line in read_file.readlines():
        words = line.strip().split(" ")
        words_all += words

    unique_words = set(words_all)  # return all the unique words

    with open("unique_words.txt", mode="w") as write_file:
        for word in sorted(unique_words):
            write_file.write(word)
            write_file.write("\n")

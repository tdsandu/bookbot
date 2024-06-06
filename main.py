def count(text):
    words_list = text.split()
    count = len(words_list)
    return count


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = count(file_contents)
    print(f"{word_count} is the number of words") 


main()
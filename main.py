def count(text):
    words_list = text.split()
    count = len(words_list)
    return count

def letter_counter(text):
    map = {}
    lowered_string = text.lower()
    for i in lowered_string:
        if i in map:
            map[i] += 1
        else:
            map[i] = 1
    return map

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = count(file_contents)
    print(f"{word_count} is the number of words")
    print(letter_counter(file_contents)) 


main()

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    word_count = count_words(file_contents)
    letter_count_dict = count_letters(file_contents)
    print_report(word_count, letter_count_dict)


def count_words(words : str) -> int:
    word_list = words.split()
    return len(word_list)

def count_letters(words : str) -> dict:
    letter_count = {}
    for c in words:
        if c not in letter_count and c.isalpha():
            letter_count[c] = 0
        if c.isalpha():
            letter_count[c] +=1
    return letter_count

def print_report(word_count : int, letter_dict : dict):
    print(f"""--- Begin report of books/frankenstein.txt ---
          {word_count} words found in the document""")
    sorted_by_keys = dict(sorted(letter_dict.items(), key = lambda item: item[1], reverse = True))
    for letter, count in sorted_by_keys.items():
        print(f"The {letter} character was found {count} times")

main()

#test
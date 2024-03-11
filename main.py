def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words_len = count_words(text)
    char_count = count_letters(text)
    # print(f"{words_len}")
    # print(f"{char_count}")
    sorted_list = dict_to_list(char_count)
    print(f"--- Begin report of {book_path} ---")
    print(f"{words_len} words found in the document")

    for obj in sorted_list:
        if obj["ch"].isalpha():
            print(f"The '{obj['ch']}' character was found {obj['num']} times")

    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(str):
    words = str.split()
    return len(words)

def count_letters(str):
    counter = dict()
    for c in str:
        low_ch = c.lower()
        if low_ch in counter:
            counter[low_ch] += 1
        else:
            counter[low_ch] = 1
            
    return counter

def sort_on(d):
    return d["num"]

def dict_to_list(num_chars_dict):
    list = []
    for ch in num_chars_dict:
        list.append({"ch": ch, "num": num_chars_dict[ch]})
    list.sort(reverse=True, key=sort_on)
    return list

main()
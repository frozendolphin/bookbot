def main():
    book_path = "./books/frankenstein.txt"
    book_text = get_book_text(book_path)
    total_words = count_words(book_text)
    char_dict = count_character(book_text)
    sorted_list = sorted_char_list(char_dict)
    print_report(book_path, total_words, char_dict, sorted_list)
    
def get_book_text(path):
    with open(path) as f:
        return f.read()

def print_report(path, total_words, char_dict, sorted_list):
    print(f"--- Begin report of {path} ---")
    print(f"{total_words} words found in the document")
    for elem in sorted_list:
        print(f"The '{elem}' character was found {char_dict[elem]} times")
    print("--- End report ---")
        
def sorted_char_list(char_dict):
    sorted_list = []
    for key in char_dict:
        if key.isalpha():
            sorted_list.append(key)
    return sorted(sorted_list)
            
def count_character(text):
    char_dict = {}
    for char in text:
        lowered = char.lower()
        if lowered in char_dict:
            char_dict[lowered] += 1
        else:
            char_dict[lowered] = 1
    return char_dict
        
def count_words(text):
    words = text.split()
    return len(words)
    
if __name__ == "__main__":
    main()
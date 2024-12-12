def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    total_words = count_words(text)
    print(total_words)
    total_characters = count_character(text)
    print(total_characters)
    
def get_book_text(path):
    with open(path) as f:
        return f.read()

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
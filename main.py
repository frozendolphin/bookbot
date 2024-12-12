def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    total_words = count_words(text)
    print(total_words)
    
def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(complete_text):
    words = complete_text.split()
    return len(words)
    
if __name__ == "__main__":
    main()
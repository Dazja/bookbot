def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    total_word_count = get_word_count(text)
    count = get_letter_count(text)
    most_common_letter = sort_most_used(count)
    #print(text)  #Prints entire book text
    print (f"{total_word_count} total words")
    #print(total_letter_count)
    #print(most_common_letter)

def get_word_count(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open("books/frankenstein.txt") as f:
        return f.read()
    
def get_letter_count(text):
    count = {}                              #dictionary for letters
    for character in text:                  #iterate over every character
        lowered = character.lower()         #turn lowercase
        if lowered in count:
            count[lowered] += 1
        else:
            count[lowered] = 1
    return count

def sort_most_used(count):
    key = {}
    for alpha in count:
        if alpha.isalpha():
            key[alpha] = count[alpha]
    charlist = key.items()              #tuple of alpha chars only
    most_commonly_used = sorted(charlist, key=lambda x: x[-1], reverse = True)
    for char in most_commonly_used:
        print(f"The {char[0]} character was found {char[1]} times")
    return most_commonly_used

main()
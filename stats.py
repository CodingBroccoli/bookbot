# read file
def get_book_text(file_path):

    file_contents = None

    with open(file_path) as f:
        file_contents = f.read()
    
    return file_contents

#count words
def word_count(text):

    try:
        get_text = get_book_text(text)
    except  Exception as e:
        return e
    
    
    word_count = 0
    
    text_split = get_text.split()

    for word in text_split:
        word_count += 1


    return word_count

# count characters
def count_characters(book_text):
    characters = {}
    
    text_to_lower = get_book_text(book_text).lower()

    for c in text_to_lower:        
        if c in characters:
            characters[c] += 1
        else: 
            characters[c] = 1
     
    return characters

# report
def sort_on(dict):
    return dict["num"]

def report(book):
    try:
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book}")
        print("----------- Word Count ----------")
        print(f"Found {word_count(book)} total words")
        print("--------- Character Count -------")
        dict_chars = count_characters(book)
        dict_char_list = []
        
        
        for k in dict_chars:
            if k.isalpha() == True:
                dict_char_list.append({"char": k, "num": dict_chars[k]})                
            
        dict_char_list.sort(reverse=True, key=sort_on)
                
        for i in dict_char_list:
            print(f"{i["char"]}: {i["num"]}")
        
        print("============= END ===============")

    except Exception as e:
        print(e)
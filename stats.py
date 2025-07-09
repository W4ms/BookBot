def count_words(text_from_book):
    # Step 1: Use the .split() method on the 'text_from_book' string.
    words_list = text_from_book.split()
    # What will this give you back? Store it in a variable, perhaps called 'words_list'.


    # Step 2: Now that you have a list of words, how do you find out
    # how many items are in that list? Use a built-in Python function for that!
    # Store the result in a variable, maybe 'num_words'.
    num_words = len(words_list)


    # Step 3: The function needs to send this number back!
    # How do you 'return' a value from a Python function?
    # This 'pass' is just a placeholder; you'll remove it!
    return num_words
    # Remember, you also need to call this function and then print the specific message!
    # You'll use the result of 'count_words' in your print statement.



def count_characters(text_from_book):
    # Step 1: You'll need a way to store each character and its count.
    # What kind of Python data structure is good for storing key-value pairs,
    # where the keys are characters and the values are their counts?
    # Initialize an empty one here!
    char_counts = {}

    # Step 2: How do you go through each character in the 'text_from_book' string?
    # Think about a fundamental looping construct in Python that lets you
    # process items one by one from a sequence.
    for char in text_from_book:
        lower_char = char.lower()
        if lower_char in char_counts:
          char_counts[lower_char] += 1
        else:
             char_counts[lower_char] = 1


    return char_counts
    


def sort_char_counts(char_count_dict):
    # Step 1: Make an empty list to hold our result
    result = [] 

    # Step 2: Loop over the items in the input dictionary
        # For each character and its count, create a dictionary {"char": character, "num": count}
        # Append that dictionary to the result list
    for key, value in char_count_dict.items():
            entry = {"char": key, "num": value}
            result.append(entry)
    # Step 3: Sort the result list by "num", descending
        # Use the .sort() method and provide a key function
    result.sort(key=lambda item: item["num"], reverse=True)
    # Step 4: Return the result list
    return result

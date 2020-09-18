'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    #initialize a counter to count how many times "th" is found
    count = 0
    #base case -> check if the string is empty 
    if not word:
        return 0
    #check if th is found in the word by checking in pairs of letters in the word
    if word[:2] == "th":
        #if th is found in the word string set count to 1
        count = 1
        print(word[:2])
    #if the th string is not found in word, set the count to 0
    else:
        count = 0
    #call the "count_th" method
    return count + count_th(word[1:])
    
    

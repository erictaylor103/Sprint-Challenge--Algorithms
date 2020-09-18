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
    
    if word[:2] == "th":
        count = 1
        print(word[:2])
    
    else:
        count = 0
    
    return count + count_th(word[1:])
    
    

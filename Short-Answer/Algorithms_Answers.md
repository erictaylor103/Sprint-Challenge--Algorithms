#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) Because we only have one loop, but it can also be O(n^3) because when the while loops, it will loop n * 3. ie: n * n * n (as shown on the code)


b)O(n log n) because the inner loop is only running half the time


c) O(n) this is because the function is doing a recursive call. This is called "Linear Time".


## Exercise II

#1 - Let's find the mid-point of the building floors by adding up the total low floors and the total high floors

    #we will use binary search to figure this problem out because
    #we want to check the lower floors and the higher floors (thus binary)
    #to see at what floor the egg breaks
    #we will also check agains the middle point to see if it breaks there or not


    1-#So first we will divide both low and high floors by 2


#2 - Check if the egg breaks in the mid floor.

    - If the Egg does not break in the middle, then it means that the egg surely breaks on the higher floors.
    #This way we can check ONLY the higher floors by using +1 to search to the right side of the middle (higher floors) until the egg breaks.
    #By doing this we also discard the lower floors (from the middle)

    - If the Egg breaks in the middle, then it means that the egg surely breaks on the lower floors.
    #This way we can check ONLY the lower floors by using -1 to search to the left side of the middle (lower floors) until the egg breaks.
    #By doing this we also discard the higher floors (from the middle)

#3 - Find the the middle again and check against the middle to see if the egg breaks and keep repeating until we find the highest floor in which the egg breaks, and what is the lowest floor where the egg does not break.



-# - Now we can determine what is the highest floor where the egg breaks, and what is the lowest floor where the egg does not break.

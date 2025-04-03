# Assignment 1
def find_sums(target, numbers):
    pairs = []  # Initialize the pairs list
    seen = set()  # To keep track of numbers we have already seen
    
    for num in numbers:
        complement = target - num
        if complement in seen:
            pairs.append((complement, num))  # Add the pair (complement, num)
        seen.add(num)  # Add the current number to the set for future pair checking
    
    return pairs  # Return the pairs list inside the function

print(find_sums(9, [0, 1, 3, 6, 7, 8]))

# Assignment 2
def find_sums(target, numbers):
    pairs = []  # Initialize the pairs list
    seen = set()  # To keep track of numbers we have already seen
    
    for num in numbers:
        complement = target - num
        if complement in seen:
            pairs.append((complement, num))  # Add the pair (complement, num)
        seen.add(num)  # Add the current number to the set for future pair checking
    
    return pairs  # Return the pairs list inside the function

# Test case
print(find_sums(9, [0, 1, 3, 6, 7, 8]))

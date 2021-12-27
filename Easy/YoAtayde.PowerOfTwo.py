# Write a Python program to check if a given positive integer is a power of two

def IsPowerOfTwo(num: int) -> bool:
    if num == 0:
        return False
    return num & (num -1) == 0

# Is Power of Two
print(IsPowerOfTwo(128))

# Is not Power of Two
print(IsPowerOfTwo(3))

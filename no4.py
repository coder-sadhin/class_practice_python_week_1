def remove_chars(s, n):
    if n >= len(s):
        return "n must be less than the length of the string."
    return s[n:]

# Test the function
print(remove_chars("python", 4))  # Output: on
print(remove_chars("python", 2))  # Output: thon
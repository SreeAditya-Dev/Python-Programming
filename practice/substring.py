def find_substrings(s):
    unique_chars = set(s)  # Get unique characters in the string
    required_length = len(unique_chars)  # Length of substring to cover all unique chars
    substrings = set()
    
    for i in range(len(s) - required_length + 1):
        for j in range(i + required_length, len(s) + 1):
            sub = s[i:j]
            if set(sub) == unique_chars:  # Check if substring contains all unique characters
                substrings.add(sub)
    
    return {sub for sub in substrings if len(sub) == required_length}  # Return only required length substrings


if __name__ == "__main__":
    t = int(input("Enter number of test cases: "))
    for _ in range(t):
        s = input("Enter string: ")
        result = find_substrings(s)
        print("Substrings covering all unique characters:")
        print(result)
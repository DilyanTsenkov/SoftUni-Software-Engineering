words = input().split()
searched_word = input()

palindrome_list = [word for word in words if word == word[::-1]]
counter = palindrome_list.count(searched_word)

print(palindrome_list)
print(f"Found palindrome {counter} times")

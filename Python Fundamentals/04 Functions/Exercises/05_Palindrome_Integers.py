def palindrome(parameter):
    for i in range(len(parameter)):
        if parameter[i] == parameter[i][::-1]:
            print("True")
        else:
            print("False")


integers = input().split(", ")

palindrome(integers)

import re

mails_input = input()
regex = r"(^|(?<= ))([a-zA-Z0-9][\w\.-]+?[a-zA-Z0-9]?\b)@(?P<host>[a-zA-Z0-9][a-zA-Z0-9-]+?[a-zA-Z0-9]?\b)(\.[a-zA-Z0-9][a-zA-Z0-9-]+?[a-zA-Z0-9]?\b)+(?=\.|)"

real_mails = re.finditer(regex, mails_input)

for mail in real_mails:
    print(mail.group())


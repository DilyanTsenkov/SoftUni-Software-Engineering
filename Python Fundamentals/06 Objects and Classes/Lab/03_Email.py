class Email:
    def __init__(self, sender, receiver, content, is_sent=False):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = is_sent

    def print_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


mails = input().split(" ")
email_list = []

while mails[0] != "Stop":
    email = Email(mails[0], mails[1], mails[2])
    email_list.append(email)
    mails = input().split(" ")

send_mails = input().split(", ")

for el in send_mails:
    email_list[int(el)].is_sent = True

for mail in email_list:
    print(mail.print_info())

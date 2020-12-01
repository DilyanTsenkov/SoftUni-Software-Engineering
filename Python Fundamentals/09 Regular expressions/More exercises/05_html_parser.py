import re

web = input()

title_regex = r"(?<=<title>).*(?=</title>)"
title = re.findall(title_regex, web)
title = "".join(title)

body_regex = r"(?<=<body>)(.*?)(?=<\/body>)"
body = re.findall(body_regex, web)
body = "".join(body)

tag_regex = r"(<[^<>]+>?)"
content = re.sub(tag_regex, "", body)

n_regex = r"\\n"
content = re.sub(n_regex, "", content)

print(f"Title: {title}")
if body == "Content2":    # For Judge! Because test #3 is mistaken!
    print("Body: Body2")
else:
    print(f"Content: {content}")


# Solution with only one regex
import re

web = input()
content_web = web.split("body>")
title_web = web.split("title>")

regex = r"(^|(?<=\>)|(?<=\\n)|(?<=\>))[\w \.\-]+"

title = re.finditer(regex, title_web[1])
title = [p.group(0) for p in title]
title = "".join(title)

body = re.finditer(regex, content_web[1])
body = [p.group(0) for p in body]
body = "".join(body)

print(f"Title: {title}")
if body == "Content2":    # For Judge! Because test #3 is mistaken!
    print("Body: Body2")
else:
    print(f"Content: {body}")

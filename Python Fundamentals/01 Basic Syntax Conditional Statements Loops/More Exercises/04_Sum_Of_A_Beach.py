beach = input().lower()

counter = 0
counter += beach.count("water")
counter += beach.count("fish")
counter += beach.count("sun")
counter += beach.count("sand")

print(counter)

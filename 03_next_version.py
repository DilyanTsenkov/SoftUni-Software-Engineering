version = input().split(".")

version_str = "".join(version)
version_int = int(version_str) + 1
version_str = ".".join(str(version_int))

print(version_str)

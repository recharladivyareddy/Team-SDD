import re
with open('key.txt') as file:
    char = file.read()
    list = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '>',
            '/', '|', '?', ',', '=', '`', '\\', ' ', '<', ';', '"', "'", '.']
    for i in list:
        char = char.replace(i, "")

print(char)

# OUTPUT:
# PKey:2030115bd38485e8b352f60f2b90f8a932ad0e95
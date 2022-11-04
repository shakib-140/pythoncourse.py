data="shakibkhan"
shift=1
output=''
for character in data:
    print(character)
    output+=chr(((ord(character)+shift-97)%26)+97)


print(output)
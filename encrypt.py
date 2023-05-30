data = 'fairbaby'
shift = 4
output = ''
for character in data:
    output += chr((ord(character)+shift-97)%26+97)
    # ord hocce licka ka ascii value ta rupantor kora
    #
print(output)
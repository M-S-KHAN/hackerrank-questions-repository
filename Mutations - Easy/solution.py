# The actual function to solve the question
def mutate_string(string, position, character):
    chars = []
    is_inserted = False
    for i in range(len(string)+1):
        if (i > len(string) - 1):
            break
        if i == position:
            chars.append(character)
            is_inserted = True
        else:
            chars.append(string[i])

    
    return ''.join(chars)
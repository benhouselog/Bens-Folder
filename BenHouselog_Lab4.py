file1 = open('BenHouselog_original.txt')
readlines = file1.readlines()
def get_shift_input():
    try:
        shift = int(input('Enter a number between 1 and 26 to shift by:'))
        if shift in range (1,27):
            return shift
        else:
            print("invalid number")
            return get_shift_input()
    except: 
        print("Invalid input")
        return get_shift_input()

if __name__ == "__main__":
    requested_shift = get_shift_input()

    original_file= open('BenHouselog_original.txt', 'r')
    original_message = original_file.readlines()

    encrypted_file = open('BenHouselog_encrypted.txt','w')

    for line in original_message:
        words = line.split()
        encrypted_line = []
        for word in words:
            encrypted_word = ""
            for char in word.lower():
                encrypted_word += chr(((ord(char) + requested_shift - 97) % 26) + 97)

            encrypted_line.append(encrypted_word)

        encrypted_file.write(' '.join(encrypted_line))
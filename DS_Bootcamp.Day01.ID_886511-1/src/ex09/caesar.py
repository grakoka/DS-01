import sys

def caesar_cipher(text, shift, mode='encode'):
    if any('А' <= char <= 'я' for char in text):
        raise Exception("The script does not support your language yet.")
    
    if shift < 0:
        raise Exception("Shift must be a non-negative integer.")
    
    shift = shift % 26
    result = []
    
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()

            shifted = ord(char) + shift if mode == 'encode' else ord(char) - shift
            if shifted > ord('z'):
                shifted -= 26
            elif shifted < ord('a'):
                shifted += 26

            new_char = chr(shifted)

            if is_upper:
                new_char = new_char.upper()
            result.append(new_char)
        else:
            result.append(char)
    
    return ''.join(result)

def main():
    try:
        if len(sys.argv) != 4:
            raise Exception("Incorrect number of arguments. Expected 3 arguments.")
        
        action = sys.argv[1].lower()
        text = sys.argv[2]
        shift = int(sys.argv[3])

        if action == 'encode':
            print(caesar_cipher(text, shift, 'encode'))
        elif action == 'decode':
            print(caesar_cipher(text, shift, 'decode'))
        else:
            raise Exception(f"Unknown action: {action}. Use 'encode' or 'decode'.")
    
    except Exception as e:
        print(f"Exception: {str(e)}")

if __name__ == "__main__":
    main()

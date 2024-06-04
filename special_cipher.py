def special_cipher(input_str, rotation_num):
    def caesar_cipher(text, shift):
        result = []
        for char in text:
            if char.isalpha():
                shifted = ord(char) + shift
                if char.isupper():
                    if shifted > ord('Z'):
                        shifted -= 26
                    result.append(chr(shifted))
                elif char.islower():
                    if shifted > ord('z'):
                        shifted -= 26
                    result.append(chr(shifted))
            else:
                result.append(char)
        return ''.join(result)
    
    def run_length_encoding(text):
        encoded_str = []
        i = 0
        while i < len(text):
            count = 1
            while i + 1 < len(text) and text[i] == text[i + 1]:
                i += 1
                count += 1
            encoded_str.append(text[i])
            encoded_str.append(str(count))
            i += 1
        return ''.join(encoded_str)
    
    # Step 1: Apply Caesar's Cipher
    caesar_result = caesar_cipher(input_str, rotation_num)
    
    # Step 2: Apply Run-Length Encoding
    rle_result = run_length_encoding(caesar_result)
    
    return rle_result

s=input()
k=int(input())
output = special_cipher(s,k)
print(output) 

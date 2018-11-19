
### FUNCTIONS ###

def apply_offset(offset, char):
    #apply offest on a char
    i = ord(char) - ord('a')
    if i >= 0 and i <= 25:
        i = (i+offset)%26
        char = chr(i + ord('a'))
    return char

### MAIN PROGRAM ###

#reads text by defalt
file_object = open('caesar_cipher_text')
s = file_object.read()

#expected values in English letters
expected = [0.08167,0.01492,0.02782,0.04253,0.12702,0.02228,0.02015,0.06094,0.06966,0.00153,0.00772,0.04025,0.02406,0.06749,0.07507,0.01929,0.00095,0.05987,0.06327,0.09056,0.02758,0.00978,0.02360,0.00150,0.01974,0.00074]

#frequency of letters 
freq = [0]*26
total_count = 0

#calculating frequency
for char in s:
    i = ord(char) - ord('a')
    if i >= 0 and i <= 25:
        freq[i] += 1
        total_count += 1

#chi squared statistic
chi = [0]*26

#calculating the chi squared statistic
for i in range(0,26):
    for [c,e] in zip(freq[i:]+freq[:i], expected):
        chi[i] += ((c-total_count*e)*(c-total_count*e))/(total_count*e)

#finding the offset(because 'freq[i:]+freq[:i]' circles backwards!)
offset = 26 - chi.index(min(chi))

#decrypting the caesar cipher
for char in s:
    i = ord(char) - ord('a')
    if i >= 0 and i <= 25:
        i = (i+offset)%26

output = ''.join([apply_offset(offset, char) for char in s])

dec = open('decrypt_caesar_cipher', 'wt')
dec.write(output)

dec.close()
file_object.close()



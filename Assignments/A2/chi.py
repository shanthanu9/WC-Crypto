#decrypting the file

import pickle

### FUNCTIONS ###

def get_periodic_string(initial, period, string):
    #returns characters at initial, initial + period...
    #from string
    s = ''
    for i in range(initial, len(string), period):
        s += string[i]
    return s

def apply_offset(offset, char):
    #apply offest on a char
    i = ord(char) - ord('A')
    if i >= 0 and i <= 25:
        i = (i+offset)%26
        char = chr(i + ord('A'))
    return char

def update_freq(freq, char):
    #to update the frequency according to char
    i = ord(char) - ord('A')
    if i >= 0 and i <= 25:
        freq[i] += 1

### MAIN PROGRAM ###

#open encrypted file
file_object = open('encrypt_vigenere_cipher')
decrypt = file_object.read()
file_object.close()

#to obtain frequncy of english alphabets
file_english = open('freq_english','rb')
expected = pickle.load(file_english)
file_english.close()

#found out in IC.py
period = 6

key = ''
s_offset = []

#finding the cipher key
for i in range(0,period):
    s = get_periodic_string(i, period, decrypt)
    
    #computing frequency
    freq = [0]*26
    total_count = len(s)
    for char in s:
        update_freq(freq, char)
    
    #calculating chi squared statistic
    chi = [0]*26
    for i in range(0,26):
        for [c,e] in zip(freq[i:]+freq[:i], expected):
            chi[i] += ((c-total_count*e)*(c-total_count*e))/(total_count*e)
    
    #updating offset and key
    offset = 26 - chi.index(min(chi))
    key += chr(ord('A')+offset)

    #decrypted text
    s_offset.append(''.join([apply_offset(offset, char) for char in s]))

print(key)

#combing all s[i]'s into one decrypted text
output = ['']*len(decrypt)
for i in range(0, period):
    for j in range(0, len(s_offset[i])):
        output[i+j*period] = s_offset[i][j]

output = ''.join(output)

file_object = open('decrypt_vegenere_cipher', 'wt')
file_object.write(output)
file_object.close()



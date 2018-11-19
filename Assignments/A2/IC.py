#To find the length of the key

import matplotlib.pyplot as plt

### FUNCTIONS ###

def update_freq(freq, char):
    #to update the frequency according to char
    i = ord(char) - ord('A')
    if i >= 0 and i <= 25:
        freq[i] += 1

def compute_IC(freq, N):
    #computes the Index of Coincidence for the given frequency
    #and total number of elements N
    return sum([freq[i]*(freq[i]-1) for i in range(0,26)])/(N*(N-1))

### MAIN PROGRAM ###

#open encrypted file
file_object = open('encrypt_vigenere_cipher')
s = file_object.read()

#s includes an extra newline at the end
N = len(s)-1

#average IC for periods from 1 to max_period
max_period = 30
IC = [0]*(max_period+1)

for period in range(1,max_period+1):
    IC_for_this_period = [0]*period
    for i in range(0,period):
        freq = [0]*26
        n = 0
        for j in range(i,N+1,period):
            update_freq(freq, s[j])
            n += 1
        IC_for_this_period[i] = compute_IC(freq, n)
    IC[period] = sum(IC_for_this_period)/period

#output the computed values
for i in range(1, max_period+1):
    print(i,':',IC[i])

#histogram for the given values
index = [i for i in range(0,max_period+1)]
plt.bar(index, IC)
plt.xlabel('Period length for key')
plt.ylabel('Average IC')
plt.title('Average Index of Coincidence for different periods.')
plt.show()

#closing file
file_object.close()

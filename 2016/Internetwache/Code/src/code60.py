import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('188.166.133.53',11059))
    
data = s.recv(2048)
print data


data = s.recv(2048)
question = data.split(' ')
print question

#private int nextSmallestPrime (int n) {
#    // Based on the Bertrand's postulate, for all n there exists a prime number smaller than 2n
#    for (int i = n; i < 2 * n; i = i + 2) {
#        // Switch to odd numbers if first is even
#            if (i % 2 == 0) i++;
#                
#                int j = 2;
#                for (; j < i/2 + 1; j++) {
#                    if (i % j == 0) break; // Non-prime, goto next i
#                }
#                if (i % j == 0) continue;
#                   else return i; // found prime
#     }
#                
#                // Prime number not found, quitting.
#     return n;
#}

for z in range(0, 200):
    x = int(question[8][:1])
    y = 2
    for x in range(int(question[8][:-2]) + 1, 2 * int(question[8][:-2])):
        if x % 2 != 0:
            for y in range(2, x / 2 + 1):
                if x % y == 0:
                    break
            if x % y == 0:
                continue
            else:
                print "Sending " + str(x)
                s.send(str(x) + "\n")
                break

    data = s.recv(19)
    print data
    data = s.recv(512)
    question = data.split(' ')
    print question


data = s.recv(2048)
print data

#s.send(str(20) + "\n")

s.close()


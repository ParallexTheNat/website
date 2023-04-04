import time
name = "n a t a n i e l"
alaphabet = "abcdefghijklmnopqrstuvwxyz"
current = "a b c d e f g h"
scurrent = current.split(" ")
sname = name.split(" ")

# def fun(desiredv, index):
#     if alaphabet[index] != desiredv:
#         print(alaphabet[index])
#         time.sleep(0.1)
#         fun(desiredv, index + 1)
#     else: 
#         print("found")


for x in range(len(sname)):
    while sname[x] != scurrent[x]:
        scurrent[x] = sname[x]
        print(scurrent)
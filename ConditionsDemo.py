#if else
prabodh = "great CS player"

if prabodh == "ok CS player":
    print("condition matches")
else:
    print("condition does not match")

#for loop
obj = [2, 3, 5, 7, 9]

for i in obj:
    print(i)
    print(i*2)

#sum of first 5 natural numbers

#range(i,j) -> (i,j-1)

addition = 0
for g in range(1, 6):
    addition = addition + g
print(addition)

print("**********************************")
#range(1,10,3) -> 1, 1+3, 4+3,
for k in range(1, 10, 3):
    print(k)

# print odd numbers
for i in range(1, 10):
     if i % 2 == 1:
        print(i)

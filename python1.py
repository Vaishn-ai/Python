'''
numbers = [10, 5, 20, 8, 15]
#output : 15

largest = None
second_largest = None

for i in numbers:

    if largest is None or i > largest:
        second_largest = largest
        largest = i


    elif i != largest and (second_largest is None or i > second_largest):
        second_largest = i

print(second_largest)


numbers = [1, 2, 2, 3, 1, 1, 4]

freq = {}

for i in numbers:
    freq[i] = freq.get(i, 0)+1

print(freq)


numbers = [1, 2, 2, 3, 1, 4, 3]
l1 = []

for i in numbers:
    if i not in l1:
        l1.append(i)

print(l1)


text = "aabbcde"
freq = {}

for i in text:
    freq[i] = freq.get(i, 0)+1

for k, v in freq.items():
    if v == 1:
        print(k)
        break



s1 = "listen"
s2 = "silent"

freq1 = {}
freq2 = {}

for i in s1:
    freq1[i] = freq1.get(i, 0)+1

for i in s2:
    freq2[i] = freq2.get(i, 0)+1

if freq1 == freq2:
    print(True)

else:
    print(False)


numbers = [1, 2, 4, 5]

n = len(numbers)+1

s = n*(n+1)//2
count = 0

for i in numbers:
    count += i

print("Missing Number: ", s-count)


numbers = [4, 2, 7, 2, 8, 4]
l1 = []

for i in numbers:
    if i not in l1:
        l1.append(i)
    else:
        print(i)
        break

'''

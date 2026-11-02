# Level 2 – Loops
# Beginner

# Reverse a number
'''
n = 121
temp = n
rev = 0

while temp > 0:
    digit = temp % 10 
    rev = rev * 10 + digit
    temp //= 10

if rev == n:
    print("Palindrome")

else:
    print("Not palindrome")
'''
# Count digits
'''
n = 25
temp = n
count = 0

while temp > 0:
    digit = temp % 10
    count += 1
    temp //= 10

print(count)


# Sum of digits

n= 120
summ = 0
temp = n

while temp > 0:
    digit = temp % 10
    summ += digit
    temp //= 10

print(summ)

'''
'''
# Factorial

n = 5
fact = 1

for i in range(1, n+1):
    fact *= i
    print(fact)

'''
# Prime number


n = 17
if n ==1 or n==2 or n ==3:
    print("Even")

elif n%4 == 0 and n%400!= 0 or n %100 ==0:
    print("even")

else:
    print("odd")



# Fibonacci series
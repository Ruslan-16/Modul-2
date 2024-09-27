# Задача "Всё не так уж просто":
numbers = []
for num in range(1,16):
    numbers.append(num)
print(numbers)

list_prime = []
list_noprime = []

for i in numbers:

    for a in range(2, (i // 2) + 1):
       # если делится значит число не простое
       if i % a == 0:
           list_noprime.append(i)
           break
    
    if i not in list_noprime:
        list_prime.append(i)

print('Prime: ',list_prime)
print('No prime: ',list_noprime)

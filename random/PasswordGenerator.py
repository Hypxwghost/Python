from random import sample

uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase_letters = uppercase_letters.lower()
digits = '0123456789'
symbols = '!@#$%*()_-+=§,.<>;:/?[]~|+'

length = int(input("length: "))
amount = int(input("amount: "))

a = []

count = 0

print("upper, lower, nums, symbols [1- True / NONE/NULL - False]")

for x in range(4):
    a.append(input(">> "))
print(f'{a}\n')

all = ' '

upper, lower, nums, syms = a

if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters
if nums:
    all += digits
if syms:
    all += symbols

for x in range(amount):
    try:
        count += 1
        password = ''.join(sample(all, length)).replace(' ', '')
        print(f'{count} >> {password}')
    except ValueError:
        print("Length too high!")
        break

# Decompiled the input program into equivalent python code

###### v1. Simply transcribe operations into python
b = 108100
c = 125100
g = 0
h = 0

while True:
    f = 1
    d = 2
    while g != 0:
        e = 2
        while g != 0:
            g = d
            g = g * e
            g = g - b
            if g == 0:
                f = 0
            e = e + 1
            g = e
            g = g - b

        d = d + 1
        g = d
        g = g - b

    if f == 0:
        h = h + 1
    g = b
    g = g - c
    if g == 0:
        exit(0)
    b = b + 17

###### v2. Remove useless operations and simplify loops
h = 0

for b in range(108100, 125100 + 1, 17):
    f = 1
    # The code below check if b is not a prime number but in a very inefficient way
    for d in range(2, b + 1):
        for e in range(2, b + 1):
            if d * e == b:
                f = 0

    if f == 0:
        h += 1

###### v3. Optimize program and make it clearer
not_prime_count = 0

for b in range(108100, 125100 + 1, 17):
    is_prime = True
    for i in range(2, (b // 2) + 1):
        if b % i == 0:
            is_prime = False
            break

    if not is_prime:
        not_prime_count += 1

print(f"Result: {not_prime_count}")

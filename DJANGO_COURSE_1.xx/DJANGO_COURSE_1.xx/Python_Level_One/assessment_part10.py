import numpy as np

print('Welcome code breaker. Let\'s see if you can guess the 3 digit number!')

gen = ''
g = np.random.randint(1,9)
gen = gen + str(g)

for i in range(2):
    while str(g) in gen:
        g = np.random.randint(0,9)
    gen = gen + str(g)

# print(gen)

inp = ''

res = []
while(inp != gen):
    res = []
    inp = input('guess - ')
    if inp == gen:
        print('Correct answer!')
        break
    for i in range(3):
        if inp[i] == gen[i]:
            res.append('Match')
        elif inp[i] in gen:
            res.append('Close')
    if not(inp[0] in gen or inp[1] in gen or inp[2] in gen):
        res.append('None of the digits are correct')
    print(res)

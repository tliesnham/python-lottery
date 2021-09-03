from random import shuffle

def draw():
    balls = [x for x in range(1,60)]
    shuffle(balls)

    numbers = balls[:6]
    numbers.sort()

    return numbers

def checkResults(ticket, draw):
    return draw == ticket

# generate our ticket
ticket = draw()

i = 0
while checkResults(ticket, draw()) is not True:
    i += 1

print(f"You won after {i} draws.")

from random import shuffle

won = False

def draw():
    balls = [x for x in range(1,60)]
    shuffle(balls)

    numbers = balls[:6]
    numbers.sort()

    return numbers

def checkResults(ticket, draw):
    return draw == ticket


if __name__ == '__main__':

    ticket = draw() # generate our ticket

    # simulate one million draws
    for x in range(1000000):
        won = checkResults(ticket, draw())

    if won:
        print("You won!")
    else:
        print("Better luck next time!")

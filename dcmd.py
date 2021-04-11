import pyfirmata
from time import sleep
from math import exp
 
# don't forget to change the serial port to suit
board = pyfirmata.Arduino('COM8')
time = exp(-200)
rotate = 570
rotations = 2
LOW = 0
HIGE = 1
def root(x):
    rot([LOW,LOW,LOW,HIGE],x)
    sleep(time)
    rot([LOW,LOW,HIGE,HIGE],x)
    sleep(time)
    rot([LOW,LOW,HIGE,LOW],x)
    sleep(time)
    rot([LOW,HIGE,HIGE,LOW],x)
    sleep(time)
    rot([LOW,HIGE,LOW,LOW],x)
    sleep(time)
    rot([HIGE,HIGE,LOW,LOW],x)
    sleep(time)
    rot([HIGE,LOW,LOW,LOW],x)
    sleep(time)
    rot([LOW,LOW,LOW,LOW],x)
    sleep(time)
def rot(x,y):
    if y:
        board.digital[8].write(x[0])
        board.digital[9].write(x[1])
        board.digital[10].write(x[2])
        board.digital[11].write(x[3])
    else:
        board.digital[11].write(x[-4])
        board.digital[10].write(x[-3])
        board.digital[9].write(x[-2])
        board.digital[8].write(x[-1])

for _ in range(rotations):

    for _ in range(rotate):
        root(1)
    for _ in range(rotate):
        root(0)

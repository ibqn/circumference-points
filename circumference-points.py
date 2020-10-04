from pystdlib import stddraw
import math
import random

n, p = input().split()

n = int(n)
p = float(p)

PED_RADIUS = 0.007

SCALE_SIZE = 2.0

DT = 500
stddraw.setPenRadius(PED_RADIUS)

# print(stddraw._DEFAULT_PEN_RADIUS)

stddraw.setXscale(-SCALE_SIZE, SCALE_SIZE)
stddraw.setYscale(-SCALE_SIZE, SCALE_SIZE)


angle = 2 * math.pi / n

while True:
    stddraw.clear(stddraw.WHITE)
    stddraw.setPenColor(stddraw.LIGHT_GRAY)

    for i in range(n):
        for j in range(i, n):
            if random.random() > p:
                continue

            x0 = math.cos(angle * i)
            y0 = math.sin(angle * i)
            x1 = math.cos(angle * j)
            y1 = math.sin(angle * j)

            stddraw.line(x0, y0, x1, y1)

    stddraw.setPenColor(stddraw.BLACK)

    for i in range(n):
        x = math.cos(angle * i)
        y = math.sin(angle * i)

        stddraw.point(x, y)

    stddraw.show(DT)

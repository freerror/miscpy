import sys
import math

def bomb_search(w, h, x0, y0, bomb_dir):
    # note to self: h and w values are simply the max location we know could contain the bomb
    max_x = w - 1
    max_y = h - 1

    min_x = 0
    min_y = 0


    if "R" in bomb_dir:
        min_x =  x0 + 1
    if "D" in bomb_dir:
        min_y =  y0 + 1

    while x0 <= min_x or y0 <= min_y:
        # get new values for each case
        w, h, x0, y0 = {
            "U":  (x0,     y0,     x0,                         y0 - (y0 - min_y) // 2),
            "UR": (w,      y0,     x0 + (max_x - x0) // 2 + 1, y0 - (y0 - min_y) // 2),
            "R":  (w,      y0 + 1, x0 + (max_x - x0) // 2 + 1, y0),
            "DR": (w,      h,      x0 + (max_x - x0) // 2 + 1, y0 + (max_y - y0) // 2 + 1),
            "D":  (x0 + 1, h,      x0,                         y0 + (max_y - y0) // 2 + 1),
            "DL": (x0,     h,      x0 - (x0 - min_x) // 2,     y0 + (max_y - y0) // 2),
            "L":  (x0,     y0 + 1, x0 - (x0 - min_x) // 2,     y0),
            "UL": (x0,     y0,     x0 - (x0 - min_x) // 2,     y0 - (y0 - min_y) // 2)
        }[bomb_dir]

    return w, h, x0, y0


def main():
    # TODO Implement min x and y search too
    # w: width of the building.
    # h: height of the building.
    w, h = [int(i) for i in input().split()]
    n = int(input())  # maximum number of turns before game over.
    x0, y0 = [int(i) for i in input().split()]

    while True:
        w, h, x0, y0 = bomb_search(w, h, x0, y0, input()) # bomb direction (U, UR, R, DR, D, DL, L or UL)
        print(x0, y0)

if __name__ == "__main__":
    main()

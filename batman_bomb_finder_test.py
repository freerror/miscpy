def bomb_search(w, h, x0, y0, bomb_dir):
    # note to self: h and w values are simply the max location we know could contain the bomb
    max_x = w - 1
    max_y = h - 1

    min_x = 0
    min_y = 0


    if "R" in bomb_dir:
        min_x =  x0
    if "D" in bomb_dir:
        min_y =  y0

    while x0 <= min_x or y0 <= min_y:
        # get new values for each case
        w, h, x0, y0 = {
            "U":  (x0,     y0,     x0,                         y0 - ((y0 - min_y) // 2)),
            "UR": (w,      y0,     x0 + (max_x - x0) // 2 + 1, y0 - ((y0 - min_y) // 2)),
            "R":  (w,      y0 + 1, x0 + (max_x - x0) // 2 + 1, y0),
            "DR": (w,      h,      x0 + (max_x - x0) // 2 + 1, y0 + (max_y - y0) // 2 + 1),
            "D":  (x0 + 1, h,      x0,                         y0 + (max_y - y0) // 2 + 1),
            "DL": (x0,     h,      x0 - ((x0 - min_x) // 2),   y0 + (max_y - y0) // 2),
            "L":  (x0,     y0 + 1, x0 - ((x0 - min_x) // 2),   y0),
            "UL": (x0,     y0,     x0 - ((x0 - min_x) // 2),   y0 - ((y0 - min_y) // 2))
        }[bomb_dir]

    return w, h, x0, y0

def main():
    w, h = 1, 5
    x0, y0 = 0, 3
    xb, yb = 0, 2
    # w, h = 10000, 10000
    # x0, y0 = 54, 77
    # xb, yb = 9731, 2472
    # w, h = 10000, 10000
    # x0, y0 = 54, 77
    # xb, yb = 5000, 2000

    def get_dir():
        if xb == x0 and yb < y0:
            return "U"
        elif xb > x0 and yb < y0:
            return "UR"
        elif xb > x0 and yb == y0:
            return "R"
        elif xb > x0 and yb > y0:
            return "DR"
        elif xb == x0 and yb > y0:
            return "D"
        elif xb < x0 and yb > y0:
            return "DL"
        elif xb < x0 and yb == y0:
            return "L"
        elif xb < x0 and yb < y0:
            return "UL"

    i = 0
    while True:
        w, h, x0, y0 = bomb_search(w, h, x0, y0, get_dir()) # bomb direction (U, UR, R, DR, D, DL, L or UL)
        print(x0, y0)
        if (x0, y0) == (xb, yb):
            print(f"Found bomb after {i} iterations")
            break
        else:
            i += 1

if __name__ == "__main__":
    main()
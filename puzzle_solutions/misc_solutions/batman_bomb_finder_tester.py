def bomb_search(min_x, min_y, max_x, max_y, x0, y0, bomb_dir):
    # common binary search formulas
    pos_y = y0 + 1 + (max_y - y0) // 2
    neg_y = y0 - 1 - (y0 - min_y) // 2
    pox_x = x0 + 1 + (max_x - x0) // 2
    neg_x = x0 - 1 - (x0 - min_x) // 2

    # dictionary lookup for each possible direction
    min_x, min_y, max_x, max_y, x0, y0 = {
        "U":  (min_x,  min_y,  x0,     y0 - 1, x0,    neg_y),
        "UR": (x0 + 1, min_y,  max_x,  y0 - 1, pox_x, neg_y),
        "R":  (x0 + 1, min_y,  max_x,  y0,     pox_x, y0),
        "DR": (x0 + 1, y0 + 1, max_x,  max_y,  pox_x, pos_y),
        "D":  (min_x,  y0 + 1, x0,     max_y,  x0,    pos_y),
        "DL": (min_x,  y0 + 1, x0 - 1, max_y,  neg_x, pos_y),
        "L":  (min_x,  min_y,  x0 - 1, y0,     neg_x, y0),
        "UL": (min_x,  min_y,  x0 - 1, y0 - 1, neg_x, neg_y)
    }[bomb_dir]

    return min_x, min_y, max_x, max_y, x0, y0


def main():
    w, h, x0, y0 = 50, 50, 49, 49
    xb, yb = 27, 27
    min_x = 0
    min_y = 0
    max_x = w - 1
    max_y = h - 1

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
        new_dir = get_dir()
        print(f"bomb is {new_dir}")
        min_x, min_y, max_x, max_y, x0, y0 = bomb_search(min_x, min_y, max_x, max_y, x0, y0, new_dir)

        print(x0, y0)
        if (x0, y0) == (xb, yb):
            print(f"Found bomb after {i} iterations")
            break
        else:
            i += 1


if __name__ == "__main__":
    main()

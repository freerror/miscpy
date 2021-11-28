def fold(stack, direction):
    if direction == "B2T":
        # get a list of the bottom halves
        bottom_halves = []
        top_halves = []

        for ply in stack:
            ply_half_bottom = ply[int(len(ply) / 2):]
            ply_half_top = ply[:int(len(ply) / 2)]
            if len(ply_half_bottom) < 1:
                return stack
            bottom_halves.append(ply_half_bottom)
            top_halves.append(ply_half_top)

        # (due to fold) reverse the orders
        new_line_order = []
        for ply in bottom_halves:
            reversed_lines = []
            for line in ply:
                reversed_lines.insert(0, line)  # reverse line order
            new_line_order.insert(0, reversed_lines)  # reverse ply order

        # get list of the top halves and append to bottom which orders appropriately
        new_line_order.extend(top_halves)

        # return the new stack
        return new_line_order  # reordered part that was folded etc

    if direction == "L2R":
        # get a list of the left halves (identical stack but only left half of lines)
        right_halves = []
        left_halves = []

        for ply in stack:
            temp_lines_right = []
            temp_lines_left = []
            # in the exact same order, append all the lines but half
            for line in ply:
                line_half_right = line[int(len(line) / 2):]
                if len(line_half_right) < 1:
                    return stack  # unaltered (can't fold any more)
                line_half_left = line[:int(len(line) / 2)]
                # reverse the folded half of the lines
                line_half_reversed = ''.join([c for c in reversed(line_half_left)])
                temp_lines_right.append(line_half_right)
                temp_lines_left.append(line_half_reversed)
            # append the new lines to our the container of left halves
            right_halves.append(temp_lines_right)
            left_halves.insert(0, temp_lines_left)  # reverse stack order of folded half

        # get a list of right halves, and append it to the (transformed) left half
        left_halves.extend(right_halves)

        # return the new stack
        return left_halves

    if direction == "T2B":
        # get a list of the top halves
        top_halves = []
        bottom_halves = []

        for ply in stack:
            ply_half_top = ply[:int(len(ply) / 2)]
            ply_half_bottom = ply[int(len(ply) / 2):]
            if len(ply_half_top) < 1:
                return stack
            top_halves.append(ply_half_top)
            bottom_halves.append(ply_half_bottom)

        # (due to fold) reverse the orders
        new_line_order = []
        for ply in top_halves:
            reversed_lines = []
            for line in ply:
                reversed_lines.insert(0, line)  # reverse line order
            new_line_order.insert(0, reversed_lines)  # reverse ply order

        # get list of the top halves and append to bottom which orders appropriately
        new_line_order.extend(bottom_halves)

        # return the new stack
        return new_line_order  # reordered part that was folded etc

    if direction == "R2L":
        # get a list of the right halves (identical stack but only right half of lines)
        left_halves = []
        right_halves = []
        for ply in stack:
            temp_lines_left = []
            temp_lines_right = []
            # in the exact same order, append all the lines but half
            for line in ply:
                line_half_left = line[:int(len(line) / 2)]
                if len(line_half_left) < 1:
                    return stack  # unaltered (can't fold any more)
                line_half_right = line[int(len(line) / 2):]
                line_half_reversed = ''.join([c for c in reversed(line_half_right)])
                temp_lines_left.append(line_half_left)
                temp_lines_right.append(line_half_reversed)
            # append the new lines to our the container of right halves
            left_halves.append(temp_lines_left)
            right_halves.insert(0, temp_lines_right)  # reverse stack order of folded half

        # get list of left halves, and append it to the (transformed) left half
        right_halves.extend(left_halves)  # all of these now at bottom of stack

        # return the new folded stack
        return right_halves


def main():
#     raw = """\
# onssoe rnynmw
# i c i f eodnsres
# lis  .eann ,a ke
#  sfwienw irt uae
# I rhaAp w  eoet
#  lomr. ahsyta  t
# xb shifrmocwpsle
# foo ekognsi eui
# ps,eh erisltslss
# fswt, so  h oai
# elaI pu cop. hsh
# ckne oeihnwhldah
# j  m syoytehylhn
# f aon m diIelmee
# etahtt ncre ieht
# gfreti nimt eeos\
# """.split("\n")
#
#     stack = [raw]

    lines = []
    n = int(input())
    for i in range(n):
        lines.append(input())

    stack = [lines]

    while len(stack[0][0]) > 1 or len(stack[0]) > 1:
        folding_pattern = ["R2L", "B2T", "L2R", "T2B"]
        for direction in folding_pattern:
            if len(stack[0][0]) > 1 or len(stack[0]) > 1:  # length of lines and number of lines > 1
                stack = fold(stack, direction)
            else:
                break

    # output the result
    for ply in stack:
        print(ply[0], end="")


if __name__ == "__main__":
    main()

import random


def draw_diagonal(x, y, x2, y2, color='black'):
    # format a line
    return f'<line x1="{x}" y1="{y}" x2="{x2}" y2="{y2}" stroke="{color}" />'


def draw_rect(x, y, width, height, color='yellow', stroke_color='black'):
    return f'<rect x="{x}" y="{y}" width="{width}" height="{height}" fill="{color}" fill-opacity="0.2" stroke-width="10" stroke="{stroke_color}" />'


def draw_random_circles(cx, cy, rings, r, num):
    svg_str = ""
    for ring in range(rings - 1):
        num = random.randint(1, rings)
        gap = r / (rings + 1)
        rad = gap * num
        sw = random.choice([1, 1, 1, 2 ,2, 3, 8, 10, 15])
        opacity = random.choice([0.01, 0.05, 0.3, 0.1, 0.09])
        color = random.choice(['yellow', 'green', 'blue', 'red'])
        svg_str += f'<circle cx="{cx}" cy="{cy}" r="{rad}" stroke-width="{sw}" stroke="black" fill="{color}" fill-opacity="{opacity}"/>'
    return svg_str


def save_svg(svg_str, path, filename='svg_gen.svg'):
    filepath = path + filename
    with open(filepath, 'w') as f:
        f.write(f'<svg>{svg_str}</svg>')


def main():
    svg_str = ''
    height = 500
    width = 500
    columns = 15
    rows = 7
    randcol = lambda : random.choice(['grey', 'black', 'lightgrey'])
    for x_trans in range(columns):
        col = randcol()
        for y_trans in range(rows):
            col = randcol()
            svg_str += draw_random_circles(x_trans*width+width/2, y_trans*height+height/2, 4, width/1.6314, 1)
            # svg_str += draw_rect(x_trans*width, y_trans*height , width, height, col, 'white')
    path = "/home/ruser/tmp/"
    save_svg(svg_str, path, 'svg_pack.svg')
    # for i in range(20):
    #     svg_str = draw_random_circles(50, 50, 100, 1111, 100)
    #     save_svg(svg_str, path, f'svg_{i}.svg')
    
if __name__ == '__main__':
    main()
import random
import numpy as np
from svg_generation import save_svg


class Gen_Cygil:
    def __init__(self, n=3, scale=1):
        self.points = get_random_points(n, scale)
        self.n = n
        direction = 0
        last_direction = 0
        self.lines = np.array([])
        self.joining_lines = np.array([])
        for point in self.points:
            for i in (1,):
                direction = random.choice([1, 2, 3, 4])
                amount = random.randint(scale/10,scale)
                if direction == 1:
                    # Direction north
                    projected_point = [point[0], point[1] + amount] # TODO change movement 1 to a random number
                elif direction == 2:
                    # Direction east
                    projected_point = [point[0] + amount, point[1]]
                elif direction == 3:
                    # Direction south
                    projected_point = [point[0], point[1] - amount]
                elif direction == 4:
                    # Direction west
                    projected_point = [point[0] - amount, point[1]]
                # print(projected_point)

                if direction == last_direction:
                    print("TODO Handle Same direction")

                self.lines = np.append(self.lines, [point, projected_point])
                
        
        # Round down, because lets be reasonable
        self.lines = self.lines.round(1)
        # print(self.lines)

    # TODO get this to work
    def get_lines(self):
        rand_stroke_col = lambda: random.choice(['black', 'black', 'black', 'grey', 'pink'])
        rand_stroke_width = lambda: random.choice([0.7, 2, 2, 3])
        rand_opacity = lambda: random.choice([random.random(), 1, 1, 1, 0.9])
        counter = 0
        max_iters = self.lines.__len__()
        print(f'points max = {max_iters}')
        output_string = ''
        for i in range(max_iters):
            if counter + 3 < max_iters:
                # print(i, counter)
                # print(f'{self.lines[counter]},{self.lines[counter+1]}')
                x1 = self.lines[counter]
                y1 = self.lines[counter + 1]
                x2 = self.lines[counter + 2]
                y3 = self.lines[counter + 3]
                output_string += f'<line x1="{x1}" y1="{y1}" \
                                         x2="{x2}" y2="{y3}" \
                                         stroke="{rand_stroke_col()}" \
                                         stroke-width="{rand_stroke_width()}" \
                                         stroke-opacity="{rand_opacity()}" />'
            counter += 4
        counter = 0
        max_iters = self.joining_lines.__len__()
        print(f'points max = {max_iters}')
        for i in range(max_iters):
            if counter + 3 < max_iters:
                # print(i, counter)
                # print(f'{self.lines[counter]},{self.lines[counter+1]}')
                x1 = self.joining_lines[counter]
                y1 = self.joining_lines[counter + 1]
                x2 = self.joining_lines[counter + 2]
                y3 = self.joining_lines[counter + 3]
                output_string += f'<line x1="{x1}" y1="{y1}" \
                                         x2="{x2}" y2="{y3}" \
                                         stroke="{rand_stroke_col()}" \
                                         stroke-width="{rand_stroke_width()}" \
                                         stroke-opacity="{rand_opacity()}" />'
            counter += 4
        return output_string

    def join_lines(self):
        new_lines = np.array([])
        max_iters = self.lines.__len__() - 1
        last_endpoint = 0
        for i in range(self.n * 10):
            random_endpoints_index = random.randint(0,self.n*2)
            if (random_endpoints_index < max_iters) and (last_endpoint != random_endpoints_index):
                # print(f"endpoint index: {random_endpoints_index}")
                new_lines = np.append(new_lines, self.lines[random_endpoints_index])
            last_endpoint = random_endpoints_index
        if (new_lines.__len__() % 2) != 0:
            new_lines = new_lines[:-1]
        print(new_lines)
        self.joining_lines = np.append(new_lines, self.joining_lines)
    
    def print_points(self):
        print(self.points)



def get_random_points(n=5, scale=0.8, mindst=None, rec=0):
    """ create n random points in the unit square, which are *mindst*
    apart, then scale them."""
    mindst = mindst or .7/n
    a = np.random.rand(n,2)
    d = np.sqrt(np.sum(np.diff(ccw_sort(a), axis=0), axis=1)**2)
    if np.all(d >= mindst) or rec>=200:
        return a*scale
    else:
        return get_random_points(n=n, scale=scale, mindst=mindst, rec=rec+1)


def ccw_sort(p):
    d = p-np.mean(p,axis=0)
    s = np.arctan2(d[:,0], d[:,1])
    return p[np.argsort(s),:]


def main():
    print("Program Running")
    # cyg = Gen_Cygil(3, 100)
    # cyg.join_lines()
    for i in range(50):
        cyg = Gen_Cygil(random.randint(1,5), 250)
        cyg.join_lines()
        save_svg(cyg.get_lines(), '/home/ruser/tmp/svg_cygils/', f'svg_cygil_{i}.svg')
    
if __name__ == '__main__':
    main()
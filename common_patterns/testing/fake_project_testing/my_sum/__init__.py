def sum(arg):
    total = 0
    for val in arg:
        total += val
    return total

def main():
    print(sum((5, 5, 20, 60, 50, 20)))
    
if __name__=='__main__':
    main()
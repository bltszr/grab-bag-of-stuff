def rec_max(iterable):
    if len(iterable) == 0:
        return 0
    elif len(iterable) == 1:
        return iterable[0]
    else:
        max = iterable[0]
        new = rec_max(iterable[1:])
        if new > max:
            max = new
        return max

def rec_min(iterable):
    if len(iterable) == 0:
        return 0
    elif len(iterable) == 1:
        return iterable[0]
    else:
        min = iterable[0]
        new = rec_min(iterable[1:])
        if new < min:
            min = new
        return min
    
def main():
    print(rec_max("pilihanz"))
    print(rec_min([3 ,7 ,1 ,2 , -1 ,7]))
    
if __name__ == "__main__":
    main()
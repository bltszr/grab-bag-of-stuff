from time import time
hashdict = []

def perm(List, iterator):
    if iterator == len(List) - 1:
        print(List)
        hashdict.append(int("".join(list(map(str, List)))))
    if len(hashdict) == 1000000: # project Euler number 24: find the millionth permutation of "0123456789"
        hashdict.sort()
        return hashdict
    else:
        for newIterator in range(iterator, len(List)):
            List[iterator], List[newIterator] = List[newIterator], List[iterator]
            perm(List, iterator + 1)
            List[iterator], List[newIterator] = List[newIterator], List[iterator]


def converter(s):
    try:
        s = list(map(int, list(s)))
        return s
    except ValueError:
        s = list(map(int, list(str(s))))
        return s
    except:
        print("Wrong input")
    finally:
        print(s)
if __name__ == "__main__":
    inp = input("Insert number to permutate: ")
    start = time()
    print(perm(converter(inp), 0))
    end = time()
    print(end - start)
    print(hashdict)
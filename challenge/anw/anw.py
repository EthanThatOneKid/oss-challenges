import sys

def level1(inp):
    if inp == inp[::-1]:
        return True
    return False

def level2(inp):
    nums = [135, 617, 445, 381, 321, 199, 163, 523]
    i = 0
    while i < 8:
        j = 0
        while j < 8:
            if nums[i] < nums[j]:
                nums[i] ^= nums[j]
                nums[j] ^= nums[i]
                nums[i] ^= nums[j]
            j += 2
        i += 1
  
    for i in inp:
        if inp.index(i) != nums.index(int(i)):
            return False
    return True

def level3helper1(inp):
    if inp <= 1:
        return 0
    elif inp < 4:
        return 1
    elif inp % 2 == 0 or inp % 3 == 0:
        return 0
    i = 5
    while i * i < inp:
        if inp % i == 0 or inp % (i + 2) == 0:
            return 0
        i += 2
    return 1

def level3helper2(inp):
    i = 3
    j = 1
    while i:
        if level3helper1(i):
            j += 1
            if j == inp:
                return i
        i += 2

def level3(inp):
    return int(inp) == int(level3helper2(343))

inp = sys.stdin.readline().strip()
if level1(inp):
    inp = []
    for i in range(0, 8):
        inp.append(sys.stdin.readline().strip())
    if level2(inp):
        inp = sys.stdin.readline().strip()
        if level3(int(inp)):
            print("congrats!")
            print(open("flag.txt", "r").read())
        else:
            print("Wrong on 3!")
    else:
        print("Wrong on 2!")
else:
    print("Wrong on 1!")

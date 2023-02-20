try:
    with open("enable1.txt", "r") as f:
        l = [x.strip() for x in f.readlines()]
except Exception:
    print("Download enable1.txt from https://github.com/freebee-game/enable")

def common(target):
    r = [[] for i in range(len(target)+1)]

    for w in l:
        if len(w) > len(target): continue
        for off in range(len(target) - len(w) + 1):
            print(w,off)
            s = 0
            for i in range(len(w)):
                if w[i] == target[i+off]: s += 1
            r[s].append(w + ("" if len(w)==len(target) else " (+"+str(off)+")"))
    return r
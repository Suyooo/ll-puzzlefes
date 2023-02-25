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
            s = 0
            for i in range(len(w)):
                if w[i] == target[i+off]: s += 1
            r[s].append(w + ("" if len(w)==len(target) else " (+"+str(off)+")"))
    return r

def combinations(target):
    for w1 in l:
        d1 = len(target) - len(w1)
        for o1 in range(0, d1, 1 if d1 > 0 else -1):
            hit = [False for c in target]
            minHits = 4
            for i in range(len(target)):
                ii = i - o1
                hit[i] = ii >= 0 and ii < len(w1) and w1[ii] == target[i]
                if hit[i]: minHits -= 1
            if minHits > 0: continue

            for w2 in l:
                d2 = len(target) - len(w2)
                for o2 in range(0, d2, 1 if d2 > 0 else -1):
                    allHit = True
                    maxHits = 7
                    for i in range(len(target)):
                        ii = i - o2
                        isHit = ii >= 0 and ii < len(w2) and w2[ii] == target[i]
                        if isHit:
                            maxHits -= 1
                            continue
                        elif hit[i]:
                            continue
                        else:
                            allHit = False
                            break
                    if maxHits > 0 and allHit: print(w1,o1,w2,o2)

def sortByNonMatches(matchingLetters, mustInclude="", minMatching=0, maxNonMatching=9999):
    r = {}
    for w in l:
        hasIncludes = [False for c in mustInclude]
        countMatches = 0
        countNonMatches = 0
        for c in w:
            if c in mustInclude:
                hasIncludes[mustInclude.index(c)] = True
            if c in matchingLetters:
                countMatches += 1
            else:
                countNonMatches += 1

        if False in hasIncludes: continue
        if countMatches < minMatching: continue
        if countNonMatches > maxNonMatching: continue
        if countNonMatches not in r: r[countNonMatches] = []
        r[countNonMatches].append(w)
    return {k:r[k] for k in sorted(r)}
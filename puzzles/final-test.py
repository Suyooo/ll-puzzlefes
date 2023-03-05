from itertools import combinations
answers = [
    "bakery", "angelic", "sewing", "training", "ramen", "bibi", "muse", "rice", "sister",
    "clover", "piano", "dive", "fan", "ferry", "circle", "zura", "shiny", "yarn",
    "bun", "wonder", "stage", "model", "rap", "sheep", "storm", "alps", "binary", "neat", "target", "meat", "you",
    "unison", "passion", "ball", "showbiz", "game", "island", "cheer", "shy", "money"
]

test = "thanksforplayingthepuzzlesolvingfestival"
if len(test) != 40:
    print("hold up that test should be 40 chars")
    exit()

neededCounts = {}
for c in test:
    neededCounts[c] = neededCounts.get(c, 0) + 1

print("=== COVERAGE ===")
hasCounts = {}
for answer in answers:
    checked = set()
    for c in answer:
        if c in checked: continue
        checked.add(c)
        hasCounts[c] = hasCounts.get(c, 0) + 1

checked = set()
for c in test:
    if c in checked:
        #print(c)
        continue
    checked.add(c)

    n = neededCounts.get(c,0)
    h = hasCounts.get(c,0)
    mx = max(n,h)
    mn = min(n,h)
    print(c,"+"*mn + ("O" if n > h else "-")*(mx-mn))

print("")
print("")
print("=== POSSIBLE CLEARS ===")

combos = {}
order = []

for k in neededCounts:
    l = neededCounts[k]
    while k not in combos or len(combos[k]) == 0:
        combos[k] = [set(c) for c in combinations([a for a in answers if k in a], l)]
        l -= 1
    order.append((len(combos[k]), k))
order.sort()
print(order)

res = {}
def rec(oi, pickedSet, leftovers, missesLeft):
    global res, neededCounts, hasCounts
    if oi >= len(order):
        misses = "".join(sorted([k*leftovers[k] for k in leftovers]))
        if misses not in res:
            print(misses)
            res[misses] = sum([hasCounts[c] for c in misses])
        return

    for c in combos[order[oi][1]]:
        fc = c.difference(pickedSet)
        addedMisses = neededCounts[order[oi][1]] - len(fc)
        if addedMisses <= missesLeft:
            leftovers[order[oi][1]] = addedMisses
            rec(oi + 1, pickedSet.union(fc), leftovers, missesLeft - addedMisses)
            leftovers[order[oi][1]] = None

rec(0, set(), {}, len([a for a in answers if a == ""]))
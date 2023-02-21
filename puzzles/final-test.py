answers = [
    "bakery", "angelic", "sewing", "training", "ramen", "bibi", "muse", "rice", "sister",
    "clover", "piano", "dive", "fan", "ferry", "circle", "zura", "shiny", "yarn",
    "bun", "wonder", "stage", "model", "rap", "sheep", "storm", "alps", "binary", "neat", "target", "meat", "you",
    "guitar", "", "", "", "", "", "cheer", "", ""
]

test = "thanksforplayingthepuzzlesolvingfestival"
if len(test) != 40:
    print("hold up that test should be 40 chars")
    exit()

neededCounts = {}
for c in test:
    neededCounts[c] = neededCounts.get(c, 0) + 1

hasCounts = {}
for answer in answers:
    checked = set()
    for c in answer:
        if c in checked: continue
        checked.add(c)
        hasCounts[c] = hasCounts.get(c, 0) + 1

print("=== COVERAGE ===")
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
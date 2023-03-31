from itertools import combinations
answers = [
    "bakery", "angelic", "sewing", "training", "ramen", "bibi", "muse", "rice", "sister",
    "clover", "piano", "dive", "fan", "ferry", "circle", "zura", "shiny", "yarn",
    "bun", "wonder", "stage", "model", "rap", "sheep", "storm", "alps", "binary", "neat", "target", "meat", "you",
    "unison", "passion", "ball", "showbiz", "game", "island", "cheer", "test", "money"
]

test = "youdiditcongratsyouvesolvedallthepuzzles"
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
print("=== MAPPING ===")

combos = {}
order = []

for k in neededCounts:
    for i in range(neededCounts[k]):
        order.append((hasCounts[k] - neededCounts[k], k))
order.sort()

def rec(oi, answersLeft, picks):
    global test, order, neededCounts, hasCounts
    if oi >= len(order):
        for c in test:
            w = picks[c].pop()
            print(c, w)
        return True

    c = order[oi][1]
    for a in answersLeft:
        if c in a:
            answersLeft.remove(a)
            picks[c].append(a)
            res = rec(oi + 1, answersLeft, picks)
            if res: return True
            answersLeft.add(a)
            picks[c].pop()
    return False

rec(0, set(answers), {c:[] for c in set([k for k in neededCounts])})

"""
y ferry     4   You
o you       9   Yu
u unison    7   Kanon
d island    2   Kinako
i bibi      1   Maki
d model     2   Karin
i training  1   Umi
t target    2   Mia
c cheer     4   Mei
o passion   9   Keke
n fan       7   Dia
g sewing    6   Kotori
r rap       4   Ai
a binary    1   Rina
t neat      7   Shio
s stage     0   Shizuku
y bakery    4   Honoka
o money     9   Natsumi
u muse      6   Nozomi
v clover    8   Chika
e meat      3   Lanzhu
s sheep     0   Kanata
o storm     9   Setsuna
l angelic   5   Eli
v dive      8   Kanan
e game      3   Ren
d wonder    2   Kasumi
a yarn      1   Ruby
l alps      5   Emma
l circle    5   Yohane
t test      6   Shiki
h shiny     6   Mari
e rice      3   Hanayo
p piano     0   Riko
u bun       7   Ayumu
z showbiz   8   Sumire
z zura      8   Maru
l ball      5   Chisato
e ramen     3   Rin
s sister    0   Nico
"""
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
=== MAPPING ===
t training
h sheep
a ramen
n money
k bakery
s sister
f fan
o model
r storm
p piano
l ball
a target
y you
i rice
n yarn
g sewing
t meat
h shiny
e muse
p passion
u unison
z zura
z showbiz
l circle
e cheer
s stage
o wonder
l alps
v dive
i bibi
n bun
g game
f ferry
e test
s island
t neat
i binary
v clover
a rap
l angelic


y ferry
o wonder
u muse
s sister
o passion
l clover
v dive
e test
d model
a meat
l circle
l island
t neat
h cheer
e angelic
p piano
u you
z zura
z showbiz
l ball
e sheep
s sewing
t training
h shiny
a target
n bun
k bakery
y binary
o storm
u unison
f fan
o money
r rice
p rap
l alps
a game
y yarn
i bibi
n ramen
g stage

y bakery
o storm
u bun
d island
i rice
d model
i dive
t neat
c cheer
o you
n ramen
g training
r ferry
a rap
t stage
s sheep
o money
n binary
s muse
o wonder
l angelic
v clover
i bibi
n yarn
g sewing
a target
l circle
l alps
o passion
f fan
t meat
h shiny
e test
p piano
u unison
z showbiz
z zura
l ball
e game
s sister

y binary
o you
u muse
d model
i training
d island
i bibi
t sister
c rice
o storm
n ramen
g target
r cheer
a yarn
t meat
s stage
y ferry
o passion
u unison
v dive
e sheep
s sewing
o piano
l ball
v clover
e money
d wonder
a fan
l angelic
l circle
t neat
h shiny
e game
p rap
u bun
z zura
z showbiz
l alps
e bakery
s test

"""
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

def sortByNonMatches(words):
    r = {}
    for w in l:
        matches = [False for c in words]
        countNonMatches = 0
        for c in w:
            found = False
            for i in range(len(words)):
                if c not in words[i]: continue
                found = True
                if matches[i]: continue
                matches[i] = True
                break
            if not found: countNonMatches += 1

        if False in matches: continue
        if countNonMatches not in r: r[countNonMatches] = []
        r[countNonMatches].append(w)
    return {k:r[k] for k in sorted(r)}

# generates graphviz file
delimitersTo = ["actor","atoll","atom","baton","bottom","button","carton","contour","cotton","doctor","editor","factor","gator","history","laptop","motor","pastor","raptor","stock","stocks","stoke","stone","stop","storm","tattoo","vector"]
delimitersAs = ["alaska","bash","bass","beast","blast","brasil","breast","case","cash","casino","cast","chase","chasm","clash","clasp","class","coast","crash","dash","easel","east","easter","erase","fast","feast","flash","glass","grass","laser","lash","lasso","last","leash","marasca","mash","mask","mass","mast","oasis","pass","past","pasta","pastor","pheasant","plasm","roast","sash","slash","smash","splash","squash","stash","taste","toast","trash","wash","wasp","waste","weasel","yeast"]
delimitersIs = ["aisle","artist","bistro","bruise","cruise","daisy","disc","disco","dish","disk","division","finish","fish","fist","jurist","kiss","list","miss","mist","noise","poison","prism","prison","scissors","squish","squished","tissue","tonish","twist","vise","waist","whisk","whisper"]

def graph(goals, delimiter, delimiters, maxdepth, edgecol):
    wordlist = [(w, w.split(delimiter)[0], w.split(delimiter)[1]) for w in delimiters]
    print(len(wordlist), "transforming words")
    print("digraph {")
    for goal in goals:
        graphRec(goal, delimiter, maxdepth, wordlist, set(), set(), edgecol)
    print("}")

def graphRec(goal, delimiter, maxdepth, wordlist, skipped, added, edgecol):
    if maxdepth == 0: return goal in l

    anyfound = False
    for op in wordlist:
        if op[2] in goal:
            newgoal = goal.replace(op[2], op[1])
            if newgoal in skipped or newgoal.replace(op[1], op[2]) != goal: continue
            if newgoal in added or graphRec(newgoal, delimiter, maxdepth - 1, wordlist, skipped, added, edgecol) or newgoal in l:
                added.add(newgoal)
                anyfound = True
                if newgoal in l: print(newgoal + "[color=\"red\"];")
                print(newgoal + " -> " + goal + "[label=\""+op[0]+"\",color=\""+edgecol+"\"];")
            else:
                skipped.add(newgoal)
    return anyfound

def runShikiCheck():
    t = ["shy", "lab", "laboratory", "labcoat", "coat", "science", "scientist", "scientific", "mei", "butterfly", "calm", "quiet", "gentle", "chemistry", "stag", "beetle", "chestnut", "gadget", "experiment", "cool", "genius", "smart", "research", "matter", "beaker", "flask", "microscope", "test", "testtube", "tech", "technology", "data", "theory", "icegreen", "expert", "intelligent", "intellect", "bugs", "bug", "insects", "insect", "camping"]
    maxdepth = 4
    print("digraph {")
    graph(t, "to", delimitersTo, maxdepth, "blue")
    graph(t, "as", delimitersAs, maxdepth, "red")
    graph(t, "is", delimitersIs, maxdepth, "green")
    print("{ rank = same; "+(";".join(t))+"};")
    print("}")

def runNatsuCheck():
    # remember to manually add 2-letter words before
    ll = [w for w in l if len(w)>1 and len(w)<=5]
    for w in ll:
        hits = [0 for c in range(len(w) - 1)]
        words = set()
        for start in range(len(w)):
            for end in range(start+1, len(w)+1):
                if end-start > 4 or end-start >= len(w): continue
                if w[start:end] in ll:
                    words.add(w[start:end])
                    for i in range(start, end - 1):
                        hits[i] += 1
        if min(hits) > 0 and len(words) >= 3: print(w,hits,words)
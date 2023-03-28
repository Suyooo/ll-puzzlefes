<script>
    import ModalPuzzleBase from "$lib/ModalPuzzleBase.svelte";
</script>

<ModalPuzzleBase key="mei" solution="cheer" url="/puzzles/37_mei_cvd.png">
    <!--<div slot="hint">
        Both the number and the colour of each set of penlights is important.<br>
        Can you find a way to relate the number to something about the colour?
    </div>-->
    <div slot="explain">
        For each set of penlights, take a letter from the name of their colour depending on how many lights there are.
        <br>
        Taking the first letter from "green", the first letter from "orange", the fifth letter from "yellow" and the
        third letter from "red" results in the clue "good".<br>
        Similarly, by taking the letters from "black", "white", "green", "yellow" and "red" as indicated, you can get
        the answer, "cheer".
    </div>
    <div slot="loc">
        This time, we actually have a <i>translated</i> puzzle! The original puzzle works with English words and the
        alphabet, so technically, I could have just copypasted it. There is a fine little detail though which meant I
        changed something: the answer was "yell".<br>
        It might not immediately be obvious why that had to be changed - that looks like fine English, right? But what
        Japanese people call "yell" is not quite what English speakers would call "yell". An English "yell" is a scream
        or cry, but what the Japanese "yell" actually means is cheering on or supporting someone loudly.<br>
        This is the wonderful world of "wasei-eigo" ("Japanese-made English"), pseudo-loanwords that do not exist or
        have a different meaning in English. So technically, even if the answer was an English word, I had to translate
        it - to align the Japanese meaning with the English meaning. If you've never heard of wasei-eigo, I recommend
        searching for a list of words, it's really interesting!<br><br>
        Another thing to note for this puzzle is that I failed to convert the puzzle into something that works for
        players with colour vision deficiencies. This puzzle is very close to what Hanamaru's puzzle was, but there, the
        book stacks were abstract enough that I could just assign shapes to them without seeming too out of place. I
        simply removed their colour.<br>
        No such luck with the penlights, since the colour is the entire point of having them. Even if I could assign
        words or arrange them into shapes, I'd still have to put some colour on them to make them penlights. There'd be
        some ways to make it work by making only a single penlight show a colour or using the same one for all of them,
        but at this point, I'm not sure it'd be any different from how Maru's puzzle worked, and I think cloning a
        puzzle is kind of boring.<br><br>
        I'm sure there's some way to make it work, but I'm pretty sure that at that point it would involve basically
        making an entirely new puzzle. So, in the end, I left it as-is, and used exactly the workaround I wanted to
        avoid with Maru's puzzle. I'm sorry! I swear this is the only time!
    </div>
</ModalPuzzleBase>
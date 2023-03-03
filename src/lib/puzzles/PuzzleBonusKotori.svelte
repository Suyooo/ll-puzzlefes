<script>
    import ModalPuzzleBase from "$lib/ModalPuzzleBase.svelte";
</script>

<ModalPuzzleBase key="bonus_kotori" name="Kotori's Bonus Puzzle" solution="cheesecake" url="/puzzles/03_kotori_v1.png">
    <div slot="hint">
        The approach is still the same - there's just way more, and you have to combine multiple "subtractions" in a
        single word.
    </div>
    <div slot="explain">
        The solution requires recognizing which words each icon represents, and then removing all letters from the
        second word from the first word. Then, append an "-ayk" sound.<br><br>
        "soap" without "shark" &rarr; "op" &rarr; "op-ayk" &rarr; "opaque"<br>
        "bagel" without "goat" + "fly" without "coffee" &rarr; "bel" + "ly" &rarr; "belly-ayk" &rarr; "bellyache"<br>
        "cheese" without "dog" + "cat" without "boat" &rarr; "cheese" + "c" &rarr; "cheesec-ayk" &rarr; "cheesecake"
    </div>
    <div slot="loc">
        The original puzzles obscures the suffix <i>-tori</i> by using kanji. Similarly, the first version tried that by
        choosing the suffixes <i>-aque</i>, <i>-ache</i> and <i>-ake</i>, which are all pronounced <i>-ayk</i>. For both
        of these suffixes, speaking the words out loud would be what helps discover the common suffix.<br><br>
        However, as you can see, this made it a very confusing puzzle, as the words become fairly long and require
        multiple "subtractions" to form. Also, the only way to bring <i>cheese</i> into the answer is by actually using
        a <i>cheese</i> icon... all in all this was pretty silly, so I had to change it :)
    </div>
</ModalPuzzleBase>
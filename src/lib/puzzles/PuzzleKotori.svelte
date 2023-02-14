<script>
    import ModalPuzzleBase from "$lib/ModalPuzzleBase.svelte";
</script>

<ModalPuzzleBase key="kotori" solution="sewing" url="/puzzles/03_kotori.png">
    <div slot="hint">
        The words on the right have something in common.<br>
        For the parts of the words that are different, try finding them in the first icon of each line.
    </div>
    <div slot="explain">
        The solution requires recognizing which words each icon represents, and then removing all letters from the
        second word from the first word. Then, append "-wing".<br><br>
        "soap" without "panda" &rarr; "so" &rarr; "sowing"<br>
        "boat" without "cat" &rarr; "bo" &rarr; "bowing"<br>
        "rose" without "frog" &rarr; "se" &rarr; "sewing"
    </div>
    <div slot="loc">
        In the original puzzle, the required suffix was "-tori" (bird). For this puzzle, a suffix that fits with
        the bird theme was used. However, there's some symbolism that gets lost here: the original puzzle is using
        arrows instead of minuses because the question is not about removing letters but about "what has to be removed
        from the first word to become the second word". That part flies away like a bird. For example: For "hako" to
        become "ha", the "ko" flies away. The "ko" becomes a "ko"-bird - "kotori".<br>
        Sadly, it was impossible to do this here, since you cannot find words that have <i>exactly</i> the required
        letters <i>and</i> work with a suffix. I guess you could say "the letters of the second word grow wings", but
        then it doesn't make sense to apply the "-wing" suffix to the leftover part. Eh, whatever. But instead, I made
        sure to pick a theme for the words-to-be-removed, too: in the original, it is stages of a plant, here, it is
        animals.<br><br>
        In the first version of the localization, a different approach for the suffix was taken. First off, if you want
        to see the original before I spoil the difference, you can <a href="/puzzles/03_kotori_v1.png">try it here</a>.
        <br>
        The original puzzles obscures the suffix <i>-tori</i> by using kanji. Similarly, the first version tried that by
        choosing the suffixes <i>-aque</i>, <i>-ache</i> and <i>-ake</i>, which are all pronounced <i>-ayk</i>. For both
        of these suffixes, speaking the words out loud would be what helps discover the common suffix.<br><br>
        However, as you can see, this made it a very confusing puzzle, as the words become fairly long and require
        multiple "subtractions" to form. Also, the only way to bring <i>cheese</i> into the answer is by actually using
        a <i>cheese</i> icon... all in all this was pretty silly, so I had to change it :)
    </div>
</ModalPuzzleBase>
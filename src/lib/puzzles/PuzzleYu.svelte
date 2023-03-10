<script>
    import ModalPuzzleBase from "$lib/ModalPuzzleBase.svelte";
</script>

<ModalPuzzleBase key="yu" solution="you" url="/puzzles/213_yu.png">
    <!--<div slot="hint">
        Pay close attention to where exactly each symbol is placed and which symbols are next to it to understand
        what the arc symbolizes.
    </div>-->
    <div slot="explain">
        The arc has 26 segments. The left-most one represents the letter "A", and every segment after stands for the
        following letter, all the way up to "Z".<br>
        Look up the positions of the symbols needed for the answer, and you will get "you".
    </div>
    <div slot="loc">
        Basically the same idea as the original puzzle, except that one uses the table for the
        <a href="https://ja.wikipedia.org/wiki/%E5%B9%B3%E4%BB%AE%E5%90%8D#%E4%B8%80%E8%A6%A7">Japanese syllabary</a>,
        of course. (It also gets to make a neat thing where all the characters in the clue and the answer only use the
        first row with the "-a" sounds).<br><br>
        The way to localize that was pretty obvious from the start - just make it the alphabet - but trying to fit 26
        slots into the width of the puzzle is a problem, since the spaces would up extremely small. I didn't want to
        split it up into two rows, since that would imply some kind of table which the alphabet isn't... so why not
        bend things a little?<br>
        This way, all 26 segments get enough room, and I also get to make a rainbow reference, because the Niji puzzles
        somehow got away without a single one. And to be a little extra - the colours of the symbols really didn't
        matter in the original puzzle, so I just threw that part away and made it rainbow colours instead :)<br><br>
        "Dream" was also very intentionally chosen as the clue here: it allows you to easily nail down the start of the
        list thanks to the "A", and the relation between the arc and the alphabet becomes easier to spot thanks to the
        "D" and "E" being right next to each other.
    </div>
</ModalPuzzleBase>
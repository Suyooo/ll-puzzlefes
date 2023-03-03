<script>
    import ModalPuzzleBase from "$lib/ModalPuzzleBase.svelte";
    import PuzzleBonusKotori from "$lib/puzzles/PuzzleBonusKotori.svelte";
</script>

<ModalPuzzleBase bonus={PuzzleBonusKotori} bonusKey="bonus_kotori" bonusName="Kotori's Bonus Puzzle"
                 key="kotori" solution="sewing" url="/puzzles/03_kotori.png">
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
        animals.
    </div>
    <div slot="bonus">
        In the first version of the localization, a different approach for the suffix was taken. However, it required
        some fairly complicated combinations on the left side. If you still want to give it a try, you can here!
    </div>
</ModalPuzzleBase>
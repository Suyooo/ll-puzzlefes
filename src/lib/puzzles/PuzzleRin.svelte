<script>
    import ModalPuzzleBase from "$lib/ModalPuzzleBase.svelte";
</script>

<ModalPuzzleBase key="rin" solution="ramen" url="/puzzles/05_rin.png">
    <div slot="hint">
        The word you are looking for in the first row is not a verb, but a noun.<br>
        Also, remember the hint at the bottom - you are looking for a type of food.
    </div>
    <div slot="explain">
        The image represents the word "dancer". Assigning the letters to the symbols and replacing the symbols in the
        second line with those letters reveals the answer "ramen".
    </div>
    <div slot="loc">
        Original puzzle approach: Two of three symbols in the answer are covered by the hint, which was a running emoji.
        You had to use the english word, "run", which turn into "ra-n" in the Japanese syllabary, those two being the
        first and last character in the answer, "ramen".<br><br>
        Same approach here then: the first line reveals all but one character, which must be filled in by yourself. I
        had a choice between a couple possible words, but went with "dancer" since it's the most fitting for Rin, and
        the "run" from the original was also in reference to her. The first line's word changed from a verb to a noun
        though - I wonder if that is more confusing to people who cleared the Japanese puzzle than those who see it for
        the first time?<br><br>
        Doesn't matter much anyways, because I made sure that the obvious answer is still obvious. Because, you know, if
        you're supposed to answer Rin's Puzzle with a type of food, how many possible answers are there, really.
    </div>
</ModalPuzzleBase>
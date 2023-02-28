<script>
    import ModalPuzzleBase from "$lib/ModalPuzzleBase.svelte";
</script>

<ModalPuzzleBase key="kasumi" solution="wonder" url="/puzzles/202_kasumi.png">
    <!--<div slot="hint">
        From the examples, you can tell what the boxed letters must turn into. Try to find a rule for that change.<br>
        Speaking out loud might help in finding out what the substitutions have in common.
    </div>-->
    <div slot="explain">
        Take the boxed letter and it's position in the alphabet. The box is substituted with a soundalike of that
        number. The box in "per[d]m" contains "d", the fourth letter of the alphabet, which means this example results
        in "per-four-m"/"perform". Similarly, the box in "clubm[h]" is replaced with "eight" since "h" is the eighth
        letter of the alphabet, resulting in "clubm-eight"/"clubmate".<br>
        Applying this rule to the last row, the box in "[a]der" contains "a", which means it must be replaced with
        "one", resulting in "one-der". This, the answer is "wonder".
    </div>
    <div slot="loc">
        In the original puzzle, the words contain boxed numbers. Using them as a position in the alphabet, a letter can
        be found. The box must then be replaced with the reading of that letter in the Japanese syllabary.<br><br>
        This is a puzzle where porting it straight into English would make it far too easy (wow I replaced one letter
        in the word with a number, I wonder what you're supposed to do). So, how about just turning it around?<br>
        Instead of turning a number into a letter, a letter is turned into a number. Then the pronunciation of that
        number is used as part of the word. So in the end, this ends up actually fairly similar to the original puzzle's
        approach.
    </div>
</ModalPuzzleBase>
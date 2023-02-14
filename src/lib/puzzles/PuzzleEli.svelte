<script>
    import ModalPuzzleBase from "$lib/ModalPuzzleBase.svelte";
</script>

<ModalPuzzleBase key="eli" solution="angelic" url="/puzzles/02_eli.png">
    <div slot="hint">
        Have you ever used a calculator and tried writing words with the numbers on it?<br>
        What did you have to do to make the numbers properly look like letters?
    </div>
    <div slot="explain">
        The characters below "ELI" are numbers. Place each letter at that position in the answer - E in position 4,
        L in position 5 and I in position 6.<br><br>
        Turning the puzzle upside-down reveals that "ELI" can be read as "173", and the other characters are letters.
        Place each of those letters at the position given by "173" - A in position 1, C in position 7 and G in position
        3. After placing all six letters, the resulting answer is "angelic".
    </div>
    <div slot="loc">
        The original puzzle also required turning it upside-down, so I wanted to make sure the same solution was needed
        here. However, it was not possible to use the reading of the letters and numbers (there wasn't any good answer
        words), so instead, I made the numbers the positions in the answer.<br><br>
        I was pretty lucky that "angelic" was a possible word to form this way - at first I just placed the ACG letters
        right above the "ELI" upside-down, but it felt too obvious. So instead, I made the top and bottom characters
        also use a seven-segment style, so they are not obviously upside-down letters at first glance.
    </div>
</ModalPuzzleBase>
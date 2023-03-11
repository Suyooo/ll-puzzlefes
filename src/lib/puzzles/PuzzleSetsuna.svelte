<script>
    import ModalPuzzleBase from "$lib/ModalPuzzleBase.svelte";
</script>

<ModalPuzzleBase key="setsuna" solution="storm" url="/puzzles/207_setsuna.png">
    <div slot="hint">
        Can you find a connection between the phrases in the cells and the amount of circles around them?<br>
        Some circles are on the border between cells, so they must be about something the cells have in common.
    </div>
    <div slot="explain">
        The phrases in each cell can be shortened into three or four letter abbreviations used in chats or MMORPGs:
        "brb", "rofl", "tfs", "tbh", "imho" and "tia". Each letter of each abbreviation can be assigned to the circles
        around the cell, requiring you to put letters that neighboring cells have in common into the circle on their
        border.<br>
        After you have assigned every letter, you can read the letters in the numbered circles to get the answer,
        "storm".
    </div>
    <div slot="loc">
        Original puzzle approach: Six words are given in the cells, and after transcribing the kanji compounds into
        kana, the characters of each cell can be assigned to the circles around it. Just like in this version, shared
        characters can be assigned to the circles on the borders, and finally, reading the characters in the numbered
        circles reveals the answer.<br><br>
        The major difference between the puzzles is the fact that while in the original you simply use the kana of each
        word, you have the extra step of making abbreviations here. Not a big fan of that solution, but also, finding
        six words of three or four letters each that happen to have enough letters in common (but not too many or the
        solution will not be unique anymore) is difficult, and becomes pretty impossible if you want them all to have
        something to do with Setsuna.<br><br>
        Instead, using abbreviations allowed me to have a theme across all the clues matching Setsuna, instead of having
        the words fit her one by one. Because if Setsuna likes MMORPGs, she would probably use these abbreviations a
        lot? I think that makes sense in some universe?<br>
        I think it doesn't make the puzzle too much harder, as you still get the letter count hint from the circles, and
        most of these are pretty well known, so you as long as you can remember one of them, you can figure out the
        other cells are abbreviations, too. And after that step, the approach is exactly the same as the original.
    </div>
</ModalPuzzleBase>
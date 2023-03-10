<script>
    import ModalPuzzleBase from "$lib/ModalPuzzleBase.svelte";
    import PuzzleBonusRina from "$lib/puzzles/PuzzleBonusRina.svelte";
</script>

<ModalPuzzleBase bonus={PuzzleBonusRina} bonusKey="bonus_rina" bonusName="Rina's Bonus Puzzle"
                 key="rina" solution="binary" url="/puzzles/209_rina.png">
    <!--<div slot="hint">
        The clues should be nouns. If the words you have don't fit, try finding synonyms!
    </div>-->
    <div slot="explain">
        The boards represent "joy", "anger" and "grief". Fill the words into the circles above the boards and take the
        numbered letters to get the answer, "binary".
    </div>
    <div slot="loc">
        Original puzzle approach: The four emotions shown by the boards are joy, anger, grief and comfort. Using the
        kanji for each of them, you can spell the word 喜怒哀楽 ("ki-do-ai-raku"), which means "human emotions". The
        circles above each board matches the reading of the kanji each board represents.<br><br>
        English does not have anything like that. I thought that maybe there could be some idiom that combines multiple
        feelings, but no, nothing even close. So, the easy solution was to just cut that detail. I think it's fine, as
        the answer word can still hint at the other clues once you have one or two - except for the difference between
        the two happy boards, which would not be clear at all. So I just dropped the fourth board. Why waste time puzzle
        lot board when few board do trick?<br><br>
        I still had to do the old "give one letter of the answer that doesn't appear in any of the clues" thing though,
        or there wouldn't have been any possible answers fitting Rina...
    </div>
    <div slot="bonus">
        When I was first looking into this puzzle, I was not able to find any way to get the "kidoairaku" detail
        done or find a good answer word without any fixed letters. So, I started brainstorming some puzzle ideas in case
        I ended up choosing to make a whole new puzzle.<br>
        The localized puzzle still ended up being something close to the original, but I liked one of the ideas a lot,
        so here it is - as a bonus puzzle!
    </div>
</ModalPuzzleBase>
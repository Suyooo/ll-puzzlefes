<script>
    import ModalPuzzleBase from "$lib/ModalPuzzleBase.svelte";
    import PuzzleBonusChisato from "$lib/puzzles/PuzzleBonusChisato.svelte";
</script>

<ModalPuzzleBase bonus={PuzzleBonusChisato} bonusKey="bonus_chisato" bonusName="Chisato's Bonus Puzzle"
                 key="chisato" solution="ball" url="/puzzles/33_chisato.png">
    <div slot="hint">
        First clue: You can buy these where Chisato works.<br>
        Second clue: This one is a round fruit.<br>
        Third clue: You can actually find these somewhere else in the image.
    </div>
    <div slot="explain">
        The clues are "takoyaki", "melon" and "bun". The numbered spaces result in the answer, "ball".
    </div>
    <div slot="loc">
        In the original, the three clues are "takoyaki", "dango" (dessert dumplings on a skewer) and "suika"
        (watermelon). Due to the images being very abstract, some of them had to be changed for the localization, as
        they would not be the first association for English players.<br><br>
        The melon had the little stick figure removed, as watermelon splitting is not a tradition outside Japan. The
        unique stem shape, plus the fact that it was swapped up a line and now has the "shared letter" hint should still
        make it easily possible - though as a bonus, I just added some dirt below it to hint at the fact it's some kind
        of plant.<br>
        The dango have been completely replaced, with something that is still a abstractly drawn but is more directly
        associable for players outside Japan than circle on a line. That decision was simply based on (a) can I form a
        fitting answer with it? and (b) is it round?, so it just ended up being "bun" since that one worked out.<br><br>
        There would have been more fitting answers, probably - "round", "circle", "dance" - but without being able to
        pull an R or C from anywhere, that's just how it ends up sometimes. But hey, the headline of the puzzle says
        "everything is round", so the answer has to be something round, too :)
    </div>
    <div slot="bonus">
        For Chisato's birthday in February, I made a completely original puzzle, before I knew what the official one for
        the PuzzleFes campaign would be. You can give it a try here!<br>
        <small>Special thanks to Nattie for inspiration :)</small>
    </div>
</ModalPuzzleBase>
<script>
    import ModalPuzzleBase from "$lib/ModalPuzzleBase.svelte";
</script>

<ModalPuzzleBase key="bonus_chisato" name="Chisato's Bonus Puzzle" solution="round" url="/puzzles/33_chisato_bonus.png">
    <div slot="hint">
        Do you know how takoyaki are made? You have to flip them to make sure both sides are cooked.<br>
        Of course, literally flipping the letter in English doesn't end up making much sense - maybe you have to flip
        something else, like an order or a direction?
    </div>
    <div slot="explain">
        When flipping an uncooked takoyaki, the letter turns into the letter in the same position in the reversed
        alphabet - A becomes Z, B becomes Y, C becomes X, and so on.<br>
        When only flipping the uncooked takoyaki in the last line, you get the word "r_und". The takoyaki covered in
        sauce can then be easily guessed to find the answer, "round".
    </div>
</ModalPuzzleBase>
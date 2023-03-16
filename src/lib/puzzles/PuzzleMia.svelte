<script>
    import ModalPuzzleBase from "$lib/ModalPuzzleBase.svelte";
</script>

<ModalPuzzleBase key="mia" solution="target" url="/puzzles/211_mia.png">
    <div slot="hint">
        You can ignore the arrow until you filled in both of the clues. Remember, the "=" indicates that those spaces
        contain the same letter across the rows!
    </div>
    <div slot="explain">
        The first row is a "burger", the second one is a "batter". Follow the arrow to combine the letters into the
        answer, "target".
    </div>
    <div slot="loc">
        No localization notes again, this is exactly the original puzzle!
    </div>
</ModalPuzzleBase>
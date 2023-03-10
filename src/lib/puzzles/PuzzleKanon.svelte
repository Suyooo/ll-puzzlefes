<script>
    import ModalPuzzleBase from "$lib/ModalPuzzleBase.svelte";
</script>

<ModalPuzzleBase key="kanon" solution="unison" url="/puzzles/31_kanon.png">
    <!--<div slot="hint">
        The words you are looking for are all things that could come out of headphones.<br>
        The word on the last line ends with a "D".
    </div>-->
    <div slot="explain">
        The clues, from top to bottom, are "song", "music" and "sound". By following the numbers, you can find the
        answer, "unison".
    </div>
    <div slot="loc">
        The original puzzle is basically the same: Find three words that have to do with the headphone output, put them
        in the right slots, read the numbered squares.<br><br>
        There is one difference thanks to the language - the smaller squares for the smaller characters aren't possible.
        Thanks to those, there is pretty much only one word that can fit in each line. There wasn't really a way to
        recreate this in English, so here, you just get a free letter.<br>
        I think "music" will be the first thought for many players anyways, and this way, you don't have to experiment
        with whether it's supposed to be in the second or third line. Instead, you get the shared "S" right away, and
        can work from there.
    </div>
</ModalPuzzleBase>
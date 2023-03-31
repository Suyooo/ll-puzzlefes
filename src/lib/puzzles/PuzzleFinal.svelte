<script>
    import ModalPuzzleBase from "$lib/ModalPuzzleBase.svelte";
</script>

<ModalPuzzleBase key="final" name="the Final Puzzle" solution="youdiditcongratsyouvesolvedallthepuzzles"
                 url="/puzzles/final.png">
    <div slot="hint">
        Have you noticed the puzzle list looks a little different...? Start by writing down everything you need, then
        come back here!<br>
        Try to find out which numbers are the easiest to start with, and don't be afraid of guessing short or
        half-finished words - trial-and-error is fine!
    </div>
    <div slot="explain">
        Using a letter from each of the fourty puzzles as marked on the main page, you can form the message shown.<br>
        Starting with groups that have only one or two different letters allows you to more easily fill the first few
        spots, until you get the final answer - "You did it! Congrats, you've solved all the puzzles!"<br><br>
        Thank you for playing!
    </div>
</ModalPuzzleBase>
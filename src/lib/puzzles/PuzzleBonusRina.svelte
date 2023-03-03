<script>
    import ModalPuzzleBase from "$lib/ModalPuzzleBase.svelte";
</script>

<ModalPuzzleBase key="bonus_rina" name="Rina's Bonus Puzzle" solution="telepathy" url="/puzzles/209_rina_bonus.png">
    <div slot="hint">
        What could you fill the boxes above the boards with that relates to what is drawn on them?<br>
        The table at the bottom not only lets you know how symbols can change, but indirectly, it also tells you what
        symbols you can use in the first place.
    </div>
    <div slot="explain">
        The boards represent the emoticons ":D", "XD", ";)" and ":'(". Using the table below the boards, the symbols
        used result in the answer, "telepathy".
    </div>
    <div slot="loc">
        The goal of this one was to make a new puzzle while reusing the materials given - in this case, the Rina-chan
        boards. The actual localized puzzle uses the names of the emotions shown, so I tried emoticons as a different
        representation here.<br><br>
        Of course, a mess of symbols can't be the answer, so I have implemented a emoticon-based cipher encryption on
        the secret word. Which has the additional advantage of restricting the emoticons you can build - so people don't
        try ";_;" or ":c" or ":|" for the sad emoticon, I just left them out of the cipher table. I just had to change
        the anger board into something else to make it work with what letters were in the answer.
    </div>
</ModalPuzzleBase>
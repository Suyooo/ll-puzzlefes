<script>
    import ModalPuzzleBase from "$lib/ModalPuzzleBase.svelte";
</script>

<ModalPuzzleBase key="nico" solution="sister" url="/puzzles/09_nico.png">
    <!--<div slot="hint">
        The word you are looking for in the first row is not a verb, but a noun.<br>
        Also, remember the hint at the bottom - you are looking for a type of food.
    </div>-->
    <div slot="explain">
        Count the items, then take letters from the start and end of the description as shown.<br><br>
        In the example, there are "nine tacos". Taking the first two letters and last two letters before the "S" as
        shown results in "Nico". In the second row, "six hamsters" are shown. The first two letters and last four
        letters before the "S" form the answer, "sister".
    </div>
    <div slot="loc">
        Similarly to the original puzzle, this one is set up using an example to find the pattern, and then a second
        line to apply that pattern to. English doesn't have counter words, but using the actual name of the item works
        just fine.<br><br>The main difference is that because English numbers make real bad words, I had to add a step
        where you have to cut out some letters. That's also why the layout is different from the original puzzle - I
        wanted to make it clear that the two lines are independent from each other, the answer does not contain anything
        from the "Nico" example.
    </div>
</ModalPuzzleBase>
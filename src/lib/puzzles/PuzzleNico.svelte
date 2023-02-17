<script>
    import ModalPuzzleBase from "$lib/ModalPuzzleBase.svelte";
</script>

<ModalPuzzleBase key="nico" solution="sister" url="/puzzles/09_nico.png">
    <div slot="hint">
        The amount of letters in the second row is unknown - so use the example in the first row, where you know how
        many letters you need to fill in, to work out the pattern (the "me" refers to Nico). Then, you should be able to
        easily apply that pattern in the second row.
    </div>
    <div slot="explain">
        Count the items, then take letters from the start and end of the description as shown.<br><br>
        In the example, there are "nine tacos". Taking the first two letters and last two letters before the "S" as
        shown results in "Nico". In the second row, "six hamsters" are shown. The first two letters and last four
        letters before the "S" form the answer, "sister".
    </div>
    <div slot="loc">
        Original puzzle approach: Japanese uses different counter words depending on what you count. Two apples is
        counted with "ni-ko", "ko" being the correct counter for apples. Alpacas are animals, so you use the counter
        "tou" for them - "kyuu-tou", which results in the answer "cute".<br><br>
        Similarly to the original puzzle, this one is set up using an example to find the pattern, and then a second
        line to apply that pattern to. English doesn't have counter words, but using the actual name of the item works
        just fine.<br><br>The main difference is that because English numbers make real bad words, I had to add a step
        where you have to cut out some letters. That's also why the layout is different from the original puzzle - I
        wanted to make it clear that the two lines are independent from each other, the answer does not contain anything
        from the "Nico" example.
    </div>
</ModalPuzzleBase>
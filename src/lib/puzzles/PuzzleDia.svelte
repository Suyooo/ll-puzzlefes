<script>
    import ModalPuzzleBase from "$lib/ModalPuzzleBase.svelte";
</script>

<ModalPuzzleBase key="dia" solution="fan" url="/puzzles/14_dia.png">
    <div slot="hint">
        What is that shape behind the numbers on the left side?<br>
        Try finding out how you can represent the character on the right side of each arrow in the shape on the left
        side.
    </div>
    <div slot="explain">
        The numbers on the left side are mapped to a seven-segment display in reading order - top to bottom, left to
        right. Applying this mapping to the last line results in letters spelling out the answer "fan".
        <div class="w-full flex items-center justify-center">
            <img alt="Stroke diagram" src="/puzzles/14_dia_explainer.png"/>
        </div>
    </div>
    <div slot="loc">
        In the original, the kanji for day/sun is used (日). Kanji have a defined stroke order, so the numbers for each
        character represent which strokes should be drawn and which ones should be skipped, resulting in katakana
        characters that spell out the answers.<br><br>
        In English, there's no such thing as a defined stroke order. For a hot minute, I considered just completely
        scrapping the original for that reason, as there is no way to do something like this in English. However, if
        I could use some shape, there could be some logical order applied to it's parts. Hence, the seven-segment
        display appears once more (it also kinda looks close to 日 as a bonus).<br><br>
        To make it easier to reason out the number to seven-segment mapping, "S" and "2" were chosen as the examples as
        they are mirrors of each other, resulting in three lines they have in common and the others flipping in pairs.
        Once you have the seven-segment representation of the two characters, the common lines and changing lines are
        hopefully obvious enough.<br>
        I wish I had another option to do the example with less numbers, so it's not as overwhelming from the first
        line, but I thought that would be be far more important to give a chance to nail down the stroke order easily
        once you notice the seven-segment shape, instead of leaving things vague.<br><br>
        The fact that the Dia's puzzle has the answer "fan" and shares a mechanic with Eli's puzzle was completely
        unintended - I had the puzzle idea and answer before I realized. It's a lucky coincidence, but a very welcome
        accidental reference :)
    </div>
</ModalPuzzleBase>
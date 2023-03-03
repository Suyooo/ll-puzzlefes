<script>
    import ModalPuzzleBase from "$lib/ModalPuzzleBase.svelte";
</script>

<ModalPuzzleBase key="yoshiko" solution="circle" url="/puzzles/16_yoshiko.png">
    <!--<div slot="hint">
        There is one obvious way to put 13 into that grid. But how can that other axis be filled?<br>
        Think about what else 13 can represent or stand for.
    </div>-->
    <div slot="explain">
        On the horizontal, "thirteen" fits. On the vertical, the figurative meaning of 13 has to be used - "unlucky".
        <br>
        Matching the symbols on the grid to the ones at the bottom reveals the answer, "circle".
    </div>
    <div slot="loc">
        Original puzzle approach: An image of an angel was presented, and a grid had to be filled with two words related
        to it - which was the Japanese word for angel ("tenshi") and the representation of the English word in the
        Japanese syllabary ("enjeru"), crossing on the "n".<br><br>
        This has been the hardest puzzle to find word replacements for so far. The search started off by looking for
        words that could have the same layout as the original puzzle, where one crosses the other in the centre. But
        that was already extremely complicated: the words had to be synonyms or combinations that can be described by a
        single image, one of had to have an odd number of letters to cleanly cross the other and that letter in the
        middle had to be one shared with the other word. And anything that even remotely worked (the candidates I found
        were "crystal"/"orb" and "eclipse"/"dim"), I couldn't find a fitting answer word for.<br>
        So that had me stuck, until I just went "hot take: cross shape is bad????" and discarded the word layout
        constraints. Shortly after, I also came up with the idea for the clues used in this version of the puzzle:
        something that has both a literal and figurative meaning, instead of straight up synonyms.
        <br><br>
        The next problem was a little weird though: "thirteen" is such a good word. It's way too good. Since it's the
        obvious part of the clues in this puzzle, I had to avoid using an answer that would already reveal itself with
        just that word, so people wouldn't be able to just skip the entire point of the puzzle with the secondary
        meaning of "thirteen". But the letters in "thirteen" are just too good! I had to throw away so many great
        potential answers... "hell", "nether", "night", "twilight", "rebirth", "little", "enchant", "rune", "internet",
        "thriller", "heroine", "throne", "eccentric"...<br>
        For a while, I wanted to use "chili" since Yohane likes spicy food, but turns out that she doesn't ever use or
        eat chili, in any media. So I skipped that one in favor of something that is less of a reach, since you
        explicitly see her magic circles multiple times in the anime alone.
    </div>
</ModalPuzzleBase>
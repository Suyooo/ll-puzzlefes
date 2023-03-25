<script>
    import ModalPuzzleBase from "$lib/ModalPuzzleBase.svelte";
</script>

<ModalPuzzleBase key="ren" solution="game" url="/puzzles/35_ren.png">
    <div slot="hint">
        All of these clues are inside the school. If you see these clues inside a school, when would that usually be?
        <br>
        Or rather, what would you be having when these clues become relevant?
    </div>
    <div slot="explain">
        Each line represents a school subject - "geography", "math", "music" and "PE".<br>
        Following the marked column allows you to read the answer, "game".
    </div>
    <div slot="loc">
        Original puzzle approach: Each word in each line represents the reading of a kanji. Take an alternative reading
        of that kanji, and find a school subject using that alternative reading. The second line, for example: "かず"
        ("kazu") &rarr; "数" (count - "kazu" or "suu") &rarr; "数学" (math - "suugaku").<br>
        The character count of the reading of the subject matches the amount of squares, so fill the kana in, then read
        the middle column for the answer.<br><br>
        Once again, it's a kanji reading puzzle that has no possible straight localization. I tried to make it resemble
        the original approach though - just like the previous kanji reading puzzles that were about puns or shared
        characters, this one is about finding a word with a kanji inside it, so I wanted to recreate that.<br>
        In this version, instead of looking for a school subject with a certain letter in it's name, I made it about the
        physical place - looking for a school subject where you would have that item inside the classroom. While not the
        intended way, it's also a valid way to solve the original (where in the school would you "count"? In "math"
        class) so I made the localized puzzle use that approach.
    </div>
</ModalPuzzleBase>
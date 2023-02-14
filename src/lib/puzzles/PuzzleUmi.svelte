<script>
    import ModalPuzzleBase from "$lib/ModalPuzzleBase.svelte";
</script>

<ModalPuzzleBase key="umi" solution="training" url="/puzzles/04_umi.png">
    <div slot="hint">
        It seems like each row has the same amount of arrows in the targets as there are letters in the word.
    </div>
    <div slot="explain">
        The missing letter in the boxes is N, forming "ring" and "tanning".<br><br>
        The targets represent letters, and the arrows show how often they appear in the word. From the line for "rain",
        you can tell the 2nd, 4th, 5th and 8th targets represent R, I, N and G respectively. Similarly, the line for
        "tanning" reveals the 1st, 3rd, 6th and 7th targets represent T, A, I and N.<br><br>
        With this information, the last line can be solved: one arrow in each target means each letter appears once,
        forming the answer "training".
    </div>
    <div slot="loc">
        The targets were hinted at representing the word in the original puzzle by the smaller target, which stands for
        the small "ゅ" in "きゅうどう". To recreate that hint, the localized puzzle has the double-hit target, only
        appearing for the word that has the same character twice in a row.<br>
        What wasn't quite as easy to translate into another language was the missing block, since you don't something in
        English like using a radical as both the whole and half of a kanji. Instead, I just hid the most common letter -
        after all, this bit is not meant as much more as a quick distraction to start the puzzle with.<br><br>
        In the first attempt at localizing this puzzle, the words "arch" and "cherry" were chosen, to form the answer
        "archery" like the original puzzle. However, if you read the words right after each other, "arch-cherry" will
        immediately reveal "archery" as the answer, without needing to figure out the targets and arrows at all.<br>
        The words in this final version could also immediately hint at the answer, just from seeing the available
        letters, which is impossible to cover up since we English doesn't have the luxury of something like kanji, as
        mentioned above - but it's still a little more obscured than in the first version.
    </div>
</ModalPuzzleBase>
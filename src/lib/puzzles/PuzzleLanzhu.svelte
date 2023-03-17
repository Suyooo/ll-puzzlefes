<script>
    import ModalPuzzleBase from "$lib/ModalPuzzleBase.svelte";
</script>

<ModalPuzzleBase key="lanzhu" solution="meat" url="/puzzles/212_lanzhu.png">
    <div slot="hint">
        Something in this puzzle is not what it seems to be.<br>
        Try taking a look at the words for the icons you know for sure, and find what they have in common.
    </div>
    <div slot="explain">
        The first three rows seem like calculations, but actually, the character that looks like the multiplication sign
        is just an "X". All of the clue words contain an "X", and can be split there. For example, in the first row,
        "mexico" is split into "me" for A and "ico" for B. Similarly, "axe" and "next" can be split.<br>
        Combining only the groups mentioned in the last line reveals the answer, "meat".
    </div>
    <div slot="loc">
        In the original puzzle, the prolonged sound character ("ー") is used, which looks like a minus sign. All of the
        clues can be split on that character, and the groups in the answer are also split by the prolonged sound mark.
        <br><br>
        The first decision about which sign to use for the fake out was basically already made for me: "X" as the
        multiplication sign was pretty much the only choice. The closest thing to a plus would be a lower-case "t" which
        would look bad since the bottom stroke is longer, I can't do a minus unless I write words vertically and nothing
        quite looks like a division.<br>
        I guess one more possibility would have been using a very small "O" as a multiplication dot, but that would
        have to be so small that you would have trouble even identifying it as a character if not zoomed in. So, "X" had
        to be chosen, which made things really complicated because "X" is a bad letter to play with in English.<br><br>
        Something I dropped right away was using the "operator" in the answer, as the original puzzle does. The only
        word in English (not counting proper nouns) with two "X" in it is "textboxes". That would just not work for
        Lanzhu's puzzle.<br>
        I basically had no choice but to come up with a possible answer, and then test the entire wordlist for words
        that (a) had a properly placed "X" to split on, (b) formed the answer I thought of when combined and (c) could
        be represented with emoji. Even after I decided I'd drop the goal of having a shared theme across the clues like
        the original puzzle, it took two days :)
    </div>
</ModalPuzzleBase>
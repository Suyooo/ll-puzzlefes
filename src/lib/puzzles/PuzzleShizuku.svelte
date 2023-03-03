<script>
    import ModalPuzzleBase from "$lib/ModalPuzzleBase.svelte";
</script>

<ModalPuzzleBase key="shizuku" solution="stage" url="/puzzles/203_shizuku.png">
    <!--<div slot="hint">
        For the first clue, you probably already have some idea of what word could work in the sentence. Try looking up
        synonyms, maybe you can find a word that fits in the slots!<br>
        For the second clue, think about that time frame that is mentioned - what might be different in two years?
    </div>-->
    <div slot="explain">
        The first row can be filled with "passionate", the second row can be filled with "graduate".<br>
        Following the numbered slots, you can find the answer, "stage".
    </div>
    <div slot="loc">
        In both the original and this version, the gaps in two sentences must be filled, too. However, in the original,
        the two gaps were filled with different readings of the same kanji compound ("上手" can be read as "jouzu" or
        "kamite").<br>
        To recreate this in English, I decided to make the two words share an ending instead. However, to keep a little
        bit of the idea of different readings, I made sure the endings are pronounced differently in both words, to make
        it a little confusing in that way :)<br><br>
        I'd say to think the solution approach is still very similar to the original puzzle - even if it looks a lot
        different. Once you solve one of the clues, the answer is extremely obvious because you get four of five
        characters - while in the original, you already get the kanji and immediately can solve the other clue with the
        other reading (if you haven't already guess the answer - the original makes the answer fairly obvious right from
        the start by revealing one of the letters already).<br>
        I thought about changing the answer to "troupe" - which would be less easy to guess from just one or even no
        clues - but I thought if the original was kind of obvious, this one should be, too.
    </div>
</ModalPuzzleBase>
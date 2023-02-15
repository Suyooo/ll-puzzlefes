<script>
    import ModalPuzzleBase from "$lib/ModalPuzzleBase.svelte";
</script>

<ModalPuzzleBase key="nozomi" solution="muse" url="/puzzles/07_nozomi.png">
    <div slot="hint">
        The answer is four letters long.<br>
        Each card stands for one letter. Imagine drawing the letter onto the cards. How would they look when laid down
        as shown in the reading?
    </div>
    <div slot="explain">
        Each candle or card represents one letter from the words "candles" or "cards" respectively. You can use that
        mapping to find the meaning of the reading. The circle card and the candle can simply be replaced with "S" and
        "E".<br>
        The star card is placed sideways. Rotating "C" sideways results in a "U". Finally, there are two triangle cards
        stacked on top of each other, slightly to the side. They form the last letter together: drawing two "A"s the
        same way the cards are placed, like
        <span class="whitespace-nowrap">"<span class="inline-block w-2 overflow-hidden align-bottom -mr-0.5">A</span>A"</span>,
        will reveal the final letter, "M". Together, the letters form the answer "muse".
    </div>
    <div slot="loc">
        Just like in the original, characters must be formed by combining others. Of course, it's far harder with the
        latin alphabet than with radicals. So yeah, just between us two: I think the "AA" as "M" thing kinda stinks. I'm
        not really happy with it, it can be too much of a stretch depending on how exactly people write the letters out
        or how they overlap them.<br><br>
        However, we do have an advantage thanks to English: Our answer can't have just two characters like in the
        original, there's no words that fit there. By going up to four letters, it is more obvious that the "reading" is
        an encoded word, but we can also mix up the puzzle with the other letters. The "S", "U" and "M" are the same
        thing but in increasing difficulty: just the straight card to letter, then rotating the letter, then combining
        letters. So then, if the "AA" doesn't work out to an "M", the answer can be guessed from just "_use" - and in
        that case, you still solved a puzzle involving the layout of cards having to be applied to letters thanks to the
        "U" card.
    </div>
</ModalPuzzleBase>
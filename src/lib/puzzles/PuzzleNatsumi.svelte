<script>
    import ModalPuzzleBase from "$lib/ModalPuzzleBase.svelte";
</script>

<ModalPuzzleBase key="natsumi" solution="money" url="/puzzles/39_natsumi.png">
    <div slot="hint">
        Each of the clues has only two bars in the signal meter lit up. What could those mean?
    </div>
    <div slot="explain">
        The clues are "me" (Natsumi), "ny" (New York) and "on". The signal meter has five bars, and assigning each
        letter of the clues to the bars lit up in the same line, you can form the answer, "money".
    </div>
    <div slot="loc">
        The original puzzle worked similarly, each signal bar representing one character. Each of the clues covers two
        consecutive characters of the four total.<br>
        This is one of the puzzles that really hurts from the difference between the Japanese syllabary and the
        alphabet. Each of the clues in the original covers the first character of the next clue, so they just chain
        together nicely. I wrote a script again, and got zero unusable results.<br><br>
        The obvious reason is that my choices are limited due to the golden rule of having the answer fit the character
        - there were some words which would have worked, but are completely unrelated. But I think another part is that
        in English, words with two or three letters are just <i>boring</i>.<br>
        It's mostly prepositions, pronouns, articles and abbreviations. It's way harder to find a combination that can
        make interesting clues like the original puzzle. That means I had to drop some limitations, so both of the clue
        requirements went right out the window - both the fact that each clue overlaps another, and that they only cover
        consecutive signal meter bars.<br>
        I'm not a linguist, but I feel like this could be caused by the language relying on vowels so much, while that's
        not a problem in Japanese? It's interesting how a simple word puzzle like this works perfectly fine in one
        language but completely falls apart in another due to a small language feature like that.<br><br>
        So, with those limitations removed, it was just down to finding an answer word with four or five letters that
        contains at least three other words that could make alright clues. And unsurprisingly, it was still difficult!
        In the end, "money" worked the best out of everything, but I still had to use a clue that is actually an
        abbreviation.<br>
        But I think the clues work fine-ish: once you realize all the clues must be two letters, the second and third
        clue just become research questions. And then, with just two letters of the answer unknown, it is still possible
        to figure out the answer even though there is no overlap, by either figuring out the trick to fit "Natsumi" into
        two letters, or by simply filling in the gaps in the answer. It's just Wordle at that point!
    </div>
</ModalPuzzleBase>
<script>
    import ModalPuzzleBase from "$lib/ModalPuzzleBase.svelte";
</script>

<ModalPuzzleBase key="hanayo" solution="rice" url="/puzzles/08_hanayo.png">
    <div slot="hint">
        The spade symbol (♤) stands for a "T".<br>
        Some of the symbols needed for the answer might look like they do not show up in either word. Think about what
        symbols you have available and how you could find those missing symbols among them.
    </div>
    <div slot="explain">
        The first word is "barista", the second word is "airport".<br>
        You can map the letters of the words to the symbols on the answer. The last two symbols are a half circle and a
        half triangle, meaning you also only take that half of the letter. The left half of "O" is "C", and the left
        half of "B" is "E", resulting in the answer "rice".
    </div>
    <div slot="loc">
        Original puzzle approach: The questions were "a word for bad luck" and "there's 23 of these in Tokyo". Applying
        the kanji of the answers to those questions to the symbols, observing the rotation of the heart symbol for the
        radical surrounding three sides, reveals the katakana コ and メ, which form the answer together.<br><br>
        I tried to make sure as many details as possible from the original puzzle were also in this one:<br>
        <i>Character transformation</i> - English can't form letters out of other letters very well, so in this puzzle,
        we cut letters in half.<br>
        <i>Only one word required</i> - if you can answer either question, you don't get all the characters like in the
        original, but you do get three out of four letters for a fairly obvious answer.<br>
        <i>Dictionary question</i> - for the first question, you either already know the kanji/word, or you can easily
        find it in a dictionary.<br>
        <i>Tokyo question</i> - some probably immediately know, but otherwise a bit of research still works. I just had
        to phrase the question with a lot more detail than just the number of airports - because I was afraid I'd get
        "ackshually"'d with "Narita is technically not in the Tokyo prefecture"/"there's lots of third class airports in
        Tokyo too" lol<br>
        <i>Questions can be used to cross-check</i> - obviously each word fills in some symbols that also appear in the
        other word so you can tell whether you have both correct. There's one thing I explicitly tried to watch out for:
        some people might try to answer the second question with a plural noun because it fits with the question better,
        so I made sure the first word contains an "S" so you can tell the second word does not end with one.
    </div>
</ModalPuzzleBase>
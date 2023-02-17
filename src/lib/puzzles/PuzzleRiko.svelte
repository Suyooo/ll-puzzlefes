<script>
    import ModalPuzzleBase from "$lib/ModalPuzzleBase.svelte";
</script>

<ModalPuzzleBase key="riko" solution="piano" url="/puzzles/12_riko.png">
    <div slot="hint">
        This puzzle is not related to music notes. Look for what the notes on each line of the staff have in common.<br>
        There are seven notes on the staff. Try finding something you can map those seven notes to.
    </div>
    <div slot="explain">
        The seven notes represent seven syllables of "The answer is ? ? ?": Each line represents one vowel (in
        alphabetical order from the top), and the letters in the flag are the consonant letters in this syllable.<br>
        <br>
        The fifth note is on the line for "I" and has a "P", resulting in "PI". The sixth note is on the line for "A"
        and has no consonants, resulting in "A". The final note is on the line for "O" and has an "N", resulting in "NO"
        as the final syllable. The syllables read from notes form the sentence "The answer is piano".
    </div>
    <div slot="loc">
        This one is basically the same as the original. Each line stands for a vowel, and must be combined with the
        consonant in the flag to form the sentence "the answer is piano". There are just a few small differences - one
        of them is the fact that in English, we need multiple consonants per note, so I had to make the flags scale
        accordingly.<br>To avoid the "swer" being too obvious, the consonants are alphabetically ordered, which also
        hints at the vowels along the lines being alphabetically ordered, too. (Which is another small difference: in
        Japan, vowels go A-I-U-E-O, but here, they go A-E-I-O-U.)<br><br>
        The last difference is that the original puzzle can easily hint at the relation between the syllables of the
        hint and the notes thanks to the Japanese syllabary. The word for answer, "kotae", is even written in hiragana
        instead of using a kanji as usual, and the kana are spaced so they align with each note. That would look really
        weird in English, since you would have a big mid-word space.<br>Luckily, we already have spaces between words in
        this language, so all that was done to resemble that hint was to add that little mysterious dot in "answer". It
        also helps players in case they erroneously assume the syllables are "ans-wer" instead of "an-swer" (like I did
        at first :^) ).
    </div>
</ModalPuzzleBase>
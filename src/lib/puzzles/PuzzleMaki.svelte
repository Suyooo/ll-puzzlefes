<script>
    import ModalPuzzleBase from "$lib/ModalPuzzleBase.svelte";
</script>

<ModalPuzzleBase key="maki" solution="bibi" url="/puzzles/06_maki.png">
    <div slot="explain">
        Using the solfège scale ("do-re-mi-fa-so-la-ti"), look up the piano keys for each note in the four words. Each
        white key is one of the main tones, and a # indicates you must raise the note by half a step (the next black key
        to the right).<br><br>
        Sum up all of the numbers on the keys you found for each word to get the numbers 2, 9, 2, 9. Looking up the 2nd
        and 9th letter in the alphabet maps these numbers to the answer "BiBi".
    </div>
    <div slot="loc">
        In the original, the lookup step was to take the radical names recieved from mapping the notes using the solfège
        scale, and finding the katakana that looks like that radical. Technically, I could have done something similar
        by making the note lookup result in words, and having you pick the letter that looks like that word for the
        answer ("tent" &rarr; "A" looks like a tent?).<br><br>
        However, that would have meant that for one, I would have to heavily hint at it, since it's not an intuitive
        solution in English (if you are tasked with mapping the word "tent" to one letter, you would most likely just
        take the first or last letter), and also, it's open to subjectivity ("M" could maybe look like a <i>circus</i>
        tent?).<br>
        So that's why I decided to go with something less likely to be misinterpreted, and made the lookup step looking
        up a position in the alphabet. It's still kinda similar to lookup up a radical, isn't it?<br><br>
        Another important bit was the answer choice. I could have easily picked something more directly related to Maki,
        like "tomato", "composer", or "tsundere"... However, I decided against having words this long. Once you have
        figured out the trick of summing up the numbers, having a lot of characters just means you have to do extra work
        even though you technically already solved the puzzle. Four characters is enough to see that you have worked out
        and can apply the mapping, anything more is just the puzzle equivalent of a filler episode.
    </div>
</ModalPuzzleBase>
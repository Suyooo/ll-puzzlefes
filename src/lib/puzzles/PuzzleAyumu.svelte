<script>
    import ModalPuzzleBase from "$lib/ModalPuzzleBase.svelte";
</script>

<ModalPuzzleBase key="ayumu" solution="bun" url="/puzzles/201_ayumu.png">
    <div slot="hint">
        What do the amount of slices, including the ones already eaten, and the thing in the image have in common? Make
        sure you start from the top of each circle, going clockwise.<br>
        In case you have trouble recognizing the thing on the right side, it is a kind of spit cake - a group of cakes
        mainly from Europe - that was brought over to Japan and got very popular there.
    </div>
    <div slot="explain">
        The left image shows a cherry pie. Assigning the nine letters to the nine slices, from the top in clockwise
        order so the "p" lines up with the fork, and then combining the letters in the slices that have been taken away,
        results in "eye".<br>
        On the right, the image shows a baumkuchen. Once the ten letters are assigned and combined as above, the answer
        reveals itself as "bun".
    </div>
    <div slot="loc">
        The original puzzle worked similarly, except the example was the baumkuchen and the answer image was an apple
        pie. Another difference is that the forks only hint at the correct words by showing the diacritics for the
        character assigned to a slice in the original. Such a hint wouldn't be possible English, so instead, the amount
        of forks in the answer image has been reduced to one, but it instead reveals the entire letter.<br><br>
        The cherry is meant as a pie flavour indicator for people with color vision deficiencies. I guess it makes it a
        little more obvious that the flavour of pie is relevant to solve the puzzle, which I usually try to avoid - I
        want the added details to just make the puzzle possible for CVD people, not make it easier - but I think the
        amount of letters required already is a pretty big hint that a word longer than "pie" is needed.
    </div>
</ModalPuzzleBase>
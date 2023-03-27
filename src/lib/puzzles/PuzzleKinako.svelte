<script>
    import ModalPuzzleBase from "$lib/ModalPuzzleBase.svelte";
</script>

<ModalPuzzleBase key="kinako" solution="island" url="/puzzles/36_kinako.png">
    <!--<div slot="hint">
        The position of the circle on the animal is important. Where would you say the front and the back of an animal
        are?<br>
        Besides the front and the back of the animal, you can just consider the rest of animal as one big part.
    </div>-->
    <div slot="explain">
        If the head of an animal is circled, take the first letter from it's name. If the tail is circled, take the last
        letter. If the torso is circled, take the rest of the letters.<br>
        The images in the first line show a cat, a wolf and a bird. Taking letters from these words as described above
        forms the clue, "cold". The bottom line shows a fish, a lion and a panda. If you pick the correct letters again,
        you will get the answer, "island".
    </div>
    <div slot="loc">
        The original puzzle worked similarly: depending on whether the head, torso or tail of the animal is circled,
        take the first, middle or last character of their name to form words. The Japanese puzzle has one very
        convenient advantage though: every animal you need the middle letter from has exactly three characters.<br><br>
        This is something that already came up during Emma's puzzle, where I also was unable to limit the clues to
        three-letter words, so I could have any chance at localizing it. As explained in the localization notes for that
        one, I just dropped the concept of the "word middle" since it would be confusing. But here, I was fine with it
        for a few reasons.<br>
        For one, you have an extensive clue demonstrating the behaviour of the "middle". I intentionally chose "wolf"
        as the example here, since it's a four-letter word - there is no clear middle, and instead, that already hints
        that when the middle is asked for, it might not be a single letter.<br>
        Second, I made sure to only use the middle part of words with four or more letters. That was one problem I had
        considered for Emma - the meaning of "middle" switching between a single and multiple letters - and that was one
        way to avoid it, by simply making the middle always be multiple letters.<br><br>
        The final problem to solve was the images. The animals in the original puzzle seem to have been drawn just for
        this instead of being stock images. I could have drawn some new animals myself, but I thought that players being
        able to recognize the animals would be kind of important for the puzzle to work.<br>
        Instead, I spent almost twice as long looking for animal images than I needed for localizing the answer. It was
        pretty hard finding a set of images that have similar styles, are well recognizable even if simplified, is
        licensed in a way that allows me to use them here, and has this specific set of animals I needed...<br>
        <br>
        <a href="https://www.flaticon.com/authors/freepik">Animal icons by Freepik</a><br>
    </div>
</ModalPuzzleBase>
<script>
    import ModalPuzzleBase from "$lib/ModalPuzzleBase.svelte";
</script>

<ModalPuzzleBase key="ruby" solution="yarn" url="/puzzles/19_ruby.png">
    <!--<div slot="hint">
        What is that shape, and what to the icons of people on it mean? What does it repesent?<br>
        Once you figure out what the icons are, you should be able to fill in the clues by thinking about how the two
        icons are related.
    </div>-->
    <div slot="explain">
        The figure is a family tree. On the left, you have "Dia", on the right, you have "Ruby". They are "sisters".<br>
        Putting these three words in the appropriate slots and taking the letters in the numbered spots reveals the
        answer, "yarn".
    </div>
    <div slot="loc">
        In the original puzzle, the box was still labeled as sisters ("shimai"), but the labels below the icons weren't
        Dia and Ruby - they just used the generic terms for big and little sister, "ane" and "imouto".<br>
        There's no way that would work for a localization. First, nobody calls their siblings "big sister" or "little
        sister" in English, they mostly call them by their name. Second, if the three clues all shared "sister", that
        would be very extremely silly.<br><br>
        That's why I decided to make the generic family tree into a Kurosawa family tree. One problem with that though
        is that I'm pretty locked into the clues, which means for the answer, I have to work with what I have. All that
        you can do in such a case is find all the words that consist out of the letters in the clues and pick the most
        fitting one.<br>
        However, there just... wasn't anything. "Dress" was the most fitting I could find, since Ruby is Aqours'
        wardrobe supervisor, but "outfit" or "costume" would have been the word you'd pick over dress. So, I just did a
        little cheeky cheating and added all words that have at most one letter that is not in the clues. "Yarn" ended
        up being a fit as it refers to Ruby's hobbies, and each of the clues is represented in it's letters. Phew.
    </div>
</ModalPuzzleBase>
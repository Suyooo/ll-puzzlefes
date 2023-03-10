<script>
    import ModalPuzzleBase from "$lib/ModalPuzzleBase.svelte";
</script>

<ModalPuzzleBase key="emma" solution="alps" url="/puzzles/208_emma.png">
    <!--<div slot="hint">
        First clue: Yoshiko claims hers is "dark".<br>
        Second clue: The shape of the icon is a hint.<br>
        Third clue: You should not rest on them.<br>
        Fourth clue: It's similar to a carrot.
    </div>-->
    <div slot="explain">
        The clues are "aura", "swiss", "laurel" and "parsnip". Placing the starting and ending letters in the shown
        order forms the answer, "alps".
    </div>
    <div slot="loc">
        The original puzzle worked similarly - all clues were words that started and ended with the same character. One
        difference is that all the clues were also three characters long and a seperate icon was used for the middle
        character, so it could be used as part of the answer.<br>
        That was one bit I couldn't replicate unless I use three letter abbreviations, and I think it would be hard to
        make all of those relate to Emma in some way. Dropping the three-letter requirement means I could find some
        fitting words instead (especially proud that evergreen one).<br><br>
        For a bit, I considered replicating the middle icon from the original by making everything but the first/last
        letter of each clue it's own icon, which would have allowed me to use "calc" as a clue and "al" in the answer,
        which would keep the puzzle at three clues just like the original.<br>
        However, I decided to drop that since for one, calc is hard to hint at, and also, it would be somewhat confusing
        to have icons switch between representing a single letter and multiple letters. So this is why this puzzle ended
        up with more clues - but unlike other puzzles like Maki's, I'm fine with extending here.<br>
        I chose shorter answers for puzzles which are about figuring out a rule and applying it, because increasing the
        amount of times you have to apply the rule doesn't add anything to the puzzle. Here though, every clue is it's
        own mini-riddle, which means adding an additional clue poses a new question instead of just being filler. I
        think it's fair then, especially since having four clues makes the main puzzle easier to understand!
    </div>
</ModalPuzzleBase>
<script>
    import ModalPuzzleBase from "$lib/ModalPuzzleBase.svelte";
</script>

<ModalPuzzleBase key="honoka" solution="bakery" url="/puzzles/01_honoka.png">
    <div slot="explain">
        You cannot subtract a number from a blackberry. So, instead, the digits represent the positions of the
        characters that must be "subtracted" from the words.<br><br>
        Removing the 2nd, 4th, 6th and 8th characters from "blackberry" leaves "bakery".
    </div>
    <div slot="loc">
        The original puzzle was about subtracting from a word, too: 10050 is read as <i>ichi man go juu</i>, and the
        Japanese word for strawberry is <i>ichigo</i>. Removing <i>ichi</i> and <i>go</i> from <i>ichi man go juu</i>
        leaves <i>manjuu</i>, which is the answer.<br><br>
        Doing something like this is not as easy in English though, as numbers barely make useable words. So instead,
        the berry is the minuend, and instead of subtracting words, the subtrahend must be interpreted as positions.
        That way, the puzzle is still about misleading math being applied to words instead of interpreting operands
        as numbers.
    </div>
</ModalPuzzleBase>
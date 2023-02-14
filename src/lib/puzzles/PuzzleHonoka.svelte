<script>
    import ModalPuzzleBase from "$lib/ModalPuzzleBase.svelte";
</script>

<ModalPuzzleBase key="honoka" solution="bakery" url="/puzzles/01_honoka.png">
    <div slot="hint">
        Obviously, you cannot subtract a number from a blackberry.<br>
        A minus means taking something away, but if it's not a number, what else can be taken away?
    </div>
    <div slot="explain">
        You cannot subtract a number from a blackberry. So, instead, the digits represent the positions of the
        characters that must be "subtracted" from the word.<br><br>
        Removing the 2nd, 4th, 6th and 8th characters from "blackberry" leaves "bakery".
    </div>
    <div slot="loc">
        The original puzzle was about taking something away from a word, too. However, something like the original is
        not as easy in English though, as numbers barely make useable words. So instead, I just took the idea of "making
        it look like a math puzzle but you actually have to do something else".<br><br>
        The berry is the minuend here, and instead of subtracting the words themselves, the subtrahend must be
        interpreted as positions. That way, the puzzle is still about correctly interpreting the operands as something
        other than numbers.
    </div>
</ModalPuzzleBase>
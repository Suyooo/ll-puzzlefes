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
        Original puzzle approach: 10050 is read as "ichi-man-go-juu". A strawberry is "ichigo". Interpreting the minus
        as "taking away", and removing "ichi" and "go" from the reading of the number, leaves "manjuu" as the answer.
        <br><br>
        Like the original puzzle, the localization should be about taking something away from a word, too. However,
        something like the original is not as easy in English though, as numbers barely make useable words. So instead,
        I went with the idea of "making it look like a math puzzle but you actually have to do something else".<br><br>
        The berry is the minuend here (I'm honestly surprised I managed to squeeze another type of berry in this
        localization), and instead of subtracting the words themselves, the subtrahend must be interpreted as positions.
        That way, the puzzle is still about correctly interpreting the operands as something other than numbers.
        <br><br>
        <a href="https://pngset.com/download-free-png-yaahg">
            Blackberry image by Darien Watkins, used under CC BY-NC 4.0.
        </a>
    </div>
</ModalPuzzleBase>
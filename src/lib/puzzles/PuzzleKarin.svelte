<script>
    import ModalPuzzleBase from "$lib/ModalPuzzleBase.svelte";
</script>

<ModalPuzzleBase key="karin" solution="model" url="/puzzles/204_karin.png">
    <div slot="hint">
        Pay close attention to the corners of the shapes. Make sure you rotate and flip the lines correctly.
    </div>
    <div slot="explain">
        Drawing the lines into the answer shapes as shown at the top of the puzzle, it will spell out the answer,
        "model".
        <div class="w-full flex items-center justify-center">
            <img alt="The answer shapes, with the lines drawn in" src="/puzzles/204_karin_explainer.png"/>
        </div>
    </div>
    <div slot="loc">
        Very similar to the original once again - the original puzzle had three squares with lines and them, and the
        answer arranged them so two squares would form one katakana character.<br><br>
        There are only small differences. For one, the original never really rotates characters - it only slightly tilts
        them at most, but up remains up. This localized puzzle requires full rotation though, so the squares were
        changed into unique shapes, running double duty as both an indicator for rotation/flips, and as a helper for
        those with colour vision deficiencies.<br>
        The other one is that I tried to use less shapes - as mentioned, in the original, two squares form one
        character. That would require ten shapes in English, which is kind of a lot to deal with. Instead, I turned it
        around, and made it so one of the shapes can actually be part of two of the characters. Both the left and right
        shape were built with that in mind, so they can share parts with other letters and I can get away with just
        seven shapes, only one more than the original.
    </div>
</ModalPuzzleBase>
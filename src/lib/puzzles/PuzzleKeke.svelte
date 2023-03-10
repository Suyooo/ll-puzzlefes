<script>
    import ModalPuzzleBase from "$lib/ModalPuzzleBase.svelte";
</script>

<ModalPuzzleBase key="keke" solution="passion" url="/puzzles/32_keke.png">
    <!--<div slot="hint">
        Start with the clues you know for sure - you should know which city Keke is from, for example - and work from
        there.<br>
        One of the clues contains a space - but just leave it out when entering it into the grid!
    </div>-->
    <div slot="explain">
        The clues are "napolitan", "shanghai", "schoolidols" and "shibuya". The numbered spaces can then be read to get
        the answer, "passion".
    </div>
    <div slot="loc">
        In the original puzzle, the kanji for Shanghai are requested. By then taking alternative reading for each of the
        two kanji ("ue" and "umi", as indicated by the first characters needing to be equal), the answer "emi" ("smile")
        can be found.<br><br>
        Once again, puzzle about kanji readings are pretty much impossible to localize straight into English. So, I took
        the idea I used in Shizuku's puzzle again, and made it about words sharing characters. The other puzzle was
        about words with common endings, but for this one, I thought the original puzzle already kind of has the layout
        of a crossword - so I just went with a classic crossword for Keke.<br>
        I thought finding clues that would cross each other and are still about Keke would be fairly difficult, but it
        kind of just worked out? One important point was to make sure that each of these clues can be researched easily,
        and it's not something subjective - for example, one clue I thought about was "stamina" with a hint like
        "something I lack", but I feel that it would have been too hard to find the specific word the puzzle is looking
        for.
    </div>
</ModalPuzzleBase>
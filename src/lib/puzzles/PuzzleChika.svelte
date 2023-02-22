<script>
    import ModalPuzzleBase from "$lib/ModalPuzzleBase.svelte";
</script>

<ModalPuzzleBase key="chika" solution="clover" url="/puzzles/11_chika.png">
    <div slot="hint">
        Try writing out the puzzle text without the images. Is there anything catching your eye? Where does the
        replacement used in the example answer on the right come from?<br>
        You can also read out the puzzle text loudly and see whether you notice something. Try pronouncing the second
        word as wrong as possible.
    </div>
    <div slot="explain">
        Replace "mikan" with "coral". Splitting up the word "coral", you can get "c or al".<br>
        Replacing the mikan with "al" gives you the example answer "allover", so using the "c", you can get the real
        answer, "clover".
    </div>
    <div slot="loc">
        I HONESTLY CANNOT BELIEVE HOW PERFECTLY THIS ONE WORKED OUT AAAA<br><br>
        To quickly recap the original puzzle: "mikan" can be read as "mi-ka-n", the "ka" standing for an "or". So the
        puzzle, when read out loud, asks you to "replace the circle symbol with 'mi' or 'n'". At first, I was giving up
        on trying to copy this approach straight over, as I just couldn't find anything that worked with the ideas I had
        for the answer word. Finding a word combination that worked for the altered version of the puzzle still took an
        entire day! If you want to give it a try, <a href="/puzzles/11_chika_v1.png">here's what this puzzle could have
        been</a>.<br><br>
        The next day though, I decided to give it another shot, and just searching for "or" in the
        <a href="https://unicode.org/emoji/charts/full-emoji-list.html">Unicode Consortium's Emoji list</a> turned up
        the coral. Hey, that kind of fits, and works out, and now I just need to find a fitting answer! It was time to
        get the big guns out.<br>
        I downloaded the ENABLE word list, a public domain collection of 150000+ words, and wrote a script to look for
        every possible pair of words where "c" and "al" are the only difference. There's surprisingly many, actually -
        89 pairs! And this one was not even the only one fitting for Chika: another candidate would have been "alanine"
        and "canine" for the Shiitake shoutout. And I almost went for that one, because looking at the
        "clover"/"allover" pair, I thought it looked weird that the top hint would end up being "○LOVER". I originally
        wanted it to be some weird hint that doesn't make sense as a word standalone. But then I thought that maybe, it
        could be another Chika-related bit. What could I put instead of the circle to make that work? Wait, I don't have
        any mikan in the puzzle right now...<br><br>
        And it was perfect.
    </div>
</ModalPuzzleBase>
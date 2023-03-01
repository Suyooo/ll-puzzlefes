<script>
    import ModalPuzzleBase from "$lib/ModalPuzzleBase.svelte";
</script>

<ModalPuzzleBase key="ai" solution="rap" url="/puzzles/205_ai.png">
    <!--<div slot="hint">
        The first two spots are parts of full words. Can you tell what they are supposed to be? If you read those
        <i>words</i> out loud, they might point you to-<i>words</i> the answer!
    </div>-->
    <div slot="explain">
        The slots can be filled with "rep", "rep", "rap" and "wrap". Out of those words, the <i>sole</i> one that fits
        the clue is "rap" - so that one is the <i>sole</i>-ution!
    </div>
    <div slot="loc">
        You want to know more about this puzzle? Alright, <span class="whitespace-nowrap">st-<i>rap</i></span> in!<br>
        <br>
        In the original, the clue asks for a food, and all the underlined spots are puns on "monja" (as in, monjayaki).
        However, both Ai-related foods, monja and nukazuke, are impossible to pun with in English, so the idea of a food
        answer was immediately <span class="whitespace-nowrap">sc-<i>rap</i>-ped</span>.<br><br>
        Another problem was that when I tried to think about words I can make several puns with, I couldn't come up with
        anything that wouldn't go against the golden rule: every answer has to be something about the character. So that
        means a lot of words with easy pun chances, like "sea" (<span class="whitespace-nowrap">"sea-mingly"</span>,
        "sea you later", <span class="whitespace-nowrap">"sea-cret"</span>), were impossible to use as the answer. It
        took me a bit to give up on the approach I had <span class="whitespace-nowrap">p-<i>rap</i>-pared</span> for
        this puzzle localization - it just refused to work out.<br>
        So, I tried approaching it from the other side: I need to start off from the answer, decide on a word that is
        related to Ai that is easy to make puns with first, and then write the text. A few candidates were "sun" (though
        I couldn't find much beyond "son" and "some") and "eye" (I think it would've been funny to go full meta and have
        the answer be a pun on "Ai" itself - but I was afraid people would think "Ai" is the answer then, and marking it
        as wrong would be confusing and a pretty unfair <span class="whitespace-nowrap">t-<i>rap</i></span>).<br><br>
        I decided on "rap" since it's an easy replacement for "rep", and "wrap" is a neat sound-alike. I thought about
        bringing in some idioms too ("have a bad rap", "rap on something"...) but couldn't fit it in. I also removed an
        additional pun that was originally part of the text I wrote - I thought "Sorry to
        <span class="whitespace-nowrap">inter-<i>rap</i>-t</span>" ("interrupt") was too much of a stretch. I just
        kicked it out and replaced it with the "Hey", so people wouldn't have to
        <span class="whitespace-nowrap">g-<i>rap</i>-ple</span> with having to wrongly pronounce a word to solve the
        puzzle.<br><br>
        I was waiting to make bad puns for this puzzle since the beginning, and I will not apologize.
    </div>
</ModalPuzzleBase>
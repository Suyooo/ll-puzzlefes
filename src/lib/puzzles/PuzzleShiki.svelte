<script>
    import ModalPuzzleBase from "$lib/ModalPuzzleBase.svelte";
</script>

<ModalPuzzleBase key="shiki" solution="test" url="/puzzles/38_shiki.png">
    <!--<div slot="hint">
        Have you already found some of the clue words for the images? Is there anything they have in common?<br>
        The amount of question marks in each space tell you how long the answer word should be at that point. You can
        use this information to check how long the clue word for each image should be!
    </div>-->
    <div slot="explain">
        Each of the clue words contains "as", and can be parsed as an instruction in the form of
        <span class="whitespace-nowrap">"X as Y"</span>.<br>
        The first step shows "east". Following the instruction <span class="whitespace-nowrap">"e as t"</span>, the
        answer word "else" becomes "tlst". The second step, <span class="whitespace-nowrap">"l as er"</span>, turns the
        answer into "terst". Finally, the last step instructs <span class="whitespace-nowrap">"er as e"</span>, which
        results in the final answer, "test".
    </div>
    <div slot="loc">
        Same approach as the original puzzle, except the original uses the particle "ga" to seperate the instructions.
        I noticed very early that I couldn't keep the detail of all the clue images being related to Shiki as I needed
        at least two characters as the delimiter instead of one, which restricted words a lot. But even with that
        limitation gone, localizing this puzzle was pretty bad.<br>
        How bad? <a href="/puzzles/38_shiki_graph.png">Look at this graph.</a><br><br>
        Lets back up a bit and break down what is going on in there.<br>
        This graph contains every single possibility to create a puzzle like this, going in reverse from possible answer
        words trying to reach any valid dictionary word using only words that can be used as an operation. Of course, I
        could not use every word. The candidates for the delimiter were "to", "as" and "is", so I searched every word
        that contains one of these words once.<br>
        I then had to manually filter those lists. After all, I had to make images of these things - so any solve paths
        containing words like "isotopic" would be useless to me. I ended up with 26 "to" words, 60 "as" words and 33
        "is" words. And then, I made a script to run this big old search. Nothing fancy, just some backtracking.<br><br>
        You might have already wondered why I didn't use "to" instead of "as" as the operation delimiter, as that would
        make far more sense in English, right? Well, let's get back to that graph. The possible paths for "to" words are
        marked in blue - and if you scroll all the way to the bottom left, you see the lonely single-step path which is
        the only one possible with those words.<br>
        Similarly, the serach using "is" words (marked in green) only found eight possible starts, and none of them got
        past two steps. "as" words were the only choice, and all I could do now was look at what paths the script found.
        This was all that was possible - the puzzle had to be one of these, there were no other ways.<br><br>
        So, let's quickly see why the answer ended up "test":<br>
        All the paths for "shy" include "trash". I dropped that clue word from the puzzle, as it would be easy to mix up
        with "waste". I can't make an icon that distinguishes between the two, both of them contain "as" and thus look
        right, it would be pretty unfair.<br>
        The "coal" to "coat" path only changes the last letter three times. I don't think that reflects the original
        puzzle well. The two three-step paths for "stag" similarly only change a single spot in the word, but also, both
        of the start words are profanities.<br>
        The "matter" and "tech" subgraphs use a lot of words I should have filtered out. In my initial filtering, I left
        in any word I could potentially find an image of, but I didn't think about how they would be represented as
        icons. Clue words like "plasm", "past", "beast" or "taste" would be difficult to depict as a simple picture
        without adding copius amounts of detail.<br>
        And "damar" to "data" only worked because of "marasca", which I accidentally left in the filtered list because
        I thought it said "mascara" :)<br><br>
        And that's how we ended up here. That's how you localize a puzzle!<br>
        Definitely, without a doubt, the most complicated localization in the entire set. It was not the one that took
        the longest, because I was able to write a script to deal with the part that would have taken me at least a
        week, but still, the most involved approach at least.
    </div>
</ModalPuzzleBase>
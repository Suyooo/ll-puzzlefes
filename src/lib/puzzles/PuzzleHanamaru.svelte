<script>
    import ModalPuzzleBase from "$lib/ModalPuzzleBase.svelte";
</script>

<ModalPuzzleBase key="hanamaru" solution="zura" url="/puzzles/17_hanamaru.png">
    <div slot="hint">
        Can you make a connection between the amount of books in each stack and the shape below it?<br>
        It's not a property of the shapes, like the amount of sides - it's far more literal.
    </div>
    <div slot="explain">
        The shapes are a trapezium (or trapezoid depending on where you live), a square and a circle. The stacks have as
        many books as there are characters in the shape names, so each book represents one letter. Taking the letters
        mapped to the highlighted books from each stack (the fourth to last character) and adding the A results in the
        answer, "zura".
    </div>
    <div slot="loc">
        The original puzzle worked similarly, by assigning the characters of a word to a stack of books, and then
        taking all the characters from the highlighted books to form the answer word. The key difference is where those
        hint words come from: in the original, there is a stack of green books ("mi-do-ri"), a stack of black books
        ("ku-ro") and a stack of white books ("shi-ro").<br><br>
        Why use shapes instead of colours in this one? For two reasons: One, it helps people with colour vision
        deficiencies. If I used colours, the only way around it would be writing out the colour names, and that would
        probably give the key to the puzzle away to everyone playing.<br><br>
        Two, it just lined up nicely. I wanted to do the same thing as in the original puzzle where the stacks are
        placed at the same height, as if on a shelf, so I had to make sure all the used letters are in the same position
        in each word, but from the end. So I just wrote a little script, fed it with some shape names to test it out,
        and "zura" as a possible word was just too perfect to pass up on.<br><br>
        "Trapezium" might feel like it's a little out there as a shape name. At first, I wanted the "z" to be the given
        letter, and have the "a" be the result of a "hexagon" stack, but I thought the answer would be too obvious if
        you saw it's a four letter word, starting with "z", and it's related to Maru. That's why I had to turn the "z"
        into a stack, and the trapezium was the only match here.<br>
        However, it still works fine, because the same thing can be applied still, but in reverse: if you see the answer
        ends in "ura", it is also very obvious what the answer is, so you can still solve the puzzle even if you don't
        know the word "trapezium". The difference being that instead of being obvious from the start, you still have to
        figure out the approach to the puzzle first.<br>
        I'm also very glad the entire trapezium/trapezoid confusion doesn't matter as they are the same length and have
        the "z" in the same place, otherwise I'd be in big trouble...
    </div>
</ModalPuzzleBase>
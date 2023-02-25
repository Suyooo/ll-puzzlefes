<script>
    import ModalPuzzleBase from "$lib/ModalPuzzleBase.svelte";
</script>

<ModalPuzzleBase key="hanamaru" solution="zura" url="/puzzles/17_hanamaru.png">
    <!--<div slot="hint">
        Can you make a connection between the amount of books in each stack and the shape below it?<br>
        You don't need to think about the properties of the shapes themselves. You need to map the books in the stacks
        to something about the shape - what is something that can easily be represented in small parts?
    </div>-->
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
        and "zura" as a possible word was just too perfect to pass up on.
    </div>
</ModalPuzzleBase>
<script>
    import ModalPuzzleBase from "$lib/ModalPuzzleBase.svelte";
</script>

<ModalPuzzleBase key="kanan" solution="dive" url="/puzzles/13_kanan.png">
    <!--<div slot="hint">
        The words for the first two lines describe the person in the picture who is doing the activity, not the activity
        itself.<br>
        The first word starts with an "H".
    </div>-->
    <div slot="explain">
        The first word is "hiker", the second is "driver". By copying the highlighted letters, you get the answer,
        "dive".
    </div>
    <div slot="loc">
        In the original puzzle, the shown activities were described instead ("diving" and "hiking"). However, no matter
        how much I tried, I couldn't get anything to fit "hug" as the answer. I finally dropped the "-ing" words as
        "diving" would share all but one letter with "driving" which would be kind of weird and obvious, so I went with
        "-er" nouns instead so I could fake people out with just "dive" instead of "diver".<br>
        <br>
        <a href="https://www.flaticon.com/free-icon/hiking_9003815">Hiker icon by Irfansusanto20</a><br>
        <a href="https://www.flaticon.com/free-icon/driving-control_8301843">Driver icon by Prashanth Rapolu 15</a>
    </div>
</ModalPuzzleBase>
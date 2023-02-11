<script lang="ts">
    import Spinner from "$lib/Spinner.svelte";
    import PageButton from "$lib/styled/PageButton.svelte";
    import {timeFormat} from "$lib/timeFormat.js";
    import {fade} from "svelte-reduced-motion/transition";

    export let key: string;
    export let url: string;
    export let solution: string;

    let answer: string, imagePromise: Promise<string>, justSolved: boolean = false;
    $: {
        // https://stackoverflow.com/a/20285053/1381397
        imagePromise = fetch(url)
            .then(response => response.blob())
            .then(blob => new Promise((resolve, reject) => {
                const reader = new FileReader();
                reader.onloadend = () => {
                    resolve(reader.result);
                };
                reader.onerror = reject;
                reader.readAsDataURL(blob);
                document.scrollingElement.scrollTop = 0;
            }));
    }

    function submit() {
        if (answer.toLowerCase() === solution) {
            justSolved = true;
            document.scrollingElement.scrollTop = 0;
        } else {
            alert("um nah");
        }
    }
</script>

{#key justSolved}
    <div class="flex flex-col space-y-4 items-center w-3xl max-w-3xl" in:fade>
        {#if !justSolved}
            {#await imagePromise}
                <Spinner/>
            {:then imageB64}
                <img class="w-full" src={imageB64} alt="Puzzle"/>
                <div class="max-w-md">
                    <span class="text-xs tracking-widest uppercase font-bold text-primary-400">Enter Your Answer!</span>
                    <div class="w-full flex items-center gap-x-2">
                        <input class="flex-grow px-2 py-1 border-primary-400 border-2 rounded-full" bind:value={answer}>
                        <PageButton label="Submit" on:click={submit}>Submit</PageButton>
                    </div>
                </div>
            {:catch _}
                There was a problem loading the puzzle. Please try again!
            {/await}
        {:else}
            <span class="text-3xl tracking-widest uppercase text-primary-400 -mb-8">Congratulations!</span>
            <span class="text-[6rem] tracking-widest uppercase font-bold text-amber-400">CORRECT</span>
            <span class="text-xl">You solved the puzzle in {timeFormat(0)}!</span>
        {/if}
    </div>
{/key}
<script lang="ts">
    import Spinner from "$lib/Spinner.svelte";
    import PageButton from "$lib/styled/PageButton.svelte";
    import {timeFormat} from "$lib/timeFormat.js";
    import {createState, endTimer, startTimer, STATES} from "$stores/state";
    import {onDestroy} from "svelte";
    import {fade, fly} from "svelte-reduced-motion/transition";

    export let key: string;
    export let url: string;
    export let solution: string;

    let answer: HTMLInputElement, imagePromise: Promise<string>, justSolved: boolean = false,
        showExplain: boolean = false, showLoc: boolean = false, blockTimerStart: boolean = false;

    if ($STATES[key] === undefined) {
        createState(key);
    }

    // Ensure image is loaded before starting the timer: https://stackoverflow.com/a/20285053/1381397
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
            if (!blockTimerStart && !$STATES[key].solved) {
                startTimer(key);
            }
        }));

    function submit() {
        const submittedAnswer = answer.value.toLowerCase().trim();
        if (submittedAnswer === "") return;

        if (submittedAnswer === solution) {
            justSolved = true;
            document.scrollingElement.scrollTop = 0;
            endTimer();

            if (!$STATES[key].solved) {
                STATES.update(states => {
                    states[key].solved = true;
                    return states;
                });
            }
        } else {
            answer.disabled = true;
            answer.value = "Wrong Answer!";
            setTimeout(() => {
                if (answer) {
                    answer.disabled = false;
                    answer.value = submittedAnswer;
                }
            }, 2000);

            if (!$STATES[key].solved && $STATES[key].wrongGuesses.indexOf(submittedAnswer) === -1) {
                STATES.update(states => {
                    states[key].wrongGuesses.push(submittedAnswer);
                    return states;
                });
            }
        }
    }

    onDestroy(() => {
        blockTimerStart = true;
        endTimer();
    });
</script>

{#key justSolved}
    <div class="flex flex-col space-y-4 items-center w-3xl max-w-3xl" in:fade>
        {#if !justSolved}
            {#await imagePromise}
                <Spinner/>
            {:then image}
                <img class="w-full" src={image} alt="Puzzle"/>
                <div class="w-full max-w-md">
                    <div class="text-xs tracking-widest uppercase font-bold text-primary-400 mb-1">Enter Your Answer!
                    </div>
                    <div class="w-full flex items-center gap-x-2">
                        <input class="flex-grow px-2 pb-1 pt-0.5 border-primary-400 border-2 rounded-full"
                               bind:this={answer}
                               class:bg-primary-400={answer?.disabled ?? false}
                               class:text-white={answer?.disabled ?? false}
                               class:text-center={answer?.disabled ?? false}
                               on:keyup={(e) => {if (e.key === "Enter") submit();}}>
                        <PageButton label="Submit" on:click={submit}>Submit</PageButton>
                    </div>
                    {#if !$STATES[key].solved && $STATES[key].wrongGuesses.length > 0}
                        <div class="pt-6 w-full max-w-md">
                            <div class="text-xs tracking-widest uppercase font-bold text-gray-500">
                                Previous Answers
                            </div>
                            {#each [...$STATES[key].wrongGuesses].reverse() as guess (guess)}
                                <div class="w-full mt-1 rounded-full px-3 pb-1 pt-0.5 border border-gray-500 text-gray-500"
                                     in:fly|local="{{ x: 100, duration: 300 }}">
                                    {guess}
                                </div>
                            {/each}
                        </div>
                    {/if}
                </div>
            {:catch e}
                There was a problem loading the puzzle. Please try again! {@html e.stack.replace(/\n/g, "<br>")}
            {/await}
        {:else}
            <div class="text-3xl tracking-widest uppercase text-primary-400 -mb-8">Congratulations!</div>
            <div class="text-[6rem] tracking-widest uppercase font-bold text-amber-400">CORRECT</div>
            <div class="text-xl">You solved the puzzle in {timeFormat($STATES[key].totalTime)}!</div>
        {/if}

        {#if $STATES[key].solved}
            <div class="pt-6 w-full max-w-md">
                <PageButton label="Reveal Explanation" on:click={() => showExplain = !showExplain}
                            extraClasses="w-full">
                    Solution
                </PageButton>
                {#if showExplain}
                    <div class="w-full border-2 bg-white mt-1 px-4 py-2 border-primary-400 rounded-2xl">
                        <slot name="explain"/>
                    </div>
                {/if}
                <PageButton label="Reveal Localization Notes" on:click={() => showLoc = !showLoc}
                            extraClasses="w-full mt-4">
                    Localization Notes
                </PageButton>
                {#if showLoc}
                    <div class="w-full border-2 bg-white mt-1 px-4 py-2 border-primary-400 rounded-2xl">
                        <slot name="loc"/>
                    </div>
                {/if}
            </div>
        {/if}
    </div>
{/key}
<script lang="ts">
    import ShareButton from "$lib/ShareButton.svelte";
    import Spinner from "$lib/Spinner.svelte";
    import PageButton from "$lib/styled/PageButton.svelte";
    import {timeFormat} from "$lib/timeFormat.js";
    import {createState, endTimer, startTimer, STATES} from "$stores/state";
    import {getContext, onDestroy} from "svelte";
    import {fade, fly} from "svelte-reduced-motion/transition";

    export let key: string;
    export let url: string;
    export let solution: string;
    export let bonus: any | undefined = undefined;
    export let bonusName: string | undefined = undefined;
    export let bonusKey: string | undefined = undefined;
    export let name: string | undefined = undefined;
    export let cvdAlt: any | undefined = undefined;

    let answer: HTMLInputElement, imagePromise: Promise<string>, justSolved: boolean = false,
        showHint: boolean = false, showExplain: boolean = false, showLoc: boolean = false, showBonus: boolean = false,
        blockTimerStart: boolean = false;
    if (name === undefined) name = key.charAt(0).toUpperCase() + key.substring(1) + "'s Puzzle";

    const modal = getContext<(title: string, component: any) => (() => void)>("modal");

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
        const submittedAnswer = answer.value.toLowerCase().replace(/[^a-z]/g, "");
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
    <div class="flex flex-col space-y-4 items-center w-full max-w-3xl" in:fade>
        {#if !justSolved}
            {#await imagePromise}
                <Spinner/>
            {:then image}
                <img class="w-full" src={image} alt="Puzzle"/>
                <div class="w-full max-w-md">
                    <label for="answer"
                           class="text-xs tracking-widest uppercase font-bold text-primary-400 mb-1 select-none">
                        Enter Your Answer!
                    </label>
                    <div class="w-full flex items-center gap-x-2">
                        <input class="flex-grow px-2 pb-1 pt-0.5 border-primary-400 border-2 rounded-full"
                               id="answer" bind:this={answer}
                               class:bg-primary-400={answer?.disabled ?? false}
                               class:text-white={answer?.disabled ?? false}
                               class:text-center={answer?.disabled ?? false}
                               on:keyup={(e) => {if (e.key === "Enter") submit();}}>
                        <PageButton label="Submit" on:click={submit}>Submit</PageButton>
                    </div>
                    <div class="pt-6 w-full max-w-md">
                        {#if !$STATES[key].solved && $STATES[key].wrongGuesses.length > 0}
                            <div class="pb-6">
                                <div class="text-xs tracking-widest uppercase font-bold text-gray-500 select-none">
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

                        {#if $$slots.hint}
                            <PageButton label="Reveal Hint" on:click={() => showHint = !showHint} extraClasses="w-full">
                                Hint
                            </PageButton>
                            {#if showHint}
                                <div class="w-full border-2 bg-white mt-1 px-4 py-2 border-primary-400 rounded-2xl">
                                    <slot name="hint"/>
                                </div>
                            {/if}
                        {:else}
                            <div class="bg-gray-500 h-8 flex items-center justify-center rounded-full px-4 py-2 uppercase tracking-widest select-none font-bold text-white">
                                Hint unlocking tomorrow!
                            </div>
                        {/if}
                        {#if cvdAlt}
                            <PageButton label="Assistance for Color Vision Deficiencies" on:click={modal(name, cvdAlt)}
                                        extraClasses="w-full mt-4">
                                Assistance for Color Vision Deficiencies
                            </PageButton>
                        {/if}
                    </div>
                </div>
            {:catch e}
                There was a problem loading the puzzle. Please try again! {@html e.stack.replace(/\n/g, "<br>")}
            {/await}
        {:else}
            <div class="text-[4rem] tracking-widest uppercase font-bold text-amber-400"
                 style:text-shadow="0 0 5px darkgoldenrod">
                CORRECT
            </div>
            <div class="text-xl text-center">
                <div class="tracking-widest uppercase text-primary-400">Congratulations!</div>
                You solved {name} in {timeFormat($STATES[key].totalTime)}!
            </div>
            <div class="pb-6 pt-4">
                <ShareButton {name} time={$STATES[key].totalTime}/>
            </div>
        {/if}

        {#if $STATES[key].solved}
            <div class="w-full max-w-md">
                <PageButton label="Reveal Explanation" on:click={() => showExplain = !showExplain}
                            extraClasses="w-full">
                    Solution
                </PageButton>
                {#if showExplain}
                    <div class="w-full border-2 bg-white mt-1 px-4 py-2 border-primary-400 rounded-2xl">
                        <slot name="explain"/>
                    </div>
                {/if}
                {#if bonus}
                    <PageButton label="See Bonus Puzzle" on:click={() => showBonus = !showBonus}
                                extraClasses={`w-full mt-4${$STATES[bonusKey] ? "" : " animate-pulse"}`}>
                        Bonus Puzzle
                    </PageButton>
                    {#if showBonus}
                        <div class="w-full border-2 bg-white mt-1 px-4 py-2 border-primary-400 rounded-2xl">
                            <slot name="bonus"/>
                            <PageButton label="Play Bonus Puzzle" on:click={modal(bonusName, bonus)}
                                        extraClasses="w-full mt-4">
                                Play Bonus Puzzle
                            </PageButton>
                        </div>
                    {/if}
                {/if}
                {#if $$slots.loc}
                    <PageButton label="Reveal Localization Notes" on:click={() => showLoc = !showLoc}
                                extraClasses="w-full mt-4">
                        Localization Notes
                    </PageButton>
                    {#if showLoc}
                        <div class="w-full border-2 bg-white mt-1 px-4 py-2 border-primary-400 rounded-2xl">
                            <slot name="loc"/>
                        </div>
                    {/if}
                {/if}
            </div>
        {/if}
    </div>
{/key}
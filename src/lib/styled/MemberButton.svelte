<script lang="ts">
    import Correct from "$icon/Correct.svelte";
    import {STATES} from "$stores/state.js";

    export let name: string;
    export let color: string;
    export let whiteText: boolean = false;
    export let disabled: boolean = false;
    export let forceNew: boolean = false;
    export let flip: boolean = false;
    export let flipClue: string;

    let key: string;
    $: key = name.toLowerCase();

    function change() {
        if (forceNew) {
            forceNew = false;
            disabled = true;
        } else if (disabled) {
            disabled = false;
        } else {
            forceNew = true;
        }
    }
</script>

<button aria-disabled={disabled} aria-label={name} class="mb-4 basis-1/3 px-2 h-12 w-full font-bold" on:click={change}
        class:cursor-default={disabled} title={name}>
    <div class="flex flex-col sm:flex-row items-center justify-center rounded-full p-1 uppercase select-none outline outline-[.125rem] outline-offset-[-.125rem]"
         class:bg-gray-300={!disabled} class:bg-gray-500={disabled} class:hover:bg-gray-200={!disabled}
         class:outline-gray-300={!disabled} class:outline-gray-500={disabled}>
        <div class="w-[90%] rounded-full h-10 px-2 py-1 flex items-center justify-center basis-2/3 tracking-wide sm:tracking-widest"
             class:basis-full={flip} class:text-white={whiteText || disabled}
             class:w-full={flip} style:background-color={disabled ? "#888" : color}>{flip ? flipClue : name}</div>
        {#if !flip}
            <div class="flex items-center justify-center gap-x-1 text-black basis-1/3 leading-3 px-2 state">
                {#if disabled}
                    <span class="text-white text-xs">Coming Soon</span>
                {:else if $STATES[key] === undefined || forceNew}
                    <span class="text-primary-400 sm:my-0">NEW!</span>
                {:else if $STATES[key].solved === false}
                    <span class="text-xs">Not Solved</span>
                {:else}
                    <Correct/>
                {/if}
            </div>
        {/if}
    </div>
</button>

<style lang="postcss">
    .state > span {
        display: flex;
        align-items: center;
        min-height: 20px;
    }
</style>
<script lang="ts">
    import focusTrap from "$actions/focusTrap";
    import Close from "$icon/Close.svelte";
    import HeaderButton from "$lib/styled/HeaderButton.svelte";
    import {createEventDispatcher} from "svelte";
    import {fade} from "svelte-reduced-motion/transition";

    export let inner: any;
    export let title: string;

    const dispatch = createEventDispatcher<{ closemodal: undefined }>();

    function closeModal() {
        dispatch("closemodal");
    }
</script>

<svelte:window on:keydown={e => { if (e.key === "Escape") closeModal() }}/>

<div class="fixed left-0 top-0 w-full bottom-0 bg-gray-900 bg-opacity-80" transition:fade={{duration: 300}}>&nbsp;</div>
<!--
    svelte-ignore a11y-click-events-have-key-events
    Accessibility is handled with the key event above ^, and there's also an accessible close button as the alternative
-->
<div class="absolute left-0 top-0 w-full bottom-0 flex items-start justify-center px-2 pt-24" on:click={closeModal}
     transition:fade={{duration: 300}} use:focusTrap>
    <div class="max-w-4xl bg-gray-50 rounded p-4 relative" on:click|stopPropagation={() => null}>
        <h3 class="flex-grow h-8 p-2 uppercase tracking-widest font-bold text-gray-400">{title}</h3>
        <HeaderButton extraClasses="absolute right-4 top-4" label="Close" on:click={closeModal}>
            <Close/>
        </HeaderButton>
        <div class="p-2 mt-4">
            <svelte:component on:closemodal this={inner}/>
        </div>
    </div>
</div>
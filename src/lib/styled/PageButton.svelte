<script lang="ts">
    export let label: string | undefined = undefined;
    export let disabled: boolean = false;
    export let extraClasses: string | undefined = undefined;
</script>

<button aria-disabled={disabled} aria-label={label}
        class="min-h-8 flex items-center justify-center rounded-full px-4 py-1 uppercase tracking-widest select-none font-bold text-white {extraClasses ?? ""}"
        class:active:bg-primary-700={!disabled}
        class:active:text-white={!disabled}
        class:bg-gray-500={disabled} class:bg-primary-400={!disabled}
        class:hover:bg-gray-500={disabled} class:hover:bg-primary-200={!disabled} on:click
        title={label}>


<slot/>
</button>
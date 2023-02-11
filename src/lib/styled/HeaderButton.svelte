<script lang="ts">
    export let label: string | undefined = undefined;
    export let extraClasses: string | undefined = undefined;
</script>

<button aria-label={label} class="w-10 h-10 text-gray-400 hover:text-black flex items-center justify-center rounded
active:text-white active:bg-primary-800 {extraClasses ?? ""}"
        on:click title={label}>

<slot/>
</button>
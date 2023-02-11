<script lang="ts">
    export let name: string;
    export let color: string;
    export let whiteText: boolean = false;
    export let state: string;
    export let disabled: boolean = false;
</script>

<button aria-disabled={disabled} aria-label={name} class="mb-4 basis-1/3 px-2 h-12 w-full font-bold" on:click
        title={name}>
    <div class="flex items-center justify-center rounded-full p-1 uppercase select-none transition-shadow outline outline-[.125rem] outline-offset-[-.125rem]"
         class:bg-gray-300={!disabled} class:bg-gray-500={disabled} class:hover:bg-gray-200={!disabled}
         class:outline-gray-300={!disabled} class:outline-gray-500={disabled}>
        <span class="rounded-full h-10 flex items-center justify-center basis-2/3 tracking-widest"
              class:text-white={whiteText} style:background-color={disabled ? "#888" : color}>{name}</span>
        <span class="text-black basis-1/3 leading-3" class:text-white={disabled} class:text-xs={disabled}>
            {disabled ? "coming soon" : state}
        </span>
    </div>
</button>
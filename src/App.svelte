<script lang="ts">
    import Modal from "$lib/Modal.svelte";
    import ModalAbout from "$lib/ModalAbout.svelte";
    import PageButton from "$lib/styled/PageButton.svelte";
    import {fade} from "svelte-reduced-motion/transition";

    let modalTitle: string = "";
    let modalComponent = null;

    function modal(title: string, component: any) {
        return openModal.bind(this, title, component);
    }

    function openModal(title: string, component: any) {
        modalTitle = title;
        modalComponent = component;
    }

    function closeModal() {
        modalComponent = null;
    }
</script>

<div class="flex flex-col w-full h-full items-center overflow-auto" in:fade={{duration: 100}} tabindex="-1">
    <div class="max-w-3xl my-8 flex items-center">
        <div class="basis-1/4 flex-shrink">
            <img alt="SIF2 Game Logo" class="w-full" src="/logo.png"/>
        </div>
        <div class="basis-3/4 flex-shrink">
            <img alt="Puzzle Solving Fes Logo" class="w-full" src="/title.svg"/>
        </div>
    </div>
    <div class="flex-grow">
        <PageButton on:click={modal("About", ModalAbout)}>Test Modal</PageButton>
    </div>
    <div class="justify-self-end mb-4 text-xs text-gray-400">
        This site was made by Suyooo.
        <button class="underline" on:click={modal("About", ModalAbout)}>About</button>
    </div>
</div>

{#if modalComponent != null}
    <Modal title={modalTitle} inner={modalComponent} on:closemodal={closeModal}/>
{/if}
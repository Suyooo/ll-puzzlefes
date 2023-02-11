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
    <PageButton on:click={modal("About", ModalAbout)}>Test Modal</PageButton>
</div>

{#if modalComponent != null}
    <Modal title={modalTitle} inner={modalComponent} on:closemodal={closeModal}/>
{/if}
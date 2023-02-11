<script lang="ts">
    import Modal from "$lib/Modal.svelte";
    import {fade} from "svelte-reduced-motion/transition";

    let modalTitle: string = "";
    let modalComponent = null;

    function openModalEvent(event: CustomEvent<{ title: string, component: any }>) {
        openModal(event.detail.title, event.detail.component);
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

</div>

{#if modalComponent != null}
    <Modal title={modalTitle} inner={modalComponent} on:closemodal={closeModal}/>
{/if}
<script lang="ts">
    import Modal from "$lib/Modal.svelte";
    import ModalAbout from "$lib/ModalAbout.svelte";
    import MemberButton from "$lib/styled/MemberButton.svelte";
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
    <div class="w-full max-w-3xl flex-grow flex flex-wrap content-start">
        <MemberButton color="#FFA336" name="Honoka"/>
        <MemberButton color="#7AEEFF" name="Eli"/>
        <MemberButton color="#CEBFBF" name="Kotori"/>
        <MemberButton color="#1769FF" name="Umi" whiteText/>
        <MemberButton color="#FFF832" disabled name="Rin"/>
        <MemberButton color="#FF503E" disabled name="Maki"/>
        <div class="w-full h-8">&nbsp;</div>
    </div>
    <div class="justify-self-end mb-4 text-xs text-gray-400">
        This site was made by Suyooo.
        <button class="underline" on:click={modal("About", ModalAbout)}>About</button>
    </div>
</div>

{#if modalComponent != null}
    <Modal title={modalTitle} inner={modalComponent} on:closemodal={closeModal}/>
{/if}
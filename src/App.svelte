<script lang="ts">
    import Modal from "$lib/Modal.svelte";
    import ModalAbout from "$lib/ModalAbout.svelte";
    import PuzzleHonoka from "$lib/puzzles/PuzzleHonoka.svelte";
    import MemberButton from "$lib/styled/MemberButton.svelte";
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
        document.scrollingElement.scrollTop = 0;
    }

    function closeModal() {
        modalComponent = null;
    }
</script>

<div class="relative flex flex-col w-full items-center" in:fade={{duration: 100}} tabindex="-1">
    <div class="max-w-3xl my-8 flex items-center">
        <div class="basis-1/4 flex-shrink">
            <img alt="SIF2 Game Logo" class="w-full" src="/logo.png"/>
        </div>
        <div class="basis-3/4 flex-shrink">
            <img alt="Puzzle Solving Fes Logo" class="w-full" src="/title.svg"/>
        </div>
    </div>
    <div class="w-full max-w-3xl flex-grow flex flex-wrap content-start">
        <MemberButton color="#FFA336" name="Honoka" on:click={modal("Honoka's Puzzle", PuzzleHonoka)}/>
        <MemberButton color="#7AEEFF" name="Eli"/>
        <MemberButton color="#CEBFBF" name="Kotori"/>
        <MemberButton color="#1769FF" name="Umi" whiteText/>
        <MemberButton color="#FFF832" disabled name="Rin"/>
        <MemberButton color="#FF503E" disabled name="Maki"/>
        <MemberButton color="#C455F6" disabled name="Nozomi"/>
        <MemberButton color="#6AE673" disabled name="Hanayo"/>
        <MemberButton color="#FF4F91" disabled name="Nico"/>
        <div class="w-full h-12">&nbsp;</div>
        <MemberButton color="#FF9547" disabled name="Chika"/>
        <MemberButton color="#FF9EAC" disabled name="Riko"/>
        <MemberButton color="#27C1B7" disabled name="Kanan"/>
        <MemberButton color="#DB0839" disabled name="Dia" whiteText/>
        <MemberButton color="#66C0FF" disabled name="You"/>
        <MemberButton color="#C1CAD4" disabled name="Yohane"/>
        <MemberButton color="#FFD010" disabled name="Hanamaru"/>
        <MemberButton color="#C252C6" disabled name="Mari"/>
        <MemberButton color="#FF6FBE" disabled name="Ruby"/>
        <div class="w-full h-12">&nbsp;</div>
        <MemberButton color="#FFBFE0" disabled name="Ayumu"/>
        <MemberButton color="#F5FF8A" disabled name="Kasumi"/>
        <MemberButton color="#BBEDFF" disabled name="Shizuku"/>
        <MemberButton color="#4A2FED" disabled name="Karin" whiteText/>
        <MemberButton color="#FF8246" disabled name="Ai"/>
        <MemberButton color="#BE82FF" disabled name="Kanata"/>
        <MemberButton color="#F60E0E" disabled name="Setsuna"/>
        <MemberButton color="#B1F69C" disabled name="Emma"/>
        <MemberButton color="#D0CEE1" disabled name="Rina"/>
        <MemberButton color="#24BD8B" disabled name="Shioriko"/>
        <MemberButton color="#F1F0E6" disabled name="Mia"/>
        <MemberButton color="#F8C8C4" disabled name="Lanzhu"/>
        <MemberButton color="#000" disabled name="Yuu" whiteText/>
        <div class="w-full h-12">&nbsp;</div>
        <MemberButton color="#FF7F27" disabled name="Kanon"/>
        <MemberButton color="#A0FFF9" disabled name="Keke"/>
        <MemberButton color="#FF6E90" disabled name="Chisato"/>
        <MemberButton color="#74F466" disabled name="Sumire"/>
        <MemberButton color="#0000A0" disabled name="Ren" whiteText/>
        <MemberButton color="#FFF442" disabled name="Kinako"/>
        <MemberButton color="#FF3535" disabled name="Mei"/>
        <MemberButton color="#B2FFDD" disabled name="Shiki"/>
        <MemberButton color="#FF51C4" disabled name="Natsumi"/>
    </div>
    <PageButton extraClasses="mt-4"
                label="Visit Original Site"
                on:click={() => window.open("https://lovelive-sif2.bushimo.jp/nazotoki/list.html", "_blank")}>
        Visit Original Site
    </PageButton>
    <div class="justify-self-end mt-2 mb-4 text-xs text-gray-500">
        This site was made by Suyooo.
        <button class="underline" on:click={modal("About", ModalAbout)}>About</button>
    </div>

    {#if modalComponent != null}
        <Modal title={modalTitle} inner={modalComponent} on:closemodal={closeModal}/>
    {/if}
</div>
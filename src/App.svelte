<script lang="ts">
    import Modal from "$lib/Modal.svelte";
    import ModalAbout from "$lib/ModalAbout.svelte";
    import PuzzleChika from "$lib/puzzles/PuzzleChika.svelte";
    import PuzzleDia from "$lib/puzzles/PuzzleDia.svelte";
    import PuzzleEli from "$lib/puzzles/PuzzleEli.svelte";
    import PuzzleHanayo from "$lib/puzzles/PuzzleHanayo.svelte";
    import PuzzleHonoka from "$lib/puzzles/PuzzleHonoka.svelte";
    import PuzzleKanan from "$lib/puzzles/PuzzleKanan.svelte";
    import PuzzleKotori from "$lib/puzzles/PuzzleKotori.svelte";
    import PuzzleMaki from "$lib/puzzles/PuzzleMaki.svelte";
    import PuzzleNico from "$lib/puzzles/PuzzleNico.svelte";
    import PuzzleNozomi from "$lib/puzzles/PuzzleNozomi.svelte";
    import PuzzleRiko from "$lib/puzzles/PuzzleRiko.svelte";
    import PuzzleRin from "$lib/puzzles/PuzzleRin.svelte";
    import PuzzleSetsuna from "$lib/puzzles/PuzzleSetsuna.svelte";
    import PuzzleUmi from "$lib/puzzles/PuzzleUmi.svelte";
    import PuzzleYou from "$lib/puzzles/PuzzleYou.svelte";
    import MemberButton from "$lib/styled/MemberButton.svelte";
    import PageButton from "$lib/styled/PageButton.svelte";
    import {fade} from "svelte-reduced-motion/transition";

    let showHelp: boolean = false, modalTitle: string = "", modalComponent = null;

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
    <div class="max-w-3xl px-2 mt-8 mb-4 flex items-center">
        <div class="basis-1/4 flex-shrink">
            <img alt="SIF2 Game Logo" class="w-full" src="/logo.png"/>
        </div>
        <div class="basis-3/4 flex-shrink">
            <img alt="Puzzle Solving Fes Logo" class="w-full" src="/title.svg"/>
        </div>
    </div>
    <PageButton extraClasses="w-full max-w-md px-2" label="Reveal Help" on:click={() => showHelp = !showHelp}>
        What Is This?
    </PageButton>
    {#if showHelp}
        <div class="w-full max-w-md border-2 bg-white mt-1 px-4 py-2 border-primary-400 rounded-2xl">
            The <b>Puzzle Solving Festival</b> is a campaign by Bushiroad to celebrate the upcoming release of SIF2.<br>
            <br>
            Every day, a new puzzle is released on the official site, where the answer is some word relating to the
            member. Analyze the puzzle to find hints, think about what words could be answers fitting for that member,
            and solve all of the riddles!<br><br>
            On this site, you can find localized versions of the original puzzles for those who don't know Japanese.
            The localizations try to work the same way as the originals wherever possible, so you can still work out the
            solutions with the intended approach!<br><br>
            <a href="https://lovelive-sif2.bushimo.jp/preregistration/">Remember to preregister for SIF2!</a>
        </div>
    {/if}
    <div class="w-full mt-8 max-w-3xl flex-grow flex flex-wrap content-start">
        <MemberButton color="#FFA336" name="Honoka" on:click={modal("Honoka's Puzzle", PuzzleHonoka)}/>
        <MemberButton color="#7AEEFF" name="Eli" on:click={modal("Eli's Puzzle", PuzzleEli)}/>
        <MemberButton color="#CEBFBF" name="Kotori" on:click={modal("Kotori's Puzzle", PuzzleKotori)}/>
        <MemberButton color="#1769FF" name="Umi" on:click={modal("Umi's Puzzle", PuzzleUmi)} whiteText/>
        <MemberButton color="#FFF832" name="Rin" on:click={modal("Rin's Puzzle", PuzzleRin)}/>
        <MemberButton color="#FF503E" name="Maki" on:click={modal("Maki's Puzzle", PuzzleMaki)}/>
        <MemberButton color="#C455F6" name="Nozomi" on:click={modal("Nozomi's Puzzle", PuzzleNozomi)}/>
        <MemberButton color="#6AE673" name="Hanayo" on:click={modal("Hanayo's Puzzle", PuzzleHanayo)}/>
        <MemberButton color="#FF4F91" name="Nico" on:click={modal("Nico's Puzzle", PuzzleNico)}/>
        <div class="w-full h-8">&nbsp;</div>
        <MemberButton color="#FF9547" name="Chika" on:click={modal("Chika's Puzzle", PuzzleChika)}/>
        <MemberButton color="#FF9EAC" name="Riko" on:click={modal("Riko's Puzzle", PuzzleRiko)}/>
        <MemberButton color="#27C1B7" name="Kanan" on:click={modal("Kanan's Puzzle", PuzzleKanan)}/>
        <MemberButton color="#DB0839" name="Dia" on:click={modal("Dia's Puzzle", PuzzleDia)} whiteText/>
        <MemberButton color="#66C0FF" name="You" on:click={modal("You's Puzzle", PuzzleYou)}/>
        <MemberButton color="#C1CAD4" disabled name="Yohane"/>
        <MemberButton color="#FFD010" disabled name="Hanamaru"/>
        <MemberButton color="#C252C6" disabled name="Mari"/>
        <MemberButton color="#FF6FBE" disabled name="Ruby"/>
        <div class="w-full h-8">&nbsp;</div>
        <MemberButton color="#FFBFE0" disabled name="Ayumu"/>
        <MemberButton color="#F5FF8A" disabled name="Kasumi"/>
        <MemberButton color="#BBEDFF" disabled name="Shizuku"/>
        <MemberButton color="#4A2FED" disabled name="Karin" whiteText/>
        <MemberButton color="#FF8246" disabled name="Ai"/>
        <MemberButton color="#BE82FF" disabled name="Kanata"/>
        <MemberButton color="#F60E0E" name="Setsuna" on:click={modal("Setsuna's Puzzle", PuzzleSetsuna)}/>
        <MemberButton color="#B1F69C" disabled name="Emma"/>
        <MemberButton color="#D0CEE1" disabled name="Rina"/>
        <MemberButton color="#24BD8B" disabled name="Shioriko"/>
        <MemberButton color="#F1F0E6" disabled name="Mia"/>
        <MemberButton color="#F8C8C4" disabled name="Lanzhu"/>
        <MemberButton color="#000" disabled name="Yuu" whiteText/>
        <div class="w-full h-8">&nbsp;</div>
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
    <PageButton extraClasses="mt-4 w-full max-w-md px-2"
                label="Visit Original Site"
                on:click={() => window.open("https://lovelive-sif2.bushimo.jp/nazotoki/list.html", "_blank")}>
        Visit The Official Site
    </PageButton>
    <div class="justify-self-end mt-2 mb-4 text-xs text-gray-500">
        This site was made by Suyooo.
        <button class="underline" on:click={modal("About", ModalAbout)}>About</button>
    </div>

    {#if modalComponent != null}
        <Modal title={modalTitle} inner={modalComponent} on:closemodal={closeModal}/>
    {/if}
</div>
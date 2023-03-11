<script lang="ts">
    import Correct from "$icon/Correct.svelte";
    import Modal from "$lib/Modal.svelte";
    import ModalAbout from "$lib/ModalAbout.svelte";
    import PuzzleAi from "$lib/puzzles/PuzzleAi.svelte";
    import PuzzleAyumu from "$lib/puzzles/PuzzleAyumu.svelte";
    import PuzzleChika from "$lib/puzzles/PuzzleChika.svelte";
    import PuzzleDia from "$lib/puzzles/PuzzleDia.svelte";
    import PuzzleEli from "$lib/puzzles/PuzzleEli.svelte";
    import PuzzleFinal from "$lib/puzzles/PuzzleFinal.svelte";
    import PuzzleHanamaru from "$lib/puzzles/PuzzleHanamaru.svelte";
    import PuzzleHanayo from "$lib/puzzles/PuzzleHanayo.svelte";
    import PuzzleHonoka from "$lib/puzzles/PuzzleHonoka.svelte";
    import PuzzleKanan from "$lib/puzzles/PuzzleKanan.svelte";
    import PuzzleKanata from "$lib/puzzles/PuzzleKanata.svelte";
    import PuzzleKarin from "$lib/puzzles/PuzzleKarin.svelte";
    import PuzzleKasumi from "$lib/puzzles/PuzzleKasumi.svelte";
    import PuzzleKotori from "$lib/puzzles/PuzzleKotori.svelte";
    import PuzzleMaki from "$lib/puzzles/PuzzleMaki.svelte";
    import PuzzleMari from "$lib/puzzles/PuzzleMari.svelte";
    import PuzzleNatsumi from "$lib/puzzles/PuzzleNatsumi.svelte";
    import PuzzleNico from "$lib/puzzles/PuzzleNico.svelte";
    import PuzzleNozomi from "$lib/puzzles/PuzzleNozomi.svelte";
    import PuzzleRiko from "$lib/puzzles/PuzzleRiko.svelte";
    import PuzzleRin from "$lib/puzzles/PuzzleRin.svelte";
    import PuzzleRuby from "$lib/puzzles/PuzzleRuby.svelte";
    import PuzzleShizuku from "$lib/puzzles/PuzzleShizuku.svelte";
    import PuzzleUmi from "$lib/puzzles/PuzzleUmi.svelte";
    import PuzzleYoshiko from "$lib/puzzles/PuzzleYoshiko.svelte";
    import PuzzleYou from "$lib/puzzles/PuzzleYou.svelte";
    import MemberButton from "$lib/styled/MemberButton.svelte";
    import PageButton from "$lib/styled/PageButton.svelte";
    import {timeFormat} from "$lib/timeFormat.js";
    import {STATES} from "$stores/state";
    import {setContext} from "svelte";
    import {fade} from "svelte-reduced-motion/transition";

    let showHelp: boolean = false, modalTitle: string = "", modalComponent = null,
        solved: number = Object.keys($STATES).filter(k => !k.startsWith("bonus_") && $STATES[k].solved).length,
        flip: boolean = solved === 40 /* only flip by default if all but the final puzzle have been solved */;

    function modal(title: string, component: any) {
        return openModal.bind(this, title, component);
    }

    setContext<(title: string, component: any) => (() => void)>("modal", modal);

    function openModal(title: string, component: any) {
        modalTitle = title;
        modalComponent = component;
        document.scrollingElement.scrollTop = 0;
    }

    function closeModal() {
        modalComponent = null;

        const newSolved = Object.keys($STATES).filter(k => !k.startsWith("bonus_") && $STATES[k].solved).length;
        if (solved < 40 && newSolved === 40) {
            // The player just solved the last normal puzzle - reveal the final puzzle!
            const endLock = Date.now() + 3000;
            const scrollBottom = () => {
                document.scrollingElement.scrollTop = document.scrollingElement.scrollHeight;
                if (Date.now() <= endLock) {
                    requestAnimationFrame(scrollBottom);
                }
            }
            requestAnimationFrame(scrollBottom);
            flip = true;
        } else {
            if (solved < 41 && newSolved === 41) {
                // The player just solved the final puzzle!! Flip clues back
                flip = false;
            }
            document.scrollingElement.scrollTop = 0;
        }
        solved = newSolved;
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
    {#if solved > 40}
        <div class="w-full px-2 bg-clip-text mt-8 text-5xl font-bold tracking-widest text-transparent thankyou text-center">
            THANK YOU FOR PLAYING!!
        </div>
        {@const unsolvedBonus = ["bonus_kotori", "bonus_chika", "bonus_rina", "bonus_chisato"].filter(k => (!($STATES[k]?.solved)) ?? true)}
        {#if unsolvedBonus.length > 0}
            <div class="w-full max-w-3xl px-2 mt-4 italic text-sm text-center">
                Psst... you are missing {unsolvedBonus.length > 1 ? "a few bonus puzzles" : "a bonus puzzle"}!
                There's no additional reward for finishing {unsolvedBonus.length > 1 ? "them" : "it"}, but if you're
                still up for some more, you can find
                {unsolvedBonus.length > 1 ? "them on these members' puzzles:" : "it on"}
                {unsolvedBonus.map(s => s.charAt(6).toUpperCase() + s.substring(7)).join(", ")}{unsolvedBonus.length > 1 ? "!" : "'s puzzle!"}
            </div>
        {/if}
    {/if}
    <div class="w-full mt-8 max-w-3xl flex-grow flex flex-wrap content-start gap-y-2 sm:gap-y-0">
        <MemberButton color="#FFA336" {flip} flipClue="·····4" name="Honoka"
                      on:click={modal("Honoka's Puzzle", PuzzleHonoka)}/>
        <MemberButton color="#7AEEFF" {flip} flipClue="····5··" name="Eli" on:click={modal("Eli's Puzzle", PuzzleEli)}/>
        <MemberButton color="#CEBFBF" {flip} flipClue="·····6" name="Kotori"
                      on:click={modal("Kotori's Puzzle", PuzzleKotori)}/>
        <MemberButton color="#1769FF" {flip} flipClue="···1····" name="Umi" on:click={modal("Umi's Puzzle", PuzzleUmi)}
                      whiteText/>
        <MemberButton color="#FFF832" {flip} flipClue="···3·" name="Rin" on:click={modal("Rin's Puzzle", PuzzleRin)}/>
        <MemberButton color="#FF503E" {flip} flipClue="·1··" name="Maki" on:click={modal("Maki's Puzzle", PuzzleMaki)}/>
        <MemberButton color="#C455F6" {flip} flipClue="·6··" name="Nozomi"
                      on:click={modal("Nozomi's Puzzle", PuzzleNozomi)}/>
        <MemberButton color="#6AE673" {flip} flipClue="···3" name="Hanayo"
                      on:click={modal("Hanayo's Puzzle", PuzzleHanayo)}/>
        <MemberButton color="#FF4F91" {flip} flipClue="··0···" name="Nico"
                      on:click={modal("Nico's Puzzle", PuzzleNico)}/>
        <div class="w-full h-8">&nbsp;</div>
        <MemberButton color="#FF9547" {flip} flipClue="···8··" name="Chika"
                      on:click={modal("Chika's Puzzle", PuzzleChika)}/>
        <MemberButton color="#FF9EAC" {flip} flipClue="0····" name="Riko"
                      on:click={modal("Riko's Puzzle", PuzzleRiko)}/>
        <MemberButton color="#27C1B7" {flip} flipClue="··8·" name="Kanan"
                      on:click={modal("Kanan's Puzzle", PuzzleKanan)}/>
        <MemberButton color="#DB0839" {flip} flipClue="··7" name="Dia" on:click={modal("Dia's Puzzle", PuzzleDia)}
                      whiteText/>
        <MemberButton color="#66C0FF" {flip} flipClue="····4" name="You" on:click={modal("You's Puzzle", PuzzleYou)}/>
        <MemberButton color="#C1CAD4" {flip} flipClue="····5·" name="Yoshiko"
                      on:click={modal("Yoshiko's Puzzle", PuzzleYoshiko)}/>
        <MemberButton color="#FFD010" {flip} flipClue="8···" name="Hanamaru"
                      on:click={modal("Hanamaru's Puzzle", PuzzleHanamaru)}/>
        <MemberButton color="#C252C6" {flip} flipClue="·6···" name="Mari"
                      on:click={modal("Mari's Puzzle", PuzzleMari)}/>
        <MemberButton color="#FF6FBE" {flip} flipClue="·1··" name="Ruby" on:click={modal("Ruby's Puzzle", PuzzleRuby)}/>
        <div class="w-full h-8">&nbsp;</div>
        <MemberButton color="#FFBFE0" {flip} flipClue="·7·" name="Ayumu"
                      on:click={modal("Ayumu's Puzzle", PuzzleAyumu)}/>
        <MemberButton color="#F5FF8A" {flip} flipClue="···2··" name="Kasumi"
                      on:click={modal("Kasumi's Puzzle", PuzzleKasumi)}/>
        <MemberButton color="#BBEDFF" {flip} flipClue="0····" name="Shizuku"
                      on:click={modal("Shizuku's Puzzle", PuzzleShizuku)}/>
        <MemberButton color="#4A2FED" {flip} flipClue="··2··" name="Karin"
                      on:click={modal("Karin's Puzzle", PuzzleKarin)}
                      whiteText/>
        <MemberButton color="#FF8246" {flip} flipClue="4··" name="Ai" on:click={modal("Ai's Puzzle", PuzzleAi)}/>
        <MemberButton color="#BE82FF" {flip} flipClue="0····" name="Kanata"
                      on:click={modal("Kanata's Puzzle", PuzzleKanata)}/>
        <MemberButton color="#F60E0E" disabled {flip} flipClue="··9··" name="Setsuna"/>
        <MemberButton color="#B1F69C" disabled {flip} flipClue="·5··" name="Emma"/>
        <MemberButton color="#D0CEE1" disabled {flip} flipClue="···1··" name="Rina"/>
        <MemberButton color="#24BD8B" disabled {flip} flipClue="···7" name="Shioriko"/>
        <MemberButton color="#F1F0E6" disabled {flip} flipClue="·····2" name="Mia"/>
        <MemberButton color="#F8C8C4" disabled {flip} flipClue="·3··" name="Lanzhu"/>
        <MemberButton color="#000" disabled {flip} flipClue="·9·" name="Yu" whiteText/>
        <div class="w-full h-8">&nbsp;</div>
        <MemberButton color="#FF7F27" disabled {flip} flipClue="7·····" name="Kanon"/>
        <MemberButton color="#A0FFF9" disabled {flip} flipClue="·····9·" name="Keke"/>
        <MemberButton color="#FF6E90" disabled {flip} flipClue="··5·" name="Chisato"/>
        <MemberButton color="#74F466" disabled {flip} flipClue="······8" name="Sumire"/>
        <MemberButton color="#0000A0" disabled {flip} flipClue="···3" name="Ren" whiteText/>
        <MemberButton color="#FFF442" disabled {flip} flipClue="·····2" name="Kinako"/>
        <MemberButton color="#FF3535" disabled {flip} flipClue="4····" name="Mei"/>
        <MemberButton color="#B2FFDD" disabled {flip} flipClue="6···" name="Shiki"/>
        <MemberButton color="#FF51C4" {flip} flipClue="·9···" name="Natsumi"
                      on:click={modal("Natsumi's Puzzle", PuzzleNatsumi)}/>
        <div class="w-full my-6 px-2 w-full font-bold flex gap-x-4">
            {#if solved < 40}
                <div class="w-full h-12 rounded-full p-1 uppercase select-none outline outline-[.125rem] outline-offset-[-.125rem] bg-gray-300 outline-gray-300">
                    <div class="w-full rounded-full overflow-hidden relative flex items-center">
                        <div class="absolute left-4 text-black tracking-widest w-[100vw]">{solved} / 40 solved</div>
                        <div class="relative flex-grow-0 h-10 px-2 py-1 tracking-widest flex items-center overflow-hidden"
                             class:bg-primary={solved > 0} style:width={(solved/0.4)+"%"}>
                            <div class="absolute left-4 text-white w-[100vw]">{solved} / 40 solved</div>
                        </div>
                    </div>
                </div>
            {:else if solved === 40}
                <div class="w-full flex flex-col sm:flex-row items-center justify-center rounded-full p-1 uppercase select-none outline outline-[.125rem] outline-offset-[-.125rem] bg-primary outline-primary hover:bg-primary-300"
                     in:fade={{delay: 500, duration: 3000}} on:click={modal("Final Puzzle", PuzzleFinal)}>
                    <div class="w-[90%] rounded-full h-10 px-2 py-1 flex items-center justify-center basis-2/3 tracking-wide sm:tracking-widest bg-white text-primary">
                        Final Puzzle
                    </div>
                    <div class="flex items-center justify-center gap-x-1 text-black basis-1/3 leading-3 px-2 state text-white">
                        {#if $STATES["final"] === undefined}
                            <span class="motion-safe:animate-bounce mt-1 -mb-1 sm:my-0">NEW!</span>
                        {:else}
                            <span class="text-xs">Not Solved</span>
                        {/if}
                    </div>
                </div>
            {:else}
                <div class="basis-2/3 flex flex-col sm:flex-row items-center justify-center rounded-full p-1 uppercase select-none outline outline-[.125rem] outline-offset-[-.125rem] bg-primary outline-primary hover:bg-primary-300 flex-shrink-0"
                     on:click={modal("Final Puzzle", PuzzleFinal)}>
                    <div class="w-[90%] rounded-full h-10 px-2 py-1 flex items-center justify-center basis-2/3 tracking-wide sm:tracking-widest bg-white text-primary">
                        Final Puzzle
                    </div>
                    <div class="flex items-center justify-center gap-x-1 text-black basis-1/3 leading-3 px-2 state text-white">
                        <Correct/> {timeFormat($STATES["final"]?.totalTime ?? 0)}
                    </div>
                </div>
                <div class="basis-1/3 flex flex-col sm:flex-row items-center justify-center rounded-full p-1 uppercase select-none outline outline-[.125rem] outline-offset-[-.125rem] bg-gray-300 outline-gray-300 hover:bg-gray-200 flex-shrink-1 text-sm"
                     on:click={() => flip = !flip}>
                    Toggle Clues
                </div>
            {/if}
        </div>
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

<style lang="postcss">
    @keyframes movebg {
        0% {
            background-position: 0 0;
        }
        100% {
            background-position: 400% 0;
        }
    }

    .thankyou {
        background-image: linear-gradient(to right, red, gold, lawngreen, deepskyblue, violet, red);
        background-size: 50% 100%;
        animation: movebg 20s linear infinite;
    }

    @media (prefers-reduced-motion) {
        .thankyou {
            animation: none;
        }
    }
</style>
<script lang="ts">
    import Checkmark from "$icon/Copied.svelte";
    import Share from "$icon/Share.svelte";
    import isDesktop from "$lib/isDesktop";
    import PageButton from "$lib/styled/PageButton.svelte";
    import {timeFormat} from "$lib/timeFormat";

    export let name: string;
    export let time: number;
    let copied: boolean = false;

    function getShareText(): string {
        return `I solved ${name}'s Puzzle!
My time was: ${timeFormat(time)}! #SIF2PuzzleFes
https://puzzlefes.suyo.be/`;
    }

    function shareResult() {
        const shareText = getShareText();
        if (navigator.share && navigator.canShare({text: shareText}) && !isDesktop()
            // Firefox for Android does not support sharing text via navigator.share
            // There is no way to programmatically check whether a browser supports sharing text via the native share
            // mechanism, so we simply have to remember to manually remove this when it is implemented in Firefox
            && !navigator.userAgent.includes("Firefox")) {
            navigator.share({text: shareText});
        } else {
            // PC browsers usually don't have a native share mechanism - just copy it instead
            navigator.clipboard.writeText(shareText)
                .then(() => {
                    copied = true;
                })
                .catch((err) => {
                    alert("Unable to share or copy your result: " + err);
                });
        }
    }
</script>

<PageButton extraClasses="gap-x-2" label="Share Your Result" on:click={shareResult} type="button">
    {#if copied}
        <Checkmark/>
        <span aria-hidden="true">Copied to your Clipboard</span>
    {:else}
        <Share/>
        <span aria-hidden="true">Share Your Result</span>
    {/if}
</PageButton>
<script>

import { env } from '$env/dynamic/public';
import VideoCardInfo from "./VideoCardInfo.svelte";
import VideoCardWaiting from "./VideoCardWaiting.svelte";
import VideoCardError from "./VideoCardError.svelte";
import {fade} from "svelte/transition";

export let url;
export let card_id;

const fetchInfo = (async () => {
    const response = await fetch(`${env.PUBLIC_API_URL}/api/info`,{
        method: 'POST',
        headers: {
            "Content-type": "application/json",
            "Accept":"application/json"
        },
        body: JSON.stringify({"url":url})
    })
    return await response.json();
})();

</script>

<div class="card" transition:fade>
{#await fetchInfo}

    <VideoCardWaiting />

{:then data}

    {#if !data.detail}
    <VideoCardInfo on:popCard {data} {card_id}/>
    {/if}

{:catch error}

    <VideoCardError on:popCard {error} {card_id}/>
    
{/await}
</div>

<style>
    .card{
        margin-bottom: 1rem;
    }
</style>
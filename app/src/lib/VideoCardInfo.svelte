<script>
    
    import DownloadBar from "./DownloadBar.svelte";
    import {slide} from "svelte/transition";

    import { createEventDispatcher } from "svelte";
    const dispatch = createEventDispatcher();

    let cardOpen = true;

    export let data;
    export let card_id;
    
</script>

<header class="card-header">
	<p class="card-header-title">
        <img class="icon" src="https://{data.site}/favicon.ico" alt="{data.site}">
		{data.title}
	</p>
	<button class="card-header-icon" type="button" on:click={() => cardOpen = !cardOpen}>
		<span class="icon">
			<i class="fas fa-angle-{cardOpen ? 'up' : 'down'}"/>
		</span>
	</button>
    <button class="card-header-icon" type="button" on:click={() => dispatch('popCard',card_id)} >
		<span class="icon">
			<i class="fas fa-close"/>
		</span>
	</button>
</header>

{#if cardOpen}
    <div class="card-content" transition:slide|local>
        <figure class="thumbnail">
            <img src="{data.thumbUrl}" alt="{data.site} video - {data.title}">
        </figure>
        <div class="details">
            <small><a href="{data.url}">{data.url}</a></small>
            <p> {data.title} </p>
        </div>
    </div>
{/if}

<footer class="card-footer">
    <DownloadBar url={data.url} />
</footer>

<style>

    .card-content{
        display: flex;
        flex-direction: row;
        padding: 0.8rem;
    }
    .thumbnail{
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 40%;
        padding-right: 1rem;
    }
    .details {
        width: 60%;
    }

    .card-header-title{
        overflow: hidden hidden;
        white-space: nowrap;        
        text-overflow: '...';
    }

    .thumbnail > img { 
        max-height: 6em;
    }
    .icon{
        display: inline;
        width: 18px;
        height: 16px;
        margin-right: 0.5rem;
    }
    .card-footer{
        display: unset;
    }

</style>
<script>
    export let data;
    import DownloadBar from "./DownloadBar.svelte";
    import {slide} from "svelte/transition";

    let cardOpen = true;

</script>

<div class="card"></div>
<header class="card-header">
	<p class="card-header-title">
        <img class="icon" src="https://{data.site}/favicon.ico" alt="{data.site}">
		{data.title}
	</p>
	<button class="card-header-icon" aria-label="more options" type="button" on:click={() => cardOpen = !cardOpen}>
		<span class="icon">
			<i class="fas fa-angle-{cardOpen ? 'up' : 'down'}" aria-hidden="true" />
		</span>
	</button>
</header>
{#if cardOpen}
<div class="card-content" transition:slide>
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
    }
    .thumbnail{
        width: 40%;
        padding-right: 1rem;
    }
    .details {
        width: 60%;
    }

    .card-header-title{
        text-overflow: ellipsis;
    }

    .thumbnail > img {
        width: 100%;
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
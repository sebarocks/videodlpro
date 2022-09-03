<script>
	import UrlField from '$lib/UrlField.svelte';
	import VideoCard from '$lib/VideoCard.svelte';

	let videos = [];

	function addUrl(ev) {
		console.log(`Se agrego ${ev.detail}`);
		videos = [...videos, ev.detail];
	}
</script>


<main>
	
	<img src="/logo.png" class="logo" alt="YT Logo" />
	<h1 class="title">Video-DL Pro</h1>
	

	<div class="field">
		<UrlField on:addedUrl={addUrl} />
	</div>

	<div class="video-list">
	{#each videos as vidUrl}
		<VideoCard url={vidUrl} />
	{/each}
	</div>

</main>

<style>
	.logo {
		height: 12rem;
		width: 12rem;
		will-change: filter;
	}
	.logo:hover {
		filter: drop-shadow(0 0 2em #12ea85aa);
	}

	h1  {
		padding: 1rem;
		font-size: 2.5rem;
	}

	main {
		display: flex;
		flex-direction: column;
		align-items: center;
		width: 30rem;
	}
	
	.field, .video-list {
		width: 100%;
	}

</style>

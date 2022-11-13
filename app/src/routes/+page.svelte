<script>
	import UrlField from '$lib/UrlField.svelte';
	import VideoCard from '$lib/VideoCard.svelte';

	let videos = [];

	let card_id = 0;

	function addUrl(ev) {
		console.log(`Se agrego url ${ev.detail}`);
		let newVideo = {
			url: ev.detail,
			id: ++card_id
		}
		videos = [newVideo, ...videos];
	}

	function removeVideo(ev){
		console.log(`Se elimino tarjeta ${ev.detail}`);
		videos = videos.filter( vid => vid.id != ev.detail);
	}

</script>


<main>
	
	<img src="/logo.png" class="logo" alt="YT Logo" />
	<h1 class="title">Video-DL Pro</h1>

	<div class="field">
		<UrlField on:addedUrl={addUrl} />
	</div>

	<div class="video-list">
	{#each videos as vid (vid.id)}
		<VideoCard url={vid.url} card_id={vid.id} on:popCard={removeVideo}/>
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

<script>
	import socket from '$lib/downloader.js';
	import { writable } from 'svelte/store';
	import { env } from '$env/dynamic/public';

	const progress = writable(0);

	export let url;

	let status = 'ready';
	var download_id = Date.now();
	let download_filename;
	let intervalQuery;
	let saved = false;

	let progressData = {
		status: 'ready',
		percentage: 0,
		filename: ''
	};

	socket.on(`finished.${download_id}`, (filename) => {
		clearInterval(intervalQuery);
		status = 'complete';
		download_filename = filename;
	});

	socket.on(`progress.${download_id}`, (data) => {
		progressData = data;
		progress.set(data.percentage / 100);
	});

	function askProgress() {
		socket.emit('queryprogress', download_id);
	}

	function requestVideo(ev) {
		status = 'downloading';
		socket.emit('download', {
			url: url,
			download_id: download_id
		});
		askProgress();
		intervalQuery = setInterval(askProgress, 250);
	}

    function requestMp3(ev) {
		status = 'downloading';
		socket.emit('download', {
			url: url,
			download_id: download_id,
            mp3: true
		});
		askProgress();
		intervalQuery = setInterval(askProgress, 250);
	}
</script>

<div class="downloadbar">
	{#if status == 'ready'}
        <div>
            <button class="button is-info" type="button" on:click={requestMp3}>Mp3</button>
            <button class="button is-success" type="button" on:click={requestVideo}>Video</button>            
        </div>
		
	{:else if status == 'downloading'}
		<small class="barinfo">
            {progressData.status}
			{progressData.filename}
			{Math.round(progressData.percentage, 2)}%
        </small>
		<progress class="progress is-success" value={$progress} />

	{:else if status == 'complete'}
		<small class="barinfo">{status} {download_filename}</small>
		<a href={env.PUBLIC_API_URL + '/api/files/' + download_filename} 
            download target="_blank">
            <button class="button" class:is-link={!saved} class:is-light={saved} on:click={()=>saved=true}>
				{#if saved} Guardado {:else} Guardar {/if}
			</button>
        </a>
	{/if}
</div>

<style>
	.downloadbar {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: stretch;
		padding-bottom: 0.5rem;
		padding-top: 0.5rem;
	}
</style>

<script>
import socket from '$lib/downloader.js';
import { writable } from 'svelte/store';
import { env } from '$env/dynamic/public';

const progress = writable(0);

export let url;


let status = "ready";
var download_id = Date.now();
let download_filename;
let intervalQuery;

let progressData = {
    "status":'ready',
    "percentage":0,
    "filename":'',
}

socket.on(`finished.${download_id}`, (filename) => {
    clearInterval(intervalQuery);
    status = "finished";
    download_filename = filename;
});

socket.on(`progress.${download_id}`, (data) => {
    progressData = data;
    progress.set(data.percentage/100);
});


function askProgress() {
    socket.emit('queryprogress', download_id);
}

function requestDownload(ev) {
    status = "downloading";
    socket.emit("download", {
        "url": url,
        "download_id": download_id
    });
    askProgress();
    intervalQuery = setInterval(askProgress,250);        
}
</script>

<div class="downloadbar">
    {#if status == "ready"}
        <button class="button is-success" type="button" on:click={requestDownload}>Download</button>
    {:else if status == "downloading"}
        <small class="barinfo">{progressData.status} {progressData.filename} {Math.round(progressData.percentage,2)}%</small>
        <progress class="progress is-success" value={$progress}></progress>        
    {:else if status == "finished"}
        <small class="barinfo">{status} {download_filename}</small>
        <a href={env.PUBLIC_API_URL +"/api/files/" + download_filename} download target="_blank"><button class="button is-success">Descargar</button></a>
    {/if}
</div>

<style>
.downloadbar{
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: stretch;
}

</style>
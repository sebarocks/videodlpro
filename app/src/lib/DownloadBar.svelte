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
    console.log(`finished ${filename}`);
    clearInterval(intervalQuery);
    status = "finished";
    download_filename = filename;
});

socket.on(`progress.${download_id}`, (data) => {
    //console.log(`progress-${download_id}`);
    progressData = data;
    progress.set(data.percentage/100);
});


function askProgress() {
    socket.emit('queryprogress', download_id);
    //console.log(`queryprogress ${download_id}`);
}

function requestDownload(ev) {
    
    ev.preventDefault();
    status = "downloading";
    socket.emit("download", {
        "url": url,
        "download_id": download_id
    });    
    console.log("request download " + url);
    askProgress();
    intervalQuery = setInterval(askProgress,250);        
}
</script>

<div>
    {#if status == "ready"}
        <button on:click={requestDownload}>Download</button>
    {:else if status == "downloading"}
        <p class="infomini">{progressData.status} {progressData.filename} {Math.round(progressData.percentage,2)}%</p>
        <progress value={$progress}></progress>        
    {:else if status == "finished"}
        <p class="infomini">{status} {download_filename}</p>
        <a href={env.PUBLIC_API_URL +"/api/files/" + download_filename} download target="_blank"><button>Descargar</button></a>
    {/if}
</div>


<style>
    .infomini {
        font-size: 14px;
    }
</style>
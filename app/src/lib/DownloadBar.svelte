<script>
    import io from 'socket.io-client';

    export let url;

    const BASE_URL = 'http://localhost:8000';

    let status = 'ready';
    let download_url;
    
    const socket = io("ws://localhost:8000", {path: "/ws/"});

    socket.on('finished', (filename) => {
        console.log(filename);
        status = 'finished';
        download_url = BASE_URL+'/downloads/'+filename;
    });

    function requestDownload(ev) {
        console.log('request download '+url);
        ev.preventDefault();
        socket.emit('download', url);
        status = 'downloading';
    }

</script>

<div>
{#if status=='ready'}    
<button on:click={requestDownload}>Download</button>

{:else if status=='downloading'}
<p>Downloading...</p>

{:else if status=='finished'}
<p>Finished</p>
<a href="{download_url}" target="_blank"><button>Descargar</button></a>    
{/if}
</div>



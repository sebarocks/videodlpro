<script>
    import io from "socket.io-client";

    export let url;

    const BASE_URL = "http://localhost:8000";

    let status = "ready";
    var download_id = Date.now();
    let saved_url;
    let intervalQuery;

    let progressData = {
        "status":'ready',
        "percentage":0,
        "filename":'',
    }

    const socket = io("ws://localhost:8000", { path: "/ws/" });

    socket.on("finished", (filename) => {
        console.log(filename);
        clearInterval(intervalQuery);
        status = "finished";
        saved_url = BASE_URL + "/downloads/" + filename;
    });

    socket.on("progress", (data) => {
        //console.log(data);
        progressData = data;
    });

    function askProgress() {
        //console.log(download_id);
        socket.emit('queryprogress', download_id);
    }

    function requestDownload(ev) {
        console.log("request download " + url);
        ev.preventDefault();
        socket.emit("download", {
            "url": url,
            "download_id": download_id
        });
        status = "downloading";

        intervalQuery = setInterval(askProgress,250);
    }
</script>

<div>
    {#if status == "ready"}
        <button on:click={requestDownload}>Download</button>
    {:else if status == "downloading"}
        <p class="infomini">{progressData.status} {progressData.filename} {Math.round(progressData.percentage,2)}%</p>
    {:else if status == "finished"}
        <p class="infomini">{progressData.status} {progressData.filename}</p>
        <a href={saved_url} download target="_blank"><button>Descargar</button></a>
    {/if}
</div>


<style>
    .infomini {
        font-size: 14px;
    }
</style>
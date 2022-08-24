<script>
    import io from 'socket.io-client';

    export let url;

    let info = '';
    
    const socket = io("ws://127.0.0.1:8000",
        {
        path: "/ws/"
    });

    socket.on('finished', (data) => {
        console.log(data);
        info = 'finalizado '+ data;
    });

    function requestDownload(ev) {
        ev.preventDefault();
        socket.emit('download', url);
        info = 'downloading...';
    }

</script>

<form action="" on:submit={requestDownload}>
    <p>url: {url}</p>
    <button>Download</button>
    <p>{info}</p>
</form>

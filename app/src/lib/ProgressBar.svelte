<script>
    import io from 'socket.io-client';

    let mensaje = '';
    let chat = '';
    
    const socket = io("ws://127.0.0.1:8000",
        {
        path: "/ws/"
    });

    socket.on('progress', (data) => {chat = data });

    function sendMessage(ev) {
        ev.preventDefault();
        socket.emit('msg', mensaje);
    }

</script>

<form action="" on:submit={sendMessage}>
    <input type="text" autocomplete="off" bind:value={mensaje}/>
    <button>Send</button>
    <p>{chat}</p>
</form>

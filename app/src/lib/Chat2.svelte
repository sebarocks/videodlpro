<script>
    let client_id = Date.now()
    let mensaje = ''
    let chat = []
    let ws = new WebSocket(`ws://localhost:8000/ws/`);

    ws.onmessage = function(event) {
        chat = [...chat, event.data]
    };

    function sendMessage(event) {
        ws.send(mensaje)
        mensaje = ''
        event.preventDefault()
    }
</script>

<h2>WebSocket Chat</h2>
<h3>Your ID: <span id="ws-id">{client_id}</span></h3>
<form action="" on:submit={sendMessage}>
    <input type="text" autocomplete="off" bind:value={mensaje}/>
    <button>Send</button>
</form>
<ul id='messages'>
{#each chat as msg}
    <li>{msg}</li>
{/each}
</ul>



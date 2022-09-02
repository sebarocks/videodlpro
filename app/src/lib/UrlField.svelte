<script>
    import { createEventDispatcher } from "svelte";

    const dispatch = createEventDispatcher();

    let url = "";

    function pasteIt(ev) {
        dispatch("addedUrl", url);
        url = "";
        ev.preventDefault();
    }

    var urlRegex = new RegExp(/^(https?):\/\/[^\s$.?#].[^\s]*$/);
</script>

<p>Ingrese URL del video:</p>
<input  type="text" bind:value={url} />
<button on:click={pasteIt} disabled={!urlRegex.test(url) || url == ""}>Add</button>

<style>
    input {
        width: 70%;
    }
</style>

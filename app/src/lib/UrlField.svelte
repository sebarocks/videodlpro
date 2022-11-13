<script>

    import { createEventDispatcher } from "svelte";

    const dispatch = createEventDispatcher();
    let urlRegex = new RegExp(/^(https?):\/\/[^\s$.?#].[^\s]*$/);
    let url = "";

    $: btnEnabled = !urlRegex.test(url) || url == "";

    function pasteIt(ev) {
        dispatch("addedUrl", url);
        url = "";
    }
    
</script>

<label class="label" for="videourl">Ingrese URL del video:</label>
<div class="control">
    <input class="input" id="videourl" type="text" bind:value={url} />
    <button class="button" type="button" class:is-primary={!btnEnabled} on:click={pasteIt} disabled={btnEnabled}>Agregar</button>
</div>


<style>
.control {
    display: flex;
    flex-direction: row;
    column-gap: 0.5rem;
}

.input {
    flex-grow: 8;
}

.button {
    flex-grow: 2;
}

</style>

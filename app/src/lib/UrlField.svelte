<script>
    import { createEventDispatcher } from 'svelte';

    const dispatch = createEventDispatcher();

    let url = '';

    function pasteIt(ev){
        dispatch('addedUrl',url);
        url = '';
    }

    var urlRegex = new RegExp(/^(https?):\/\/[^\s$.?#].[^\s]*$/);

</script>

<div>
    <label for="urlinput">Ingrese URL del video:</label>
    <input name="urlinput" type="text" bind:value={url}>
    <button disabled={!urlRegex.test(url) || url==''} on:click={pasteIt}>Add</button>
</div>


<style>
    input {
        width: 70%;
    }
</style>
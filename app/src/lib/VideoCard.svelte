<script>
import DownloadBar from "./DownloadBar.svelte";
import { env } from '$env/dynamic/public';

export let url;

const fetchInfo = (async () => {
    const response = await fetch(`${env.PUBLIC_API_URL}/api/info`,{
        method: 'POST',
        headers: {
            "Content-type": "application/json",
            "Accept":"application/json"
        },
        body: JSON.stringify({"url":url})
    })
    return await response.json();
})();

</script>

{#await fetchInfo}
    <p>...Waiting</p>
{:then data}
    {#if !data.detail}
        <div class="card">
            <img class="icon" src="https://{data.site}/favicon.ico" alt="{data.site}">
            <small class="url"><a href="{data.url}">{data.url}</a></small>
            <h3> {data.title} </h3>
            <img src="{data.thumbUrl}" alt="{data.title}">
            <DownloadBar url={data.url} />
        </div>
    {/if}
{:catch error}
	<p class="red">An error occurred! {error}</p>
{/await}

<style>
    img {
        height: 10em;
    }
    .card{
        width: 400px;
        border: solid 1px #747474;
        border-radius: 1%;
        padding: 1rem;
    }
    .icon{
        display: inline;
        width: 18px;
        height: 16px;
    }
    .red{
        color:red;
    }
    .url{
        font-style: italic;
    }
</style>
<script>
  import ProgressBar from "./lib/DownloadBar.svelte";
  import UrlField from "./lib/UrlField.svelte";
  import VideoCard from "./lib/VideoCard.svelte";

  let videos = [];

  function addUrl(ev) {
    console.log(`Se agrego ${ev.detail}`);
    videos = [...videos, ev.detail];
  }
</script>

<main>
  <div>
    <img src="/logo.png" class="logo" alt="YT Logo" />
  </div>
  <h1>Video-DL Pro</h1>

  <div class="urlfield">
    <UrlField on:addedUrl={addUrl} />
  </div>
  {#each videos as vidUrl}
    <VideoCard url={vidUrl} />
  {/each}
</main>

<style>
  .logo {
    height: 10em;
    padding: 0.5em;
    will-change: filter;
  }
  .logo:hover {
    filter: drop-shadow(0 0 2em #12ea85aa);
  }
  .urlfield {
    width: 30rem;
  }
</style>

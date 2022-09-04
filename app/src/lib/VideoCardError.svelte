<script>
	export let error;

  export let card_id;

  import { createEventDispatcher } from "svelte";
  const dispatch = createEventDispatcher();


</script>

<div class="card-content">
	<div class="content">
    <button class="delete" on:click={() => dispatch('popCard',card_id)}></button>
    Ocurrio un error!
    <p class="info"> {error}</p>   
	</div>
</div>

<style>
  .info {
    color: red;
  }
  .delete {
    float: right;
  }
</style>
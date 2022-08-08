<script>
function dropHandler(ev) {
    console.log('File(s) dropped');

    // Prevent default behavior (Prevent file from being opened)
    ev.preventDefault();

    if (ev.dataTransfer.items) {
        // Use DataTransferItemList interface to access the file(s)
        for (let i = 0; i < ev.dataTransfer.items.length; i++) {
        // If dropped items aren't files, reject them
        if (ev.dataTransfer.items[i].kind === 'file') {
            const file = ev.dataTransfer.items[i].getAsFile();
            console.log(`… file[${i}].name = ${file.name}`);
        }
        }
    } else {
        // Use DataTransfer interface to access the file(s)
        for (let i = 0; i < ev.dataTransfer.files.length; i++) {
        console.log(`… file[${i}].name = ${ev.dataTransfer.files[i].name}`);
        }
    }
}

function dragOverHandler(ev) {
  console.log('File(s) in drop zone');

  // Prevent default behavior (Prevent file from being opened)
  ev.preventDefault();
}

</script>


<div id="drop_zone" on:drop={dropHandler} on:dragover={dragOverHandler}>
    <p>Drag one or more files to this <i>drop zone</i>.</p>
</div>

<style>
#drop_zone {
  border: 5px solid blue;
  width:  200px;
  height: 100px;
}
</style>
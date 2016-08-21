<template>
  <div class="content-type-container">
    <div class="content-type">
      <h2 class="title">content-type</h2>
      <p class="subtitles">it works here</p>
    </div>
  </div>
</template>

<script>
import items from '../store'

export default {
  name: 'ItemContentType',

  data: function() {
    return {
      items: items
    };
  }

}
</script>

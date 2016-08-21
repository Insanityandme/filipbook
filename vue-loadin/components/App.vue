<template>
  <div id="wrapper">
    <!-- main view -->
    <router-view
      class="view"
      keep-alive
      transition
      transition-mode="out-in">
    </router-view>
  </div>
</template>
<script>
import items from '../store'

export default {
  name: 'App',

  data: function() {
    return {
      items: items
    }   
  } 
}

</script>

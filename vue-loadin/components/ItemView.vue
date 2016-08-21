<template>
<div>
  <item v-for="item in items" :item="item"></item>
</div>
</template>

<script>
import Item from './Item.vue'

export default {
  name: 'ItemView',

  components: {
    'item': Item,
  }

}
</script>

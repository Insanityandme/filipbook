<template>
  <div class="item">
    <div v-html="content" class="item-content">
      <p>hi</p>
    </div>
  </div>
</template>

<script>
import marked from 'marked'
import items from '../store'

export default { 

  name: 'ItemContentView',

  // first time, only once
  data: function() {
    return {
      content: ""
    };
  },

  route: {
    // gets called each route change
    data: function(transition) {
      var link = transition.to.params.link;

      var item = items
          .filter(function(item) { return item.fields.link == link; })
          .reduce(function(_, n) { return n; });

      var content = marked(item.fields.content);

      return {
        content: content
      }
    }
  }
}
</script>

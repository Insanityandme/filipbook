<template>
  <div class="item-content">
    {{{ content }}}
  </div>
</template>

<script>
export default {

  // first time, only once
  data: function() {
    return {
      content: ""
    }
  },

  route: {
    // gets called each route change
    data: function(transition) {
      const link = transition.to.params.link;
      fetch(`/api/posts/${link}`)
        .then(response => response.json())
        .then(json => {
          this.content = marked(json.content)
          console.log(this.content)
        })
        .catch(e => console.log(e))
    }
  }
}
</script>

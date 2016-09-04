<template>
<div>
  <div class="content-type" v-for="(content_type, objects) in data"> 
    <div class="content-type-container"> 
      <div class="title">{{ objects["title"] }}</div>
      <div class="subtitle">{{ objects["subTitle"] }}</div>
    </div>
    <br>
      
    <div class="item-row" v-for="(categories, items) in objects.categories">
      <p class="category">{{ categories }}</p>
      <a v-for="item in items" class="item-container" href="#!/{{ item.fields.link }}">
          <div class="item image">
              <img class="thumbnail" :src="'/media/'+item.fields.thumbnail" alt="">
              <div class="text-in-a-box">
                <h2 class="title">{{ item.fields.title | uppercase }}</h2>
                <p class="subtitle">{{ item.fields.subtitle }}</p>
              </div>
          </div>
      </a>
      <div class="item-container"></div>
    </div>
    <br>
  </div>
</div>
</template>

<style>
:root {
  --mainColor: red;
}

body {
  background: var(--mainColor);
}
</style>

<script>
export default {

  data: function() {
    return {
      data: {}
    }
  },

  route: {
    data: function(transition) {
      fetch('/api/posts/')
        .then(response => response.json())
        .then(json => {
          var data = json.reduce((acc, next) => {
              const contentType = next.fields.content_type[0]
              const title = next.fields.content_type[0]
              const subTitle = next.fields.content_type[1]
              const category = next.fields.category

              if (!acc[contentType]) {
                  acc[contentType] = {
                    title: title,
                    subTitle: subTitle,
                    categories: {}
                  }
              }
              
              if (!acc[contentType].categories[category]) {
                  acc[contentType].categories[category] = []
              }
              

              acc[contentType].categories[category].push(next)

              return acc
          }, {})
          this.data = data
          window.data = data
        })
        .catch(e => console.log(e))
    }
  }
}
</script>

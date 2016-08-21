import Vue from 'vue'
import Router from 'vue-router'
import marked from 'marked'

const items = JSON.parse(window.items_json);

var App = Vue.extend({});

var ItemContentView = Vue.extend({
  template: '<div v-html="content" class="item-content"></div>',

  // first time, only once
  data: function() {
    return {
      content: ""
    }
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
});


var Item = Vue.extend({
  template:  '<a href="#!/{{ item.fields.link }}">' +
                '<div>' +
                  '<img :src="/item.fields.image">' +
                  '<h2>{{ item.fields.title }}</h2>' +
                  '<p>{{ item.fields.subtitle }}</p>' +
                '</div>' +
              '</a>',

  props: ['item']

});

Vue.component('item', Item);

var ItemView = Vue.extend({
  template: '<div>' +
            '<item v-for="item in items" :item="item"></item>' +
            '</div>',

  data: function(){
    return {
      items: items
    }
  }
});



// Vue config
Vue.config.debug = true; 

// install router
Vue.use(Router);

// routing
var router = new Router();

router.map({

    ':link': {
        component: ItemContentView
    },

    '/': {
      component: ItemView
    }
    
});

router.start(App, '#app');

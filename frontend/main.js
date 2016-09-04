import 'whatwg-fetch';
import Vue from 'vue'
import Router from 'vue-router'
import marked from 'marked'
import App from './components/App.vue'
import IndexView from './components/IndexView.vue'
import ItemContentView from './components/ItemContentView.vue'

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
      component: IndexView
    }
    
});

router.start(App, '#app');

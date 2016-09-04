var cssnext = require('postcss-cssnext');

module.exports = {
  // entry point of our application
  entry: './frontend/main.js',
  // where to place the compiled bundle
  output: {
    path: './mysite/static/js/',
    filename: 'build.js'
  },

  module: {
    loaders: [
      // `loaders` is an array of loaders to use.
      {
        test: /\.js$/,
        exclude: /node_modules/,
        loader: 'babel'
      },
      {
        test: /\.vue$/,  // a regex for matching all files that end in `.vue`
        loader: 'vue'  // loader to use for matched files
      }
    ]
  },

  babel: {
    presets: ['es2015'],
  },
  vue: {
    // use custom postcss plugins in vue components
    postcss: [cssnext],
    // disable vue-loader autoprefixing. 
    // this is a good idea since cssnext comes with it too.
    autoprefixer: false
  }
}

var webpack = require('webpack');

module.exports = {
  entry: './src/main.js',
  output: {
    path: './mysite/static/js/',
    filename: 'build.js'
  },

  module: {
    loaders: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        loader: 'babel'
      }
    ]
  },

  babel: {
    presets: ['es2015'],
    plugins: ['transform-runtime']
  },

}

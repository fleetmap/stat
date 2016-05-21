'use strict';

var ExtractTextPlugin = require("extract-text-webpack-plugin");
var autoprefixer = require('autoprefixer');
var webpack = require('webpack');
module.exports = {
    context: __dirname + '/src',
    entry: {
        'js/app':"./app.js",
        'style/style':"./style/style.scss"
    },
    output: {
        path: __dirname,
        filename: "[name].js"
    },
    resolve:{
      extensions: ['', '.js', '.scss']
    },
    module: {
        loaders: [
            {
                test: /\.js$/,
                loaders: ["react-hot", "babel?presets[]=react,presets[]=es2015,plugins[]=transform-object-rest-spread"]
            },
            {
                test: /\.scss$/,
                loader: ExtractTextPlugin.extract("css!postcss-loader!sass")
            }
        ]
    },
    postcss:[ autoprefixer({browsers: ['last 3 versions']})],
    resolveLoader:{
        modulesDirectories: ['node_modules'],
        moduleTemplates: ['*-loader','*'],
        extensions: ['','.js']
    },
    plugins: [
        new ExtractTextPlugin('[name].css', {allChunks: true})
    ],
    watch: false
    
};
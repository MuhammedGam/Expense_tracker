const path = require('path');

module.exports = {
    mode: 'development',
    entry: './static/script.js',
    output: {
        filename: 'bundle.js',
        path: path.resolve(__dirname, 'static')
    },
    devServer: {
        contentBase: './templates',
        hot: true
    }
};

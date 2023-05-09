const proxy = require('http-proxy-middleware');

module.exports = {
  // ...
  devServer: {
    before: function(app) {
      app.use(
        '/json',
        proxy({
          target: 'http://localhost:5000',
          changeOrigin: true,
        })
      );
    },
  },
};

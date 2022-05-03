const { createProxyMiddleware } = require('http-proxy-middleware');
console.log("Teste proxy");

const proxy = {
    target: 'http://localhost:5000',
    changeOrigin: true
}
module.exports = function(app) {
  app.use(
    '/api',
    createProxyMiddleware(proxy)
  );
};
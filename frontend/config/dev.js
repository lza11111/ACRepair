module.exports = {
  env: {
    NODE_ENV: '"development"'
  },
  defineConstants: {
  },
  weapp: {},
  h5: {
    devServer: {
      proxy: {
        '/api/': {
          target: 'http://localhost:8080/',
          changeOrigin: true,
        }
      }
    }
  },
}

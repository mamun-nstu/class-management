module.exports = {
  transpileDependencies: [
    'vuetify'
  ],
  devServer: {
    proxy: {
      "^/api": {
        target: "http://localhost:8000",
        ws: true,
        changeOrigin: true,
        logLevel: "debug",
      },
      "^/media": {
        target: "http://localhost:8000",
        ws: true,
        changeOrigin: true,
        logLevel: "debug",
      },
    }
  }
}

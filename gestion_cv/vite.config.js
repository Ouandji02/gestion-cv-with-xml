import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import { createProxyMiddleware } from 'http-proxy-middleware';

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    middleware: {
      // configure le middleware de proxy pour toutes les requêtes qui commencent par "/api"
      '/api': createProxyMiddleware({
        target: 'http://localhost:5000',
        changeOrigin: true,
        secure: false,
        pathRewrite: {
          '^/api': '',
        },
      }),
    },
  },
})


// https://vitejs.dev/config/




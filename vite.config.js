import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import path from 'path'
// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  server:{
      '/': {
        target: 'http://localhost:8000',	//实际请求地址
        changeOrigin: true,
        pathRewrite: {
          '^/api': ''
        }
    
  },
  resolve:{
    alias:{
      '@': path.resolve(__dirname,'./src'),
      '@components': path.resolve(__dirname,'./src/components/'),
      '@routers':path.resolve(__dirname,'./src/router'),
    }
  }
}
})

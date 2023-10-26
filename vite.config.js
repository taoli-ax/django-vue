import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

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
    
  }
}
})

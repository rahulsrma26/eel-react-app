import { defineConfig, loadConfigFromFile } from 'vite'
import react from '@vitejs/plugin-react'
import { createHtmlPlugin } from 'vite-plugin-html'

export default defineConfig(async ({ command, mode }) => {

  const config = (await loadConfigFromFile('', './public/config.json'))?.config;
  if (!config) {
    throw new Error('Could not load config.json');
  }

  return {
    plugins: [react(), createHtmlPlugin({
      inject: {
        data: config.app
      }
    })],
    base: '',
    root: 'src',
    publicDir: '../public',
    build: {
      outDir: '../dist'
    },
    server: {
      port: config.vite.port,
    }
  }
})

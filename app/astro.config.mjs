import { defineConfig } from 'astro/config';
import vercel from '@astrojs/vercel';

export default defineConfig({
  output: 'static',
  integrations: [],
  adapter: undefined,
  vite: {
    build: {
      target: 'esnext',
    },
  },
});

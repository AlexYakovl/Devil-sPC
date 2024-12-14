import { createApp } from 'vue';
import App from './App.vue';
import router from './router';

createApp(App)
  .use(router) // Подключаем Vue Router
  .mount('#app'); // Монтируем приложение в элемент с id="app"

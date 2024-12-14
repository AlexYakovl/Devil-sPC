<template>
  <div class="auth">
    <h2>Login / Register</h2>
    <div v-if="isLogin">
      <h3>Login</h3>
      <form @submit.prevent="login">
        <input v-model="username" placeholder="Username" required />
        <input v-model="password" type="password" placeholder="Password" required />
        <button type="submit">Login</button>
      </form>
    </div>

    <div v-else>
      <h3>Register</h3>
      <form @submit.prevent="register">
        <input v-model="username" placeholder="Username" required />
        <input v-model="password" type="password" placeholder="Password" required />
        <button type="submit">Register</button>
      </form>
    </div>

    <button @click="toggleAuthMode">
      Switch to {{ isLogin ? 'Register' : 'Login' }}
    </button>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      username: "",
      password: "",
      isLogin: true,
    };
  },
  methods: {
    async login() {
      try {
        const response = await axios.post("http://localhost:8000/api/token/", {
          username: this.username,
          password: this.password,
        });
        localStorage.setItem("access_token", response.data.access);
        localStorage.setItem("refresh_token", response.data.refresh);
        this.$emit("authenticated", true);
      } catch (error) {
        console.error("Login failed:", error);
      }
    },
    async register() {
      try {
        await axios.post("http://localhost:8000/api/register/", {
          username: this.username,
          password: this.password,
        });
        alert("Registration successful!");
        this.toggleAuthMode();
      } catch (error) {
        console.error("Registration failed:", error);
      }
    },
    toggleAuthMode() {
      this.isLogin = !this.isLogin;
    },
  },
};
</script>

<style scoped>
.auth {
  text-align: center;
  margin-top: 20px;
}
</style>

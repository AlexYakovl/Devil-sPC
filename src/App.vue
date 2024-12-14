<template>
  <div id="app">
    <h1>PC Configurator</h1>
    <auth v-if="!isAuthenticated" @authenticated="isAuthenticated = true" />
    <component-selection v-if="isAuthenticated" @update-selection="updateSelection" />
    <configuration-summary v-if="isAuthenticated" :selectedComponents="selectedComponents" />
  </div>
</template>

<script>
import ComponentSelection from './components/ComponentSelection.vue';
import ConfigurationSummary from './components/ConfigurationSummary.vue';
import Auth from './components/Auth.vue';

export default {
  components: {
    ComponentSelection,
    ConfigurationSummary,
    Auth,
  },
  data() {
    return {
      selectedComponents: {},
      isAuthenticated: localStorage.getItem('access_token') !== null,
    };
  },
  methods: {
    updateSelection(newSelection) {
      this.selectedComponents = newSelection;
    },
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  margin-top: 60px;
}
</style>

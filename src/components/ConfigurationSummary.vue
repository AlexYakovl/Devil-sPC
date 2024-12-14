<template>
  <div class="configuration-summary">
    <h2>Your Configuration</h2>
    <div v-for="(component, index) in selectedComponents" :key="index">
      <p>{{ component }} selected</p>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    selectedComponents: Object,
  },
};
</script>

<style scoped>
.configuration-summary {
  margin-top: 20px;
}
</style>

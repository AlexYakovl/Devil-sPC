<template>
  <div class="component-selection">
    <h2>Select Components</h2>
    <div v-for="(component, index) in components" :key="index">
      <label>{{ component.name }}</label>
      <select v-model="selectedComponents[component.name]" :disabled="component.disabled">
        <option v-for="option in component.options" :key="option.id" :value="option.id">
          {{ option.name }} - {{ option.specifications }}
        </option>
      </select>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      components: [],
      selectedComponents: {},
    };
  },
  created() {
    this.fetchComponents();
  },
  methods: {
    async fetchComponents() {
      try {
        const response = await axios.get("http://localhost:8000/api/cases/");
        this.components.push({ name: "Case", options: response.data });

        const gpuResponse = await axios.get("http://localhost:8000/api/gpus/");
        this.components.push({ name: "GPU", options: gpuResponse.data });

        const cpuResponse = await axios.get("http://localhost:8000/api/cpus/");
        this.components.push({ name: "CPU", options: cpuResponse.data });

        const ramResponse = await axios.get("http://localhost:8000/api/ram/");
        this.components.push({ name: "RAM", options: ramResponse.data });

      } catch (error) {
        console.error("Error fetching components:", error);
      }
    },
  },
  watch: {
    selectedComponents: {
      handler(newValue) {
        this.$emit("update-selection", newValue);
      },
      deep: true,
    },
  },
};
</script>

<style scoped>
.component-selection {
  display: flex;
  flex-direction: column;
}
</style>

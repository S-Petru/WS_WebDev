<script setup>
  import Login from './components/Login.vue'
  import Resgister from './components/Register.vue'
  import Menu from './components/Menu.vue'
  import Highscores from './components/Highscores.vue'
</script>

<template>
  <div v-if="state == 0">
    <Login @changeState="state = $event"></Login>
  </div>

  <div v-else-if="state == 1">
    <Menu></Menu>
  </div>


</template>

<script>
export default {
  components: {
    Login,
    Menu
  },

  data () {
    return {
      state: 0
    }
  }
}
</script>

<style scoped>
</style>

<script setup>
  import Register from './components/Register.vue'
  import Login from './components/Login.vue'
  import LoginNav from './components/LoginNav.vue'
  import Menu from './components/Menu.vue'
  import Highscores from './components/Highscores.vue'
  import MenuNav from './components/MenuNav.vue'
  import PopUp from './components/PopUpLogout.vue'
</script>

<template>

    <div v-if="state == -1">
    <LoginNav @changeState="state = $event"></LoginNav>
    <Register @changeState="state = $event"></Register>
  </div>

  <div v-if="state == 0">
    <LoginNav @changeState="state = $event"></LoginNav>
    <Login @changeState="state = $event"></Login>
  </div>

  <div v-else-if="state == 1">
    <MenuNav  @changeState="state = $event"></MenuNav>
    <Menu></Menu>
    <PopUp></PopUp>
  </div>

  <div v-else-if="state == 2">
    <MenuNav  @changeState="state = $event"></MenuNav>
    <Highscores></Highscores>
    <PopUp></PopUp>
  </div>

</template>

<script>

export default {
  components: {
    Register,
    Login,
    LoginNav,
    Menu,
    Highscores,
    MenuNav
  },

  data () {
    return {
      state: 0
    };
  }
}
</script>

<style scoped>
</style>

<script setup>
  import Register from './components/Register.vue';
  import Login from './components/Login.vue';
  import LoginNav from './components/LoginNav.vue';
  import Menu from './components/Menu.vue';
  import Highscores from './components/Highscores.vue';
  import MenuNav from './components/MenuNav.vue';
  import PopUp from './components/PopUpLogout.vue';

  // import { ref } from 'vue';
</script>

<template>

    <div v-if="state.state == -1">
    <LoginNav @changeState="updatedStateHandler"></LoginNav>
    <Register @changeState="updatedStateHandler"></Register>
  </div>

  <div v-if="state.state == 0">
    <LoginNav @changeState="updatedStateHandler"></LoginNav>
    <Login @changeState="updatedStateHandler"></Login>
  </div>

  <div v-else-if="state.state == 1">
    <Menu  @changeState="updatedStateHandler" @selectedGame="game = $event" @selectedGameID="id = $event"></Menu>
    <div v-if="state.showPopup == true">
      <PopUp @changeState="updatedStateHandler"></PopUp>
    </div>
  </div>

  <!-- Pagina de highscores a fiecarui joc sa aiba state uri diferite?-->

  <div v-else-if="state.state == 2 || state.state == 3 || state.state == 4">
    <MenuNav  @changeState="updatedStateHandler" :name="game" :id="id"></MenuNav>
    <Highscores :id="id"></Highscores>
    <div v-if="state.showPopup == true">
      <PopUp @changeState="updatedStateHandler"></PopUp>
    </div>
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
    MenuNav,
    PopUp
  },

  data () {
    return {
      search: '',

      state: {
        state: 0,
        showPopup: false,
      },

      game: ''
    };
  },

  methods: {
    updatedStateHandler(newState) {
      this.state.state = newState.state;
      this.state.showPopup = newState.showPopup;
    },
  },
};
</script>

<style scoped>
</style>

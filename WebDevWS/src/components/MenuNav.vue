<template>
     <nav>
        <div class="navbar">
            <a href="#" @click = "goToMenu">TinyClip</a>
            <div class="nav-links">
                <a class="current-page" href="#" @click = "goToMenu">Menu</a>
                <a href="#" @click = "goToHighscores">High Scores</a>
                <a href="#" @click = "tryLogOut">Logout</a>
            </div>
        </div>
    </nav>
</template>

<!-- goToLogin() {
    this.$emit('changeState', 0);
},

goToRegister() {
    this.$emit('changeState', -1);
} -->

<script>
    export default {
        name: 'MenuNav',
        methods: {
            goToMenu() {
                this.$emit('changeState', 1);
            },
            tryLogOut() {
                this.$emit('changeState', 0);
            },
            goToHighscores() {
                this.$emit('changeState', 2);
            }
        }
    }
</script>

<style scoped>
.navbar > a {
    text-decoration: none;
    color: rgb(255, 208, 0);
    font-size: 2rem;
    margin: 0;
    align-items: center;
    justify-content: center;
}

.navbar {
    box-sizing: border-box;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
    padding: 0 30px 0 30px;
    background-color: rgb(39, 39, 39);
    height: 5rem;
}

.navbar .nav-links {
    justify-content: space-between;
    margin: 0;
}

.nav-links a {
    text-decoration: none;
    color: rgb(255, 208, 0);
}

.nav-links a:not(:last-of-type) {
    margin-right: 1.5rem;
}

a.current-page {
    border-radius: 0.5rem;
    padding: 0.25rem;
    color: rgb(39, 39, 39);
    background-color: rgb(255, 208, 0);
}
</style>
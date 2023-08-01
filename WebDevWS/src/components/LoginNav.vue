<template>
     <nav>
        <div class="navbar">
            <a href="#" @click = "goToLogin">TinyClip</a>
            <div class="nav-links">
                <a href="#" @click= "goToLogin">Login</a>
                <a href="#" @click= "goToRegister">Register</a>
            </div>
        </div>
    </nav>
</template>

<script>
    export default {
        name: 'LoginNav',
        methods: {
            goToLogin() {
                this.$emit('changeState', {
                    state: 0,
                    showPopup: false,
                });
            },

            goToRegister() {
                this.$emit('changeState', {
                    state: -1,
                    showPopup: false,
                });
            }
        }
    }
</script>

<style>
    nav {
    width: 100%;
}

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

.nav-links a:first-of-type {
    margin-right: 1.5rem;
}
</style>
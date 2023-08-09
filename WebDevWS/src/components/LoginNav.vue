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
                this.$emits('changeState', {
                    state: 0,
                    showPopup: false,
                });
            },

            goToRegister() {
                this.$emits('changeState', {
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
    font-size: 2.5rem;
    font-weight: 500;
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
    font-size: 1.25rem;
    font-weight: 300;
    padding: 1px 4px;
    border-radius: 5px;
    transition: ease-in-out 0.15s;
}

.nav-links a:hover {
    background-color: rgb(255, 208, 0);
    color: rgb(39, 39, 39);
}

.nav-links a:first-of-type {
    margin-right: 1.5rem;
}
</style>
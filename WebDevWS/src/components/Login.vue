<template>
    <div class="content">
        <div class="container">
            <h1>Sign In</h1>
            <label>Username: </label>
            <input type="text" placeholder="Enter Username" id="username">
            <label>Password: </label>
            <input type="password" placeholder="Enter Password" id="password">  
            <p style="color: red;" id="err"></p>
            <button type="button" @click="tryLogIn">Login</button>
            <a href="#">Forgot Password?</a>
        </div>
    </div>
</template>


<script>
    export default {
        name: 'Login',
        methods: {
            tryLogIn() {
                if (document.getElementById('username').value && document.getElementById('password').value) {
                    //document.location.assign("menu.html")
                    this.$emit('changeState', {
                        state: 1,
                        showPopup: false,
                    });
                    this.$emit('username', document.getElementById('username').value)

                } else {
                    document.getElementById('err').textContent = 'Please fill in all fields';
                    setTimeout(() => {
                        document.getElementById('err').textContent = '';
                    }, 1000)
                }
            }
        }
    }
</script>

<style scoped>
.content {
    width: 100vw;
    display: flex;
    justify-content: center;
    align-items: start;
    margin-top: 3rem;
}

.container {
    display: flex;
    flex-direction: column;
    align-items: center;
    background-color: rgb(39, 39, 39);
    color: rgb(255, 208, 0);
    width: 40%;
    padding: 3rem 0;
    border-radius: 5px;
}

.container h1 {
    font-size: 3rem;
    margin: 0;
    font-weight: 400;
    letter-spacing: 1px;
}

.container label {
    font-weight: 400;
    margin-top: 1.5rem;
}

.container input {
    color: white;
    border-color: white;
    width: 50%;
}

button {
    background-color: rgb(255, 208, 0);
    border: none;
    border-radius: 3px;
    color: white;
    width: 30%;
    font-size: 1.25rem;
    padding: 0.25rem;
    margin: 0.75rem 0 0 0;
    transition: ease-in-out 0.25s;
}

button:hover {
    cursor: pointer;
    transform: scale(1.1);
}

input {
    width: 30%;
    padding: 0.5rem;
    margin: 0.75rem 0 0 0;
    border-radius: 3px;
    border: solid 1px black;
}

a {
    text-decoration: none;
    color: rgb(255, 208, 0);
    font-weight: 200;
    margin-top: 1rem;
}

a:hover {
    text-decoration: underline;
}






/* ============ MEDIA 1200 ============ */
@media screen and (max-width: 1200px) {
    .content {
        align-items: start;
        margin-top: 2rem;
    }

    .container {
        width: 70%;
    }  
  }





/* ============ MEDIA 600 ============ */
@media screen and (max-width: 600px) {
    .navbar > a {
        margin: 0;
    }

    .navbar .nav-links {
        margin: 0;
        padding: 0.75rem 0;
    }


    .navbar {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }

    .content {
        align-items: start;
        margin-top: 2rem;
    }

    .container {
        width: 90%;
    }  

    input {
        width: 50%;
    }     
  }
</style>
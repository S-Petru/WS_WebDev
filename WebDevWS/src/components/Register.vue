<template>
    <div class="content">
        <div class="container">
            <h1>Register</h1>
            <!-- <label>Email: </label>
            <input type="text" placeholder="Lasa fara" id="username"> -->
            <label>Username: </label>
            <input v-model="username" placeholder="Choose Username" id="username" />
            <label>Password: </label>
            <input v-model="password" placeholder="Choose Password" type="password" id="password" />
            <p style="color: red;" id="err"></p>
            <p v-if = "registrationStatus" style="color: yellow;">{{ registrationStatus }}</p>
            <button type="button" @click="tryRegister()">Register</button>
        </div>
    </div>
</template>

<script scoped>
    import axios from 'axios'
    export default {
        name: 'Register',
        props: [],
        // mounted() {
        //     this.init()
        // },
         data() {
            return {
                username: '',
                password: '',
                registrationStatus: ''
            };
        },
        methods: {
             async tryRegister() {
                
                if (document.getElementById('username').value && document.getElementById('password').value) {

                    this.username = document.getElementById('username').value
                    this.password = document.getElementById('password').value
                    try {

                        const api = axios.create({
                            baseURL: 'http://127.0.0.1:5000',
                            headers: { 'Content-Type': 'multipart/form-data'
                            },
                            timeout: 10000
                        })

                        const response = await api.post(`/registerUser/${this.username}/${this.password}`);
                        
                        if (response.data === 'Userul exista') {
                            this.registrationStatus = 'User already exists';
                        } else {
                            this.registrationStatus = 'User registered successfully';
                        }
                    } catch (error) {
                        console.error('Err registering user:', error);
                        this.registrationStatus = 'Error registering user';
                    }
                    // const api = axios.create({
                    //     baseURL: 'http://127.0.0.1:5000',
                    //     headers: {
                    //         'Content-Type': 'multipart/form-data'
                    //     },
                    //     timeout: 10000
                    // })
                        
                    //     usrName = String(document.getElementById('username').value)
                    //     passWrd = String(document.getElementById('password').value)

                    //     const response =  await axios.post('/registerUser/' + usrName + '/' + passWrd,
                    //     formData,
                    //     {
                    //         headers: {
                    //             'Content-Type': 'multipart/form-data'
                    //     }
                    //     })
                    //     console.log(response)

                    //     this.$emit('changeState', {
                    //         state: 0,
                    //         showPopup: false,
                    //     });
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
.container label {
    margin-top: 1.5rem;
}

.container input {
    color: white;
    border-color: white;
    width: 50%;
}
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
    letter-spacing: 0.1px;
}

.container label {
    font-weight: 400;
    margin-top: 1.5rem;
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
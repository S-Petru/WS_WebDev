<template>
    <nav>
        <div class="navbar">
                <a href="#"  class="title" @click = "goToMenu">TinyClip</a>
                <input type="text" id="search" placeholder="Search" autocomplete="off" @input = "search()">
                <div class="nav-links">
                    <a href="#" @click = "goToMenu">Menu</a>
                    <a href="#" @click = "goToHighscores">High Scores</a>
                    <v-icon color="rgb(255, 208, 0)">mdi-logout</v-icon>
                    <a href="#" @click = "tryLogOut">Logout</a>
                </div>
            </div>
    </nav>

    <v-container class="container">
        <v-row class="row">
            <v-col class="col" v-for="i in count" :key="i" cols="3" :id="'element' + i" style="display: block;">
                <!-- <v-card class="mx-auto card" max-width="400" height="400"> -->
                <v-card class=" card" @click="selectGame(i)">
                    <v-img :src= "games[i-1].image" class="img" height="200px" cover></v-img>
                    <v-card-title class="card-title">{{ games[i-1].title }}</v-card-title>
                    <v-card-text class="card-description">{{ games[i-1].title }}</v-card-text>
                </v-card>
            </v-col>
        </v-row>
    </v-container>
</template>

<script scoped>
    export default {
        name: "Menu",
        data() {
            return {
                games: [],
                count: 0
            }
        },
        mounted() {
            this.init()
        },
        methods: {
            init () {
                var game1 = {
                    title: 'Balloon Madness',
                    description: '[Description Balloons]',
                    image: 'public/balloons.avif'
                }
                var game2 = {
                    title: 'Endless Runner',
                    description: '[Description Runner]',
                    image: 'public/runner.jpg'
                }
                var game3 = {
                    title: 'Coming Soon',
                    description: '[Description Soon]',
                    image: 'public/comingSoon.jpg'
                }
                this.games.push(game1)
                this.games.push(game2)
                this.games.push(game3)
                this.count = this.games.length

            },
            search() {
                for(var i = 0; i < this.count; i++) {
                    if(this.games[i].title.toLowerCase().includes(document.getElementById("search").value.toLowerCase())) {
                        document.getElementById('element' + (i + 1)).style.display = "block"
                    }else {
                        document.getElementById('element' + (i + 1)).style.display="none"
                    }
                }
            },

            goToMenu() {
                this.$emit('changeState', {
                        state: 1,
                        showPopup: false,
                    });
            },
            tryLogOut() {
                this.$emit('changeState', {
                        state: 1,
                        showPopup: true,
                    });
            },
            goToHighscores() {
                this.$emit('changeState', {
                        state: 2,
                        showPopup: false,
                    });
            },
            selectGame(pos) {
                this.$emit('changeState', {
                    state: 2,
                    showPopup: false,
                });
                this.$emit('selectedGame', this.games[pos-1].title)
            }
        }
    }
</script>

<style scoped>

input {
    border: 1px solid rgb(255, 208, 0);
    border-radius: 0.5rem;
    padding: 0 0.25rem;
    color: white;
    font-weight: 200;
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
    border-radius: 0.5rem;
    padding: 0 0.25rem;
    transition: 0.25s ease;
}
.nav-links a:hover {
    text-decoration: none;
    color: rgb(39, 39, 39);
    background-color: rgb(255, 208, 0);
    transition: 0.25s ease;
}

.nav-links a:not(:last-of-type) {
    margin-right: 1.5rem;
}





.container {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
    margin: 2rem auto;
    padding: 0;
}

.col {
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 0 0.5rem;
    padding: 0;
}

.card {
    width: 300px;
    height: 300px;
}

.v-row {
    display: flex;
    justify-content: center;
    flex: none;
}
.row {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 1rem;
    padding: 0;
    margin: 0;
}



.card {
    box-sizing: border-box;
    border-radius: 0.5rem;
    background-color: rgb(39, 39, 39);
    color: white;
    transition: 0.15s ease;
}

.card:hover {
    transition: transform 0.15s ease;
    transform: scale(1.035);

}


@media screen and (max-width: 1280px) {
    .row {
        grid-template-columns: 1fr 1fr;
    }
}





  @media screen and (max-width: 765px) {
    .navbar input {
        width: 245px;
        height: auto;
    }
    .navbar > a {
        margin: 0;
    }

    .navbar .nav-links {
        margin: 0;
        padding: 0.75rem 0;
    }


    .navbar {
        height: auto;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
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

    .row {
        align-items: center;
        grid-template-columns: 1fr;
    }

  }
</style>
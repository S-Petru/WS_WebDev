<template>
     <div class="container">
        <h3>Your user ID: {{ id }}</h3>
        <table id="scores">
            <tr>
                <th>USERNAME</th>
                <th>H_SCORE</th>
            </tr>
            <tr v-for="i in scores.length" :key="i">
                <td> {{ scores[i-1].user }}</td>
                <td> {{ scores[i-1].score }}</td>
            </tr>
        </table>
    </div>
</template>

<script scoped>
    import axios from 'axios'
    export default {
        name: "HighScores",
        props: ['id', 'user'],
        data(){
            return {
                scores: [],
                // score: Math.floor(Math.random() * (100 - 50 + 1) + 50)
            }
        },

        mounted() {
            this.init()
        },

        methods: {
            async init() {
                // console.log('TEST')
                const api = axios.create({
                    baseURL: 'http://127.0.0.1:5000',
                    headers: {
                        'Content-Type': 'multipart/form-data'
                    },
                    timeout: 10000
                })

                const response = await api.get('/getScoresByGameID/' + this.id)
                console.log(response)
                this.scores = response.data.result
            },


            async updateScores() {
                const formData = new FormData()

                formData.append('game', this.id)
                formData.append('user', this.user)
                formData.append('score', this.score)
                // formData.append('_id', this.)

                var position = -1 // usr doesn't exist
                for (var i = 0; i < this.scores.length; i++) {
                    if (this.user == this.scores[i].user) {
                        if (this.score > this.scores[i].score) {
                            position = i
                        }else {
                            position = -2 // user exists, but score is too low
                        }
                        break
                    }
                }

                if (position == -1) {
                    // POST
                    const response = await axios.post('http://127.0.0.1:5000/addScore',
                    formData,
                    {
                        headers: {
                            'Content-Type': 'multipart/form-data'
                    }
                    })

                    console.log(response)
                    this.scores.push({'game': this.id, 'user': this.user})
                    this.getScore(response.data.id, this.scores.length - 1)
                }else {
                    if (position != -2) {
                        // PUT
                        formData.append('_id', this.scores[position]._id)
                        const response = await axios.put('http://127.0.0.1:5000/addScore',
                    formData,
                    {
                        headers: {
                            'Content-Type': 'multipart/form-data'
                    }
                    })

                    this.getScore(response.data.id, position)
                    }
                }
            },



            async getScore(id, index) {
                const api = axios.create({
                    baseURL: 'http://127.0.0.1:5000',
                    headers: {
                        'Content-Type': 'multipart/form-data'
                    },
                    timeout: 10000
                })

                const response = await api.get('/getScoreById/' + id)
                console.log(response)
                this.scores[index]['score'] = response.data.result
            }
        }
    }

</script>

<style>
    .container {
    display: flex;
    flex-direction: column;
    margin: 3rem 0 0 0;
    display: flex;
    width: 100vw;
    justify-content: center;
    align-items: center;
}

#scores {
    width: 60%;
}

table {
    border-collapse: collapse;
    border-radius: 1em;
    overflow: hidden;
  }

#scores th {
    color: rgb(39, 39, 39);
    background-color: rgb(255, 208, 0);
}

#scores td {
    border-radius: 10px;
}
#scores td, #scores th {
    padding: 0.25rem;
    text-align: center;
}

#scores tr:nth-child(2n) {
    color: white;
    background-color:rgb(39, 39, 39);
}
#scores tr:nth-child(2n+1) {
    color: white;
    background-color:rgb(76, 76, 76);
}

#scores tr:hover {
    opacity: 0.4;
}

@media screen and (max-width: 1200px) {
    #scores {
        width: 80%;
    }
     
  }


@media screen and (max-width: 900px) {
    #scores {
        width: 90%;
    }
     
  }

@media screen and (max-width: 600px) {
    #scores {
        width: 90%;
    }
     
  }
</style>
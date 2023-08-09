<template>
     <div class="container">
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
        props: ['id'],
        data(){
            return {
                scores: []
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
            
            }
        }
    }

</script>

<style>
    .container {
    margin: 3rem 0 0 0;
    display: flex;
    width: 100vw;
    justify-content: center;
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
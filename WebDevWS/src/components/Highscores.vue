<template>
     <div class="container">
        <table id="scores">
            <tr>
                <th>USERNAME</th>
                <th>H_SCORE</th>
            </tr>
            <tr>
                <td>Usr1</td>
                <td>312</td>
            </tr>
    
            <tr>
                <td>Usr2</td>
                <td>56</td>
            </tr>
    
            <tr>
                <td>Usr3</td>
                <td>123</td>
            </tr>
    
            <tr>
                <td>Usr4</td>
                <td>11</td>
            </tr>
    
            <tr>
                <td>Usr5</td>
                <td>11</td>
            </tr>
    
            <tr>
                <td>Usr6</td>
                <td>11</td>
            </tr>
    
            <tr>
                <td>Usr7</td>
                <td>11</td>
            </tr>
        </table>
    </div>
</template>

<script scoped>

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
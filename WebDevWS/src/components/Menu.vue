<template>
    <div class="content">
        <div class="card">
            <div class="img-container to-center">
                <img src="public/runner.jpg" alt="Endless Runner">
            </div>
            <h3>Endless Runner</h3>
            <p>[Description]</p>
        </div>
    
        <div class="card">
            <div class="img-container">
                <img src="public/balloons.avif" alt="Balloons">
            </div>
            <h3>Balloons</h3>
            <p>[Description]</p>
        </div>
    
        <div class="card">
            <div class="img-container">
                <img src="public/comingSoon.jpg" alt="Coming Soon">
            </div>
            <h3>[Coming Soon]</h3>
            <p>[Description]</p>
        </div>
    </div>
</template>

<script scoped>
</script>

<style scoped>
.content {
    margin: 2rem auto;
    width: 90%;
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1rem;
    justify-items: center;
}

.card {
    box-sizing: border-box;
    border-radius: 0.5rem;
    background-color: rgb(39, 39, 39);
    color: white;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    width: 100%;
    padding: 8px 4px ;

    transition: 0.15s ease;
}

.card:hover {
    transition: transform 0.15s ease;
    transform: scale(1.035);

}

.card .img-container {
    width: 90%;
    height: 60%;
}

.img-container img {
    border-radius: 5px;
    width: 100%;
    height: 100%;
    object-fit: cover;   
} 

.to-center img {
    object-position: -30px;
}









/* ============ MEDIA 1400 ============ */
@media screen and (max-width: 1400px) {
    .content {
        grid-template-columns: repeat(2, 1fr);
    }

    .card {
        width: 100%;
        height: 32rem;
        padding: 8px 4px ;
    }
     
  }

  @media screen and (max-width: 970px) {
    .content {
        width: 60%;
        grid-template-columns: repeat(1, 1fr);
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
        width: 90%;
        grid-template-columns: repeat(1, 1fr);
    }
     
  }
</style>
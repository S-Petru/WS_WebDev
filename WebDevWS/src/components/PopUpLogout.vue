<template>
    <div class="popup">
        <div class="popup-inner">
            <slot></slot>
            <h2>Are you sure you want to logout?</h2>
            <div class="choices">
                <h4 class="popup-confirm" @click = "LogOut">Yes</h4>
                <h4 class="popup-close" @click = "ClosePopUp">No</h4>
            </div>
            
        </div>
    </div>
</template>

<script scoped>
export default {
    name: 'PopUp',
    methods: {
        LogOut() {
            this.$emit('changeState', {
                        state: 0,
                        showPopup: false,
                    });
            },
        ClosePopUp() {
            this.$emit('changeState', {
                state: 1,       
                showPopup: false,
            });
        }
    }
}
</script>

<style scoped>
    .popup {
        border-radius: 10px;
        height: 15rem;
        width: 35%;
        background-color: rgb(39, 39, 39);
        border: 1px solid white;
        position: fixed;
        top: 40%;
        left: 50%;
        transform: translate(-50%, -50%);
        padding: 10px;
    }

    .popup-inner {
        display: flex;
        flex-direction: column;
        color: rgb(255, 208, 0);
        justify-content: center;
        align-items: center;
        text-align: center;
    }

    .choices {
        width: 50%;
        display: flex;
        flex-direction: row;
        justify-content: space-between;
    }
    .choices h4 {
        color: rgb(255, 208, 0);
        cursor: pointer;
        width: 30%;
        text-align: center;
    }

    .choices h4:hover {
        border-radius: 0.5rem;
        background-color: rgb(255, 208, 0);
        color: rgb(39, 39, 39);
        cursor: pointer;
    }

    @media screen and (max-width: 1200px) {
        .popup {
        width: 40%;   
        }
    }
    

    @media screen and (max-width: 900px) {
        .popup {
        width: 60%;   
        }
    } 

    @media screen and (max-width: 700px) {
        .popup {
        width: 65%;   
        }
    }   

    @media screen and (max-width: 600px) {
        .popup {
        width: 80%;   
    }   

    }
</style>


function mainMenu() {
    if (document.getElementById("username").value && document.getElementById("password").value) {
        document.location.assign("menu.html")
    } else {
        document.getElementById("err").textContent = "Please fill in all fields";
        setTimeout(() => {
            document.getElementById("err").textContent = "";
        }, 1000)
    }
    document.location.assign("menu.html");
}


function highScores(game) {
    document.location.assign("highScores.html");
}
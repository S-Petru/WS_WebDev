function tryLogIn() {
    if (document.getElementById('username').value && document.getElementById('password').value) {
        document.location.assign("menu.html")
    } else {
        document.getElementById('err').textContent = 'Please fill in all fields';
        setTimeout(() => {
            document.getElementById('err').textContent = '';
        }, 1000)
    }
}

function tryRegister() {
    if (document.getElementById('username').value && document.getElementById('password').value) {
        document.location.assign("login.html")
    } else {
        document.getElementById('err').textContent = 'Please fill in all fields';
        setTimeout(() => {
            document.getElementById('err').textContent = '';
        }, 1000)
    }
}


function logIn() {
    document.location.assign("login.html")
}


function highScores(game) {
    document.location.assign("highScores.html");
}

function logout() {
    // Display the confirmation dialog and store the result (true for OK, false for Cancel)
    var confirmed = window.confirm("Are you sure you want to logout?");

    if (confirmed) {
      // User clicked OK, perform logout
      // Add your logout code here
      alert("Logged out successfully!");
      document.location.assign("login.html")
    } else {
      // User clicked Cancel, do nothing or handle the cancellation
      alert("Logout canceled.");
    }
  }

// function logOut() {
//     let result = confirm("Are you sure you want to logout?");
//     console.log('TEST');
//     if(result) {
//         console.log('YES');
//         document.location.assign('login.html');
//     } else {
//         console.log('Changed my mind');
//     }
// }

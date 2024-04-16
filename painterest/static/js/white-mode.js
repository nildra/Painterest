var isWhiteMode = false;

function whiteMode() {

    isWhiteMode = !isWhiteMode;

    document.querySelector("body").classList.toggle("white-mode");
    document.querySelector(".navbar").classList.toggle("white-mode-navbar");

    document.querySelector(".movie-box").classList.toggle("white-mode-box");
    document.querySelector(".home").classList.toggle("white-mode");

    document.querySelector(".loupe").classList.toggle("white-mode");
    document.querySelector(".profile").classList.toggle("white-mode");

    document.querySelector(".twitterIcon").classList.toggle("white-mode");
    document.querySelector(".fbIcon").classList.toggle("white-mode");
    document.querySelector(".igIcon").classList.toggle("white-mode");
    document.querySelector(".redditIcon").classList.toggle("white-mode");

    if (isWhiteMode) {
        document.querySelector(".loupe").src = "img/loupeNoire52.png";
        document.querySelector(".profile").src = "img/profileNoir64.png";
        document.querySelector(".blur-dialog").style.backgroundColor = "#FFFFFF75"
        document.querySelector(".ham-dialog-blur").style.backgroundColor = "#FFFFFF75"
        document.querySelector(".menuHam").src = "img/hamburgerNoir50.svg";
        document.querySelector(".twitterIcon").src = "img/twitterxNoir50.svg";
        document.querySelector(".fbIcon").src = "img/facebookNoir50.svg";
        document.querySelector(".igIcon").src = "img/instagramNoir50.svg";
        document.querySelector(".redditIcon").src = "img/redditNoir50.svg";
        document.querySelector(".dropdown-content").style.backgroundColor = "#e3dad6"

    }else{
        document.querySelector(".loupe").src = "img/loupeBlanche52.svg";
        document.querySelector(".profile").src = "img/profileBlanc64.png";
        document.querySelector(".blur-dialog").style.backgroundColor = "#2F2F2F75"
        document.querySelector(".ham-dialog-blur").style.backgroundColor = "#2F2F2F75"
        document.querySelector(".menuHam").src = "img/hamburgerBlanc50.svg";
        document.querySelector(".twitterIcon").src = "img/twitterxBlanc50.svg";
        document.querySelector(".fbIcon").src = "img/facebookBlanc50.svg";
        document.querySelector(".igIcon").src = "img/instagramBlanc50.svg";
        document.querySelector(".redditIcon").src = "img/redditBlanc50.svg";
        document.querySelector(".dropdown-content").style.backgroundColor = "#2F2F2F75"
    }

 }
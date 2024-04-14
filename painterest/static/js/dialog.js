function openDialog() {
    console.log("openDialog ");
    var dialog = document.querySelector('.dialog');
    var video = document.querySelector('#video');
    video.currentTime = 0;
    var dialog_blur = document.querySelector('.blur-dialog');
    dialog.show();
    dialog_blur.show();
}

function closeDialog() {
    console.log("close Dialog ");
    var dialog = document.querySelector('.dialog');
    var dialog_blur = document.querySelector('.blur-dialog');    
    var video = document.querySelector('#video');
    video.pause();
    dialog.close()
    dialog_blur.close();
}


function openDialogHam() {
    console.log("openDialog Ham ");
    var dialog = document.querySelector('.ham-dialog-blur');
    var dialog_blur = document.querySelector('.ham-dialog');
    dialog.show();
    dialog_blur.show();
}

function closeDialogHam() {
    console.log("close Dialog Ham");
    var dialog = document.querySelector('.ham-dialog');
    var dialog_blur = document.querySelector('.ham-dialog-blur');    
    dialog.close()
    dialog_blur.close();
}
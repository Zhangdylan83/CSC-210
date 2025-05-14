var partner1 = document.getElementById("partner1")
var partner2 = document.getElementById("partner2")
var partner3 = document.getElementById("partner3")


var images = ['./image/Shanghai.jpg', './image/Company.jpg', './image/Ruizhi.jpg'];
var currentImage = 0; 

function ConfirmLeave(event){
    const confirmLeave = confirm('You are going to leave this website, and you are going to another website, are you sure?');
    if (!confirmLeave) {
        event.preventDefault();
    }
}

function changeImage() {
    currentImage++; 
    if (currentImage >= images.length) {
        currentImage = 0;
    }
    var imgElement = document.querySelector('.sideBySide img'); 
    if (imgElement) {
        imgElement.src = images[currentImage];
    }
}



if (document.getElementById("partner1")) {
    document.getElementById("partner1").addEventListener("click", ConfirmLeave);
}
if (document.getElementById("partner2")) {
    document.getElementById("partner2").addEventListener("click", ConfirmLeave);
}
if (document.getElementById("partner3")) {
    document.getElementById("partner3").addEventListener("click", ConfirmLeave);
}


setInterval(changeImage, 1500);
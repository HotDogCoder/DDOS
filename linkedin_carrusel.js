var carrucel = document.querySelector(".carousel-track")
var lis = carrucel.querySelectorAll("li")

var images = []

lis.forEach(element => {
    let img = element.querySelector("img")
    let src = img.getAttribute("src")
    if (src != null){
        images.push(src)
    }
});

console.log(images)
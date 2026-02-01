let slides = document.querySelectorAll(".slide");
let index = 0;

function showSlide() {
    slides.forEach(s => s.style.display = "none");
    slides[index].style.display = "block";
    index = (index + 1) % slides.length;
}

showSlide();
setInterval(showSlide, 2500);

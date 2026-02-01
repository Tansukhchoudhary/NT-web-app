window.addEventListener("scroll", () => {
    document.querySelectorAll(".parallax-text").forEach(t => {
        t.style.transform = `translateY(${window.scrollY * 0.3}px)`;
    });

    document.querySelectorAll(".parallax-img").forEach(img => {
        img.style.transform =
            `translateY(${window.scrollY * 0.15}px) scale(${1 + window.scrollY / 6000})`;
    });
});

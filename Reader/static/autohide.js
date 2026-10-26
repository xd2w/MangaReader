// Hide the sticky header when scrolling down, show it when scrolling up.
(function () {
    var bar = document.querySelector('.bar');
    if (!bar) return;

    var lastY = window.scrollY;
    var ticking = false;
    var threshold = 8; // ignore tiny scrolls so the bar doesn't flicker

    function update() {
        var y = window.scrollY;
        var delta = y - lastY;

        if (y <= bar.offsetHeight) {
            bar.classList.remove('bar-hidden');   // always show near the top
        } else if (delta > threshold) {
            bar.classList.add('bar-hidden');      // scrolling down
        } else if (delta < -threshold) {
            bar.classList.remove('bar-hidden');   // scrolling up
        } else {
            ticking = false;
            return;                               // too small to count
        }
        lastY = y;
        ticking = false;
    }

    window.addEventListener('scroll', function () {
        if (!ticking) {
            ticking = true;
            window.requestAnimationFrame(update);
        }
    }, { passive: true });

    // Keyboard users tabbing into the header should always see it
    bar.addEventListener('focusin', function () {
        bar.classList.remove('bar-hidden');
    });
})();
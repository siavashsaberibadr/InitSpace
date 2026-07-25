document.addEventListener('DOMContentLoaded', () => {
    // Scroll Reveal Animation
    const reveals = document.querySelectorAll('.card, .section-header');

    const revealOnScroll = () => {
        const windowHeight = window.innerHeight;
        reveals.forEach(element => {
            const elementTop = element.getBoundingClientRect().top;
            const elementVisible = 100;

            if (elementTop < windowHeight - elementVisible) {
                element.classList.add('active');
            }
        });
    };

    // Add reveal class to cards dynamically
    reveals.forEach(el => el.classList.add('reveal'));

    window.addEventListener('scroll', revealOnScroll);
    revealOnScroll(); // Trigger once on load
});

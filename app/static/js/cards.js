// Select all cards
const cards = document.querySelectorAll('.card');

// Loop through each card
cards.forEach(card => {
    card.addEventListener('click', function() {
        const paragraph = this.querySelector('p');

        // Toggle visibility by toggling the 'hidden' class
        if (paragraph.style.display === 'none' || !paragraph.style.display) {
            paragraph.style.display = 'block'; // Show the paragraph
        } else {
            paragraph.style.display = 'none'; // Hide the paragraph
        }
    });
});
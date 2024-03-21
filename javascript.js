document.querySelectorAll('.ver-mas').forEach(function(link) {
    link.addEventListener('click', function(event) {
        event.preventDefault();

        const cardText = this.previousElementSibling;
        cardText.style.webkitLineClamp = 'unset';
        this.style.display = 'none';
        this.nextElementSibling.style.display = 'inline'; // Mostrar el enlace "ver menos"
    });
});

document.querySelectorAll('.ver-menos').forEach(function(link) {
    link.addEventListener('click', function(event) {
        event.preventDefault();

        const cardText = this.previousElementSibling.previousElementSibling; // Accede al elemento card-text
        cardText.style.webkitLineClamp = '8'; // Vuelve a mostrar solo 8 líneas
        this.style.display = 'none';
        this.previousElementSibling.style.display = 'inline'; // Mostrar el enlace "ver más"
    });
});

document.getElementById('boton-personaje').addEventListener('click', () => {
    const personajeSeleccionado = document.querySelector('input[name="personaje"]:checked');
    if (personajeSeleccionado) {
        alert(`Has seleccionado a ${personajeSeleccionado.id}`);
    } else {
        alert('Por favor, selecciona un personaje.');
    }
});
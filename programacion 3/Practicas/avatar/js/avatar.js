document.getElementById('boton-personaje').addEventListener('click', () => {
    const personajeSeleccionado = document.querySelector('input[name="personaje"]:checked');
    if (personajeSeleccionado == aang) {
        alert("Has seleccionado a Aang " );
        var ventanaEmergente = window.open("", "_blank", "width=200,height=200");
        ventanaEmergente.document.write("<img src='/image/aang.jpg' alt='Imagen'>");
    } 
    if(personajeSeleccionado.id){

    }
    else {
        alert('Por favor, selecciona un personaje.');
    }
});

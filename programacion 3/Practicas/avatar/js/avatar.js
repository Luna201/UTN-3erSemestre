function iniciarJuego(){
    let botonPersonajeJugador= document.getElementById("boton-personaje")
    botonPersonajeJugador.addEventListener("click", seleccionarPersonajeJugador)
}
function seleccionarPersonajeJugador(){
    let inputZuko= document.getElementById("zuko")
    let inputKatara= document.getElementById("katara")
    let inputAang= document.getElementById("aang")
    let inputToph= document.getElementById("toph")
    let spanPersonajeJugador= document.getElementById("personaje-jugador")

    if(inputZuko.checked){
        spanPersonajeJugador.innerHTML= "Zuko"
    }else if(inputKatara.checked){
        spanPersonajeJugador.innerHTML= "Katara"
    }else if(inputAang.checked){
        spanPersonajeJugador.innerHTML= "Aang"
    }else if(inputToph.checked){
        spanPersonajeJugador.innerHTML= "Toph"
    }else{
        alert("Selecciona un personaje")
    }
}
window.addEventListener("load", iniciarJuego)
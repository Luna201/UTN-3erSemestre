function iniciarJuego(){
    let botonPersonajeJugador= document.getElementById("boton-personaje")
    botonPersonajeJugador.addEventListener("click", seleccionarPersonajeJugador)
}

function seleccionarPersonajeJugador(){
    console.log('Seleccionar personaje jugador')
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

//Funcion para los números random
function aleatorio(max, min) {
    return Math.floor(Math.random() * (max - min + 1) + min);
}

function eleccion(jugada) {
    let resultado = ""
    if (jugada == 1) {
        resultado = "escudo 🥌"
    } else if (jugada == 2) {
        resultado = "Papel 📋"
    } else if (jugada == 3) {
        resultado = "agua ✂"
    } else {
        resultado = "Mal elegido"
    }
    return resultado
}


//1 sera piedra, 2 papel y 3 tijera
let jugador = 0
let pc = aleatorio(1, 3)
let triunfos = 0
let perdidas = 0

while (triunfos < 3 && perdidas < 3) {
    pc = aleatorio(1, 3)
    jugador = prompt("Elige : 1 piedra, 2 papel, 3 tijera")

    //alert eleccion pc y jugador
    alert("PC elige: " + eleccion(pc))
    alert("Tu eliges: " + eleccion(jugador))

    //Combate
    if (pc == jugador) {
        alert("EMPATE")
    } else if (jugador == 1 && pc == 3) {
        alert("Ganaste")
        triunfos = triunfos + 1
    } else if (jugador == 2 && pc == 1) {
        alert("Ganaste")
        triunfos = triunfos + 1
    } else if (jugador == 3 && pc == 2) {
        alert("Ganaste")
        triunfos = triunfos + 1
    } else {
        alert("Perdiste")
        perdidas = perdidas + 1
    }
}


alert("Ganaste " + triunfos + " veces. Perdiste " + perdidas + " veces.")
//FUNCION= codigo reutilizable, primero se debe declarar. Una funcion puede o no, tener parametros dentro de los parentesis, que
//al ser llamadas seran argumentos. Dentro de la llave esta el CUERPO de la funcion

miFuncion(8,2);     //Hosting: se puede llamar la funcion antes de definirla

function miFuncion(a,b){
    //console.log("Sumamos: "+(a+b));
    return a + b;
}

//Llamamos la función 
miFuncion(5, 4);

let resultado = miFuncion(6, 7);       //creamos una variable llamada resultado
console.log(resultado);

//Declaramos una función de tipo expresión o anónima. Necesita cierre con ;
let x = function(a, b){return a + b};       
resultado= x(5, 6);     //al llamarla se pone la variable y parentesis
console.log(resultado);


//Funciones de tipo Self y Invoking. NO se puede reutilizar
(function(a, b){
    console.log("Ejecutando la función: "+ (a+b))
})(9, 6);


//una funcion puede ser un objeto, con sus propiedades y metodos. Propiedad ARGUMENTS, NO se puede usar fuera de la funcion
console.log(typeof miFuncion);
function miFuncionDos(a,b){
    console.log(arguments.length);
}
miFuncionDos(5, 7, 3, 6);

//To String
var miFuncionTexto= miFuncionDos.toString();
console.log(miFuncionTexto);

//Funciones flecha
// Con let podemos cambiar el valor de la referencia, no con const. No de usa la palabra FUNCTION ni las llaves, solo el simbolo
//de flecha => "operador de flecha". Define el cuerpo de la funcion. NO usa return
const sumarFuncionFlecha= (a, b) => a + b;
resultado= sumarFuncionFlecha(3, 7);        //Asignamos el valor a una variable
console.log(resultado)
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

/*
PARAMETROS: Lista de variables que definimos en una función
ARGUMENTOS: valores que pasamos cuando llamamos una funcion
FUNCIÓN: puede definirse tambien como un objeto, con una propiedad de argumento (arreglo) y toString
NO es necesario qque coincida el nro de argumentos con el nro de parametros

let sumar = function(a= 4, b= 8){
    console.log(arguments[0]);      //muestra el parametro de a
    console.log(arguments[1]);      //muestra el parametro de b
    console.log(arguments[2]);      //muestra nuevo parametro 
    return a + b;
}
resultado= sumar(3, 2, 9);
console.log(resultado);
*/

//agrega un nuevo argumento

let sumar = function(a= 4, b= 8){
    console.log(arguments[0]);      //muestra el parametro de a
    console.log(arguments[1]);      //muestra el parametro de b
    return a + b + arguments[2];      //muestra nuevo parametro
}
resultado= sumar(3, 2, 9);
console.log(resultado);

/*-En js cuando no se usa el tipo Flecha se puede usar Hosting
- Arguments es para arreglos

-Sumar todos los argumentos
*/
let respuesta= sumaTodo(5, 4, 13, 10, 9);
console.log(respuesta);
function sumaTodo(){
    let suma= 0;
    for(let i= 0; i < arguments.length; i++){
        suma += arguments[i]; 
    }
    return suma;
}

// Tipos primitivos
let k = 10;     //variable global, esta fuera de la estructura
function cambiarValor(a){//     Paso por valor, la variable (k) no sufre ningun cambio, solo pasa una copia
    a = 20;     
}
cambiarValor(k);
console.log(k);


//Paso por referencia
//Se tiene que crear un OBJETO, porque a un objeto se pueden agrgar propiedades. La buena practica al crear un objeto es agregarla
//como const

const persona= {    //atributos ->
    nombre: "Juan",
    apellido: "Lepez"
}
console.log(persona);

function cambiarValorObjeto(p1){
    p1.nombre= "Ignacio";
    p1.apellido= "Perez";
}
cambiarValorObjeto(persona);
console.log(persona);

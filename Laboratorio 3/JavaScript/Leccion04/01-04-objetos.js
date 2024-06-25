const { fetchSignInMethodsForEmail, applyActionCode } = require("firebase/auth");

let x= 10;      //Variable de tipo primitiva
console.log(x.length);
console.log('Tipos primitivos');

//Objeto
let persona= {  //propiedades del objeto
    nombre: "Carlos",
    apellido: "Gil",
    email: "cgil@gmail.com",
    edad: 28,
    idioma: 'es',
    get lang(){
        return this.idioma.toUpperCase();      //toUpperCase= convierte todos los caracteres alfabéticos en mayúsculas
    },
    set lang(lang){
        this.idioma= lang.toUpperCase();
    },

    nombreCompleto: function(){     //método o función de Js; como propiedad
        return this.nombre+" "+this.apellido;       //this apunta a un objeto
    },
    get nombreEdad(){       //Método get
        return 'El nombre es: '+this.nombre+', edad:'+this.edad;
    }
    
}
console.log(persona.nombre)
console.log(persona.apellido)
console.log(persona.email)
console.log(persona.edad)
console.log(persona)

console.log(persona.nombreCompleto());  //metodo dentro de un objeto
console.log('Ejecutando con un objeto');

let persona2= new Object(); //Debe crear un nuevo objeto en memoria
persona2.nombre= "Juan";
persona2.direccion= "Salada 14";
persona2.telefono= "123456789";
console.log(persona2.telefono) 
console.log('Creamos un nuevo objeto');

console.log(persona['apellido']);       //Accedemos como si fuera un arreglo
console.log('Usamos el ciclo for in');

//for in
for(propiedad in persona){
    console.log(propiedad)
    console.log(persona[propiedad]);
}

//agregar y eliminar propieades de un objeto
console.log('cambiamos y eliminamos un error')
persona.apellidos= 'Betancud';   //cambiamos dinamicamente el valor de un objeto. NO equivocarse de nombre de propiedad porque se crearia una nueva
delete persona.apellidos;       //Eliminamos el objeto
console.log(persona)


//Distintas formas de imprimir un objeto
//Nro 1: la más sencilla: concatenar cada valor de cada propiedad
console.log('Distintas formas de imprimir un objeto. Forma 1')
console.log(persona.nombre+', '+persona.apellido)

//Nro 2: A través del ciclo for in
console.log('Distintas formas de imprimir un objeto. Forma 2')
for (nombrePropiedad in persona){
    console.log(persona[nombrePropiedad]);
}
    // Nro 3: La función Object.values()
console.log('Distintas formas de imprimir un objeto. Forma 3')
let personaArray= Object.values(persona);
console.log(personaArray);

//Nro 4: Utilizando JSON.stringify
console.log('Distintas formas de imprimir un objeto. Forma 4')
let personaString= JSON.stringify(persona);
console.log(personaString);

//GET= OBTENER
console.log('Comenzamos a utilizar l método get');
console.log(persona.nombreEdad);

//SET= ESTABLECER/MODIFICAR
console.log('Comenzamos con el método get y set para idiomas');
persona.lang= 'en'
console.log(persona.lang);


function Persona3(nombre= 'Luis', apellido, email){     //funcion constructor. Preasignado el nombre(se cambia en este caso)
    this.nombre= nombre;
    this.apellido= apellido;
    this.email= email;
    this.nombreCompleto = function(){
        return this.nombre+' '+this.apellido;
    }
}
let padre= new Persona3('Leo', 'Lopez', 'lopez@gmail.com');     //crea un nuevo objeto
padre.nombre= "Luis"        //es posible modificar
padre.telefono = '3983648';
console.log(padre);
console.log(padre.nombreCompleto());        //Utilizamos la función

let madre= new Persona3('Laura', 'Contrera', 'contrera@gmail.com');
console.log(madre)
console.log(madre.telefono); //La propiedad no esta definida
console.log(madre.nombreCompleto())


//Diferentes formas de crear objetos
//Caso objeto 1:
let miObjeto = new Object();        // Esta es una opción formal

//Caso objeto 2:
let miObjeto2 = {};         //Esta opción es breve y recomendada

//Caso String 1:
let miCadena1 = new String('Hola');     // Sintaxis formal

//Caso String 2:
let miCadena2 = 'Hola';     // Esta es la sintaxis simplificada y recomendada

//Caso con números 1
let miNumero1 = new Number(1);      //Formal, no recomendable

//Caso con números 2
let miNumero2 = 1; //Sintaxis recomendada

//Caso boleano 1
let miBolean1 = new Boolean(false);         //Formal

//Caso boleano 2
let miBolean2 = false;      //Sintaxis recomendada

//Caso arreglos 1
let miArreglo1 = new Array();       //Formal

//Caso arreglos 2
let miArreglo2 = [];        //Sintaxis recomendada

//Caso function 1
let miFunction1 =  new function(){};        //Todo despues de new es considerado objeto

//Caso function 2
let miFunction2 = function(){};     // Notación simplificada y recomendad

//Uso de prototype      modifica a persona3 y por ende a objeto padre y madre
Persona3.prototype.telefono = '02457095874980';
console.log(padre);
console.log(madre.telefono);
madre.telefono = '0274589345'       //modificación del nro de telefono objeto madre

//Uso de CALL: utiliza un método de otro objeto
let persona4 = {
    nombre: 'Juan',
    apellido: 'Perez',
    nombreCompleto2: function(titulo, telefono){
        return titulo+': '+this.nombre+ ' '+this.apellido+' '+telefono;
        //return this.nombre+' '+this.apellido;
    }
}

let persona5 ={
    nombre: 'Carlos',
    apellido: 'Lara'
}
console.log(persona4.nombreCompleto2('Lic.', '9245387690'));
console.log(persona4.nombreCompleto2.call(persona5, ' Ing.', '4237865934'));

 
//Método APPLY: Lee el arreglo y lo asigna como argumentos. a diferencia de call se debe crear un arreglo
let arreglo = ['Ing.', '984235989']
console.log(persona4.nombreCompleto2.apply(persona5, arreglo)); 

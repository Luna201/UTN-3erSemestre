let x= 10;      //Variable de tipo primitiva
console.log(x.length);
console.log('Tipos primitivos');

//Objeto
let persona= {  //propiedades del objeto
    nombre: "Carlos",
    apellido: "Gil",
    email: "cgil@gmail.com",
    edad: 30,

    nombreCompleto: function(){     //método o función de Js; como propiedad
        return this.nombre+" "+this.apellido;       //this apunta a un objeto
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
let x= 10;      //Variable de tipo primitiva
console.log(x.length);

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

let persona2= new Object(); //Debe crear un nuevo objeto en memoria
persona2.nombre= "Juan";
persona2.direccion= "Salada 14";
persona2.telefono= "123456789";
console.log(persona2.telefono) 
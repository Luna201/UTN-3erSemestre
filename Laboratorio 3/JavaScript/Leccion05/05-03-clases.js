// let persona3= new Persona('Carla', 'Ponce');  NO es posible declarar un objeto antes de la clase con hoisting
//primero se crea la clase y despues los objetos, con constructor y objetos

class Persona{  //Clase padre
    constructor(nombre, apellido){
        this._nombre = nombre;
        this._apellido = apellido;
    }

    get nombre(){
        return this._nombre;
    }
    set nombre(nombre){
        this._nombre= nombre;
    }

    get apellido(){
        return this._apellido;
    }
    set apellido(apellido){
        this._apellido= apellido;
    }

    nombreCompleto(){
        return this._nombre+' '+this._apellido;
    }

}

class Empleado extends Persona{     //Clase hija
    constructor(nombre, apellido, departamento){        //van todos los parametros, de clase padre e hija
        super(nombre, apellido);        //se debe colocar super para obtener el constructor de la clase padre
        this._departamento= departamento;
    }

    get departamento(){     //OBTENER
        return this_departamento;
    }
    set departamento(departamento){
        this._departamento= departamento;
    }
    //sobreescritura
    nombreCompleto(){       //Debe ser el mismo nombre y parametro para ser una sobreescritura
        //return this._nombre+' '+this._apellido+', '+this._departamento; O TAMBIEN
        return super.nombreCompleto()+', '+this._departamento;
    }

}

let persona1 = new Persona('Martin', 'Perez');
console.log(persona1.nombre)
persona1.nombre= 'Juan Carlos';
persona1.apellido= 'Sanz';
console.log(persona1)
//console.log(persona1);

let persona2 = new Persona('Carlos', 'Lara');
console.log(persona2.nombre)
persona2.nombre= 'Maria Laura';
persona2.apellido= 'Diaz';
console.log(persona2)
//console.log(persona2);


let empleado1= new Empleado('Maria', ' Gimenez', 'Sistemas');
console.log(empleado1);
console.log(empleado1.nombreCompleto());        //herencia de metodo para acceder a la clase padre



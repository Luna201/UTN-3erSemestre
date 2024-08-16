// let persona3= new Persona('Carla', 'Ponce');  NO es posible declarar un objeto antes de la clase con hoisting
//primero se crea la clase y despues los objetos, con constructor y objetos

class Persona{  //Clase padre

    static contadorPersonas= 0;   //Atributo estático. Se accede desde las CLASES
    //email= 'Valor default email';       //Atributo NO estático. Se accede desde los OBJETOS

    constructor(nombre, apellido){
        this._nombre = nombre;
        this._apellido = apellido;
        this.idPersona= ++Persona.contadorPersonas;
        console.log('Se incrementa el contador: '+Persona.contadorObjetosPersona);
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
        return this.idPersona+' '+this._nombre+' '+this._apellido;
    }

    toString(){     //Regresa un String. Sobreescribe el método de la clase padre (object)
        //Se aplica el polimorfismo (Multiples formas en tiempo de ejecución)
        //El método que se ejecuta depende si es una referencia de la clase padre o hija
        return this.nombreCompleto();
    }

    static saludar(){       //un metodo static se asocia con una clase no con un objeto
                            //solo se observa en la consola, no en quokka
                            //se puede usar desde la clase hgija y con objetos de la clase hija
        console.log('Saludos desde este método static');
    }
    static saludar2(persona){
        console.log(persona.nombre+' '+persona.apellido);
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

//Object.prototype.toString    :La clase Object permite trabajar con atributos y métodos como toString   
console.log(empleado1.toString());      //ejecuta el método de la clase hija
console.log(persona1.toString());       //ejecuta el método de la clase padre

//persona1.saludar();   :NO se utiliza desde el objeto, sino desde la clase
Persona.saludar();
Persona.saludar2(persona1);

Empleado.saludar();
Empleado.saludar2(empleado1);

//console.log(persona1.contadorObjetosPersona);
console.log(Persona.contadorPersona);
console.log(Empleado.contadorPersona);   //se puede usar con clases tanto padre como hija

console.log(persona1.email);
console.log(empleado1.email);
//console.log(Persona.email)        //NO se puede acceder desde la clase
console.log(persona1.toString());
console.log(persona2.toString());
console.log(empleado1.toString());
console.log(Persona.contadorPersonas);
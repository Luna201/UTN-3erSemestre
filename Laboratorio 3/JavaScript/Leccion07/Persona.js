class Persona{ 

    static contadorPersonas = 0;

    constructor(nombre, apellido, edad){
        this._idPersona = ++Persona.contadorPersonas;
        this._nombre = nombre;
        this._apellido = apellido;
        this._edad = edad;
    }
    get idPersona(){
        return this._idPersona;
    }

    get nombre(){
        this._nombre;
    }
    
    set nombre(nombre){
        this._nombre = this.nombre;
    }

    get apellido(){
        this._apellido;
    }
    
    set apellido(apellido){
        this._apellido = this.apellido;
    }

    get edad(){
        this._edad;
    }
    
    set edad(edad){
        this._edad = this.edad;
    }

    toString(){
        // return this._idPersona+' '+this_nombre+' '+this._apellido+' '+this._edad; O TAMBIEN
        return `
        ${this._idPersona}
        ${this._nombre}
        ${this._apellido}
        ${this._edad}`;
    }

}
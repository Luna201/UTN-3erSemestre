package domain;
public class Persona {
    private final int idPersona;
    private static int contadorPersona;
    
    static {    //Bloque de inicialización estático
        System.out.println("Ejecución bloque estático");
        ++Persona.contadorPersona;  //no es necesario poner el nombre de la clase Persona
        //idPersona = 10;   NO es un atributo estático, por eso da error. No se puede usar this
    }
    {//Bloque de inicialización NO estático( o contexto dinamico)
        System.out.println("Ejercución del bloque NO estático");
        this.idPersona = Persona.contadorPersona++; //Incrementamos el atributo
    }
    //Los bloques de inicialización se ejecutan antes del constructor
    public Persona(){   //constructor
        System.out.println("Esta es la ejecución del constructor");
    }
    public int getIdPersona (){
        return this.idPersona;
    }

    @Override
    public String toString() {
        return "Persona{" + "idPersona=" + idPersona + '}';
    }
    
}

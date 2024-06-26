package test;
import domain.Persona;

public class TestForEach {      //ciclo FOR mejorado
    public static void main(String[] args) {
        int edades[] = {5, 6, 8, 9};    //sintaxis resumida
        //for (int i = 0; i < edades.length; i++){
        for (int edad: edades){ //Sintaxis del ForEach
            System.out.println("edad= "+ edad);
        }
        
        Persona personas[]= {new Persona("Juan"), new Persona("Carla"), new Persona("Beatriz")};
        
        //ForEach
        for(Persona persona: personas){
            System.out.println("persona = "+ persona);
        }
    }
}

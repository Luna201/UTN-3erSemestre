package mundoPc;

import ar.com.system2023.mundopc.*;     //*para importar todo

public class mundoPC {
    public static void main(String[] args) {
        Monitor monitorHP= new Monitor("HP", 13);   //importar la clase
        Teclado tecladoHP= new Teclado("Bluetooth", "HP");
        Raton ratonHP= new Raton("Bluetooth", "HP");
        Computadora computadoraHP= new Computadora("Computadora HP", monitorHP, tecladoHP, ratonHP);
        
        Monitor monitorGamer= new Monitor("HP", 32);   //importar la clase
        Teclado tecladoGamer= new Teclado("Bluetooth", "Gamer");
        Raton ratonGamer= new Raton("Bluetooth", "Gamer");
        Computadora computadoraGamer= new Computadora("Computadora Gamer", monitorGamer, tecladoGamer, ratonGamer);
    }
   
}

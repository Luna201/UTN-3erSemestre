package mundoPc;

import ar.com.system2023.mundopc.*;     //*para importar todo

public class mundoPC {
    public static void main(String[] args) {
        Monitor monitorHP= new Monitor("HP", 13);   //importar la clase
        Teclado tecladoHP= new Teclado("Bluetooth", "HP");
        Raton ratonHP= new Raton("Bluetooth", "HP");
        Computadora computadoraHP= new Computadora("Computadora HP", monitorHP, tecladoHP, ratonHP);
        
        Monitor monitorGamer= new Monitor("LG", 32);   //importar la clase
        Teclado tecladoGamer= new Teclado("Bluetooth", "Gamer");
        Raton ratonGamer= new Raton("Bluetooth", "Gamer");
        Computadora computadoraGamer= new Computadora("Computadora Gamer", monitorGamer, tecladoGamer, ratonGamer);
        Orden orden1= new Orden();  //Inicializamos el arreglo vacio
        
        Orden orden2= new Orden();  //Una nueva lista para el objeto orden2
        Orden orden3= new Orden();  //Una nueva lista para el objeto orden3
        Orden orden4= new Orden();  //Una nueva lista para el objeto orden4
        
        orden1.agregarComputadora(computadoraHP);
        orden1.agregarComputadora(computadoraGamer);
        
        Computadora computadoraVarias= new Computadora("Computadoras de diferentes marcas",monitorHP, tecladoGamer, ratonHP);
        orden2.agregarComputadora(computadoraVarias);
        
        Computadora computadoraVarias1= new Computadora("Equipo variado 1",monitorHP, tecladoGamer, ratonHP);
        orden3.agregarComputadora(computadoraVarias1);
        
        Computadora computadoraVarias2= new Computadora("Equipo variado 2",monitorGamer, tecladoHP, ratonGamer);
        orden4.agregarComputadora(computadoraVarias2);
        
        orden1.mostrarOrden();
        orden2.mostrarOrden();
        orden3.mostrarOrden();
        orden4.mostrarOrden();
    }
   
}

package test;
import Enumeraciones.Dias;

public class TestEnumeraciones {
    public static void main(String[] args) {
        System.out.println("Dia 1: "+Dias.MONDAY);
        indicarDiaSemana(Dias.MONDAY);    //LAS ENUMERACIONES SE TRATAN COMO CADENAS
        //AHORA NO SE DEBEN UTILIZAR COMILLAS, SE ACCEDE A TRAVÉS DEL OPERADOR DE PUNTO
    }
    private static void indicarDiaSemana(Dias dias){
        switch(dias){
            case MONDAY:
                System.out.println("Primer dia de la semana");
                break;
            case TUESDAY:
                System.out.println("Segundo dia de la semana");
                break;
            case WEDNESDAY:
                System.out.println("Tercer  dia de la semana");
                break;
            case THURSDAY:
                System.out.println("Cuarto  dia de la semana");
                break;
            case FRIDAY:
                System.out.println("Quinto  dia de la semana");
                break;
            case SATURDAY:
                System.out.println("Sexto  dia de la semana");
                break;
            case SUNDAY:
                System.out.println("Septimo  dia de la semana");
                break;
        }
    }
}

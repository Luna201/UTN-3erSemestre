package test;
import Enumeraciones.Continentes;
import Enumeraciones.Dias;

public class TestEnumeraciones {
    public static void main(String[] args) {
        //System.out.println("Dia 1: "+Dias.MONDAY);
        //indicarDiaSemana(Dias.MONDAY);    //LAS ENUMERACIONES SE TRATAN COMO CADENAS
        //AHORA NO SE DEBEN UTILIZAR COMILLAS, SE ACCEDE A TRAVÉS DEL OPERADOR DE PUNTO
 
        System.out.println("Continente Nro. 1: "+Continentes.AFRICA);
        System.out.println("Nro de paises en el 1er continente: "+Continentes.AFRICA.getPaises());
        System.out.println("Nro. de habitantes en el 1er continente: : "+Continentes.AFRICA.getHabitantes());
        
        System.out.println("Continente Nro. 2: "+Continentes.EUROPA);
        System.out.println("Nro de paises en el 2do continente: "+Continentes.EUROPA.getPaises());
        System.out.println("Nro. de habitantes en el 2do continente: : "+Continentes.EUROPA.getHabitantes());
        
        System.out.println("Continente Nro. 3: "+Continentes.ASIA);
        System.out.println("Nro de paises en el 3ro continente: "+Continentes.ASIA.getPaises());
        System.out.println("Nro. de habitantes en el 3ro continente: : "+Continentes.ASIA.getHabitantes());
        
        System.out.println("Continente Nro. 4: "+Continentes.AMERICA);
        System.out.println("Nro de paises en el 4to continente: "+Continentes.AMERICA.getPaises());
        System.out.println("Nro. de habitantes en el 4to continente: : "+Continentes.AMERICA.getHabitantes());
        
        System.out.println("Continente Nro. 5: "+Continentes.OCEANIA);
        System.out.println("Nro de paises en el 5to continente: "+Continentes.OCEANIA.getPaises());
        System.out.println("Nro. de habitantes en el 5to continente: : "+Continentes.OCEANIA.getHabitantes());        
        
        
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

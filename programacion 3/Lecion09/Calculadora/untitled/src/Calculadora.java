import java.sql.SQLOutput;
import java.util.Scanner;

public class Calculadora {

    public static void main(String[] args) {
        Scanner entrada= new Scanner(System.in);
        while (true){   //Ciclo infinito
            System.out.println("********* Aplicación calculadora *********");
            mostrarMenu();

            try {
                var operacion= Integer.parseInt(entrada.nextLine());
                if (operacion >= 1 && operacion <= 4) {

                    ejecutarOperacion(operacion, entrada);

                }//Fin del if
                else if (operacion == 5) {
                    System.out.println("Hasta pronto");
                    break;  //Rompe el ciclo
                } else {
                    System.out.println("Opción erronea: " + operacion);
                }
                //Imprimimos un salto de linea antes de repetir el menú
                System.out.println();
            }catch (Exception e){   //Fin try, comienzo del catch
                System.out.println("Ocurrio un error: "+e.getMessage());
                System.out.println();
            }
        }//Fin while
    }//Fin main

    private  static void mostrarMenu() {
        //mostramos el manú
        System.out.println("""
                    1. Suma
                    2. Resta
                    3. Multiplicación
                    4. División
                    5. Salir
                    """);
        System.out.print("¿Operación a realizar?");
    }   // Fin metodo mostarMenu

    private static void ejecutarOperacion(int operacion, Scanner entrada){
        System.out.print("Digite el valor para el operando1: ");
        var operando1 = Double.parseDouble(entrada.nextLine());
        System.out.print("Digite el valor para el operando2: ");
        var operando2 = Double.parseDouble(entrada.nextLine());
        double resultado;
        switch (operacion) {
            case 1 -> {
                resultado = operando1 + operando2;
                System.out.println("El resultado de la suma: " + resultado);
            }
            case 2 -> {
                resultado = operando1 - operando2;
                System.out.println("El resultado de la resta: " + resultado);
            }
            case 3 -> {
                resultado = operando1 * operando2;
                System.out.println("El resultado de la multiplicación: " + resultado);
            }
            case 4 -> {
                resultado = operando1 / operando2;
                System.out.println("El resultado de la división: " + resultado);
            }
            default -> System.out.println("Opción erronea: " + operacion);
        }//Finn switch
    }   //Fin metodo ejecutar operaciones
}//Fin clase
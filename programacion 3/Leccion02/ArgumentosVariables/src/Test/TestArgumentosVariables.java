package Test;
public class TestArgumentosVariables {
    public static void main(String[] args) {
        
    }
    
    private static void imprimirNumeros(int ...numeros){    //los 3 puntos son para argumentos variables, son indefinidos
        for (int i = 0; i < numeros.length; i++){//leigth es el arreglo
            System.out.println("");
        }
    }
}

package Test;
public class TestArgumentosVariables {
    public static void main(String[] args) {
        imprimirNumeros(3,4,5);
        imprimirNumeros(1,2);
        variosParametros("Juan","Perez", 7,8,9);
    }
    
    private static void variosParametros(String nombre,String apellido, int ...numeros){    //siempre va ultimo losparametros int
        System.out.println("Nombre: "+nombre+", Apellido: "+apellido);
        imprimirNumeros(numeros);
    }
    
    private static void imprimirNumeros(int ...numeros){    //los 3 puntos son para argumentos variables, son indefinidos
        for (int i = 0; i < numeros.length; i++){//leigth es el arreglo
            System.out.println("Elementos: "+numeros[i]);
        }
    }
}

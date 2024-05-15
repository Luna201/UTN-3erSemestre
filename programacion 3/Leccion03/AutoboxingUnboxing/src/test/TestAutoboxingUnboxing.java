package test;
public class TestAutoboxingUnboxing {
    public static void main(String[] args) {
        //Clases envolventes o Wrapper
        /*
        Clase envolentes de tipos primitivos
        int = la clase envolvente es Integer
        (integer es una lase que nos permite cceder a atributos y metodos,
        entero ya no es una variable primitiva, sino un objeto de la clase integer)
        long= la clase envolvente es Long
        float= la clase envolvente es Float
        double= la clase envolvente es Double
        boolean= la clase envolvente es Boolean
        byte= la clase envolvente es Byte
        char= la clase envolvente es Character
        short= la clase envolvente es Short
        */
        int enteroPrim= 10;     //Tipo primitivo
        System.out.println("entero "+enteroPrim);
        Integer entero = 10;    //Tipo objet con la clase Integer
        System.out.println("entero= "+entero); //nro entero
        System.out.println("entero= "+ entero.toString());  //to string, convierte 10 en cadena
        System.out.println("entero= "+ entero.doubleValue());   //Autoboxing, con el punto podemos convertir a distintas opciones
        
        int entero2= entero;    //Unboxing. Convierte un objeto en un primitivo
        System.out.println("entero2= "+entero2);
    }
}

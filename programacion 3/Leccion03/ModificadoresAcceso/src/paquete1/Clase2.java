package paquete1;
class Clase2 extends Clase1{      //sin modificador, esta en default. La clase hija debe estar en el mismo paquete
    String atributoDefault= "Valor del atributo default";
    
    //Clase2(){
    //    System.out.println("Contructor default");
    //}
    
    public Clase2(){
        super();
        this.atributoDefault= "Modificación del atributo default";
        System.out.println("atributoDefault = " + this.atributoDefault);
        this.metodoDefault();
    }
    
    void metodoDefault(){
        System.out.println("Método default");
    }
}

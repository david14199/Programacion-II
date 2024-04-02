/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package arreglos;
import java.util.Scanner;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
/**
 *
 * @author User
 */
//profesor faltan algunos puntos por que no encontre forma de hacerlo con mi version de java
//no encontramos ninguna documentacion adecuada
public class Arreglos {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // Punto Uno
        int vacio[];
        //Punto 2
      int lista[] = {1,2,3,4,5};
        //Punto 3
        System.out.println("la lista tiene:"+lista.length+"datos");
      //Punto 4
        System.out.println("El primer valor de la lista es:"+lista[0]);
        int fina=lista.length;
        System.out.println("El ultimo valor de la lista  es:"+lista[fina-1]);
      //Punto 5
      String datos[]={"jose","19","180","soltero","649946"};
      for (int i = 0;i<datos.length;i++){
          System.out.println(datos[i]);
        }
      
      //Punto 6
      String empresas[]={"Facebook","Google","Microsoft","Apple","IBM","Oracle","amazon"};
      for (int i = 0;i<empresas.length;i++){
          System.out.println(empresas[i]);
        }
    //Punto 7
      Scanner t=new Scanner(System.in);
      String nueva;
           
      System.out.println("ingrese una empresa para añadir a la lista");
      nueva=t.next();
   //Punto 8
   String busca;
        System.out.println("ingrese el dato a buscar");
        busca=t.next();
        
    //Punto 9  
        System.out.println("El valor  esta en la lista ? ");
  Arrays.sort(empresas);
   for (int i = 0;i<empresas.length;i++){
          System.out.println(empresas[i]);
        }
   //Punto 10
   
   
   //Punto 11
   
   
   //Punto 12
}}

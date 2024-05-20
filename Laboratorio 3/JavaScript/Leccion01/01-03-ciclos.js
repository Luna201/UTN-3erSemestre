//while (mientras)
let contador = 0;
while(contador < 3){
    console.log(contador)
    contador++;
}
console.log("Fin del ciclo while");

//do while 
let conteo = 0;
do{
    console.log(conteo)
    conteo++;       //++ Operador Unario, de post incremento
}while(conteo < 3);
console.log("Fin del ciclo do while");

//For
for(let contando= 0; contando < 3; contando++){
    console.log(contando);
}   console.log("Fin del ciclo for");


//Palabra reservada break
for(let contando = 0; contando <= 10; contando++){
    if(contando % 2 == 0){
        //console.log(contando)   // Muestra todos los pares
        console.log(contando)   // Muestra el primer nro par
        break;
    }
}
console.log("Muestra el primer nro par");

//La palabra continue
for(let contando = 0; contando <= 10; contando++){
    if(contando % 2 !== 0){
        continue;   // Ir a la siguiente iteración 
    }
    console.log(contando);
}
console.log("Termina el ciclo");

let lista = []
let topp = -1
console.log('hola')

let counter = 0;

function setTopping(product) {
    console.log(product)
    console.log('hola dentro de funcion')
    if (product == "1 topping"){
        topp = 1;
    }
    else if (product == "2 toppings"){
        topp = 2;
    }
    else if (product == "3 toppings "){
        topp = 3;
    }
    else{
        topp = 0
    }
    return topp
}

function prueba(){
    return True
}

const vehiculos = [
    {nombre: "carro", ruedas: true, alas: false, velociad: 150, tipo : "terrestre"},
    {nombre: "avion", ruedas: true, alas: true, velociad: 500, tipo: "aereo"},
    {nombre: "mula", ruedas: true, alas: false, velociad: 80, tipo : "terrestre"},
    {nombre: "barco", ruedas: false, alas: false, velociad: 120, tipo : "acuatico"},
    {nombre: "moto", ruedas: true, alas: false, velociad: 250, tipo : "terrestre"},
]

// nombre de la propiedad/cosa que se desea buscar, es igual buscar en la lista (vehiculos.find()) 
// el atributo o propiedad con la cual se desea filtrar para encontrar su determinado valor en la lista (atributo => atributo.tipo === "acuatico")
const {ruedas} = vehiculos.find(atributo => atributo.tipo === "acuatico")

console.log(ruedas)

//de la lista (vehiculos), se itera por medio del metodo (forEach), en donde se escoge cada (vehicle) y se imprime este mismo (console.log(vehicle))

vehiculos.forEach(vehicle => console.log(vehicle))

//


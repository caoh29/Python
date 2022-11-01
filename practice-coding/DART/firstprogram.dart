void main() {
  // se define la lista
  var ages = [33, 15, 27, 40, 22];
  // se ordena de forma alfabetica
  ages.sort();
  
  // se crea un loop que suma cada elemento dentro de la lista
  var sum = 0;
  int long = ages.length;
  for (var i = 0; i < long; i++) 
  {
  sum = ages[i] + sum;
  }

  // Se crea la variable promedio 
  var prom = (sum)/(long);
  
  // Se imprime el codigo
  print("La edad menor es: ${ages[0]}");
  print("La edad mayor es: ${ages[long-1]}");
  print("La edad promedio es: $prom");
}

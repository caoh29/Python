void main() {
  // se define la lista
  var ages = [33, 15, 27, 40, 22];
  // se ordena de forma alfabetica
  ages.sort();
  
  // 
  var sum = 0;
  for (var i = 0; i < ages.length; i++) 
  {
  sum = ages[i] + sum;
  }
  var prom = (sum)/(ages.length);
  int lenght = ages.length;
  print("La edad menor es: ${ages[0]}");
  print("La edad mayor es: ${ages[lenght-1]}");
  print("La edad promedio es: $prom");
}

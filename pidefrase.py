cadena = raw_input('Escribe una frase: ')
while cadena != 'q':
  cambios = 0
  for i in range(1, len(cadena)):
    if cadena[i] == ' ' and cadena[i-1] != ' ':
      cambios = cambios + 1
 
  if cadena[-1] == ' ':
    cambios = cambios - 1
 
  palabras = cambios + 1
  print 'Palabras:', palabras

  print """q""", "para salir"
 
  cadena = raw_input('Escribe una frase: ')
  

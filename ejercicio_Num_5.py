def ejercicio_num_5 ():

   def vali_number(valor):
      try: 
         if(int(valor) and int(valor) >= 1):
            return True
      except ValueError:
         return False

   def primeri_mascercano(primeri_mascercano):
         lista_str = primeri_mascercano
         lista = [int(i) for i in lista_str]

         primero = lista[0]
         cercano_prim = lista[1]
         for i in lista[2:]:

               if (i - primero) < (cercano_prim - primero):
                  cercano_prim = i
         
         print ("El más cercano es", cercano_prim)
         

   boot = ""
   print("<<------------------------------------------>>")
   print("<<------------Ejercicio Numero 5------------>>")
   print("<<------------------------------------------>> \n")

   datos_numeros = []
   rango = [10]

   for i in range(rango[0]):
      while True:
            datos_base = input("Ingresa numero " + str(i+1) +  " : ")      
            if vali_number(datos_base) == False:
               print("El dato introducido no es un entero :-( Verifica..")
            elif vali_number(datos_base):
               datos_numeros.append(int(datos_base))
               break
   print ()
   print ("-----------------------------")
   primeri_mascercano(datos_numeros)
   print ("-----------------------------")
   print ()
   print ()
   print ("----------------------------------------------------------------------")
   print("Lista : -> ", datos_numeros)
   print ("----------------------------------------------------------------------")
   print ()
ejercicio_num_5 ()
import matematica
import geometria
import estatistica
print("Escolha qual ramo da matematica vamos trabalhar:\n")
print("1 - Aritmética")
print("2 - Geometria")
print("3 - Estatística")
Y = input("")
if Y == '1':
 print("Escolha qual tipo de operação você quer fazer:\n")
 print("1 - Soma")
 print("2 - Subtração")
 print("3 - Multiplicação")
 print("4 - Divisão")
 print("5 - Porcentagem")
 print("6 - Potencia")
 print("7 - Raiz Quadrada\n")
 X = input("")
 if X == "1":
    X2 = int(input("Escolha o primeiro numero para a soma: "))
    X3 = int(input("\nEscolha o segundo numero para a soma: "))
    print(f"\nresultado:",+matematica.soma(X2,X3))
 elif X == "2":
    X2 = int(input("Escolha o primeiro numero para a subtração: "))
    X3 = int(input("\nEscolha o segundo numero para a subtração:"))
    print(f"\nresultado:",+matematica.subtracao(X2,X3))
 elif X == "3":
    X2 = int(input("Escolha o primeiro numero para a multiplicação: "))
    X3 = int(input("\nEscolha o segundo numero para a multiplicação: "))
    print(f"\nresultado:",+matematica.multiplicacao(X2,X3))
 elif X == "4":
    X2 = int(input("Escolha o primeiro numero para a divisão: "))
    X3 = int(input("\nEscolha o segundo numero para a divisão: "))
    print(f"\nresultado:",+matematica.divisao(X2,X3))
 elif X == "5":
    X2 = int(input("Escolha o numero que você vai tirar a porcentagem: "))
    X3 = int(input("\nEscolha a porcentagem: "))
    print(f"\nresultado:",+matematica.porcentagem(X2,X3))
 elif X == "6":
    X2 = int(input("Escolha o primeiro numero para tirar a potencia: "))
    X3 = int(input("\nEscolha o seggundo numero para tirar a potencia: "))
    print(f"\nresultado:",+matematica.potencia(X2,X3))
 elif X == "7":
    X2 = int(input("Escolha o numero para tirar a raiz: "))
    print(f"\nresultado:",+matematica.raiz(X2))
if Y == '2':
   print("Escolha qual calculo você quer fazer:\n")
   print("1 - Área")
   print("2 - Volume")
   print("3 - Perímetro\n")
   X0 = input("")
   if X0 == '1':
      print("Agora escolha qual forma geometrica você quer:\n")
      print("1 - Triângulo")
      print("2 - Quadrado")
      print("3 - Retângulo")
      print("4 - Círculo")
      print("5 - Trapézio\n")
      X1 = input("")
      if X1 == '1':
        b = int(input("Diga o tamanho da base do triângulo em cm: "))
        a = int(input("Diga o tamanho da altura do triângulo em cm: "))
        print("\nresultado:",geometria.areatriangulo(b,a),"cm²")
      elif X1 == '2':
        l = int(input("Diga o tamanho dos lados do quadrado em cm: "))
        print("\nresultado:",geometria.areaquadrado(l),"cm²")
      elif X1 == '3':
        b2 = int(input("Diga o tamanho da base do retângulo em cm: "))
        a2 = int(input("Diga o tamanho da altura do retângulo em cm: "))
        print("\nresultado:",geometria.arearetangulo(b2,a2),"cm²")
      elif X1 == '4':
        r = int(input("Diga o tamanho do raio do circulo em cm: "))
        print("\nresultado:",geometria.areacirculo(r),"cm²")
      elif X1 == '5':
        b3 = int(input("Diga o tamanho da base menor do trapézio em cm: "))
        B = int(input("Diga o tamanho da base maior do trapézio em cm: "))
        a3 = int(input("Diga o tamanho da altura do trapézio em cm: "))
        print("\nresultado:",geometria.areatrapezio(B,b3,a3),"cm²")
   elif X0 == '2':
      print("Agora escolha qual solido geometrico você quer:\n")
      print("1 - Prisma de Base Triangular")
      print("2 - Cubo")
      print("3 - Paralelepípedo")
      print("4 - Cilindro")
      print("5 - Prisma de Base Trapézio\n")
      X1 = input("")
      if X1 == '1':
        b = int(input("Diga o tamanho da base do triângulo em cm: "))
        a = int(input("Diga o tamanho da altura do triângulo em cm: "))
        A = int(input("Diga o tamanho da altura do prisma em cm: "))
        print("\nresultado:",geometria.volumepiramide(b,a,A),"cm³")
      elif X1 == '2':
        l = int(input("Diga o tamanho dos lados do cubo em cm: "))
        print("\nresultado:",geometria.volumecubo(l),"cm³")
      elif X1 == '3':
        c = int(input("Diga o tamanho do comprimento do paralelepípedo em cm: "))
        l = int(input("Diga o tamanho da largura do paralelepípedo em cm: "))
        a = int(input("Diga o tamanho da altura do paralelepípedo em cm: "))
        print("\nresultado:",geometria.volumeparalele(c,l,a),"cm³")
      elif X1 == '4':
        r = int(input("Diga o tamanho do raio da base do cilindro em cm: "))
        a = int(input("Diga o tamanho da altura do cilindro em cm: "))
        print("\nresultado:",geometria.volumecilindro(r,a),"cm³")
      elif X1 == '5':
        B = int(input("Diga o tamanho da base maior do trapézio em cm: "))
        b = int(input("Diga o tamanho da base menor trapézio em cm: "))
        a = int(input("Diga o tamanho da altura do trapézio em cm: "))
        A = int(input("Diga o tamanho da altura do prisma em cm: "))
        print("\nresultado:",geometria.volumeprisma(B,b,a,A),"cm³")

   elif X0 == '3':
      print("Agora escolha qual forma geometrica você quer:\n")
      print("1 - Triângulo")
      print("2 - Quadrado")
      print("3 - Retângulo")
      print("4 - Círculo")
      print("5 - Trapézio\n")
      X1 = input("")
      if X1 == '1':
        l1 = int(input("Diga o tamanho de um dos lados do triângulo em cm: "))
        l2 = int(input("Diga o tamanho de outro dos lados do triângulo em cm: "))
        l3 = int(input("Diga o tamanho do ultimo lado do triângulo em cm: "))
        print("\nresultado:",geometria.perimetrotriangulo(l1,l2,l3),"cm²")
      elif X1 == '2':
        l = int(input("Diga o tamanho dos lados do quadrado em cm: "))
        print("\nresultado:",geometria.perimetroquadrado(l),"cm²")
      elif X1 == '3':
        c = int(input("Diga o comprimento do retangulo em cm: "))
        l = int(input("Diga a largura do retangulo em cm: "))
        print("\nresultado:",geometria.perimetroretangulo(c,l),"cm²")
      elif X1 == '4':
        r = int(input("Diga o tamanho do raio do circulo em cm: "))
        print("\nresultado:",geometria.perimetrocirculo(r),"cm²")
      elif X1 == '5':
        B = int(input("Diga o tamanho da base maior do trapézio em cm: "))
        b = int(input("Diga o tamanho da base menor do trapézio em cm: "))
        l1 = int(input("Diga o tamanho de um dos lados do trapézio em cm: "))
        l2 = int(input("Diga o tamanho do outro lado não paralelo ao primeiro do trapézio em em cm: "))
        print("\nresultado:",geometria.perimetrotrapezio(B,b,l1,l2),"cm²")
if Y == '3':
  print("Escolha qual tipo de cálculos estatisticos você quer fazer:\n")
  print("1 - Média Aritmética")
  print("2 - Moda")
  x = input("")
  if x == '1':
    print('Escolha em ate 10 numeros, se você quizer parar mais cedo digite "0"')
    C = int(input("Escolha o primeiro numero: "))
    D = int(input("Escolha o segundo numero: "))
    if D == 0:
      print("A sua media foi de",estatistica.mediana(C,0,0,0,0,0,0,0,0,0,1))
    else :
      E = int(input("Escolha o terceiro numero: "))
      if E == 0:
       print("A sua media foi de",estatistica.mediana(C,D,0,0,0,0,0,0,0,0,2))
      else :
        F = int(input("Escolha o terceiro numero: "))
      if F == 0:
       print("A sua media foi de",estatistica.mediana(C,D,E,0,0,0,0,0,0,0,3))
      else :
        G = int(input("Escolha o terceiro numero: "))
      if G == 0:
       print("A sua media foi de",estatistica.mediana(C,D,E,F,0,0,0,0,0,0,4))
      else :
        H = int(input("Escolha o terceiro numero: "))

        if H == 0:
         print("A sua media foi de",estatistica.mediana(C,D,E,F,G,0,0,0,0,0,5))
        else :
         I = int(input("Escolha o terceiro numero: "))
         if I == 0:
          print("A sua media foi de",estatistica.mediana(C,D,E,F,G,H,0,0,0,0,6))
         else :
          J = int(input("Escolha o terceiro numero: "))
          if J == 0:
           print("A sua media foi de",estatistica.mediana(C,D,E,F,G,H,I,0,0,0,7))
          else :
           K = int(input("Escolha o terceiro numero: "))
           if K == 0:
             print("A sua media foi de",estatistica.mediana(C,D,E,F,G,H,I,J,0,0,8))
           else :
            L = int(input("Escolha o terceiro numero: "))
           if L == 0:
            print("A sua media foi de",estatistica.mediana(C,D,E,F,G,H,I,J,K,0,9))
           else :
            M = int(input("Escolha o terceiro numero: "))
           print("A sua media foi de",estatistica.mediana(C,D,E,F,G,H,I,J,K,L,10))
  if x == '2':
     entrada = input("Digite números separados por espaço: ")

     sequencia = list(map(int, entrada.split()))

  resultado = estatistica.moda(sequencia)
  print(resultado)

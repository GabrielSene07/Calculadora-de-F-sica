import math
print ("Teste de número 3 para um programa de equações de física.")
esc=int(input("Pressione 1 se deseja utilizar o programa de equações, 2 se deseja usar o programa de conversão e 3 para encontrar variáveis:\n"))
if (esc==1):
    print ("Pressione o número 1 para usar a equação do espaço em função do tempo.")
    print ("Pressione o número 2 para usar a equação da velocidade em função do tempo.")
    print ("Pressione o número 3 para usar Torricelli.")
    print ("Pressione o número 4 para usar a equação da velocidade uniforme.")
    print ("Pressione o número 5 para descobrir a variação de espaço")
    print ("Pressione o número 6 para descobrir a variação de tempo")
    print ("Pressione o número 7 para descobrir a aceleração")
    eq=int(input("Qual deseja usar?\n"))
    match (eq):
        case 1:
        
            s0=float(input("Informe o espaço inicial:\n")) 
            ue=str(input("Informe a unidade referente ao espaço:\n"))
            v0=float(input("Informe a velocidade inicial:\n"))
            t=float(input("Informe o tempo (se não souber, use a equação de número 6 antes):\n"))
            a=float(input("Informe a aceleração (se não souber, use a equação de número 7):\n"))
            S=s0+v0*t+(a*t**2)/2
            print(f"O resultado final é {S}{ue}\n")
        
        case 2:
    
            v0=float(input("Informe a velocidade inicial:\n"))
            uv=str(input("Informe a unidade da velocidade:\n"))
            a=float(input("Informe a aceleração (se não souber, utilize a equação de número 7):\n"))
            t=float(input("Informe o tempo (se não souber, utilize a equação de número 6):\n"))
            V=v0+(a*t)
            print(f"A velocidade obtida é {V}{uv}\n")
            
        case 3:
        
            v0=float(input("Informe a velocidade inicial:\n"))
            uv=str(input("Informe a unidade da velocidade:\n"))
            a=float(input("Informe a aceleração (se não souber utilize a equação de número 7):\n"))
            vs=float(input("Informe a variação do espaço (se não souber utilize a equação de número 5):\n"))
            V=math.sqrt((v0**2)*a*vs)
            print (f"A velocidade obtida é {V}{uv}\n")
            
        case 4:
    
            uv=str(input("Informe a unidade da velocidade:\n"))
            sf=float(input("Informe o espaço final:\n"))
            s0=float(input("Informe o espaço inicial:\n"))
            tf=float(input("Informe o tempo final:\n"))
            t0=float(input("Informe o tempo inicial:\n"))
            V=(sf-s0)/(tf-t0)
            print(f"A velocidade obtida é {V}{uv}\n")
            
        case 5:
        
            s0=float(input("Informe o espaço inicial:\n"))
            sf=float(input("Informe o espaço final:\n"))
            ue=str(input("Informe a unidade do espaço:\n"))
            S=sf-s0
            print(f"A variação do espaço é {S}{ue}\n")
            
        case 6:
        
            t0=float(input("Informe o tempo inicial:\n"))
            tf=float(input("Informe o tempo final:\n"))
            ut=str(input("Informe a unidade do tempo:\n"))
            t=tf-t0
            print ("O tempo obtido é {t}{ut}\n")
            
        case 7:
        
            v0=float(input("Informe a velocidade inicial:\n"))
            vf=float(input("Informe a velocidade final:\n"))
            t0=float(input("Informe o tempo inicial:\n"))
            tf=float(input("Informe o tempo final:\n"))
            ua=str(input("Informe a unidade da aceleração (pode digitar ms2):\n"))
            a=(vf-v0)/(tf-t0)
            print (f"A aceleração obtida é {a}{ua}\n")
elif (esc==2): 
    con=int(input("Digite 1 para converter de km/h para m/s, e digite 2 para converter de m/s para km/h:\n"))
    match (con):
        case 1:
            km=float(input("Digite a velocidade em km/h:\n"))
            ms=km/3.6
            print(f"A velocidade obtida é {ms}m/s\n")
            
        case 2: 
            ms=float(input("Digite a velocidade em m/s:\n"))
            km=ms*3.6
            print(f"A velocidade obtida é {km}km/h\n")
elif (esc==3):
    print ("Digite 1 para encontrar o tempo com a equação da velocidade em função do tempo.")
    print ("Digite 2 para encontrar a aceleração com a equação da velocidade uniforme em função do tempo.")
    print ("Digite 3 para encontrar a velocidade inicial com a equação da velocidade uniforme em função do tempo.")
    print ("Digite 4 para encontrar o espaço inicial com a equação do espaço em função do tempo.")
    print ("Digite 5 para encontrar a velocidade inicial com a equação do espaço em função do tempo.")
    print ("Digite 6 para encontrar a variação de espaço com a equação de Torricelli.")
    print ("Digite 7 para encontrar a velocidade inicial com a equação de Torricelli.")
    print ("Digite 8 para encontrar a aceleração com a equação de Torriceli.")
    print ("Digite 9 para encontrar a variação de tempo com a equação do movimento uniforme.")
    print ("Digite 10 para encontrar a velocidade com a equação do movimento uniforme.")
    print ("Digite 11 para encontrar o espaço inicial com a equação do movimento uniforme.")
    enc=int(input("Qual delas deseja usar?\n"))
    match (enc):
        case 1:
            V=float(input("Digite a velocidade final:\n"))
            V0=float(input("Digite a velocidade inicial:\n"))
            a=float(input("Digite a aceleração:\n"))
            ut=str(input("Digite a unidade do tempo:\n"))
            t=(V-V0)/a
            print (f"O tempo encontrado é de {t}{ut}\n")
        case 2:
            V=float(input("Digite a velocidade final:\n"))
            V0=float(input("Digite a velocidade inicial:\n"))
            t=float(input("Digite o tempo:\n"))
            ua=str(input("Digite a unidade da aceleração:\n"))
            a=(V-V0)/t
            print(f"A aceleração encontrada é de {a}{ua}\n")
        case 4:
            V=float(input("Digite a velocidade final:\n"))
            a=float(input("Digite a aceleração:\n"))
            t=float(input("Digite o tempo:\n"))
            uv=str(input("Digite a unidade da velocidade:\n"))
            V0=V-a*t
            print (f"A velocidade inicial encontrada é de {V0}{uv}\n")
        case 4:
            S=float(input("Digite o espaço final:\n"))
            V0=float(input("Digite a velocidade inicial:\n"))
            t=float(input("Digite o tempo:\n"))
            a=float(input("Digite a aceleração:\n"))
            ue=str(input("Digite a unidade do espaço:\n"))
            S0= S-(V0*t+a*(t**2)/ 2)
            print(f"O espaço inicial encontrado é de {S0}{ue}\n")
        case 5:
            S=float(input("Digite o espaço final:\n"))
            S0=float(input("Digite o espaço inicial:\n"))
            t=float(input("Digite o tempo:\n"))
            a=float(input("Digite a aceleração:\n"))  
            uv=str(input("Digite a unidade da velocidade:\n"))
            V0=(S-(S0+(a*t**2)/ 2))/t
            print(f"A velocidade inicial encontrada é de {V0}{uv}\n")
        case 6:
            V=float(input("Digite a velocidade final:\n"))
            V0=float(input("Digite a velocidade inicial:\n"))
            a=float(input("Digite a aceleração:\n"))
            ue=str(input("Digite a unidade do espaço:\n"))
            vs=(V**2-V0**2)/(2*a)
            print (f"A variação do espaço é de {vs}{ue}\n")
        case 7:
            V=float(input("Digite a velocidade final:\n"))
            a=float(input("Digite a aceleração:\n"))
            vs=float(input("Digite a variação do espaço:\n"))
            uv=str(input("Digite a unidade da velocidade:\n"))
            V0=math.sqrt(V**2+(2*a*vs))
            print(f"A velocidade inicial encontrada é de {V0}{uv}\n")
        case 8:
            V=float(input("Digite a velocidade final:\n"))
            V0=float(input("Digite a velocidade inicial:\n"))
            vs=float(input("Digite a variação do espaço:\n"))
            ua=str(input("Digite a unidade da aceleração:\n"))
            a=(V**2-V0**2)/(2*vs)
            print(f"A aceleração encontrada foi de {a}{ua}\n")
        case 9:
            S=float(input("Digite o espaço final:\n"))
            S0=float(input("Digite o espaço inicial:\n"))
            V=float(input("Digite a velocidade:\n"))
            ut=str(input("Digite a unidade do tempo:\n"))
            t=(S-S0)/V
            print(f"O tempo encontrado é de {t}{ut}\n")
        case 10:
            S=float(input("Digite o espaço final:\n"))
            S0=float(input("Digite o espaço inicial:\n"))
            t=float(input("Digite o tempo:\n"))
            uv=float(input("Digite a unidade da velocidade:\n"))
            V=(S-S0)/t
            print(f"A velocidade obtida é de {V}{uv}\n")
        case 11:
            S=float(input("Digite o espaço final:\n"))
            V=float(input("Digite a velocide:\n"))
            t=float(input("Digite o tempo:\n"))
            ue=str(input("Digite a unidade do espaço:\n"))
            S0=S-V*t
            print(f"O espaço inicial encontrado é de {S0}{ue}\n")
else:
    print ("Digite uma opção válida.")
print ("Obrigado por participar do teste preliminar, sua contribuição é muito importante.")

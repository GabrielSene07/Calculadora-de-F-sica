import math
print ("Teste de número 2 para um programa de equações de física.")
esc=int(input("Pressione 1 se deseja utilizar o programa de equações, e 2 se deseja usar o programa de conversão:"))
if (esc==1):
    print ("Pressione o número 1 para usar a equação do espaço em função do tempo.")
    print ("Pressione o número 2 para usar a equação da velocidade em função do tempo.")
    print ("Pressione o número 3 para usar Torricelli.")
    print ("Pressione o número 4 para usar a equação da velocidade uniforme.")
    print ("Pressione o número 5 para descobrir a variação de espaço")
    print ("Pressione o número 6 para descobrir a variação de tempo")
    print ("Pressione o número 7 para descobrir a aceleração")
    eq=int(input("Qual deseja usar?"))
    match (eq):
        case 1:
        
            s0=float(input("Informe o espaço inicial:")) 
            ue=str(input("Informe a unidade referente ao espaço:"))
            v0=float(input("Informe a velocidade inicial:"))
            t=float(input("Informe o tempo (se não souber, use a equação de número 6 antes):"))
            a=float(input("Informe a aceleração (se não souber, use a equação de número 7):"))
            S=s0+v0*t+(a*t*t)/2
            print(f"O resultado final é {S}, {ue}")
        
        case 2:
    
            v0=float(input("Informe a velocidade inicial:"))
            uv=str(input("Informe a unidade da velocidade:"))
            a=float(input("Informe a aceleração (se não souber, utilize a equação de número 7):"))
            t=float(input("Informe o tempo (se não souber, utilize a equação de número 6):"))
            V=v0+(a*t)
            print(f"A velocidade obtida é {V}{uv}")
            
        case 3:
        
            v0=float(input("Informe a velocidade inicial:"))
            uv=str(input("Informe a unidade da velocidade:"))
            a=float(input("Informe a aceleração (se não souber utilize a equação de número 7):"))
            vs=float(input("Informe a variação do espaço (se não souber utilize a equação de número 5):"))
            V=math.sqrt((v0*v0)*a*vs)
            print (f"A velocidade obtida é {V}{uv}")
            
        case 4:
    
            uv=str(input("Informe a unidade da velocidade:"))
            sf=float(input("Informe o espaço final:"))
            s0=float(input("Informe o espaço inicial:"))
            tf=float(input("Informe o tempo final:"))
            t0=float(input("Informe o tempo inicial:"))
            V=(sf-s0)/(tf-t0)
            print(f"A velocidade obtida é {V}{uv}")
            
        case 5:
        
            s0=float(input("Informe o espaço inicial:"))
            sf=float(input("Informe o espaço final:"))
            ue=str(input("Informe a unidade do espaço:"))
            S=sf-s0
            print(f"A variação do espaço é {S}{ue}")
            
        case 6:
        
            t0=float(input("Informe o tempo inicial:"))
            tf=float(input("Informe o tempo final:"))
            ut=str(input("Informe a unidade do tempo:"))
            t=tf-t0
            print ("O tempo obtido é {t}{ut}")
            
        case 7:
        
            v0=float(input("Informe a velocidade inicial:"))
            vf=float(input("Informe a velocidade final:"))
            t0=float(input("Informe o tempo inicial:"))
            tf=float(input("Informe o tempo final:"))
            ua=str(input("Informe a unidade da aceleração (pode digitar ms2):"))
            a=(vf-v0)/(tf-t0)
            print (f"A aceleração obtida é {a}{ua}")
elif (esc==2): 
    con=int(input("Digite 1 para converter de km/h para m/s, e digite 2 para converter de m/s para km/h:"))
    match (con):
        case 1:
            km=float(input("Digite a velocidade em km/h:"))
            ms=km/3.6
            print(f"A velocidade obtida é {ms}m/s")
            
        case 2: 
            ms=float(input("Digite a velocidade em m/s:"))
            km=ms*3.6
            print(f"A velocidade obtida é {km}km/h")
else:
    print ("Digite uma opção válida.")
    

print ("Obrigado por participar do teste preliminar, sua contribuição é muito importante.")

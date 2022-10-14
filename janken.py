import random

a = random.randint(0,2)
b = random.randint(0,2)

if a == 0 and b == 0:
    print('Aの手 : グー  v.s. Bの手 : グー → 引き分け')
    
elif a == 1 and b == 1:
    print('Aの手 : チョキ  v.s. Bの手 : チョキ → 引き分け')
    
elif a == 2 and b == 2:
    print('Aの手 : パー  v.s. Bの手 : パー → 引き分け')

elif a == 0 and b == 1:
    print('Aの手 : グー  v.s. Bの手 : チョキ → Aの勝ち')
    
elif a == 0 and b == 2:
    print('Aの手 : グー  v.s. Bの手 : パー → Bの勝ち')

elif a == 1 and b == 0:
    print('Aの手 : チョキ  v.s. Bの手 : グー → Bの勝ち')

elif a == 1 and b == 2:
    print('Aの手 : チョキ  v.s. Bの手 : パー → Aの勝ち')
    
elif a == 2 and b == 0:
    print('Aの手 : パー  v.s. Bの手 : グー → Aの勝ち')
    
elif a == 2 and b == 1:
    print('Aの手 : パー v.s. Bの手 : チョキ → Bの勝ち')
    

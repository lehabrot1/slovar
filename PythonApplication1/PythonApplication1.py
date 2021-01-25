def loe_failist(f):
  fail=open(f,'r',encoding="utf-8-sig")
    mas=[] 
    for rida in fail:
        mas.append(rida.strip())
    fail.close()
    return mas

rus:list=loe_failist("rus.txt")
def salvesra_failisse(f,text):
    fail=open(f,'a',encoding="utf-8-sig")
    fail.write(text+"\n")
    fail.close()
    mas=[]
    mas=loe_failist(f)
    return mas
def tolkimine():
    pass
    for rida in fail:
        mas.append(rida.strip())
    fail.close()
    return mas
def salvesta_failisse(f):
    fail=open(f,"a",encoding="utf-8-sig")
rus_list=loe_failist("rus.txt")
eng_=loe_failist("eng.txt")
print(rus_list)
print(eng_list)
while True:
    v=input("Перевод-1,Новое слово-2,Исправить ошибку-3,Проверка знаний-4 ")
if v=="1":
    tolkimine()
elif v="2"

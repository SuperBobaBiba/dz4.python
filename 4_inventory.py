inv=dict()
lim=float(input('ограничение инвентаря: '))
wlim = 0 #суммарный вес

while True:
    command=input('add/delete/look/exit?')

    if command =='add':
        name = input('введите название предмета:')
        weight = float(input('введите вес предмета:'))        
        wlim = wlim + weight
        if wlim>lim:
            wlim = wlim - weight
            print('превышен максимальный вес, предмет не добавлен')
        else:
            inv[name]=weight

    elif command =='delete':
        mass=inv.pop(input('Какой предмет удалить?'))
        wlim = wlim - mass


    elif command =='look':
        print (inv)

    elif command =='exit':
        break

    else:
        print('такой команды не существует')

#Task 2.2
def menu():

    print("1. Read menu data")
    print("2. Take order")
    print("3. Quit")
    option = input('Enter option number: ')
    if option not in ("1","2","3"):
        return None
    else:
        return option

def read_menu():
    with open("MENU.txt", 'r') as f:
        content = f.read().strip().split('\n')
    content = [i.split(' ') for i in content]
    content = [[i[0], ' '.join(i[1:-1]), i[-1]] for i in content]
    menulist = []
    for i in range(len(content)):
        minID = 9999
        minindex = None
        for i in range(len(content)):
            if int(content[i][0]) < minID:
                minID = int(content[i][0])
                minindex = i
        menulist.append(content[minindex])
        content.pop(minindex)
    return menulist

def order_search(menulist, itemindex):
    def order_search_helper(menulist, itemindex, ub, lb):
        if lb > ub:
            return False
        mid = (ub + lb) // 2
        if menulist[mid][0] == itemindex:
            return menulist[mid]
        if itemindex > menulist[mid][0]:
            return order_search_helper(menulist, itemindex, mid + 1,lb )
        else:
            return order_search_helper(menulist, itemindex, mid - 1, lb)
    return order_search_helper(menulist, itemindex, len(menulist) - 1, 0)



def take_order(menulist):
    orderlist = []
    while True:
        order = input('Please enter a menu item index (or -1 to complete order): ')
        if order == '-1':
            break
        search = order_search(menulist, order)
        if search == False:
            print("Item is not found in menu. ")
            continue
        orderlist.append(search)
    totalprice = 0
    for i in orderlist:
        totalprice += float(i[2][1:])
    print('Index   Item')
    for i in orderlist:
        print(f"{i[0]}   {i[1]}")
    print(f"Total price: ${round(totalprice, 2)}")

def run():
    readmenu = False
    while True:
        try:
            option = menu()
            if option == None:
                print("Invalid input")
                continue
            if option =='1':
                menulist = read_menu()
                readmenu = True
            if option == '2':
                if readmenu == False:
                    print("Unable to take order, menu data has need been read.")
                    continue
                take_order(menulist)
            if option == '3':
                break
        except:
            print("Bad things happen")
run()
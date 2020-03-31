from db_connector import connect

cursor,mydb = connect()

def setup():
    cursor.execute('create database if not exists shop_inventory')
    cursor.execute('use shop_inventory')
    cursor.execute('create table if not exists category(id int auto_increment, type text, name text, primary key(id))')
    cursor.execute('create table if not exists stock(id int auto_increment, name text,type text, stock_in_qty int, sale_price double, stock_out_qty int, purchase_price double, primary key(id))')

setup()    

def addCategories():
    item_type = input("Enter the type of item: ")
    item_name = input("Enter the name of item: ")
    cursor.execute('insert into category (type,name) values(%s,%s)',
                [item_type,item_name])
    mydb.commit()

def viewCatagories():
    cursor.execute('select * from category')
    for category in cursor.fetchall():
        print(f'[{category[0]}]- Item_Type: {category[1]}- Item_Name: {category[2]}')

def addStockData():
    item_name = input("Enter the name of item: ")
    item_type = input("Enter the type of item: ")
    stock_in_qty =input("Enter the stock_in_quantity: ")
    sale_price = input("Enter the sale_price of item: ")
    stock_out_qty = input("Enter the stock_out_quantity: ")
    purchase_price = input("Enter the purchase_price of item")
    cursor.execute('insert into stock (name,type,stock_in_qty,sale_price,stock_out_qty,purchase_price) values(%s,%s,%s,%s,%s,%s)',
                    [item_name,item_type,stock_in_qty,sale_price,stock_out_qty,purchase_price])
    mydb.commit()

def vieStockDatas():
    cursor.execute('select * from stock')
    for stock in cursor.fetchall():
        print(f'[{stock[0]}] - Item_name: {stock[1]} - Item_type: {stock[2]} - Stock_in_qty: {stock[3]} - Sale_price: {stock[4]} - stock_out_qty: {stock[5]} - Purchase_price: {stock[6]}')

def DisplayMenu():
    try:
        option=input(
            f'Shop Inventory\n'
            f'(1) Add Categories\n'
            f'(2) View Catogories\n'
            f'(3) Add StockDatas\n'
            f'(4) View StockDatas\n'
            f'If You wnat to exit the program press any key except 1-4\n'
            f'Enter your choice: '
        )
        if(option=='1'):
            addCategories()
        elif(option=='2'):
            viewCatagories()
        elif(option=='3'):
            addStockData()
        elif(option=='4'):
            vieStockDatas()
        choice=input('If you want to continue press "Y"')
        if(choice=='Y'):
            DisplayMenu()
        else:
            print("BYE BYE")
    except KeyboardInterrupt:
        print("BYE BYE")
DisplayMenu()
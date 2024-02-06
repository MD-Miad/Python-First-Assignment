mobile_data = {
    'status': True,
    'data': [
          {'name': 'Xiaomi Note 5', 'price': '300 USD', 'made': 'China'},
          {'name': 'Samsung Note 6', 'price': '200 USD', 'made': 'USA'},
          {'name': 'Iphone 5', 'price': '180.5 USD', 'made': 'Japan'},
          {'name': 'Pixel 5', 'price': '89.60 USD', 'made': 'Rusia'},
          {'name': 'Techno 5', 'price': '110 USD', 'made': 'Uk'},
          {'name': 'Huawei 5', 'price': '350 USD', 'made': 'Malaysia'},
            ],
    'exchnage_rate': 107.25
            }

dataCall = mobile_data["data"]
# priceCall = dataCall.get("price")
bdtExchangeRate = mobile_data.get("exchnage_rate")

counter = 1
while counter < len(dataCall):
    dataAll = dataCall[counter]
    usdPrice = dataAll["price"]
    priceAll = dataAll["price"]
    priceTextRemove = priceAll[:-4]
    priceBDT = float(priceTextRemove) * bdtExchangeRate
    priceBdtTextAdd = f"{priceBDT} BDT"
    dataAll.update({"price": priceBdtTextAdd})

    # Xiaomi Note 5 is made in China. The price is 300 USD which is almost equal to 30975 BDT
    adjustData = f"{dataAll['name']} is made in {dataAll["made"]}. The price is {usdPrice} which is almost equal to {dataAll["price"]}"

    print(adjustData)

    counter = counter + 1
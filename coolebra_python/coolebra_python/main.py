import products

data_res = {}

def iterate_data():
    for product in products.PRODUCT_LIST:
        if product["EAN"] in data_res:
            data = data_res[product["EAN"]]

            for market in product["markets"]:
                if market not in data["markets"]:
                    data["markets"].append(market)

                    if market["discount_price"] < data["price"]["min"]:
                        data["price"]["min"] = market["discount_price"]
                    if market["discount_price"] > data["price"]["max"]:
                        data["price"]["max"] = market["discount_price"]

        else:
            data_res[product["EAN"]] = {
                "name": product["name"],
                "SKU": product["SKU"],
                "markets": product.get("markets", []),
                "price": {
                    "min":  product["normal_price"],
                    "max": product["normal_price"]
                }
            }


def print_data():
    for k, v in data_res.items():
        market_counts = len(v["markets"])
        print("--------------------------------------------------------")
        print("EAN: ", k, "\n" + "NAME: ", v["name"], "\n" + "N° MARKETS: ", market_counts, "\n" + "MIN PRICE: ",
              v["price"]["min"], "\n" + "MAX PRICE: ", v["price"]["max"])
        print("--------------------------------------------------------")


if __name__ == '__main__':
    products.add_markets()
    iterate_data()
    print_data()

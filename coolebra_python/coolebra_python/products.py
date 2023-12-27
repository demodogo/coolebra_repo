import random

PRODUCT_LIST = [
    {
        "EAN": 2389,
        "name": "Leche entera",
        "SKU": f"SKU{random.randint(0, 1000)}",
        "normal_price": 1200
    },
{
        "EAN": 2389,
        "name": "Leche entera",
        "SKU": f"SKU{random.randint(0, 1000)}",
        "normal_price": 900
    },
    {
        "EAN": 2389,
        "name": "Leche entera",
        "SKU": f"SKU{random.randint(0, 1000)}",
        "normal_price": 990
    },
    {
        "EAN": 5647,
        "name": "Pan integral",
        "SKU": f"SKU{random.randint(1000, 1999)}",
        "normal_price": 1000
    },
    {
        "EAN": 5647,
        "name": "Yogurt natural",
        "SKU": f"SKU{random.randint(2000, 2999)}",
        "normal_price": 600
    },
    {
        "EAN": 5732,
        "name": "Huevos",
        "SKU": f"SKU{random.randint(3000, 3999)}",
        "normal_price": 3400
    },
    {
        "EAN": 5732,
        "name": "Huevos",
        "SKU": f"SKU{random.randint(3000, 3999)}",
        "normal_price": 3700
    },
    {
        "EAN": 8941,
        "name": "Tomates",
        "SKU": f"SKU{random.randint(4000, 4999)}",
        "normal_price": 1200
    },
    {
        "EAN": 8941,
        "name": "Tomates",
        "SKU": f"SKU{random.randint(4000, 4999)}",
        "normal_price": 990
    },
{
        "EAN": 8941,
        "name": "Tomates",
        "SKU": f"SKU{random.randint(4000, 4999)}",
        "normal_price": 880
    },
    {
        "EAN": 2167,
        "name": "Pollo",
        "SKU": f"SKU{random.randint(5000, 5999)}",
        "normal_price": 3700
    },
    {
        "EAN": 2167,
        "name": "Pollo",
        "SKU": f"SKU{random.randint(5000, 5999)}",
        "normal_price": 3400
    },
    {
        "EAN": 3489,
        "name": "Pasta",
        "SKU": f"SKU{random.randint(6000, 6999)}",
        "normal_price": 1200
    },
    {
        "EAN": 3489,
        "name": "Pasta",
        "SKU": f"SKU{random.randint(6000, 6999)}",
        "normal_price": 990
    },
    {
        "EAN": 6571,
        "name": "Sopa",
        "SKU": f"SKU{random.randint(7000, 7999)}",
        "normal_price": 900
    },
{
        "EAN": 6571,
        "name": "Sopa",
        "SKU": f"SKU{random.randint(7000, 7999)}",
        "normal_price": 990
    },
    {
        "EAN": 1203,
        "name": "Papas",
        "SKU": f"SKU{random.randint(8000, 8999)}",
        "normal_price": 1800
    },
    {
        "EAN": 1203,
        "name": "Papas",
        "SKU": f"SKU{random.randint(8000, 8999)}",
        "normal_price": 1300
    },
    {
        "EAN": 6571,
        "name": "Cereal",
        "SKU": f"SKU{random.randint(9000, 9999)}",
        "normal_price": 2700
    }
]

MARKET_LIST = [
    {
        "market_id": 1,
        "name": "MARKET ONE",
        "discount_price_mult": 0.7
    },
    {
        "market_id": 2,
        "name": "MARKET TWO",
        "discount_price_mult": 0.75
    },
    {
        "market_id": 3,
        "name": "MARKET THREE",
        "discount_price_mult": 0.8
    },
    {
        "market_id": 4,
        "name": "MARKET FOUR",
        "discount_price_mult": 0.78
    },
    {
        "market_id": 5,
        "name": "MARKET FIVE",
        "discount_price_mult": 0.72
    },
    {
        "market_id": 6,
        "name": "MARKET SIX",
        "discount_price_mult": 0.77
    },
    {
        "market_id": 7,
        "name": "MARKET SEVEN",
        "discount_price_mult": 0.76
    },
    {
        "market_id": 8,
        "name": "MARKET EIGHT",
        "discount_price_mult": 0.73
    },
    {
        "market_id": 9,
        "name": "MARKET NINE",
        "discount_price_mult": 0.79
    },
    {
        "market_id": 10,
        "name": "MARKET TEN",
        "discount_price_mult": 0.74
    }
]


def add_markets():
    for product in PRODUCT_LIST:
        markets = random.sample(MARKET_LIST, 3)
        product["markets"] = [
            {
                "market_id": market["market_id"],
                "name": market["name"],
                "discount_price": product["normal_price"] * market["discount_price_mult"]
            }
            for market in markets
        ]

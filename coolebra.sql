CREATE TABLE market
(
    id   INT AUTO_INCREMENT primary key,
    name VARCHAR(255)
);

CREATE TABLE product
(
    name      VARCHAR(255),
    SKU       VARCHAR(255) primary key,
    EAN       VARCHAR(255),
    market_id INT,
    FOREIGN KEY (market_id) REFERENCES market (id)
);

CREATE TABLE price
(
    id             INT AUTO_INCREMENT primary key,
    product_sku    VARCHAR(255),
    normal_price   DECIMAL(10, 3),
    discount_price DECIMAL(10, 3),
    active         BOOLEAN,
    created_date   TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_sku) REFERENCES product (SKU)
);


INSERT INTO market (name)
VALUES ('Market A'),
       ('Market B'),
       ('Market C');

INSERT INTO product (name, SKU, EAN, market_id)
VALUES ('Product 1', 'SKU001', 'EAN001', 1),
       ('Product 2', 'SKU002', 'EAN002', 2),
       ('Product 3', 'SKU003', 'EAN003', 3);

INSERT INTO price (product_sku, normal_price, discount_price, active)
VALUES ('SKU001', 12.000, 10.000, 0),
       ('SKU002', 32.000, 24.000, 1),
       ('SKU003', 43.000, 11.000, 1);

SELECT p.SKU,
       p.EAN,
       pr.normal_price AS 'PRECIO MINIMO',
       m.name          AS 'MARKET'
FROM product p
         JOIN market m
              on p.market_id = m.id
         JOIN (SELECT product_sku,
                      MIN(normal_price) AS 'normal_price',
                      MAX(created_date)
               FROM price
               WHERE active = 1
               GROUP BY product_sku) pr on p.SKU = pr.product_sku;

RESPUSTA 2:
Si bien el contexto entregado en la imagen 1 es poco, creo que sería de utilidad obtener información de un producto,
donde podría utilizar el EAN de cada producto para saber su valor en distintos mercados.
Asumiendo que esta información es relevante para el negocio, la almacenaría en otra tabla o incluso en caché para su rápida disponibilidad.


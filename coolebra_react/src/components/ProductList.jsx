import { products } from "../products";
import ProductCard from "./ProudctCard";
import {useEffect, useState} from "react";
import Searchbar from "./Searchbar";

export default function ProductList() {
    const [ searchValue, setSearchValue ] = useState('');
    const [ searchedProducts, setSearchedProducts ] = useState(null);

    useEffect( () => {
        if (searchValue?.length === 0 || searchValue?.length === undefined) {
            setSearchedProducts(null)
        } else {
            const filteredProducts = eanFilteredProducts.filter ( (prod) => prod.name.toLowerCase().includes(searchValue.toLowerCase()))
            setSearchedProducts(filteredProducts)
        }

    }, [searchValue])

    let eanFilteredProducts = [];
    function populateProds() {
        products.reduce((acc, product) => {
            const { EAN, markets } = product;
            if (!acc[EAN]) {
                acc[EAN] = { name: product.name, marketCount: markets.length, min: Infinity, max: -Infinity };
                eanFilteredProducts.push(acc[EAN])
            }
            acc[EAN].marketCount++;
            markets.reduce((acc, market) => {
                acc[EAN].min = Math.min(acc[EAN].min, market.discount_price);
                acc[EAN].max = Math.max(acc[EAN].max, market.discount_price);
                return acc;
            }, acc);
            return acc;
        }, {});
    }

    populateProds();

    const handleInputChange = (value) => {
        setSearchValue(value);
    }

    return (
        <div style={{ height: '100%', width: '100%', padding:'10vh 10vw'}} className={"d-flex flex-column gap-4"}>
            <Searchbar handleInputChange={handleInputChange} />
            <h2 className={"text-light fs-1"}>Productos</h2>
            <div className={"d-flex gap-3 flex-wrap"}>
                {
                    !searchedProducts ?
                        eanFilteredProducts.map((product) => (
                            <div className={"col m-2"} key={product.name}>
                                <ProductCard product={product} />
                            </div>
                        )) :
                        searchedProducts.map((product) => (
                            <div className={"col m-2"} key={product.name}>
                                <ProductCard product={product} />
                            </div>
                        ))
                }
            </div>
        </div>
    )
}
export default function ProductCard({product}) {

    return (
        <div className="card" style={{width: "18rem"}}>
            <div className="card-body">
                <h5 className="card-title">{product.name}</h5>
                <h6 className="card-subtitle mb-2 text-body-secondary">Vendido en {product.marketCount} tiendas</h6>
                <div className={"d-flex text-center gap-1 justify-content-center"}>
                    <p className="card-text fw-semibold">Precios entre:</p>
                    <span className={"fst-italic"}>${product.min}</span>
                    <span>y</span>
                    <span className={"fst-italic"}>${product.max}</span>
                </div>
            </div>
        </div>
    )
}
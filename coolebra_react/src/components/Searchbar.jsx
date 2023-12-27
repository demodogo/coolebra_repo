export default function Searchbar({handleInputChange}) {
    return (
        <div className={"text-light d-flex justify-content-start"} style={{ width: '70vw'}}>
            <input type={"text"} placeholder="Buscar" className={"border-0 form-control"} style={{ width: '400px'}}  onChange={(e) => handleInputChange(e.target.value)} />
        </div>
    )
}
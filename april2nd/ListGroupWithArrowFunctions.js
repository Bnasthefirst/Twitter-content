function ListGroup() {


    let items = [
          
          "front " ,
          "back ", 
          "truth ",
          "trey",
          "throw",
    ];

    items =[];



const messy =items.length ===0 ? <p> this is it </p>  : null

const Dre = () => {
    return <p> we are always happy </p>
}

    
    return (
        <>

       <div>
            <h1> this is a list group </h1>

            {messy}
            {Dre()}

            <ul className="list">

            {items.map(item => <li key ={item}> {item}</li>)}
            </ul>

      </div>


     
        
        
        </>



    )
}

export default ListGroup;

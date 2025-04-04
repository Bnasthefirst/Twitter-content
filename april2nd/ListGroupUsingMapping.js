
function ListGroup() {

    const items = [
         " key" ,
          "front " ,
          "back ", 
          "truth ",
          "trey",
          "throw",
    ];

    
    return (
        <>
        
        
                    <div>
            <h1> this is a list group </h1>

            <ul className="list">

            {items.map(item => <li> {item}</li>)}
            </ul>

        </div>


        
        
        
        </>



    )
}

export default ListGroup;

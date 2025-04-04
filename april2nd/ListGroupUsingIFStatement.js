import { Fragment } from "react";
function ListGroup() {


    let items = [
          
          "front " ,
          "back ", 
          "truth ",
          "trey",
          "throw",
    ];

    items =[];



   if (items.length ===0)
    return (<> <p> there are no items </p></>);
;

    
    return (
      
        
        <Fragment>
                    <div>
            <h1> this is a list group </h1>

            <ul className="list">

            {items.map(item => <li key ={item}> {item}</li>)}
            </ul>

        </div>


        </Fragment>
        
        
     



    )
}

export default ListGroup;

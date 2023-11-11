import { useState } from "react"


import { useLocation ,Link, useNavigate} from "react-router-dom"

export default function Update() {

    //   var location = useLocation()
    //   var updateData = location.state?.data || {}  

   
    
    const location = useLocation();
    const navigate = useNavigate()

    const [selectedPriority, setSelectedPriority] = useState(location.state.ob.priority);
    
    console.log(location.state)



    var title = undefined
    var dis = undefined
    var val = undefined


    // const [data, mydata] = useState([])
    const [id, myid] = useState(1)




    // console.log(data)

    const updateSave = (e) => {

        e.preventDefault()

        var title1 = title.value
        var disc = dis.value
        var value1 = val.value

        console.log(title1, disc, value1)

        var ob = {id : location.state.ob.id, title: title1, description: disc, priority: value1 }
     

        fetch('/api/updateTodo/', {
            method: "put",
            headers: { 
                'Content-Type': 'application/json',
                'X-CSRFToken': location.state.csrfToken, 
            },
            body: JSON.stringify(ob)
        }).then(response => response.json()).then(res =>{
           if(res.message == "Update successfully" ){
            navigate('/')
           }
        })


    }




    return (
        <>
            <div className="container" >
                <h2 className="alert alert-danger text-center" >Todo List Update</h2>


                <form onSubmit={(e) => updateSave(e)}>




                    <div className="row mt-4">

                        <div className="col-lg-6 col-md-6 col-sm-6">

                            <input type="text" ref={v => title = v} className="form-control" placeholder="Title" Value={location.state.ob.title} required />

                        </div>

                        <div className="col-lg-6 col-md-6 col-sm-6">

                            <input type="text" ref={v => dis = v} className="form-control" placeholder="Discription" Value={location.state.ob.description} required />

                        </div>


                    </div>

                    <div className="row mt-3">

                        <div className="col-lg-6 col-md-6 col-sm-6">

                            <select  ref={v => val = v}  value={selectedPriority}  className="form-control" onChange={(e)=> {
                                 setSelectedPriority(e.target.value);
                                
                            }} required>
                                <option value="High">High</option>
                                <option value="Medium" >Medium</option>
                                <option value="Low">Low</option>


                            </select>

                        </div>

                        <div className="col-lg-6 col-md-6 col-sm-6">

                            <button  className="btn btn-success w-50"  >Update</button>

                        </div>


                    </div>

                </form>






            </div>
        </>
    )
}
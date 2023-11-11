

import { Route, Routes  } from "react-router-dom"
import Update from "./update"
import Home from "./home"

export default function App() {


  return (
 
        <Routes>
          <Route path="/" Component={Home} />
          <Route path="/Update" Component={Update} />
        </Routes>
       
 
  )
}
import './App.css';
import Header from "./components/Header/Header";
import UserCard from "./components/UserCard/UserCard";
import {useState} from "react";


function App() {
    const [data, setData] = useState('{}')

    function update_data() {
        console.log(`update_data`)
        console.log('Click!')
        fetch(`http://localhost:8080/v1/users`, {
            method: "get",
            headers: {
                "Content-Type": "application/json"
            }
        }).then(response => {response.json().then(json => console.log(json))})
    }

    update_data()

    return (
        <div className="App">
            <Header/>
            <UserCard data={data}></UserCard>
        </div>
    );
}

export default App;

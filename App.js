import React, {useEffect,useState} from "react";

function App() {
    const [alerts, setAlerts] = useState([])

    const fetchAlerts = async () => {
        const res = await fetch("http://localhost:8000/api/alerts");
        const data = await res.json();
        setAlerst(data);
    };

    useEffect(() => {
        fetchAlerts();
        
    }, 5000);

    return () => clearInterval(interval);

}
const dismissAlert = async (id)=> {
    await fetch(
        'http://localhost:8000/api/alerts${id}',
        {
            method: "DELETE",
        }
    );

    fetchAlerts();
};

retuern(
    <div style={{padding: "20px"}}>
        <h1>IoT Alert Dashboard</h1>

        {alert.length === 0 ? (
            <p>No Active Alert</p>
        ):(
            alerts.map((alert)=> (
                <div 
                key = {alert.id}
                style = {{
                    border: "1px solid red"
                }}

            ))
        )}
    </div>
)
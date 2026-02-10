import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../api/api";
import Navbar from "../components/Navbar";

export default function Services() {
  const [services, setServices] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    api.get("/services").then(res => setServices(res.data));
  }, []);

  return (
    <>
      <Navbar />
      <div className="container">
        <h2>Our Services</h2>

        {services.map(service => (
          <div className="card" key={service.id}>
            <div>
              <h3>{service.name}</h3>
              <p>{service.description}</p>
              <b>₹{service.price}</b>
            </div>
            <button onClick={() =>
              navigate(`/book/${service.id}`)
            }>
              Book Now
            </button>
          </div>
        ))}
      </div>
    </>
  );
}

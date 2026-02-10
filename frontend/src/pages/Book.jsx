import { useParams, useNavigate } from "react-router-dom";
import { useEffect, useState } from "react";
import api from "../api/api";
import Navbar from "../components/Navbar";

export default function Book() {
  const { id } = useParams();
  const navigate = useNavigate();
  const [service, setService] = useState(null);
  const [date, setDate] = useState("");
  const [address, setAddress] = useState("");

  useEffect(() => {
    api.get("/services").then(res => {
      setService(res.data.find(s => s.id === id));
    });
  }, [id]);

  const confirmBooking = async () => {
  try {
    const payload = {
      service_id: id,
      ...(date ? { booking_time: new Date(date).toISOString() } : {}),
      address: address,
    };

    await api.post("/bookings", payload);

    navigate("/success");
  } catch (err) {
    console.error(err.response?.data);
    alert("Booking failed");
  }
};

  if (!service) return null;

  return (
    <>
      <Navbar />
      <div className="container">
        <h2>Book {service.name}</h2>

        <input
          type="datetime-local"
          value={date}
          onChange={e => setDate(e.target.value)}
        />

        <input
          placeholder="Enter Address"
          value={address}
          onChange={e => setAddress(e.target.value)}
        />

        <button onClick={confirmBooking}>
          Confirm Booking
        </button>
      </div>
    </>
  );
}

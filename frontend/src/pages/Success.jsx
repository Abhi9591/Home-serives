import { useNavigate } from "react-router-dom";
import Navbar from "../components/Navbar";

export default function Success() {
  const navigate = useNavigate();

  return (
    <>
      <Navbar />
      <div className="container center">
        <div className="success">✔</div>
        <h2>Booking Confirmed!</h2>
        <p>Your booking has been successfully created.</p>

        <button onClick={() => navigate("/")}>
          Back to Home
        </button>
      </div>
    </>
  );
}

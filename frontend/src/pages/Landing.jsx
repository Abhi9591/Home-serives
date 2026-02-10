import { useNavigate } from "react-router-dom";
import Navbar from "../components/Navbar";

export default function Landing() {
  const navigate = useNavigate();

  return (
    <>
      <Navbar />
      <div className="container center">
        <h1>Trusted Home Services<br />On Demand</h1>
        <p>
          Get professional and reliable services at your doorstep.
        </p>

        <button onClick={() => navigate("/services")}>
          Explore Services
        </button>
      </div>
    </>
  );
}

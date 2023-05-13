import { useState } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import "./App.css";
import AddCv from "./cv/AddCv1.jsx";
import "./index.css";
import TakeFile from "./cv/TakeFile";
import Form from "./cv/Form";

function App() {
  const [form, setForm] = useState(true);
  return (
    <div>
      <div style={{ textAlign: "start" }}>
        <a
          style={{
            backgroundColor: form ? "blue" : "white",
            color: form ? "white" : "gray",
          }}
          onClick={() => setForm(true)}
        >
          Via un formulaire
        </a>
        <a
          style={{
            marginLeft: "50px",
            backgroundColor: !form ? "blue" : "white",
            color: !form ? "white" : "gray",
          }}
          onClick={() => setForm(false)}
        >
          via un fichier
        </a>
      </div>
      <div
        style={{
          display: "flex",
          alignContent: "start",
          alignItems: "start",
          justifyContent: "space-between",
          paddingTop:"50px"
        }}
      >
        {form ? <Form /> : <TakeFile />}
      </div>
    </div>
  );
}

export default App;

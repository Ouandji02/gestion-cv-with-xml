import React, { useEffect, useState } from "react";

export default function FirstBlog({ setInfo }) {
  const [first, setFirst] = useState({});

  const handleChange = (e) => {
    const name = e.target.name;
    const value = e.target.value;

    setFirst((prev) => ({
      ...prev,
      [name]: value,
    }));

    setInfo(first);
  };

  useEffect(() => {
    setInfo(first);
  }, [first]);
  return (
    <div  >
      <div className="personal-info blog">
        <h2>Informations personnelles</h2>

        <div style={{ textAlign: "start" }}>
          <label>Nom</label>
          <br />
          <input type="text" name="Nom" onChange={handleChange} />
        </div>
        <div style={{ textAlign: "start" }}>
          <label>Prénom</label>
          <br />
          <input type="text" name="Prenom" onChange={handleChange} />
        </div>
        <div style={{ textAlign: "start" }}>
          <label>Email</label>
          <br />
          <input type="email" name="Email" onChange={handleChange} />
        </div>

        <div style={{ textAlign: "start" }}>
          <label>Téléphone</label>
          <br /> <input type="tel" name="Telephone" onChange={handleChange} />
        </div>
      </div>
    </div>
  );
}

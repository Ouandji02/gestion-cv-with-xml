import React from "react";

export default function SecondBlog({ setExperience }) {
  const [second, setsecond] = React.useState({});

  const handleChange = (e) => {
    const name = e.target.name;
    const value = e.target.value;

    setsecond((prev) => ({
      ...prev,
      [name]: value,
    }));

    setExperience([second]);
  };

  React.useEffect(() => {
    setExperience([second]);
  }, [second]);
  return (
    <div>
      <div className="professional-experience blog">
        <div style={{ textAlign: "start" }}>
          <h2>Expériences professionnelles</h2>
          <label>Poste</label>
          <input
            type="text"
            name="Poste"
            onChange={handleChange}
          />
        </div>
        <div style={{ textAlign: "start" }}>
          <label>Entreprise</label>
          <input type="text" name="Entreprise" onChange={handleChange} />
        </div>

        <div style={{ textAlign: "start" }}>
          <label>Date de début</label>
          <input type="date" name="DateDebut" onChange={handleChange} />
        </div>

        <div style={{ textAlign: "start" }}>
          <label>Date de fin</label>
          <input type="date" name="DateFin" onChange={handleChange} />
        </div>
        <div style={{ textAlign: "start" }}>
          <label>Description</label>
          <textarea name="Description" onChange={handleChange}></textarea>
        </div>
      </div>
    </div>
  );
}

import React from "react";

export default function ThirdBlog({ setFormations }) {
  const [third, setThird] = React.useState({});

  const handleChange = (e) => {
    const name = e.target.name;
    const value = e.target.value;

    setThird((prev) => ({
      ...prev,
      [name]: value,
    }));

    setFormations([third]);
  };

  React.useEffect(() => {
    setFormations([third]);
  }, [third]);

  return (
    <div>
      <div className="education blog">
        <h2>Formations</h2>
        <div>
          <label>Diplôme</label>
          <input
            name="Diplome"
            type="text"
            onChange={handleChange}
          />
        </div>
        <div>
          <label>Etablissement</label>
          <input
            name="Etablissement"
            type="text"
            onChange={handleChange}
          />
        </div>
        <div>
          <label>Date d'obtention</label>
          <input
            name="DateObtention"
            type="date"
            onChange={handleChange}
          />
        </div>
      </div>
    </div>
  );
}

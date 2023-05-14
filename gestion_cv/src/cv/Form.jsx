import React, { useState } from "react";
import FirstBlog from "./FirstBlog";
import SecondBlog from "./SecondBlog";
import ThirdBlog from "./ThirdBlog";
import axios from "axios";
import { Prism as SyntaxHighlighter } from "react-syntax-highlighter";
import { darcula } from "react-syntax-highlighter/dist/esm/styles/prism";

export default function Form() {
  const [info, setInfo] = useState();
  const [experience, setExperience] = useState();
  const [formations, setFormations] = useState();
  const [xml, setXML] = useState();
  const [html, setHtml] = useState();
  const [see, setSee] = useState();

  const submitFormXML = () => {
    setSee(false);
    const data = {
      InformationsPersonnelles: info,
      ExperiencesProfessionnelles: experience,
      Formations: formations,
    };
    axios
      .post("/api/json", data)
      .then((r) => setXML(r.data))
      .catch((e) => console.log(e));
  };

  const submitForSee = () => {
    setSee(true);
    const data = {
      InformationsPersonnelles: info,
      ExperiencesProfessionnelles: experience,
      Formations: formations,
    };
    axios
      .post("/api/json/see", data)
      .then((r) => setHtml(r.data))
      .catch((e) => alert(e.response.data));
  };

  console.log(info);
  console.log(experience);
  console.log(formations);
  return (
    <div
      style={{
        width:"100%",
        display: "flex",
        alignContent: "start",
        alignItems: "start",
        justifyContent: "space-between",
      }}
    >
      <div style={{ width: "400px" }}>
        <h4>Remplissez les informations pour ajouter votre CV</h4>
        <FirstBlog setInfo={setInfo} />
        <SecondBlog setExperience={setExperience} />
        <ThirdBlog setFormations={setFormations} />
        <div style={{ textAlign: "start" }}>
          <button onClick={submitForSee}>Voir le CV</button>
          <button onClick={submitFormXML}>Generer le XML</button>
        </div>
      </div>
      <div style={{
        marginLeft:"50px"
      }} >
        {see ? (
          <div dangerouslySetInnerHTML={{ __html: html }}></div>
        ) : (
          <SyntaxHighlighter language="xml" style={darcula}>
            {xml}
          </SyntaxHighlighter>
        )}
      </div>
    </div>
  );
}

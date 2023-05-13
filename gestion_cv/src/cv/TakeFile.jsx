import React, { useState } from "react";
import axios from "axios";
import { Prism as SyntaxHighlighter } from "react-syntax-highlighter";
import { darcula } from "react-syntax-highlighter/dist/esm/styles/prism";
import { saveAs } from "file-saver";

export default function TakeFile() {
  const [file, setFile] = useState();
  const [html, setHtml] = useState();
  const [seeHtml, setSeeHtml] = useState(false);
  const [filename, setFilename] = useState();

  const onChange = (e) => {
    const value = e.target.files[0];
    setFilename(e.target.value);
    setFile(value);
    console.log(value);
  };

  const submit = () => {
    axios
      .post("api/upload/in_html", file)
      .then((r) => setHtml(r.data))
      .catch((e) => {
        console.log(e);
        if (e.response.status === 400) alert(e.response.data);
        else alert("Une erreur s'est produite");
      });
  };

  const submitFormODT = () => {
    axios
      .post("api/upload/in_odt", file)
      .then((response) => {
        console.log(response);
        // Extrait le nom de fichier à partir de l'en-tête Content-Disposition
        const contentDisposition = response.headers.get("Content-Disposition");
        console.log(contentDisposition);
        const filenameMatch = contentDisposition.match(/filename="?(.+)"?/);
        const filename = filenameMatch ? filenameMatch[1] : "document.odt";
        // Crée un objet Blob à partir de la réponse
        return response.blob().then((blob) => {
          // Crée un objet URL à partir du Blob
          // Do something with the blob, like download it
          const url = window.URL.createObjectURL(blob);
          const link = document.createElement("a");
          link.href = url;
          link.download = "file.odt";
          document.body.appendChild(link);
          link.click();
          document.body.removeChild(link);
        });
      })
      .catch((e) => {
        console.log(e);
        if (e.response.status === 400) alert(e.response.data);
        else alert("Une erreur s'est produite");
      });
  };

  console.log(html);

  return (
    <div
      style={{
        display: "flex",
        alignContent: "start",
        alignItems: "start",
        justifyContent: "space-between",
      }}
    >
      <div>
        <label className="custom-file-upload">
          <input type="file" onChange={onChange} />
          {filename ? filename : "Choisir un fichier"}
        </label>
        <div>
          <button
            style={{ marginRight: "10px" }}
            onClick={() => {
              setSeeHtml(true);
              submit();
            }}
          >
            Voir le CV
          </button>
          <button
            style={{ marginRight: "10px" }}
            onClick={() => {
              setSeeHtml(false);
              submit();
            }}
          >
            Convertir en HTML
          </button>
          <button onClick={submitFormODT}>Convertir en odt</button>
        </div>
      </div>
      <div
        style={{
          marginLeft: "100px",
        }}
      >
        {seeHtml ? (
          <div dangerouslySetInnerHTML={{ __html: html }}></div>
        ) : (
          <SyntaxHighlighter language="html" style={darcula}>
            {html}
          </SyntaxHighlighter>
        )}
      </div>
    </div>
  );
}

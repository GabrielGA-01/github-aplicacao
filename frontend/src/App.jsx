import React from "react";
import { Streamlit, withStreamlitConnection } from "streamlit-component-lib";
import Pag0App from "./pag0_app";
import Pag1App from "./pag1_app";
import Pag2App from "./pag2_app";
import Pag3App from "./pag3_app";

function App({ args }) {
  const view = args?.view || "pag0";

  return (
    <>
      {view === "pag0" && <Pag0App count={args.count} />}
      {view === "pag1" && <Pag1App />}
      {view === "pag2" && <Pag2App />}
      {view === "pag3" && <Pag3App />}
      {!["pag0", "pag1", "pag2", "pag3"].includes(view) && (
        <div>⚠️ Interface não encontrada</div>
      )}
    </>
  );
}

export default withStreamlitConnection(App);

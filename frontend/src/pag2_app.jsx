import React, { useEffect } from "react";
import { Streamlit, withStreamlitConnection } from "streamlit-component-lib";
import { motion } from "framer-motion";
import "./Pages.css";

const fadeIn = {
  hidden: { opacity: 0, y: 30 },
  visible: (i) => ({
    opacity: 1,
    y: 0,
    transition: { delay: i * 0.3, duration: 0.8, ease: "easeOut" },
  }),
};

const paragraphs = [
  "O gráfico revela uma **grande desigualdade** nos salários médios das divisões analisadas.",
  "Enquanto as áreas de **advocacia pública**, **segurança** e **gestão financeira** lideram a lista com valores que ultrapassam **200 mil dólares**, setores voltados a **serviços comunitários** e **bibliotecas** possuem remunerações bem inferiores, abaixo dos **50 mil dólares**.",
  "Essa **diferença extrema** sugere que cargos de **liderança** e **gestão estratégica** são **altamente valorizados**, enquanto áreas **operacionais** e de **menor impacto financeiro** recebem menos investimentos salariais.",
  "A distribuição desigual pode **afetar a motivação dos trabalhadores** e influenciar a **qualidade dos serviços prestados**.",
  "**Tomar decisões com base em dados como esse é essencial** para garantir uma distribuição mais justa e eficiente dos recursos públicos.",
];

const Pag2App = ({ args }) => {
  useEffect(() => {
    Streamlit.setFrameHeight();
  }, []);

  return (
    <div
      style={{
        padding: "2rem",
        maxWidth: "800px",
        margin: "0 auto",
        fontFamily: "'Segoe UI', sans-serif",
        lineHeight: 1.6,
        backgroundColor: "#0d1b2a",
        color: "#d3dce6",
        borderRadius: "10px",
      }}
    >
      <motion.h1
        initial={{ opacity: 0, scale: 0.9 }}
        animate={{ opacity: 1, scale: 1 }}
        transition={{ duration: 0.6 }}
        style={{
          textAlign: "center",
          marginBottom: "2rem",
          fontSize: "2rem",
          color: "#00aaff",
          fontWeight: "bold",
        }}
      >
        Desigualdade Salarial e o Poder dos Dados
      </motion.h1>

      {paragraphs.map((text, i) => (
        <motion.p
          key={i}
          custom={i}
          initial="hidden"
          animate="visible"
          variants={fadeIn}
          style={{
            marginBottom: "1.5rem",
            fontSize: "1.1rem",
            textAlign: "justify",
          }}
          dangerouslySetInnerHTML={{ __html: text.replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>") }}
        />
      ))}
    </div>
  );
};

export default withStreamlitConnection(Pag2App);

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
  "Vivemos na **era da informação**. Todos os dias, milhões de dados são gerados por pessoas, sistemas, máquinas e ambientes digitais.",
  "Mas **dados por si só não significam nada**. É a **análise** que transforma números em conhecimento, e o conhecimento em ação.",
  "Tomar **decisões baseadas em evidências** — em vez de intuições ou achismos — é o que diferencia uma **escolha estratégica** de um **tiro no escuro**.",
  "Seja para **melhorar serviços públicos**, **orientar políticas de inclusão**, ou **otimizar processos em empresas**, a **inteligência está nos dados**.",
  "**Avaliar, entender e aplicar os dados com responsabilidade** é o primeiro passo para impactar positivamente o presente e o futuro.",
];

const Pag1App = ({ args }) => {
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
        A Força da Decisão Baseada em Dados
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

export default withStreamlitConnection(Pag1App);

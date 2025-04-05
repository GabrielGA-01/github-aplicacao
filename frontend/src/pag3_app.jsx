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
  "A análise de dados tornou-se **indispensável** para entender a viabilidade de projetos de energia renovável, especialmente quando avaliamos a relação entre **custo, eficiência e localização**.",
  "Os gráficos que exploram **Custo vs. Eficiência (LCOE × Capacity Factor)** demonstram como usinas com **alta eficiência e baixo custo** são as mais atraentes economicamente, produzindo mais energia a um custo competitivo.",
  "Projetos que aparecem com **alto custo e baixa eficiência** no gráfico sinalizam oportunidades para melhorias tecnológicas ou a necessidade de escolher locais com maior recurso energético.",
  "O gráfico de **Impacto da Distância** revela como usinas próximas à infraestrutura existente têm **custos menores**, enquanto locais remotos podem se tornar inviáveis sem investimentos em transmissão ou armazenamento.",
  "Esses insights são **cruciais** para o planejamento territorial, ajudando a identificar áreas onde a geração distribuída ou investimentos em infraestrutura são mais urgentes.",
  "Em um cenário de crescente demanda por energia limpa, dominar essa análise significa **transformar dados em decisões inteligentes**, acelerando a transição para um sistema energético mais eficiente."
];

const Pag3App = ({ args }) => {
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
          color: "#4CAF50", // Green color for energy theme
          fontWeight: "bold",
        }}
      >
        Análise de Dados para Energia Sustentável
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

export default withStreamlitConnection(Pag3App);
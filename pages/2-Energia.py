from frontend.components.mycomponent import pagina3
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pagina3()

# Configuração do Streamlit
st.title("Análise de Projetos Solares")

df = pd.read_csv("https://data.openei.org/files/8319/solar_open_access_2035_moderate_supply_curve.csv")

# Sidebar (filtros)
st.sidebar.header("Filtros")
selected_country = st.sidebar.selectbox("País", df["country"].unique())
selected_state = st.sidebar.selectbox("Estado", df[df["country"] == selected_country]["state"].unique())

# Filtrar dados
filtered_df = df[(df["country"] == selected_country) & (df["state"] == selected_state)]

# Gráfico 1: Custo vs. Eficiência (LCOE vs. Capacity Factor)
st.subheader("Custo vs. Eficiência")
fig1, ax1 = plt.subplots()
sns.scatterplot(
    data=filtered_df,
    x="capacity_factor_ac",
    y="lcoe_all_in_usd_per_mwh",
    hue="elevation_m",
    size="capacity_ac_mw",
    palette="viridis",
    alpha=0.7,
    ax=ax1
)
ax1.set_xlabel("Fator de Capacidade (AC)")
ax1.set_ylabel("Custo Total de Energia (LCOE, USD/MWh)")
ax1.set_title("Relação entre Custo e Eficiência")
st.pyplot(fig1)

# Gráfico 2: Impacto da Distância no Custo
st.subheader("Impacto da Distância na Viabilidade")
fig2, ax2 = plt.subplots()
sns.scatterplot(
    data=filtered_df,
    x="dist_spur_km",
    y="lcoe_all_in_usd_per_mwh",
    hue="cost_total_trans_usd_per_mw",
    size="capacity_ac_mw",
    palette="magma",
    alpha=0.7,
    ax=ax2
)
ax2.set_xlabel("Distância do Ponto de Conexão (km)")
ax2.set_ylabel("Custo Total de Energia (LCOE, USD/MWh)")
ax2.set_title("Impacto da Distância no Custo")
st.pyplot(fig2)

# Tabela resumo
st.subheader("Dados Filtrados - Análise de Viabilidade")

# Renomeando as colunas para português com unidades de medida
df_renomeado = filtered_df[["sc_point_gid", "capacity_ac_mw", "lcoe_all_in_usd_per_mwh", "dist_spur_km"]].rename(
    columns={
        "sc_point_gid": "ID do Projeto",
        "capacity_ac_mw": "Capacidade AC (MW)",
        "lcoe_all_in_usd_per_mwh": "Custo Energia (USD/MWh)",
        "dist_spur_km": "Distância da Rede (km)"
    }
)

# Exibindo a tabela com formatação melhorada
st.dataframe(
    df_renomeado,
    column_config={
        "Capacidade AC (MW)": st.column_config.NumberColumn(format="%.2f"),
        "Custo Energia (USD/MWh)": st.column_config.NumberColumn(format="%.2f"),
        "Distância da Rede (km)": st.column_config.NumberColumn(format="%.1f")
    },
    hide_index=True,
    use_container_width=True
)
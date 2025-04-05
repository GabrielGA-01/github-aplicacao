from frontend.components.mycomponent import pagina1, pagina2
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pagina1()

# Título do aplicativo
st.title("Análise de Salários por Divisão")
st.markdown("---")

# Função para carregar e tratar os dados
@st.cache_data
def load_data():
    url = "https://data.montgomerycountymd.gov/api/views/2nq6-auk8/rows.csv?accessType=DOWNLOAD"
    df = pd.read_csv(url)
    
    # Pré-processamento
    df.columns = df.columns.str.strip()
    df = df.dropna(subset=["Base Salary", "Division"])
    df["Base Salary"] = pd.to_numeric(df["Base Salary"], errors="coerce")
    
    return df

# Carrega os dados
try:
    df = load_data()
    
    # Cálculo das métricas
    media_por_divisao = df.groupby("Division")["Base Salary"].mean()
    top10 = media_por_divisao.nlargest(10)
    bottom10 = media_por_divisao.nsmallest(10)
    combined = pd.concat([top10, bottom10])

    # Configuração do estilo
    plt.style.use('seaborn-v0_8')
    sns.set_palette("husl")
    fig, ax = plt.subplots(figsize=(14, 8))

    # Plotagem do gráfico
    bars = combined.sort_values().plot(
        kind='barh',
        ax=ax,
        color=["#1f77b4" if x in top10 else "#ff7f0e" for x in combined.index],
        edgecolor='white',
        linewidth=0.7,
        alpha=0.9
    )

    # Adiciona os valores nas barras
    for i, (value, name) in enumerate(zip(combined.sort_values(), combined.sort_values().index)):
        ax.text(
            value + 500,
            i,
            f'${value:,.0f}',
            ha='left',
            va='center',
            fontsize=10,
            color='#333333'
        )

    # Customização do gráfico
    ax.set_title(
        'TOP 10 × BOTTOM 10 - Salários Médios por Divisão (2024)',
        fontsize=14,
        pad=20,
        fontweight='bold',
        color='#333333'
    )
    ax.set_xlabel('Salário Médio Anual (USD)', fontsize=12, labelpad=10)
    ax.set_ylabel('Divisão', fontsize=12, labelpad=10)
    ax.xaxis.grid(True, linestyle='--', alpha=0.6)
    ax.yaxis.grid(False)
    sns.despine(left=True, bottom=True)

    # Legenda customizada
    top_patch = plt.Rectangle((0,0), 1, 1, fc="#1f77b4", edgecolor='white')
    bottom_patch = plt.Rectangle((0,0), 1, 1, fc="#ff7f0e", edgecolor='white')
    ax.legend(
        [top_patch, bottom_patch],
        ['Top 10 - Maiores Salários', 'Bottom 10 - Menores Salários'],
        loc='lower right',
        frameon=True,
        framealpha=1
    )

    # Ajustes finais
    plt.tight_layout()
    fig.patch.set_facecolor('#f8f9fa')
    ax.set_facecolor('#f8f9fa')

    # Exibe o gráfico no Streamlit
    st.pyplot(fig)

    # Seção de dados brutos
    with st.expander("Ver dados completos"):
        st.dataframe(df.sort_values("Base Salary", ascending=False))

except Exception as e:
    st.error(f"Erro ao carregar dados: {str(e)}")

pagina2()

def carregar_dados():
    try:
        df = pd.read_csv("https://data.montgomerycountymd.gov/api/views/2nq6-auk8/rows.csv?accessType=DOWNLOAD")
        
        # Pré-processamento
        cols_numericas = ['Base Salary', '2024 Overtime Pay', '2024 Longevity Pay']
        for col in cols_numericas:
            df[col] = pd.to_numeric(df[col], errors='coerce')
            df[col] = df[col].fillna(0)
            
        return df
    except Exception as e:
        st.error(f"Erro ao carregar dados: {e}")
        return pd.DataFrame()

df = carregar_dados()

# Sidebar com filtros
with st.sidebar:
    st.header("Filtros")
    divisoes = sorted(df["Division"].dropna().unique())
    escolha_divisao = st.selectbox("Selecione a Área Profissional:", divisoes)

# Filtra os dados
df_filtrado = df[df["Division"] == escolha_divisao]

# Pré-formatação dos valores (solução alternativa à formatação do Streamlit)
def formatar_moeda(valor):
    return f"${valor:,.2f}" if pd.notnull(valor) else "-"

# Prepara o DataFrame final
df_formatado = df_filtrado.rename(columns={
    "Department": "Cód. Dept",
    "Department Name": "Departamento",
    "Division": "Divisão",
    "Gender": "Gênero",
    "Base Salary": "Salário Base",
    "2024 Overtime Pay": "Horas Extras",
    "2024 Longevity Pay": "Bônus Antiguidade",
    "Grade": "Nível"
})[["Departamento", "Divisão", "Gênero", "Salário Base", "Horas Extras", "Bônus Antiguidade", "Nível"]]

# Aplica formatação
for col in ["Salário Base", "Horas Extras", "Bônus Antiguidade"]:
    df_formatado[col] = df_formatado[col].apply(formatar_moeda)

# Layout principal
st.title("Análise de Remuneração por Divisão")

# Métricas resumidas
st.subheader(f"Resumo para: {escolha_divisao}")
col1, col2, col3 = st.columns(3)
with col1:
    salario_medio = df_filtrado["Base Salary"].mean()
    st.metric("Média Salarial Anual", formatar_moeda(salario_medio))
with col2:
    total_extras = df_filtrado["2024 Overtime Pay"].sum()
    st.metric("Total Horas Extras (2024)", formatar_moeda(total_extras))
with col3:
    st.metric("Total de Funcionários", len(df_filtrado))

# Tabela de dados
st.subheader("Detalhamento por Funcionário")
st.dataframe(
    df_formatado,
    column_config={
        "Salário Base": st.column_config.TextColumn("Salário Base (USD)"),
        "Horas Extras": st.column_config.TextColumn("Horas Extras (USD)"),
        "Bônus Antiguidade": st.column_config.TextColumn("Bônus (USD)")
    },
    hide_index=True,
    use_container_width=True,
    height=500
)
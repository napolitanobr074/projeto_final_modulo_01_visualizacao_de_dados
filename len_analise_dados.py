import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 01. CARREGANDO OS DADOS DOS ARQUIVOS EXPORTADOS DO freeSQL NO FORMATO .csv"
df_salario = pd.read_csv("database/sctec_len_query_01.csv")
df_regiao = pd.read_csv("database/sctec_len_query_02.csv")

# 02. VAMOS RENOMEAR AS COLUNAS PARA LIGUA PORTUGUESA BRASIL
df_salario = df_salario.rename(columns={
    "EMPLOYEE_ID": "ID_FUNCIONARIO",
    "FIRST_NAME": "NOME",
    "LAST_NAME": "SOBRENOME",
    "SALARY": "SALARIO",
    "DEPARTMENT_NAME": "DEPARTAMENTO",
    "JOB_TITLE": "CARGO"
})

df_regiao = df_regiao.rename(columns={
    "EMPLOYEE_ID": "ID_FUNCIONARIO",
    "FIRST_NAME": "NOME",
    "LAST_NAME": "SOBRENOME",
    "SALARY": "SALARIO",
    "DEPARTMENT_NAME": "DEPARTAMENTO",
    "CITY": "CIDADE",
    "STATE_PROVINCE": "UF",
    "COUNTRY_NAME": "PAIS",
    "REGION_NAME": "REGIAO"
})

print("Salário X Departamento e Cargo")
print(df_salario.head())
print(df_salario.info())

print("\n Funcionários X Região")
print(df_regiao.head())
print(df_regiao.info())

# 03.APRESENTANDO EM PYTHON AS  ESTATISTICAS DESCRITIVAS INICIAS E BÁSICAS PARA SALÁRIO
estatisticas = {
    "média": df_salario["SALARIO"].mean(),
    "mediana": df_salario["SALARIO"].median(),
    "mínimo": df_salario["SALARIO"].min(),
    "máximo": df_salario["SALARIO"].max(),
}

print("\nEstatísticas de salário:")
for nome, valor in estatisticas.items():
    print(f"{nome}: {valor:.2f}")

# 04.  APRESENTANDO ESTATISTICA/NUMEROS POR DEPARTAMENTO
estat_departamento = df_salario.groupby("DEPARTAMENTO")["SALARIO"].agg(
    ["mean", "median", "min", "max", "count"]
)
print("\nEstatísticas por departamento:")
print(estat_departamento)

# 05. APRESENTANDO ESTATISTICA/NUMEROS POR REGIÃO
estat_regiao = df_regiao.groupby("REGIAO")["SALARIO"].agg(
    ["mean", "median", "min", "max", "count"]
)
print("\nEstatísticas por região:")
print(estat_regiao)

# VAMOS INICIARA A PARTE DE VISUALIZAÇÃO DOS DADOS COM GRÁFICOS E FIGURAS

# 06. HISTOGRAMA DA DISTRIBUIÇÃO GERAL DE SALÁRIOS
plt.figure(figsize=(8, 5))
plt.hist(df_salario["SALARIO"], bins=15, color="#4C72B0", edgecolor="black")
plt.title("Distrib Salários")
plt.xlabel("Salário")
plt.ylabel("Qtde de Funcionários")
plt.tight_layout()
plt.savefig("sctec_len_histograma_salarios.png")
plt.show()

# 07. BOXPLOT COM A RELAÇÃO SALÁRIO POR DEPARTAMENTO
plt.figure(figsize=(10, 6))
sns.boxplot(data=df_salario, x="DEPARTAMENTO", y="SALARIO")
plt.title("Salário por Departamento")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("sctec_len_boxplot_departamento.png")
plt.show()

# 08. BOXPLOT COM A RELAÇÃO SALÁRIO POR REGIÃO
plt.figure(figsize=(10, 6))
sns.boxplot(data=df_regiao, x="REGIAO", y="SALARIO")
plt.title("Salário por Região")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("boxplot_regiao.png")
plt.show()

# 09. VAMOS VERIFICAR A OPORTUNIDADE EM IDENTIFICAR OS OUTLIERS
Q1 = df_salario["SALARIO"].quantile(0.25)
Q3 = df_salario["SALARIO"].quantile(0.75)
IQR = Q3 - Q1
limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

outliers = df_salario[
    (df_salario["SALARIO"] < limite_inferior) | (df_salario["SALARIO"] > limite_superior)
]
print(f"\nQuantidade de outliers encontrados: {len(outliers)}")
print(outliers[["NOME", "SOBRENOME", "SALARIO", "DEPARTAMENTO"]])
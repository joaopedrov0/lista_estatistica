from scipy.stats import norm

# ? Grupo 1: Análise e Propriedade de Curvas Normais

# ============================================================================== #
# 1.a.

# Resultado obtido: A: 45, B: 60, C: 45

# ============================================================================== #
# 1.b.

# Resultado obtido: A curva C é a mais dispersa, portanto a que tem o maior
# desvio padrão.

# ============================================================================== #
# 2.

# Média: 655
# Desvio padrão estimado: 22,5 (aproximadamente 90 valores em 95% da área)

# Resultado obtido: Média de 655 e 22,5 de desvio padrão

# ============================================================================== #
# 3.a.

print(f"Resultado 3.a: {norm.cdf(-2.19):.6f}") # (Cumulative Distribution Function)

# Resultado obtido: 0.014262

# ============================================================================== #
# 3.b.

print(f"Resultado 3.b: {norm.cdf(2.17):.6f}") # (Cumulative Distribution Function)

# Resultado obtido: 0.984997

# ============================================================================== #
# 4.b

print(f"Resultado 4.b: {norm.sf(2.13):.6f}") # (Survival Function)
# ou 1 - norm.cdf(escore_z)

# Resultado obtido: 0.016585

# ============================================================================== #
# 5.

print(f"Resultado 5: {norm.cdf(-2.16):.6f}") # (Cumulative Distribution Function)

# Resultado obtido: 0.015386

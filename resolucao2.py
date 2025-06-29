import numpy as np
from scipy.stats import norm, t, chi2
import math

# ============================================================================== #
# 1.a. 
# A média de uma curva normal corresponde ao seu ponto central, ou eixo de
# simetria (o pico da curva).
#
# Resultado obtido:
# - Média da Curva A: 45
# - Média da Curva B: 60
# - Média da Curva C: 45
# A curva B tem a maior média.
print(f"1. a) A maior média é da curva B")
# ============================================================================== #
# 1.b. 
# O desvio padrão está relacionado à dispersão (largura) da curva. Quanto mais
# "achatada" e larga a curva, maior o desvio padrão.
#
# Resultado obtido:
# A curva C é a mais dispersa (larga), portanto, tem o maior desvio padrão.
print(f"1. b) A curva C é a mais dispersa")
# ============================================================================== #
# 2. 
# A média é o centro da distribuição, que está no pico da curva.
# O desvio padrão pode ser estimado pela Regra Empírica (aproximadamente 95%
# dos dados estão a 2 desvios padrão da média).
#
# Média: O pico da curva está exatamente entre 650 e 660.
#   Média (µ) = 655
#
# Desvio Padrão Estimado:
#   A maior parte da curva (cerca de 95%) parece está entre 600 e 710.
#   A largura desse intervalo é 710 - 600 = 110.
#   Este intervalo corresponde a 4 desvios padrão (de -2σ a +2σ).
#   Desvio Padrão (σ) ≈ 110 / 4 = 22,5.
#
# Resultado obtido: Média de 655 e desvio padrão estimado de 22,5.
print(f"2. Média de 655 e desvio padrão estimado de 22,5.")
# ============================================================================== #
# 3.a. 
area_3a = norm.cdf(-2.19)
# Resultado obtido: 0.014262
print(f"3. a) {area_3a:.6f}")
# ============================================================================== #
# 3.b. 
area_3b = norm.cdf(2.17)
# Resultado obtido: 0.984997
print(f"3. b) {area_3b:.6f}")
# ============================================================================== #
# 4. 
# O exercício pede a área à ESQUERDA de z = 2.13. Isso é calculado com a
# função de distribuição acumulada (CDF).
area_4 = norm.cdf(2.13)
# Resultado obtido: 0.983415
print(f"4. b) {area_4:.6f}")
# ============================================================================== #
# 5. 
# O exercício pede a área à DIREITA de z = -2.16. Isso é calculado com a
# função de sobrevivência (SF), que é o mesmo que 1 - CDF.
area_5 = norm.sf(-2.16)
area_esquerda_5 = norm.cdf(-2.16)
# Resultado obtido: 0.984614
print(f"5. {area_5:.6f} e 5. b) {area_esquerda_5:.6f}")
# ============================================================================== #
# 6. 
# A área entre dois escores-z é a área acumulada do maior menos a do menor.
area_6 = norm.cdf(-1.35) - norm.cdf(-2.165)
# Resultado obtido: 0.073459
print(f"6. {area_6:.6f}")
# ============================================================================== #
# 7. 
# µ = 67, σ = 3.5. Qual a probabilidade de x > 70?
z_7 = (70 - 67) / 3.5
prob_7 = norm.sf(z_7)
# Resultado obtido: z = 0.8571, Probabilidade = 0.195655
print(f"7. {prob_7:.6f}")
# ============================================================================== #
# 8. 
# µ = 45, σ = 12. Qual a probabilidade de x estar entre 33 e 60?
z1_8 = (33 - 45) / 12
z2_8 = (60 - 45) / 12
prob_8 = norm.cdf(z2_8) - norm.cdf(z1_8)
# Quantos consumidores de 150?
consumidores_8 = 150 * prob_8
# Resultado obtido:
# z1 = -1.0, z2 = 1.25
# Probabilidade = 0.735661
# Número esperado de consumidores = 110.35 (aprox. 110)
print(f"8. A probabilidade é de {prob_8:.6f} e são esperados cerca de {consumidores_8:.2f} consumidores")
# ============================================================================== #
# 9. 
# O exercício é insolúvel pois não fornece a média e o desvio padrão dos
# níveis de triglicerídeos da população.
print(f"9. Não há resposta, faltam dados.")
# ============================================================================== #
# 10.1. 
# Encontrar z tal que a área à DIREITA seja 0.9616.
# Usamos a função inversa de sobrevivência (ISF).
z_10_1 = norm.isf(0.9616)
# Resultado obtido: -1.7700
print(f"10.1. {z_10_1:.6f}")
# ============================================================================== #
# 10.2. 
# 95% da área entre -z e z. Isso significa que 5% está nas caudas, ou 2.5%
# em cada cauda. A área acumulada à esquerda de +z é 95% + 2.5% = 97.5%.
# Usamos a função de ponto percentual (PPF), a inversa da CDF.
z_10_2 = norm.ppf(0.975)
# Resultado obtido: 1.95996 (o famoso 1.96)
print(f"10.2. {z_10_2:.6f}")
# ============================================================================== #
# 11. 
# Percentil é a área acumulada à esquerda. Usamos a função PPF.
# P10: 10º percentil
z_p10 = norm.ppf(0.10)
# P20: 20º percentil
z_p20 = norm.ppf(0.20)
# P99: 99º percentil (O exercício marca P999, que parece um erro de digitação
# para P99. Se fosse P99.9, a área seria 0.999)
z_p99 = norm.ppf(0.99)
# Resultado obtido:
# P10 -> z = -1.2816
# P20 -> z = -0.8416
# P99 -> z = 2.3263
print(f"11. P10: {z_p10:.6f}, P20: {z_p20:.6f}, P99: {z_p99:.6f}")
# ============================================================================== #
# 12. 
# µ = 52, σ = 15. Transformar z em x usando x = µ + z*σ.
z_scores_12 = [-2.33, 3.10, 0.58]
x_values_12 = [52 + z * 15 for z in z_scores_12]
# Resultado obtido:
# z = -2.33 -> x = 17.05 libras
# z = 3.10  -> x = 98.50 libras
# z = 0.58  -> x = 60.70 libras
print(f"12. z=-2.33 -> x={x_values_12[0]:.2f}; z=3.10 -> x={x_values_12[1]:.2f}; z=0.58 -> x={x_values_12[2]:.2f}")
# ============================================================================== #
# 13. 
# µ = 129, σ = 5.18. Maior distância no 1% mais baixo (Percentil 1).
z_p1_13 = norm.ppf(0.01)
x_13 = 129 + z_p1_13 * 5.18
# Resultado obtido:
# z = -2.3263
# x = 116.93 pés
print(f"13. {x_13:.2f} pés")
# ============================================================================== #
# 14. 
# µ = 11.2, σ = 2.1. 10% com menos tempo são demitidos (Percentil 10).
z_p10_14 = norm.ppf(0.10)
x_14 = 11.2 + z_p10_14 * 2.1
# Resultado obtido:
# z = -1.2816
# x = 8.51 anos
print(f"14. {x_14:.2f} anos")
# ============================================================================== #
# 15. 
# População: µ = 47, σ = 9. Amostra: n = 64.
# Média da distribuição amostral (µ_x̄) = µ
media_amostral_15 = 47
# Desvio padrão da distribuição amostral (Erro Padrão, σ_x̄) = σ / sqrt(n)
erro_padrao_15 = 9 / math.sqrt(64)
# Resultado obtido:
# Média da distribuição amostral = 47
# Erro Padrão = 1.125
print(f"15. Média da distribuição amostral = {media_amostral_15}, Erro Padrão = {erro_padrao_15}")
# ============================================================================== #
# 16. 
# População: µ = 3.5, σ = 0.2. Amostra: n = 16.
media_amostral_16 = 3.5
erro_padrao_16 = 0.2 / math.sqrt(16)
# Resultado obtido:
# Média da distribuição amostral = 3.5
# Erro Padrão = 0.05
print(f"16. Média da distribuição amostral = {media_amostral_16}, Erro Padrão = {erro_padrao_16}")
# ============================================================================== #
# 17. 
# População: µ = 25, σ = 1.5. Amostra: n = 100.
# Probabilidade de 24.7 < x̄ < 25.5.
mu_x_bar_17 = 25
sigma_x_bar_17 = 1.5 / math.sqrt(100)
z1_17 = (24.7 - mu_x_bar_17) / sigma_x_bar_17
z2_17 = (25.5 - mu_x_bar_17) / sigma_x_bar_17
prob_17 = norm.cdf(z2_17) - norm.cdf(z1_17)
# Resultado obtido:
# Erro Padrão = 0.15
# z1 = -2.0, z2 = 3.333...
# Probabilidade = 0.976825
print(f"17. {prob_17:.6f}")
# ============================================================================== #
# 18. 
# População: µ = 176800, σ = 50000. Amostra: n = 12.
# Probabilidade de x̄ > 160000.
mu_x_bar_18 = 176800
sigma_x_bar_18 = 50000 / math.sqrt(12)
z_18 = (160000 - mu_x_bar_18) / sigma_x_bar_18
prob_18 = norm.sf(z_18)
# Resultado obtido:
# Erro Padrão = 14433.76
# z = -1.1639
# Probabilidade = 0.877797
print(f"18. {prob_18:.6f}")
# ============================================================================== #
# 19. 
# População: µ = 190, σ = 48.
# Parte 1: P(x < 200) para um monitor
z_19_1 = (200 - 190) / 48
prob_19_1 = norm.cdf(z_19_1)
# Parte 2: P(x̄ < 200) para n = 10
sigma_x_bar_19 = 48 / math.sqrt(10)
z_19_2 = (200 - 190) / sigma_x_bar_19
prob_19_2 = norm.cdf(z_19_2)
# Resultado obtido:
# P(x < 200) = 0.5826. z = 0.2083
# P(x̄ < 200) = 0.7416. z = 0.6495
# A probabilidade de a média da amostra ser menor que 200 é maior.
print(f"19. P(x < 200) = {prob_19_1:.4f}, P(x̄ < 200) = {prob_19_2:.4f}. A probabilidade da média da amostra é maior.")
# ============================================================================== #
# 20. 
# Aproximação Normal para Binomial. n=100, p=0.34.
n_20, p_20 = 100, 0.34
q_20 = 1 - p_20
np_20 = n_20 * p_20
nq_20 = n_20 * q_20
# Pode usar a aproximação? Sim, pois np e nq são >= 5.
mu_20 = np_20
sigma_20 = math.sqrt(np_20 * q_20)
# Resultado obtido:
# np = 34, nq = 66. Sim, pode usar a aproximação.
# Média (µ) = 34
# Desvio Padrão (σ) = 4.7413
print(f"20. Pode usar aproximação. Média (µ) = {mu_20}, Desvio Padrão (σ) = {sigma_20:.4f}")
# ============================================================================== #
# 21. 
# n=100, p=0.34. P(x > 30)? Usar aproximação normal com correção.
# P(x > 30) -> P(X_norm > 30.5)
mu_21 = 34
sigma_21 = 4.7413 # Do exercício anterior
x_corrigido_21 = 30.5
z_21 = (x_corrigido_21 - mu_21) / sigma_21
prob_21 = norm.sf(z_21)
# Resultado obtido:
# z = -0.7382
# Probabilidade = 0.769812
print(f"21. {prob_21:.6f}")
# ============================================================================== #
# 22. 
# O exercício ("Qual é a probabilidade de que no máximo 100 adultos digam...")
# está incompleto. Falta o tamanho da amostra (n) para poder resolver.
print("22. Incompleto, falta o tamanho da amostra (n).")
# ============================================================================== #
# 23. 
# n=75, p=0.32. P(x = 15)? Usar aproximação normal com correção.
# P(x = 15) -> P(14.5 < X_norm < 15.5)
n_23, p_23 = 75, 0.32
mu_23 = n_23 * p_23
sigma_23 = math.sqrt(mu_23 * (1 - p_23))
z1_23 = (14.5 - mu_23) / sigma_23
z2_23 = (15.5 - mu_23) / sigma_23
prob_23 = norm.cdf(z2_23) - norm.cdf(z1_23)
# Resultado obtido:
# µ = 24, σ = 4.0398
# z1 = -2.3516, z2 = -2.1041
# Probabilidade = 0.00844
print(f"23. {prob_23:.5f}")
# ============================================================================== #
# 24. 
# Encontrar a média da amostra (estimativa pontual para µ).
dados_24 = [26, 31, 28, 25, 32, 22, 46, 22, 32, 32, 25, 28, 22, 21, 22, 20, 32, 36, 22, 32, 28, 28, 40, 25, 26, 35, 48, 38, 22, 19]
media_amostral_24 = np.mean(dados_24)
# Resultado obtido: Média amostral (x̄) = 29.4
print(f"24. {media_amostral_24:.1f}")
# ============================================================================== #
# 25. 
# Margem de erro E para 95% de confiança. n=30, σ=7.9.
n_25 = 30
sigma_25 = 7.9
confianca_25 = 0.95
z_c_25 = norm.ppf(1 - (1 - confianca_25) / 2)
E_25 = z_c_25 * (sigma_25 / math.sqrt(n_25))
# Resultado obtido:
# z_c = 1.960
# Margem de Erro (E) = 2.827 horas
print(f"25. Margem de Erro (E) = {E_25:.3f} horas")
# ============================================================================== #
# 26. 
# Intervalo de confiança de 95%. Usar x̄ de Ex24 e E de Ex25.
x_bar_26 = media_amostral_24 # 29.4
E_26 = E_25 # 2.827
limite_inf_26 = x_bar_26 - E_26
limite_sup_26 = x_bar_26 + E_26
# Resultado obtido:
# IC 95% = (26.573, 32.227)
print(f"26. IC 95% = ({limite_inf_26:.3f}, {limite_sup_26:.3f})")
# ============================================================================== #
# 26 (duplicado). 
# n=30, x̄=22.9, σ=1.5. IC 90% para µ.
n_26b, x_bar_26b, sigma_26b = 30, 22.9, 1.5
confianca_26b = 0.90
z_c_26b = norm.ppf(1 - (1 - confianca_26b) / 2)
E_26b = z_c_26b * (sigma_26b / math.sqrt(n_26b))
limite_inf_26b = x_bar_26b - E_26b
limite_sup_26b = x_bar_26b + E_26b
# Resultado obtido:
# z_c = 1.645
# E = 0.451
# IC 90% = (22.449, 23.351)
print(f"26.2) IC 90% = ({limite_inf_26b:.3f}, {limite_sup_26b:.3f})")
# ============================================================================== #
# 27. 
# Tamanho da amostra n. 95% confiança, E=2.0, σ=7.9.
confianca_27, E_27, sigma_27 = 0.95, 2.0, 7.9
z_c_27 = norm.ppf(1 - (1 - confianca_27) / 2)
n_27 = (z_c_27 * sigma_27 / E_27)**2
n_27_arredondado = math.ceil(n_27)
# Resultado obtido:
# n = 59.9...
# Tamanho mínimo da amostra = 60
print(f"27. Tamanho mínimo da amostra = {n_27_arredondado}")
# ============================================================================== #
# 28. 
# Valor crítico tc. 90% confiança, n=22.
confianca_28, n_28 = 0.90, 22
df_28 = n_28 - 1
tc_28 = t.ppf(1 - (1 - confianca_28) / 2, df=df_28)
# Resultado obtido:
# Graus de liberdade (df) = 21
# t_c = 1.721
print(f"28. t_c = {tc_28:.3f}")
# ============================================================================== #
# 29. 
# IC 90% e 99% para µ. n=16, x̄=162.0, s=10.0.
n_29, x_bar_29, s_29 = 16, 162.0, 10.0
df_29 = n_29 - 1
# IC 90%
tc_90 = t.ppf(0.95, df=df_29)
E_90 = tc_90 * (s_29 / math.sqrt(n_29))
ic_90 = (x_bar_29 - E_90, x_bar_29 + E_90)
# IC 99%
tc_99 = t.ppf(0.995, df=df_29)
E_99 = tc_99 * (s_29 / math.sqrt(n_29))
ic_99 = (x_bar_29 - E_99, x_bar_29 + E_99)
# Resultado obtido:
# IC 90%: E = 4.382, Intervalo = (157.618, 166.382)
# IC 99%: E = 7.332, Intervalo = (154.668, 169.332)
print(f"29. IC 90%: ({ic_90[0]:.3f}, {ic_90[1]:.3f}), IC 99%: ({ic_99[0]:.3f}, {ic_99[1]:.3f})")
# ============================================================================== #
# 30. 
# IC 90% e 95% para µ. n=36, x̄=9.75, s=2.39.
n_30, x_bar_30, s_30 = 36, 9.75, 2.39
df_30 = n_30 - 1
# IC 90%
tc_90_30 = t.ppf(0.95, df=df_30)
E_90_30 = tc_90_30 * (s_30 / math.sqrt(n_30))
ic_90_30 = (x_bar_30 - E_90_30, x_bar_30 + E_90_30)
# IC 95%
tc_95_30 = t.ppf(0.975, df=df_30)
E_95_30 = tc_95_30 * (s_30 / math.sqrt(n_30))
ic_95_30 = (x_bar_30 - E_95_30, x_bar_30 + E_95_30)
# Resultado obtido:
# IC 90%: E = 0.672, Intervalo = (9.078, 10.422), Largura = 1.344
# IC 95%: E = 0.809, Intervalo = (8.941, 10.559), Largura = 1.618
# O intervalo de 95% é mais largo.
print(f"30. IC 90%: ({ic_90_30[0]:.3f}, {ic_90_30[1]:.3f}), IC 95%: ({ic_95_30[0]:.3f}, {ic_95_30[1]:.3f}). O intervalo de 95% é mais largo.")
# ============================================================================== #
# 31. 
# Qual distribuição usar? n=18, σ desconhecido, população normal.
#
# Resultado: Deve-se usar a distribuição t de Student.
# Razões:
# 1. O desvio padrão da população (σ) é desconhecido; usamos o da amostra (s).
# 2. O tamanho da amostra (n=18) é menor que 30.
# 3. A população de origem é declarada como normalmente distribuída.
# Essas são as condições exatas para o uso da distribuição t.
# ============================================================================== #
# 32. 
# Encontrar p-chapéu (p̂). x=123, n=2462.
x_32, n_32 = 123, 2462
p_hat_32 = x_32 / n_32
# Resultado obtido: p̂ = 0.04996
# ============================================================================== #
print(f"32. p̂ = {p_hat_32:.5f}")
# 33. 
# IC 90% para p. Usar dados do Ex32.
p_hat_33 = p_hat_32
q_hat_33 = 1 - p_hat_33
n_33 = n_32
confianca_33 = 0.90
z_c_33 = norm.ppf(1 - (1 - confianca_33) / 2)
E_33 = z_c_33 * math.sqrt(p_hat_33 * q_hat_33 / n_33)
ic_33 = (p_hat_33 - E_33, p_hat_33 + E_33)
# Resultado obtido:
# p̂ = 0.050, q̂ = 0.950
# z_c = 1.645
# E = 0.0073
# IC 90% = (0.0427, 0.0573) ou (4.27%, 5.73%)
# ============================================================================== #
print(f"33. IC 90% = ({ic_33[0]:.4f}, {ic_33[1]:.4f})")
# 34. 
# IC 99% para p. n=498, p̂=0.25 (25% consideram >65 anos perigosos).
n_34, p_hat_34 = 498, 0.25
q_hat_34 = 1 - p_hat_34
confianca_34 = 0.99
z_c_34 = norm.ppf(1 - (1 - confianca_34) / 2)
E_34 = z_c_34 * math.sqrt(p_hat_34 * q_hat_34 / n_34)
ic_34 = (p_hat_34 - E_34, p_hat_34 + E_34)
# Resultado obtido:
# z_c = 2.576
# E = 0.0498
# IC 99% = (0.2002, 0.2998) ou (20.02%, 29.98%)
# ============================================================================== #
print(f"34. IC 99% = ({ic_34[0]:.4f}, {ic_34[1]:.4f})")
# 35. 
# Tamanho da amostra n. 90% confiança, E=0.02.
confianca_35, E_35 = 0.90, 0.02
z_c_35 = norm.ppf(1 - (1 - confianca_35) / 2)
# Caso 1: Sem estimativa preliminar (p̂=0.5)
p_hat_35_1 = 0.5
n_35_1 = p_hat_35_1 * (1 - p_hat_35_1) * (z_c_35 / E_35)**2
# Caso 2: Estimativa anterior p̂=0.31
p_hat_35_2 = 0.31
n_35_2 = p_hat_35_2 * (1 - p_hat_35_2) * (z_c_35 / E_35)**2
# Resultado obtido:
# Caso 1: n = 1691.26 -> 1692
# Caso 2: n = 1446.05 -> 1447
# ============================================================================== #
print(f"35. Caso 1: n = {math.ceil(n_35_1)}, Caso 2: n = {math.ceil(n_35_2)}")
# 36. 
# Valores críticos Qui-quadrado. 90% confiança, n=30.
confianca_36, n_36 = 0.90, 30
df_36 = n_36 - 1
alfa_36 = 1 - confianca_36
chi2_L = chi2.ppf(alfa_36 / 2, df=df_36)
chi2_R = chi2.ppf(1 - alfa_36 / 2, df=df_36)
# Resultado obtido:
# df = 29
# χ²L (crítico à esquerda) = 17.708
# χ²R (crítico à direita) = 42.557
print(f"36. χ²L = {chi2_L:.3f}, χ²R = {chi2_R:.3f}")
# ============================================================================== #
# 37. 
# IC 90% e 95% para variância (σ²) e desvio padrão (σ). n=30, s=1.20.
n_37, s_37 = 30, 1.20
df_37 = n_37 - 1
s2_37 = s_37**2
# Para 90% de confiança
chi2_L_90 = chi2.ppf(0.05, df=df_37)
chi2_R_90 = chi2.ppf(0.95, df=df_37)
ic_var_90 = ((df_37 * s2_37) / chi2_R_90, (df_37 * s2_37) / chi2_L_90)
ic_dp_90 = (math.sqrt(ic_var_90[0]), math.sqrt(ic_var_90[1]))
# Para 95% de confiança
chi2_L_95 = chi2.ppf(0.025, df=df_37)
chi2_R_95 = chi2.ppf(0.975, df=df_37)
ic_var_95 = ((df_37 * s2_37) / chi2_R_95, (df_37 * s2_37) / chi2_L_95)
ic_dp_95 = (math.sqrt(ic_var_95[0]), math.sqrt(ic_var_95[1]))
# Resultado obtido:
# IC 90% para Variância: (0.981, 2.358)
# IC 90% para Desvio Padrão: (0.990, 1.536)
# IC 95% para Variância: (0.898, 2.622)
# IC 95% para Desvio Padrão: (0.948, 1.619)
print(f"37. IC 90% para σ²: ({ic_var_90[0]:.3f}, {ic_var_90[1]:.3f}), IC 90% para σ: ({ic_dp_90[0]:.3f}, {ic_dp_90[1]:.3f})")
print(f"    IC 95% para σ²: ({ic_var_95[0]:.3f}, {ic_var_95[1]:.3f}), IC 95% para σ: ({ic_dp_95[0]:.3f}, {ic_dp_95[1]:.3f})")
# ============================================================================== #
# 38. 
# 1. Afirmação: µ ≠ 74 meses. 
#    H0: µ = 74 meses
#    Ha: µ ≠ 74 meses (A afirmação)
# 2. Afirmação: σ² ≤ 2.7. 
#    H0: σ² ≤ 2.7 (A afirmação)
#    Ha: σ² > 2.7
# 3. Afirmação: p > 0.24. 
#    H0: p ≤ 0.24
#    Ha: p > 0.24 (A afirmação)
print("38. (H0, Ha) para cada afirmação listada")
# ============================================================================== #
# 39. 
# Afirmação da empresa: taxa de falha ≤ 1% (p ≤ 0.01). Testar se é falsa.
# H0: p ≤ 0.01 (Afirmação da empresa)
# Ha: p > 0.01
# Erro Tipo I: Rejeitar H0 quando H0 é verdadeira. Concluir que a taxa de
#   falha é > 1%, quando na verdade não é. A empresa seria penalizada
#   injustamente.
# Erro Tipo II: Não rejeitar H0 quando H0 é falsa. Concluir que a taxa de
#   falha é ≤ 1%, quando na verdade é maior. Pessoas usariam um paraquedas
#   mais perigoso do que o divulgado.
# Mais grave: Erro Tipo II, pois coloca vidas em risco.
print("39. Análise dos erros Tipo I e II")
# ============================================================================== #
# 40. 
# 1. µ ≠ 74 meses. 
#    H0: µ = 74 meses; Ha: µ ≠ 74 meses. Teste BILATERAL.
# 2. p > 24%. 
#    H0: p ≤ 0.24; Ha: p > 0.24. Teste UNILATERAL À DIREITA.
# ============================================================================== #
print("40. Testes unilaterais e bilaterais")
# 41. 
# 1. H0 (afirmação): p = 0.61. 
#    - Se rejeitar H0: Há evidência suficiente para rejeitar a afirmação da
#      escola de que a proporção é 61%.
#    - Se não rejeitar H0: Não há evidência suficiente para rejeitar a
#      afirmação da escola de que a proporção é 61%.
# 2. Ha (afirmação): µ < 15 minutos. 
#    - Se rejeitar H0: Há evidência suficiente para apoiar a afirmação da
#      concessionária de que o tempo médio é menor que 15 min.
#    - Se não rejeitar H0: Não há evidência suficiente para apoiar a
#      afirmação da concessionária.
# ============================================================================== #
print("41. Decisões em testes de hipóteses")
# 42. 
# Ha (afirmação): p > 0.24.
#    - Se rejeitar H0: Há evidência suficiente para apoiar a afirmação do
#      corretor de que a proporção é maior que 24%.
#    - Se não rejeitar H0: Não há evidência suficiente para apoiar a
#      afirmação do corretor.
# ============================================================================== #
print("42. Decisões em testes de hipóteses (continuação)")
# 43. 
# Teste unilateral à esquerda, z = -1.71, α = 0.05.
z_43, alfa_43 = -1.71, 0.05
p_valor_43 = norm.cdf(z_43)
# Decisão: Rejeitar H0 se p-valor ≤ α.
decisao_43 = "Rejeitar H0" if p_valor_43 <= alfa_43 else "Não Rejeitar H0"
# Resultado obtido:
# p-valor = 0.0436
# Como 0.0436 ≤ 0.05, a decisão é Rejeitar H0.
# ============================================================================== #
print(f"43. p-valor = {p_valor_43:.4f}. Decisão: {decisao_43}")
# 44. 
# Teste bilateral, z = 1.64, α = 0.10.
z_44, alfa_44 = 1.64, 0.10
# p-valor para teste bilateral é 2 * (área na cauda)
p_valor_44 = 2 * norm.sf(abs(z_44))
decisao_44 = "Rejeitar H0" if p_valor_44 <= alfa_44 else "Não Rejeitar H0"
# Resultado obtido:
# p-valor = 0.1010
# Como 0.1010 > 0.10, a decisão é Não Rejeitar H0.
# ============================================================================== #
print(f"44. p-valor = {p_valor_44:.4f}. Decisão: {decisao_44}")
# 45. 
# H0: µ ≤ 35, Ha: µ > 35 (afirmação). n=100, x̄=36, σ=4, α=0.05.
mu0_45, n_45, x_bar_45, sigma_45, alfa_45 = 35, 100, 36, 4, 0.05
z_45 = (x_bar_45 - mu0_45) / (sigma_45 / math.sqrt(n_45))
p_valor_45 = norm.sf(z_45) # Teste unilateral à direita
decisao_45 = "Rejeitar H0" if p_valor_45 <= alfa_45 else "Não Rejeitar H0"
# Resultado obtido:
# z = 2.5
# p-valor = 0.0062
# Decisão: Rejeitar H0. Há evidência para apoiar a afirmação.
# ============================================================================== #
print(f"45. z = {z_45:.4f}, p-valor = {p_valor_45:.4f}. Decisão: {decisao_45}")
# 46. 
# H0: µ = 3 (afirmação), Ha: µ ≠ 3. n=25, x̄=3.3, σ=0.5, α=0.01.
mu0_46, n_46, x_bar_46, sigma_46, alfa_46 = 3, 25, 3.3, 0.5, 0.01
z_46 = (x_bar_46 - mu0_46) / (sigma_46 / math.sqrt(n_46))
p_valor_46 = 2 * norm.sf(abs(z_46)) # Teste bilateral
decisao_46 = "Rejeitar H0" if p_valor_46 <= alfa_46 else "Não Rejeitar H0"
# Resultado obtido:
# z = 3.0
# p-valor = 0.0027
# Decisão: Rejeitar H0. Há evidência para duvidar da afirmação do estudo.
# ============================================================================== #
print(f"46. z = {z_46:.4f}, p-valor = {p_valor_46:.4f}. Decisão: {decisao_46}")
# 47. 
# Valor crítico, teste unilateral à esquerda, α = 0.10.
alfa_47 = 0.10
z_critico_47 = norm.ppf(alfa_47)
# Resultado obtido: z_c = -1.2816
# Região de rejeição: z ≤ -1.2816
# ============================================================================== #
print(f"47. z_c = {z_critico_47:.4f}")
# 48. 
# Valores críticos, teste bilateral, α = 0.08.
alfa_48 = 0.08
z_critico_inf_48 = norm.ppf(alfa_48 / 2)
z_critico_sup_48 = norm.ppf(1 - alfa_48 / 2)
# Resultado obtido: z_c = ±1.7507
# Regiões de rejeição: z ≤ -1.7507 ou z ≥ 1.7507
# ============================================================================== #
print(f"48. z_c = ±{z_critico_sup_48:.4f}")
# 49.
# Parte 1: Salários 
# H0: µ ≥ 68000, Ha: µ < 68000 (afirmação). n=20, x̄=66900, σ=5500, α=0.05.
mu0_49_1, n_49_1, x_bar_49_1, sigma_49_1, alfa_49_1 = 68000, 20, 66900, 5500, 0.05
z_49_1 = (x_bar_49_1 - mu0_49_1) / (sigma_49_1 / math.sqrt(n_49_1))
z_crit_49_1 = norm.ppf(alfa_49_1)
decisao_49_1 = "Rejeitar H0" if z_49_1 <= z_crit_49_1 else "Não Rejeitar H0"
# Resultado obtido (Parte 1):
# z = -0.8948, z_c = -1.6449.
# Decisão: Não Rejeitar H0. Não há evidência para apoiar a afirmação.
#
# Parte 2: Horas 
# H0: µ ≥ 8.5, Ha: µ < 8.5 (afirmação). n=25, x̄=8.2, σ=0.5, α=0.01.
mu0_49_2, n_49_2, x_bar_49_2, sigma_49_2, alfa_49_2 = 8.5, 25, 8.2, 0.5, 0.01
z_49_2 = (x_bar_49_2 - mu0_49_2) / (sigma_49_2 / math.sqrt(n_49_2))
z_crit_49_2 = norm.ppf(alfa_49_2)
decisao_49_2 = "Rejeitar H0" if z_49_2 <= z_crit_49_2 else "Não Rejeitar H0"
# Resultado obtido (Parte 2):
# z = -3.0, z_c = -2.3263
# Decisão: Rejeitar H0. Há evidência para apoiar a afirmação do presidente.
# ============================================================================== #
print(f"49.1. z = {z_49_1:.4f}, z_c = {z_crit_49_1:.4f}. Decisão: {decisao_49_1}")
print(f"49.2. z = {z_49_2:.4f}, z_c = {z_crit_49_2:.4f}. Decisão: {decisao_49_2}")
# 50. 
# H0: µ = 13960 (afirmação), Ha: µ ≠ 13960. n=500, x̄=13725, σ=2345.
mu0_50, n_50, x_bar_50, sigma_50 = 13960, 500, 13725, 2345
z_50 = (x_bar_50 - mu0_50) / (sigma_50 / math.sqrt(n_50))
# Teste para α = 0.10
alfa_50_1 = 0.10
z_crit_50_1 = norm.ppf(1 - alfa_50_1 / 2)
decisao_50_1 = "Rejeitar H0" if abs(z_50) >= z_crit_50_1 else "Não Rejeitar H0"
# Teste para α = 0.01
alfa_50_2 = 0.01
z_crit_50_2 = norm.ppf(1 - alfa_50_2 / 2)
decisao_50_2 = "Rejeitar H0" if abs(z_50) >= z_crit_50_2 else "Não Rejeitar H0"
# Resultado obtido:
# z = -2.2423
# Para α=0.10 (z_c=1.645): Rejeitar H0.
# Para α=0.01 (z_c=2.576): Não Rejeitar H0.
# ============================================================================== #
print(f"50. z = {z_50:.4f}. Para α=0.10: {decisao_50_1}, Para α=0.01: {decisao_50_2}")

# 51. 
# Valor crítico t0. Teste unilateral à direita, α=0.10, n=9.
alfa_51, n_51 = 0.10, 9
df_51 = n_51 - 1
t0_51 = t.ppf(1 - alfa_51, df=df_51)
# Resultado obtido: t0 = 1.397
# ============================================================================== #
print(f"51. t0 = {t0_51:.3f}")
# 52.
# Valores críticos -t0 e t0. Teste bilateral, α=0.05, n=16.
alfa_52, n_52 = 0.05, 16
df_52 = n_52 - 1
t0_52 = t.ppf(1 - alfa_52 / 2, df=df_52)
# Resultado obtido: t0 = ±2.131
# ============================================================================== #
print(f"52. t0 = ±{t0_52:.3f}")
# 53. 
# H0: µ ≥ 1200, Ha: µ < 1200 (afirmação). n=7, x̄=1125, s=55, α=0.10.
mu0_53, n_53, x_bar_53, s_53, alfa_53 = 1200, 7, 1125, 55, 0.10
df_53 = n_53 - 1
t_stat_53 = (x_bar_53 - mu0_53) / (s_53 / math.sqrt(n_53))
t_crit_53 = t.ppf(alfa_53, df=df_53) # Unilateral à esquerda
decisao_53 = "Rejeitar H0" if t_stat_53 <= t_crit_53 else "Não Rejeitar H0"
# Resultado obtido:
# t_stat = -3.602, t_crit = -1.440
# Decisão: Rejeitar H0. Há evidência para concordar com o agente.
# ============================================================================== #
print(f"53. t = {t_stat_53:.3f}, t_c = {t_crit_53:.3f}. Decisão: {decisao_53}")
# 54.
# Parte 1: pH 
# H0: µ = 6.8 (afirmação), Ha: µ ≠ 6.8. n=39, x̄=6.7, s=0.35, α=0.05.
mu0_54_1, n_54_1, x_bar_54_1, s_54_1, alfa_54_1 = 6.8, 39, 6.7, 0.35, 0.05
df_54_1 = n_54_1 - 1
t_stat_54_1 = (x_bar_54_1 - mu0_54_1) / (s_54_1 / math.sqrt(n_54_1))
t_crit_54_1 = t.ppf(1 - alfa_54_1 / 2, df=df_54_1)
decisao_54_1 = "Rejeitar H0" if abs(t_stat_54_1) >= t_crit_54_1 else "Não Rejeitar H0"
# Resultado obtido (Parte 1):
# t_stat = -1.784, t_crit = ±2.024
# Decisão: Não Rejeitar H0. Não há evidência para rejeitar a afirmação.
#
# Parte 2: Condutividade 
# H0: µ = 1890 (afirmação), Ha: µ ≠ 1890. n=39, x̄=2350, s=900, α=0.01.
mu0_54_2, n_54_2, x_bar_54_2, s_54_2, alfa_54_2 = 1890, 39, 2350, 900, 0.01
df_54_2 = n_54_2 - 1
t_stat_54_2 = (x_bar_54_2 - mu0_54_2) / (s_54_2 / math.sqrt(n_54_2))
t_crit_54_2 = t.ppf(1 - alfa_54_2 / 2, df=df_54_2)
decisao_54_2 = "Rejeitar H0" if abs(t_stat_54_2) >= t_crit_54_2 else "Não Rejeitar H0"
# Resultado obtido (Parte 2):
# t_stat = 3.193, t_crit = ±2.708
# Decisão: Rejeitar H0. Há evidência para rejeitar a afirmação da indústria.
# ============================================================================== #
print(f"54.1. t = {t_stat_54_1:.3f}, t_c = ±{t_crit_54_1:.3f}. Decisão: {decisao_54_1}")
print(f"54.2. t = {t_stat_54_2:.3f}, t_c = ±{t_crit_54_2:.3f}. Decisão: {decisao_54_2}")
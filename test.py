def find_diameter():
    def patrons_number(Gmax, q_p):
        n_p = Gmax / q_p
        return n_p

    def patrons_recommended_number(n_p):
        n_values = [1, 3, 7, 10, 15, 24, 44]
        filter_diam_values = [0.15, 0.25, 0.35, 0.42, 0.5, 0.6, 0.8]
        F_values = [0.32, 0.96, 2.24, 3.2, 4.8, 7.68, 14.08]
        # Находим индекс для соответствующих значений
        index = next((i for i, v in enumerate(n_values)
                     if n_p < v), len(n_values) - 1)
        n = n_values[index]
        filter_diam = filter_diam_values[index]
        F = F_values[index]
        return (n, F, filter_diam)

    def find_nearest_value(d):
        # Ряд возможных значений
        values = [0.025, 0.05, 0.08, 0.1, 0.15, 0.2, 0.25, 0.3, 0.4, 0.5]
        return min(values, key=lambda x: abs(x - d))

    F = 3.14 * DN * L * 1e4
    q_p = 0.06 * k * ((DELTP * F * ROJ) / MU)
    n_p = patrons_number(Gmax, q_p)
    n, F, DN = patrons_recommended_number(n_p)
    W_sh = 1
    while (1 < W_sh < 2):
        d_shtr = math.sqrt(Gmax / (3600 * ROJ * 0.785 * W_sh))
        d_shtr = find_nearest_value(d_shtr)
        if d_shtr <= 0.5 * DN:
            break
        else:
            n = patrons_number + 1
            n, F, DN = patrons_recommended_number(n)
        W_sh = Gmax / (3600 * ROJ * 0.785 * d_shtr ** 2)

    # xi_inlet = 1
    # xi_outlet = 0.5
    delta_P_shtr = (1.5) * \
        (W_sh ** 2 * ROJ) / (2 * 9.81 * 1e5)
    alpha = 1.1
    delta_P_total = alpha * (DELTP + delta_P_shtr)
    # Проверка условия delta_P_total <= DELTPF
    if delta_P_total <= DELTPF:
        result = "Условие delta_P_total <= DELTPF выполняется."
    else:
        result = "Необходимо увеличить диаметр аппарата."


# Получаем значения из полей ввода
Gmax = 1815
P = 0.35
T = 38.6
k = 0.033
DN = 0.09
L = 1.1
DELTP = 0.015
MU = 0.0124
ROJ = 1098
DELTPF = 0.05
NZAD = 7
DHZAD = 0.05


find_diameter()

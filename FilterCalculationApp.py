import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QTextEdit, QGroupBox
import math


class FilterCalculationApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Filter Calculation')
        self.setGeometry(120, 120, 620, 420)

        self.init_input_fields()
        self.init_output_text()

        self.calculate_button = QPushButton('Рассчитать', self)
        self.calculate_button.clicked.connect(self.calculate)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.input_group)
        main_layout.addWidget(self.calculate_button)
        main_layout.addWidget(self.output_text)

        self.setLayout(main_layout)

    def init_input_fields(self):
        self.input_group = QGroupBox("Ввод данных")

        self.Gmax_label = QLabel('Производительность по жидкости, кг/ч:')
        self.Gmax_input = QLineEdit(self)

        self.P_label = QLabel('Давление рабочее, избыточное МПа:')
        self.P_input = QLineEdit(self)

        self.T_label = QLabel('Температура рабочая, °С:')
        self.T_input = QLineEdit(self)

        self.k_label = QLabel(f'Коэффициент пропорциональности '
                              f'(k=0,033 для ДЭГа, k=0,0086 для воды):')
        self.k_input = QLineEdit(self)

        self.DN_label = QLabel(
            'Наружный диаметр патрона (рекомендуется DN=0,093 м), м:')
        self.DN_input = QLineEdit(self)

        self.L_label = QLabel(
            'Длина патрона (рекомендуется L=1,1 м), м:')
        self.L_input = QLineEdit(self)

        self.DELTP_label = QLabel(f'Гидравлическое сопротивление чистого '
                                  f'патрона (рекомендуется DELTP=0,015 МПа), МПа:')
        self.DELTP_input = QLineEdit(self)

        self.MU_label = QLabel('Коэффициент динамической вязкости, Па∙с:')
        self.MU_input = QLineEdit(self)

        self.ROJ_label = QLabel('Плотность жидкости, кг/м3:')
        self.ROJ_input = QLineEdit(self)

        self.DELTPD_label = QLabel(
            'Допустимый перепад давления на фильтре, МПа:')
        self.DELTPD_input = QLineEdit(self)

        # self.NZAD_label = QLabel(
        #     'Количество фильтрующих патронов, шт:')
        # self.NZAD_input = QLineEdit(self)

        # self.DHZAD_label = QLabel(
        #     'Диаметр штуцера входа (выхода) жидкости, м:')
        # self.DHZAD_input = QLineEdit(self)

        input_layout = QVBoxLayout()
        input_layout.addWidget(self.Gmax_label)
        input_layout.addWidget(self.Gmax_input)
        input_layout.addWidget(self.P_label)
        input_layout.addWidget(self.P_input)
        input_layout.addWidget(self.T_label)
        input_layout.addWidget(self.T_input)
        input_layout.addWidget(self.k_label)
        input_layout.addWidget(self.k_input)
        input_layout.addWidget(self.DN_label)
        input_layout.addWidget(self.DN_input)
        input_layout.addWidget(self.L_label)
        input_layout.addWidget(self.L_input)
        input_layout.addWidget(self.DELTP_label)
        input_layout.addWidget(self.DELTP_input)
        input_layout.addWidget(self.MU_label)
        input_layout.addWidget(self.MU_input)
        input_layout.addWidget(self.ROJ_label)
        input_layout.addWidget(self.ROJ_input)
        input_layout.addWidget(self.DELTPD_label)
        input_layout.addWidget(self.DELTPD_input)
        # input_layout.addWidget(self.NZAD_label)
        # input_layout.addWidget(self.NZAD_input)
        # input_layout.addWidget(self.DHZAD_label)
        # input_layout.addWidget(self.DHZAD_input)

        self.input_group.setLayout(input_layout)

    def init_output_text(self):
        self.output_text = QTextEdit(self)

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

    def calculate(self):
        # Получаем значения из полей ввода
        Gmax = float(self.Gmax_input.text())
        P = float(self.P_input.text())
        T = float(self.T_input.text())
        k = float(self.k_input.text())
        DN = float(self.DN_input.text())
        L = float(self.L_input.text())
        DELTP = float(self.DELTP_input.text())
        MU = float(self.MU_input.text())
        ROJ = float(self.ROJ_input.text())
        DELTPD = float(self.DELTPD_input.text())
        # NZAD = float(self.NZAD_input.text())
        # DHZAD = float(self.DHZAD_input.text())

        # Расчет
        def patrons_number(Gmax, q_p):
            n_p = Gmax / q_p
            return n_p

        def find_q(Gmax, n):
            q = Gmax/n
            return q

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
        W_sh = 1.5
        q = find_q(Gmax, n)

        while True:
            while True:
                d_shtr = math.sqrt(Gmax / (3600 * ROJ * 0.785 * W_sh))
                d_shtr = find_nearest_value(d_shtr)
                if d_shtr <= 0.5 * DN:
                    break
                else:
                    n = patrons_number + 1
                    n, F, DN = patrons_recommended_number(n)
                    q = find_q(Gmax, n)
                W_sh = Gmax / (3600 * ROJ * 0.785 * d_shtr ** 2)
            DELTPSHT = (1.5) * \
                (W_sh ** 2 * ROJ) / (2 * 9.81 * 1e5)
            alpha = 1.1
            DELTP = 0.015
            DELTPF = alpha * (DELTP + DELTPSHT)
            if DELTPF <= DELTPD:
                break
            else:
                continue

        # Вывод результатов
        result = f"""
                       Технологический расчет фильтра тонкой очистки

                              Данные для расчета
        
                          Вид расчета - проектный

        Производительность по жидкости максимальная: {Gmax} кг/ч
        Давление рабочее, избыточное: {P} МПа
        Температура рабочая, {T} °С
        Коэффициент пропорциональности: {k}
        Наружный диаметр патрона, {DN} м
        Длина патрона: {L} м
        Гидравлическое сопротивление чистого патрона: {DELTP} МПа
        Коэффициент динамической вязкости жидкости: {MU} Па*с
        Плотность жидкости: {ROJ} кг/м3
        Допустимый перепад давления на фильтре: {DELTPD} МПа

        
                                           Результаты расчета

        Производительность одного фильтрующего патрона:
        Расчетная: {q_p} кг/ч
        Действительная: {q} кг/ч
        Поверхность фильтрации патрона: {F} см^2
        Количество фильтрующих патронов:
        расчетное: {n_p} шт
        действительное: {n} шт
        Диаметр фильтра: {DN} м
        Диаметр штуцера входа (выхода) жидкости: {d_shtr} м
        Скорость жидкости в штуцере входа (выхода): {W_sh} м/с
        Гидравлическое сопротивление в штуцерах входа (выхода) жидкости: {DELTPSHT} МПа
        Действительное гидравлическое сопротивление чистого патрона: {DELTPD} МПа
        Гидравлическое сопротивление чистого фильтра: {DELTPF} МПа

                                                   Заключение 
        На основании проведенного технологического расчета на заданные условия принят фильтр тонкой очистки диаметром {DN} м и количеством фильтрующих патронов {n} шт.
        Гидравлическое сопротивление чистого фильтра {DELTPF} МПа.
        Номинальная тонкость фильтрации 20 мкм данная конструкция обеспечивает максимальную производительность по жидкости {Gmax} кг/ч

        Действительная скорость жидкости в штуцере: {W_sh} м/с
        Гидравлическое сопротивление штуцеров: {DELTPSHT} МПа
        """

        # Отображение результата в текстовом поле
        self.output_text.setPlainText(result)


def main():
    app = QApplication(sys.argv)
    ex = FilterCalculationApp()
    ex.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

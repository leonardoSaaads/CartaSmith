# Feito por Leonardo Saads Pinto
# Setembro - 2021

# Importando as bibliotecas padrões.
import numpy as np
import matplotlib.pyplot as plt


class CartaSmith:
    """
    BIBLIOTECA PARA FUNCIONALIDADES DA CARTA DE SMITH

    FUNÇÕES:
    - AJUSTAR
    - SUMARIO
    - PLOT_SMITH
    - PLOT COEFICIENTES
    """

    def __init__(self, RF=None, ZN=None, ZL=None, Z0=None):
        # Impedancia Característica (Z0): float
        self.__Z0 = Z0
        # Impedancia da Onda (ZL): list
        self.__ZL = ZL
        # Impedancia Normalizada (ZN): list
        self.__ZN = ZN
        # Coeficiente de Reflexão (RF): list
        self.__RF = RF

    # DEFININDO GETTERS

    @property
    def Z0(self):
        """
        Getter para a impedancia característica.
        :return: impedancia característica Z0.
        """
        return self.__Z0

    @property
    def ZL(self):
        """
        Getter para a impedancia de onda.
        :return: impedancia de onda ZL.
        """
        return self.__ZL

    @property
    def ZN(self):
        """
        Getter para a impedancia normalizada.
        :return: impedancia de onda ZN.
        """
        return self.__ZN

    @property
    def RF(self):
        """
        Getter para o coeficiente de reflexão da onda.
        :return: coeficiente de reflexão da onda.
        """
        return self.__RF

    # DEFININDO SETTERS

    @Z0.setter
    def Z0(self, valor):
        """
        Setter para a Impedancia Característica.
        :param valor: parâmetro Z0.
        :return: None
        """
        self.__Z0 = valor

    @ZL.setter
    def ZL(self, valor):
        """
        Setter para a Impedancia de Onda.
        :param valor: parâmetro ZL (número complexo).
        :return: None
        """
        self.__ZL = valor

    @ZN.setter
    def ZN(self, valor):
        """
        Setter para a Impedancia Normalizada..
        :param valor: Parâmetro ZN (número complexo).
        :return: None
        """
        self.__ZN = valor

    @RF.setter
    def RF(self, valor):
        """
        Setter para a Coeficiente de Reflexão.
        :param valor: Coeficiente de Reflexão (número complexo).
        :return: None
        """
        self.__RF = valor

    # FUNÇÕES DE AJUSTES

    def ajustar(self):
        """
        Essa Função irá ajustar todos os parâmetros com base em determinados dados de entrada.
        :return: Null
        """
        # NECESSÁRIO UM FOR QUE RODE 2 VEZES (atualizar 2 dados)
        for i in range(2):
            # Ajuste do ZO
            if self.__ZL is not None and self.__ZN is not None and self.__Z0 is None:
                self.__Z0 = np.mean(self.__ZL / self.__ZN)

            # Ajuste do ZL
            if self.__Z0 is not None and self.__ZN is not None and self.__ZL is None:
                self.__ZL = self.__ZN * self.__Z0

            # Ajuste do ZN
            if self.__ZL is not None and self.__Z0 is not None and self.__ZN is None:
                self.__ZN = self.__ZL / self.__Z0

            if self.__RF is not None and self.__ZN is None:
                self.__ZN = (-self.__RF - 1)/(self.__RF - 1)

            # Ajude da Reflexão
            if self.ZL is not None and self.Z0 is not None and self.RF is None:
                self.__RF = (self.ZL - self.Z0)/(self.ZL + self.Z0)

    # FUNÇÕES DE INFORMAÇÕES

    def sumario(self):
        """
        Printa o sumário de todos os parâmetros da carta de Smith.
        :return: Null
        """

        lista_parametros = [self.RF, self.ZN, self.Z0, self.ZL]
        parametros_desconhecidos = [1 for item in lista_parametros if item is None]

        print(f'--------------------- MODELO ---------------------\n'  
              f'Impedância Característica:       {self.Z0}\n'
              f'Impedãncia de Onda:              {self.ZL}\n'
              f'Impedância Normalizada:          {self.ZN}\n'
              f'Coeficiente de Reflexão:         {self.RF}\n'
              f'--------------------------------------------------\n'
              f'O número de parâmetros desconhecidos é: {sum(parametros_desconhecidos)}\n'
              f'--------------------------------------------------')

        # ALERTAS PARA USUÁRIOS:
        if sum(parametros_desconhecidos) == 2:
            print('ATENÇÃO: Utilize o comando ".ajustar()" para determinar os parâmetros desconhecidos.\n')

        if sum(parametros_desconhecidos) == 3:
            print('ATENÇÃO: Informado apenas um parâmetro. Adicione outro para prosseguir.\n')

    # FUNÇÕES DE PLOTAGEM E ANÁLISE GRÁFICA

    # PLOTANDO A CARTA DE SMITH - SERVE DE BASE PARA AS OUTRAS FUNÇÕES
    @staticmethod
    def plotar_carta():

        # FUNÇÃO PARA A PLOTAGEM DOS CÍRCULOS
        def circulo(xc, yc, r, a1=0, a2=2*np.pi):
            # Theta vai de 0 à 2*pi particionado em 360 vezes. (OBS: Graus)
            theta = np.linspace(a1, a2, 360)
            # Parametrização do cículo.
            x = xc + r * np.cos(theta)
            y = yc + r * np.sin(theta)
            return x, y

        # DEFININDO A QUANTIDADE DE RAIOS QUE SERÃO PLOTADOS - EIXO X
        raios_eixo_x = np.linspace(0, 1, 5)
        raios_eixo_y = [0.1, 0.5, 1, 2, 4]
        a1_y = [1.8, 2.5, np.pi, 3.79, 4.22]

        # PLOTANDO OS RAIOS NO EIXO X
        for r in raios_eixo_x:
            # create the figure
            x, y = circulo(r, 0, 1 - r)
            plt.plot(x, y, color='black')

        # PLOTANDO OS RAIOS NO EIXO Y
        for i in range(len(raios_eixo_y)):
            x, y = circulo(1, raios_eixo_y[i], raios_eixo_y[i], a1_y[i], 3/2*np.pi)
            plt.plot(x, y, color='black')
            x, y = circulo(1, -raios_eixo_y[i], raios_eixo_y[i], np.pi/2, 2*np.pi - a1_y[i])
            plt.plot(x, y, color='black')

       # LINHA ENTRE (-1,0) À (1, 0)
        plt.plot([-1, 1], [0, 0], color='black')

        # PLOTANDO PONTOS IMPORTANTES
        plt.plot(0, 0, color='black', marker='o')
        plt.plot(-1, 0, color='black', marker='>')
        plt.plot(0, 1, color='black', marker='v')
        plt.plot(0, -1, color='black', marker='^')

        # EIXOS
        plt.axis('equal')
        plt.axis('off')

        # PLOTANDO O TÍTULO
        plt.title("Carta de Smith")

    def plotar_coeficiente(self):
        if self.RF is not None:
            self.plotar_carta()
            plt.plot(self.RF.real, self.RF.imag, 'ro', label="Coeficientes Reflexão")
            plt.show()
        else:
            print('Parâmetro dos coeficientes de reflexão não determinados.\n')


if __name__ == '__main__':
    teste2 = CartaSmith(
        ZL=np.array([100 + 50j, 75 - 100j, 200j, 150, 999999, 0, 50, 184-900j])
    )
    teste2.sumario()
    teste2.Z0 = 50
    teste2.ajustar()
    teste2.sumario()
    teste2.plotar_coeficiente()

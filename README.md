# Carta de Smith -  Smith Chart

<img style="-webkit-user-select: none;margin: auto;background-color: hsl(0, 0%, 90%);transition: background-color 300ms;" src="https://raw.githubusercontent.com/leonardoSaaads/CartaSmith/main/Imagens%20Projeto/Azul%20Companhia%20A%C3%A9rea%20Geral%20LinkedIn%20Banner.png?token=AQUTBFUQW2IRELV436CSF4DBJSHV2" width="800" height="200">

<a href="https://github.com/leonardoSaaads/CartaSmith/issues"><img alt="GitHub issues" src="https://img.shields.io/github/issues/leonardoSaaads/CartaSmith"></a>
<a href="https://github.com/leonardoSaaads/CartaSmith/network"><img alt="GitHub forks" src="https://img.shields.io/github/forks/leonardoSaaads/CartaSmith"></a>
<a href="https://github.com/leonardoSaaads/CartaSmith/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/leonardoSaaads/CartaSmith"></a>

## STATUS DO PROJETO: *EM CONSTRUÇÃO.* ✅


## TABELA
* Sobre
* Instalação
* Como Utilizar
* Funcionalidades
* Pré-Requisitos
* Autor
* Licença


## Sobre

A Carta de Smith é uma ferramenta gráfica muito utilizada em radares, antenas e em pesquisas que envolvem o desenvolvimento de parâmetros relacionados ao casamento de impedância. Nesse sentido, é válido explorar as funcionalidades que envolvam Impedância, Transmissão e Reflexão de ondas com esse importante mecanismo. Essa carta é baseada em um modelo complexo, isto é, o plano de plano de Argand-Gauss, para a plotagem de curvas e pontos específicos. Assim sendo, o foco dessa biblioteca é uma rica análise gráfica baseada em na liguagem Python e uma automação de Parâmetros relativos à valores característicos de circuitos elétricos.

## Instalação

Para o uso e instalação, são necessárias as bibliotecas abaixo previamente instaladas:

* matplotlib
* numpy

Após a garantida dessas bibliotecas, basta utilizar o arquivo, disponível [aqui](), como uma biblioteca e desfrutar de suas funcionalidades.

## Funcionalidades

* Sumário

```
--------------------- MODELO ---------------------
Impedância Característica:       90
Impedãncia de Onda:              (100+120j)
Impedância Normalizada:          None
Coeficiente de Reflexão:         None
--------------------------------------------------
O número de parâmetros desconhecidos é: 2
--------------------------------------------------
ATENÇÃO: Utilize o comando ".ajustar()" para determinar os parâmetros desconhecidos.
```

* Ajustes (Automação de manejo de informações)

```
--------------------- MODELO ---------------------
Impedância Característica:       90
Impedãncia de Onda:              (100+120j)
Impedância Normalizada:          (1.1111111111111112+1.3333333333333333j)
Coeficiente de Reflexão:         (0.3227722772277228+0.42772277227722777j)
--------------------------------------------------
O número de parâmetros desconhecidos é: 0
--------------------------------------------------
```

* Plotagem

<img style="-webkit-user-select: none;margin: auto;cursor: zoom-in;background-color: hsl(0, 0%, 90%);transition: background-color 300ms;" src="https://raw.githubusercontent.com/leonardoSaaads/CartaSmith/main/Imagens%20Projeto/Figure_1.png" width="476" height="357">

<img style="-webkit-user-select: none;margin: auto;cursor: zoom-in;background-color: hsl(0, 0%, 90%);transition: background-color 300ms;" src="https://raw.githubusercontent.com/leonardoSaaads/CartaSmith/main/Imagens%20Projeto/Figure_2.png" width="476" height="357">

## Como Utilizar:

Para utilizar a biblioteca, você pode adicionar os parâmetros na chamada da classe.
Exemplo: 
```
exemplo = CartaSmith(
        Z0=50,
        ZL=[50 + 50j, 50 + 49j, 50 + 48j, 50 + 38j, 50 + 12j]
    )
```
ou colocando-se diretamente na classe feita.
Exemplo:
```
    exemplo = CartaSmith()
    exemplo.Z0 = 50
    vetor = np.arange(0, 2 * np.pi, 0.1)
    exemplo.ZL = 50 + 50j * np.sin(vetor)
```
Utilize o comando ```.sumario()``` para exibir o sumário.

Utilize o comando ```.ajustar()``` para adequart todos os valores da classe.

## Autores

By Leonardo Saads Pinto

2021 - Setembro

# ENGLISH

## PROJECT STATUS: *UNDER CONSTRUCTION.* ✅


## TABLE
* About
* Installation
* How to use
* Functionalities
* Prerequisites
* Author
* License


## About

Smith's Chart is a graphical tool widely used in radar, antennas and in research involving the development of parameters related to impedance matching. In this sense, it is worth exploring the functionalities involving Impedance, Transmission and Reflection of waves with this important mechanism. This chart is based on a complex model, ie the Argand-Gauss plane plane, for plotting specific curves and points. Therefore, the focus of this library is a rich graphical analysis based on the Python language and an automation of parameters related to characteristic values of electrical circuits.

## Installation

For use and installation, the libraries previously installed below are required:

* matplotlib
* numpy

After these libraries are guaranteed, just use the file, available [here](), as a library and enjoy its functionalities.

## Functionalities

* Summary

```
--------------------- MODEL ---------------------
Characteristic Impedance: 90
Wave Impedance: (100+120j)
Normalized Impedance: None
Reflection Coefficient: None
-------------------------------------------------
The number of unknown parameters is: 2
-------------------------------------------------
ATTENTION: Use the ".adjust()" command to determine the unknown parameters.
```

* Adjustments (Information handling automation)

```
--------------------- MODEL ---------------------
Characteristic Impedance: 90
Wave Impedance: (100+120j)
Normalized Impedance: (1.11111111111111112+1.3333333333333333j)
Reflection Coefficient: (0.3227722772277228+0.42772277227722777j)
-------------------------------------------------
The number of unknown parameters is: 0
-------------------------------------------------
```

* Plot


<img style="-webkit-user-select: none;margin: auto;cursor: zoom-in;background-color: hsl(0, 0%, 90%);transition: background-color 300ms;" src="https://raw.githubusercontent.com/leonardoSaaads/CartaSmith/main/Imagens%20Projeto/Figure_1.png" width="476" height="357">

<img style="-webkit-user-select: none;margin: auto;cursor: zoom-in;background-color: hsl(0, 0%, 90%);transition: background-color 300ms;" src="https://raw.githubusercontent.com/leonardoSaaads/CartaSmith/main/Imagens%20Projeto/Figure_2.png" width="476" height="357">

## How to use:

To use the library, you can add the parameters in the class call.
Example:
```
example = CartaSmith(
        Z0=50,
        ZL=[50 + 50j, 50 + 49j, 50 + 48j, 50 + 38j, 50 + 12j]
    )
```
or by placing yourself directly in the made class.
Example:
```
    example = CartaSmith()
    example.Z0 = 50
    vector = np.arange(0, 2 * np.pi, 0.1)
    example.ZL = 50 + 50j * np.sin(vector)
```
Use the ```.sumario()``` command to display the summary.

Use the ```.ajustar()``` command to adjust all values in the class.

## Authors

By Leonardo Saads Pinto

2021 - September

## License

MIT;

A licença é permissiva e considerada equivalente a BSD Simplificada sem a cláusula de endosso. Porém, seu texto é bem mais explícito ao tratar dos direitos que estão sendo transferidos, afirmando que qualquer pessoa que obtém uma copia do software e seus arquivos de documentação associados pode lidar com eles sem restrição, incluindo sem limitação os direitos a usar, copiar, modificar, mesclar, publicar, distribuir, vender copias do software. As condições impostas para tanto são apenas manter o aviso de copyright e uma copia da licença em todas as cópias do software. Disponível em: https://pt.wikipedia.org/wiki/Licen%C3%A7a_MIT, Acesso em 14 de outubro de 2021.

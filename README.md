<h1 align='center'>Hashtag-treinamento</h1>

<p>Evento de intensivão de python realizado do dia 15/05 a 18/05.<br/>
Cada aula aborda um tema diferente do python, com problemas reais do dia a dia, e com projetos práticos, como:
<ul>
  <li><a href="https://github.com/M4theus13/Hashtag-treinamento/blob/main/README.md#aula1-150523">Automação de Processos</a></li>
  <li><a href="https://github.com/M4theus13/Hashtag-treinamento/blob/main/README.md#aula2-160523">Análise de Dados</a></li>
  <li><a href="https://github.com/M4theus13/Hashtag-treinamento/blob/main/README.md#aula3-170523">Automação Web(Web Scrapping)</a></li>
  <li><a href="https://github.com/M4theus13/Hashtag-treinamento/blob/main/README.md#aula4-180523">Machine Learning +Data Science</a></li>
</ul>
</p>

<h1 align='center'>Aula1 15/05/23</h1>
<h2>Automação de Sistemas e Processos com Python</h2>
<h2>Problema Exemplo:</h2>

<p>Para controle de custos, todos os dias, seu chefe pede um relatório com todas as compras de mercadorias da empresa. O seu trabalho, como analista, é enviar um e-mail para ele, assim que começar a trabalhar, com o total gasto, a quantidade de produtos e o preço médio dos produtos.</p>

<p>
<h4>Resumo do Programa:</h4>
O programa usa a biblioteca pyautogui do python e simula uma rotina de trabalho, controla o mouse e teclado do computador, abrindo o navegador entrando
em um site de login(fake) e realizando o download da planilha, faz uma análise e tratamento dos dados, abre o email e digita as informações da tabela para enviar para uma pessoa.
</p>

<h1 align='center'>Aula2 16/05/23</h1>
<h2>Análise de Dados com Python</h2>
<h2>Problema Exemplo:</h2>

<p>Você trabalha em uma empresas do varejo e tem milhares de clientes diferentes.</p>
<p>Com o objetivo de aumentar o faturamento e o lucro da sua empresa, a diretoria quer conseguir indetificar quem é o cliente ideal para seus produtos, baseado no histórico de compras dos clientes.</p>
<p>Para isso, foi feito um trabalho de classificar os clientes com uma nota de 1 a 100. só que agora, sobrou para você conseguir, a partir dessa nota, descobrir qual o perfil de cliente ideal da empresa.</p>
<p>Qual a profissão? Qual a idade? Qual a faixa de renda? E todas as informações que você puder analisar para dizer qual o cliente ideal da empresa.</p>

<h4>Resumo do Programa:</h4>

<p>
O programa utiliza a biblioteca pandas do python para fazer a importação da base de dados de clientes, faz o tratamento desses dados, e cria histogramas com as informações dessa planilha para fazer a análise.
</p>

<h3 align='center'>Resultado</h3>

<div align='center'>
  <a href='https://github.com/M4theus13'>
    <img width='49%' src='https://github.com/M4theus13/Assets_Projects/blob/main/Hashtag-treinamento/Aula2/graf%20(1).png'>
  </a>

  <a href='https://github.com/M4theus13'>
    <img width='49%' src='https://github.com/M4theus13/Assets_Projects/blob/main/Hashtag-treinamento/Aula2/graf%20(2).png'>
  </a>

  <a href='https://github.com/M4theus13'>
    <img width='49%' src='https://github.com/M4theus13/Assets_Projects/blob/main/Hashtag-treinamento/Aula2/graf%20(3).png'>
  </a>

  <a href='https://github.com/M4theus13'>
    <img width='49%' src='https://github.com/M4theus13/Assets_Projects/blob/main/Hashtag-treinamento/Aula2/graf%20(4).png'>
  </a>

  <a href='https://github.com/M4theus13'>
    <img width='49%' src='https://github.com/M4theus13/Assets_Projects/blob/main/Hashtag-treinamento/Aula2/graf%20(5).png'>
  </a>
</div>

<h1 align='center'>Aula3 17/05/23</h1>
<h2>Automação Web e Busca de Informações com Python</h2>
<h2>Problema Exemplo:</h2>

<p>
Trabalhamos em uma importadora e compramos e vendemos commodities: <br/>
  • Soja, Milho, Trigo, Petróleo, etc.
Precisamos pegar na internet, de forma automática, a cotação de todas as commodities e ver se ela está abaixo do nosso preço ideal de compra.
Se tiver, precisamos marcar como uma ação de compra para a equipe de operações.
</p>

<h4>Resumo do Programa:</h4>

<p>
O programa utiliza a biblioteca selenium do python para a controlar o navegador da máquina, abre o navegador, faz a leitura da tabela utilizando a biblioteca pandas do python, e entra em um site com os valores atualizados do preço de cada produto da tabela, coleta essa informação de cada produto, faz o tratamento e insere esse valor na tabela. <br/>
Logo após verifica se o produto está abaixo do valor de compra, colocando um resultado de VERDADEIRO ou FALSO na tabela
</p>

<div align='center'>
  <h3>Banco de dados</h3>
  <a href='https://github.com/M4theus13'>
    <img width='60%' src='https://github.com/M4theus13/Assets_Projects/blob/main/Hashtag-treinamento/Aula3/tabela.png'>
  </a>

  <h3>Resultado</h3>
  <a href='https://github.com/M4theus13'>
    <img width='60%' src='https://github.com/M4theus13/Assets_Projects/blob/main/Hashtag-treinamento/Aula3/tabela-atualizada.png'>
  </a>
</div>

<h1 align='center'>Aula4 18/05/23</h1>
<h2>Projeto Ciência de Dados - Previsão de Preços</h2>
<h2>Problema Exemplo:</h2>

<p>Trabalhamos em uma empresa de venda de barcos, o desafio é conseguir prever o preço de barcos que vamos vender baseado nas características do barco, como: <br/>
ano, tamanho, tipo de barco, se é novo ou usado, qual material usado, etc.
</p>

<h4>Resumo do Programa:</h4>

<p>O programa faz a leitura de uma tabela, utilizando a biblioteca pandas do python, mostra uma correlação do preço do barco com suas características, e com a leitura feita, utiliza a biblioteca sklearn do python para criar duas IAs que são treinadas com esse banco de dados.
</p>

<p>
Foram implementadas duas IAs para ter uma comparação em porcentagem entre os dois métodos.
</p>

<p>
A primeira IA utiliza o método de Regressão Linear, a segunda IA utiliza o método de Árvore de Decisão, após o treinamento é exibido uma porcentagem, de acerto de cada IA, foi utilizada a IA com melhor porcentagem para prever o valor dos barcos, a IA de Árvore de Decisão.
</p>

<div align='center'>
  <h3>Banco de dados</h3>
  <a href='https://github.com/M4theus13'>
    <img width='60%' src='https://github.com/M4theus13/Assets_Projects/blob/main/Hashtag-treinamento/Aula4/banco-dados.png'>
  </a>

  <h3>Resultado</h3>
  <a href='https://github.com/M4theus13'>
    <img width='60%' src='https://github.com/M4theus13/Assets_Projects/blob/main/Hashtag-treinamento/Aula4/tabela.png'>
  </a>
</div>

# Análise de Churn
___

**Churn**, também chamado de *churn rate* ou *attrition rate*, é uma métrica que mede a evasão de clientes de determinada empresa, ou seja, a taxa de cancelamento. Ou seja, caso a taxa de evasão seja alta, quer dizer que os clientes estão insatisfeitos com a empresa, e que há algum problema que deve ser tratado. Nesse caso, o notebook trata de um dataset fictício de um banco visando previsão de churns.

### O problema de negócio
O [Dataset](https://www.kaggle.com/mervetorkan/churndataset?select=churn.csv) apresenta 10.000 instâncias com dados fictícios de um banco que atua na Europa, com 14 atributos diversos acerca de clientes como nome, pontuação de crédito, salário estimado, se possui ou não cartão de crédito, entre outros, e por fim, se existiu evasão ou não por parte do cliente i.e. churn. 

A taxa média de churn é claramente variável de acordo com o porte e segmento da empresa. No caso do setor bancário, taxas de churn entre 11% a 34% podem ser encontradas [[1]](https://thefinancialbrand.com/59779/digital-banking-branch-channel-switching/). Partindo desse princípio, o notebook apresenta um modelo de aprendizado de máquina de previsão de churn utilizando o dataset pré-processado.

### Avaliação em função do problema de negócio

Os algoritmos de aprendizado de máquina utilizados foram:
- Naïve Bayes (baseline)
- Regressão Logística
- SVM
- Random Forest
- Gradient Boosting




A priori, temos como resultado do modelo de classificação a matriz de confusão, que apresenta os seguintes valores:

- TP: previsão de churn, que realmente ocorre $\to$ perda monetária pois cliente sai
- TN: previsão de não churn, que realmente ocorre $\to$ sem perda monetária, pois cliente permanece
- FP: previsão de churn, mas cliente não sai $\to$ sem perda monetária, pois cliente permanece
- FN: previsão de não churn, mas cliente sai $\to$ perda monetária, pois previu que cliente ficaria e ele saiu

Até tal ponto, é possível compreender as previsões, porém não dentro de um contexto monetário. Faz-se necessário então aplicar um conceito bastante utilizado onde pode-se concatenar as previsões do modelo de aprendizado de máquina com valores do negócio - conceito de **valor esperado**:

$$EV = p(o_1)v(o_1) + p(o_2)v(o_2) + ...$$

onde $p(o_i)$ é a probabilidade do evento, e $v(o_i)$ é seu valor.

Nesse contexto, visando calcular o valor esperado de lucro de uma campanah de retenção de clientes, pode-se realizar uma análise de curso-benefício, onde temos TP e TN como benefícios (modelo previu corretamente), e FP e FN como os custos (modelo previu incorretamente). A matriz de custo-benefício utilizada para avaliação do projeto, com valores fictícios retirados de [[2]](http://rstudio-pubs-static.s3.amazonaws.com/277278_427ca6a7ce7c4eb688506efc7a6c2435.html), com as mesmas dimensões da matriz de confusão do modelo, foi:

- TP $\to$ benefício $\to$ $1000 - cliente responde positivamente à campanha e tinha intenção de churn

- TN $\to$ benefício $\to$ $50 - cliente não recebe a campanha pois não tinha intenção de churn, e continua contribuindo

- FP $\to$ custo $\to$ -$250 - cliente responde positivamente à campanha, mas não tinha intenção de churn

- FN $\to$ custo $\to$ -$2000 - cliente não responde positivamente à campanha e churn

Entretanto, é importante também levar em consideração a probabilidade de se encontrar cada classe *a priori*, ou seja, a probabilidade *a priori* de ocorrer churn ou não [[3]](https://www.oreilly.com/library/view/data-science-for/9781449374273/), ou seja, $P(0)$ ou $P(ñ churn)$ e $P(1)$ ou $P(churn)$. Assim, temos que:

$$EV_{profit} = p(1)*[p(Y|1)b(Y,1) + p(N|1)c(N,1)] + $$
$$p(0)*[p(N|0)b(N,0) + p(Y|0)c(Y,0)] $$

onde:
- p $\to$ probabilidade
- b e c $\to$ benefício e custo
- 0 e 1 $\to$ não churn e churn
- N e Y $\to$ previsão de não churn e churn

O valor esperado de lucro pode ser expresso, portanto, como:

$$EV_{profit} = 0.2037*[1000p(Y|1) - 2000p(N|1)] + 0.7963*[50p(N|0) - 250p(Y|0)] \to$$

$$\to EV_{profit} = 203.7p(Y|1) + 39.815p(N|0) - 407.4p(N|1) - 199.075p(Y|0) $$

Nota-se, portanto, que FP tendem a reduzir fortemente o valor esperado. Nesse caso, é importante compreender como a matriz de custo-benefício pode influenciar no valor esperado de lucr.

Entretanto, como existe um trade-off entre precision e recall, os modelos foram treinados utilizando-se como score a métrica F1, média harmônica entre as métricas mencionadas, a qual apresentou os melhores resultados de valor esperado com o algoritmo SVM.


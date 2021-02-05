# Análise de Churn
___

**Churn**, também chamado de *churn rate* ou *attrition rate*, é uma métrica que mede a evasão de clientes de determinada empresa, ou seja, a taxa de cancelamento. Ou seja, caso a taxa de evasão seja alta, quer dizer que os clientes estão insatisfeitos com a empresa, e que há algum problema que deve ser tratado. Nesse caso, o notebook trata de um dataset fictício de um banco visando previsão de churns.

### O problema de negócio
___
O [Dataset](https://www.kaggle.com/mervetorkan/churndataset?select=churn.csv) apresenta 10.000 instâncias com dados fictícios de um banco que atua na Europa, com 14 atributos diversos acerca de clientes como nome, pontuação de crédito, salário estimado, se possui ou não cartão de crédito, entre outros, e por fim, se existiu evasão ou não por parte do cliente i.e. churn. 

A taxa média de churn é claramente variável de acordo com o porte e segmento da empresa. No caso do setor bancário, taxas de churn entre 11% a 34% podem ser encontradas [[1]](https://thefinancialbrand.com/59779/digital-banking-branch-channel-switching/). Partindo desse princípio, o repositório apresenta dois notebooks, um primeiro que apresenta a EDA e pré-processamento de dados, e um segundo que apresenta um modelo de aprendizado de máquina de previsão de churn utilizando o dataset pré-processado, e previsão de faturamento.

### Avaliação em função do problema de negócio
___
Os algoritmos de aprendizado de máquina utilizados foram:
- Decision Stump (baseline)
- Regressão Logística
- Random Forest
- Gradient Boosting
- Extreme Gradient Boosting

A priori, temos como resultado do modelo de classificação a matriz de confusão, que apresenta os seguintes valores:

- TP: previsão de churn, que realmente ocorre -> perda monetária pois cliente sai
- TN: previsão de não churn, que realmente ocorre -> sem perda monetária, pois cliente permanece
- FP: previsão de churn, mas cliente não sai -> sem perda monetária, pois cliente permanece
- FN: previsão de não churn, mas cliente sai -> perda monetária, pois previu que cliente ficaria e ele saiu

Até tal ponto, é possível compreender as previsões, porém não dentro de um contexto monetário. Faz-se necessário então aplicar um conceito bastante utilizado onde pode-se concatenar as previsões do modelo de aprendizado de máquina com valores do negócio - conceito de **valor esperado**:

![image](https://user-images.githubusercontent.com/63553829/103578232-f5367a00-4eb4-11eb-99f3-1b697a32c203.png)

onde p(o_i) é a probabilidade do evento, e v(o_i) é seu valor.

Nesse contexto, visando calcular o valor esperado de lucro de uma campanha de retenção de clientes, pode-se realizar uma análise de curso-benefício, onde temos TP e TN como benefícios (modelo previu corretamente), e FP e FN como os custos (modelo previu incorretamente). A matriz de custo-benefício utilizada para avaliação do projeto com valores fictícios foi baseada em [[2]](https://carmenlai.com/2016/11/12/user-churn-prediction-a-machine-learning-workflow.html). Nesse escopo, foi assumido que caso o modelo preveja churn, o plano de retenção terá um gasto de $150 com o cliente. Se o plano tiver sucesso na retenção, o lucro será do *lifetime value* do cliente menos o custo com o próprio plano, nesse caso, $325 - $150 = $175, simplificando custos com FP e TN:

- TP -> benefício -> $175 - cliente responde positivamente à campanha e tinha intenção de churn

- FN -> custo -> -$150 - cliente não responde positivamente à campanha e não ocorre retenção

Portanto, pode-se calcular o valor esperado como:

![image](https://user-images.githubusercontent.com/63553829/103697675-02b83680-4f7f-11eb-8b85-96effcc936f6.png)

Entretanto, é importante também levar em consideração a probabilidade de se encontrar cada classe *a priori*, ou seja, a probabilidade *a priori* de ocorrer churn ou não [[3]](https://www.oreilly.com/library/view/data-science-for/9781449374273/), ou seja, p(0) ou p(ñ churn) e p(1) ou p(churn), principalmente para classes desbalanceadas. Assim, temos que:

![image](https://user-images.githubusercontent.com/63553829/103697707-0ea3f880-4f7f-11eb-83df-693005e346eb.png)

onde:
- p -> probabilidade
- b e c -> benefício e custo
- 0 e 1 -> não churn e churn
- N e Y -> previsão de não churn e churn

O valor esperado de lucro pode ser expresso, portanto, como:

![image](https://user-images.githubusercontent.com/63553829/103697750-1e234180-4f7f-11eb-8985-d673790b56c9.png)

Nota-se que são considerados apenas as ocorrências de churn, sendo considerados TP e FN e, como consequência, valores de recall culminarão em maior lucro esperado.

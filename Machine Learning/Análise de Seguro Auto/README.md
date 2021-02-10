# Seguro Auto
---


## Objetivo :dart:

Uma seguradora que fornece seguro saúde para seus clientes tem interesse na construção de um modelo para prever se seus clientes do ano passado também estarão interessados no seguro auto fornecido pela empresa.

Uma apólice de seguro é um acordo pelo qual uma empresa se compromete a fornecer uma garantia de compensação por perdas, danos, doenças ou morte especificados em troca do pagamento de um prêmio especificado - uma quantia em dinheiro, que o cliente precisa pagar regularmente a uma seguradora por essa garantia.

Assim como o seguro de saúde, existe o seguro auto em que todos os anos o cliente paga um prêmio de determinado valor à seguradora para que, em caso de acidente com o veículo, a seguradora forneça uma indenização para o consumidor.


## Os dados :floppy_disk:

O [dataset](https://www.kaggle.com/anmolkumar/health-insurance-cross-sell-prediction) apresenta dados de treinamento para um modelo de previsão de seguros auto, com 381109 instâncias e 11 variáveis, dentre as quais:
- `id` -> id único do cliente
- `Gender` -> gênero do cliente
- `Age` -> idade do cliente
- `Driving_License` -> se o cliente possui (1) ou não (0) habilitação
- `Region_Code` -> código único da região do cliente
- `Previously_Insured` -> cliente possui (1) ou não (0) seguro
- `Vehicle_Age` -> idade do veículo
- `Vehicle_Damage` -> veículo danificado (1) ou não (0) no passado
- `Annual_Premium` -> montante pago pelo cliente à seguradora
- `Policy_Sales_Channel` -> canal de atendimento ao cliente
- `Vintage` -> número de dias como cliente
- `Response` -> cliente interessado (1) ou não (0) no seguro


## Problema de Negócio :snake: :car: :moneybag: :briefcase:

O problema de negócio consiste basicamente em prever quais clientes do ano anterior estarão interessados no seguro auto oferecido pela empresa, para que assim o time de vendas possa priorizar as pessoas com maior interesse no produto oferecido, otimizando assim a campanha voltada para os principais clientes. De acordo com [[1]](https://coverager.com/improve-customer-retention-with-the-power-of-apis/#:~:text=The%20average%20customer%20retention%20rate,success%20factors%20for%20auto%20insurers.), a retenção média de clientes para seguradoras de veículos nos EUA gira em torno de 88%.
Nesse contexto, o repositório possui 2 notebooks, um primeiro visando EDA e pré-processamento dos dados, e um segundo com a criação do modelo de aprendizado ed máquina, avaliação e previsão de valor esperado de lucro.

Os algoritmos utilizados foram:
- Decision stump
- Regressão Logística
- Random Forest
- XGBoost

Nesse contexto, temos que:
- TP -> previsão de que o cliente manteria o seguro, o que ocorre -> ganho monetário, pois cliente permanece
- TN -> previsão de que o cliente cancelaria o seguro, o que ocorre -> perda monetária, pois cliente cancela seguro
- FP -> previsão de que o cliente manteria o seguro, o que não ocorre -> perda monetária, pois o cliente cancela o seguro
- FN -> previsão de que o cliente cancelaria o seguro, o que não ocorre -> ganho monetário, pois o cliente permanece

BBaseando-se nas métricas, procuramos um modelo que apresente um baixo valor de FP i.e. clientes que manteriam o seguro, mas que na realidade o cancelaram, pois gera perda monetária, bem como uma alta taxa de TP, os seja, retenção clientes -> e.g. boa performance de ROC-AUC i.e. baixa taxa de falsos positivos, e alta taxa de verdadeiros positivos.

Considerando os valores de prêmio anuais da base de dados pré-processada, a média é aproximadamente $30k, valor muito acima da média de mercado. No projeto, foram considerados um prêmio médio nos EUA de $1427 (*customer lifetime value*) [[1]](https://www.nerdwallet.com/blog/insurance/car-insurance-basics/how-much-is-car-insurance/#:~:text=The%20national%20average%20cost%20of,and%20a%20clean%20driving%20record.), e um custo de campanha de marketing de 3.3% em relação ao prêmio médio, ou seja, $42.8 [[2]](https://www.iamagazine.com/viewpoints/student-of-the-industry-insurance-ads-who-spends-what-and-why). 

Aplicando, portanto, uma campanha de marketing aplicada aos clientes com maior probabilidade de permanecer, é possível elaborar uma matriz de custo-benefício em função da própria campanha, onde caso a campanha de marketing consiga manter o cliente, a receita seria do número $n$ de clientes multiplicado pelo LTV menos o custo com marketing -> *n*(LTV-marketing)*, e caso a campanha seja aplicada a clientes que de fato sairiam (FP), a receita seria -> *k*marketing*:

- TP - benefício -> $1384.2 -> previu que o cliente continuaria, e aplicou campanha de marketing - retenção
- TN - benefício -> $0 -> previu que o cliente sairia, e ele saiu, então não houve campanha de marketing
- FP - custo -> $-42.8 -> previu que o cliente ficaria, mas o cliente saiu, e aplicou campanha de marketing - sem retenção
- FN - custo -> $0 -> previu que o cliente sairia, mas ele permaneceu

É importante denotar que a matriz de custo-benefício acima, como comentado, foi elaborada em função da campanha de marketing. Claramente, existe perda de receita devido ao TN i.e. para clientes que cancelam o seguro, onde a perda de receita seria o número $n$ de clientes multiplicado pelo LTV -> *n*LTV$*. 

É possível calcular também o retorno sobre o investimento (ROI) de marketing devido à retenção de clientes:

![image](https://user-images.githubusercontent.com/63553829/105252634-96cbf580-5b5c-11eb-9467-10b3401fe883.png)

Outra análise de grande importância é a de valor esperado, a qual calcula o valor esperado de lucro para a campanha de marketing em função do resultado dos modelos de aprendizado de máquina, ou seja:

![image](https://user-images.githubusercontent.com/63553829/103578232-f5367a00-4eb4-11eb-99f3-1b697a32c203.png)

onde p(o_i) é a probabilidade do evento, e v(o_i) é seu valor. Considerando a matriz de custo-benefício apresentada acima, é juntamente com a equação de valor esperado, pode-se calcular o valor esperado de lucro em função das probabilidades de TP,TN,FP,FN, considerando as probabilidades de ocorrência de cada classe i.e. p(0) = 0.878, e p(1) = 0.122 [[3]](https://www.oreilly.com/library/view/data-science-for/9781449374273/):

![image](https://user-images.githubusercontent.com/63553829/103697707-0ea3f880-4f7f-11eb-83df-693005e346eb.png)

onde:
- p -> probabilidade
- b e c -> benefício e custo
- 0 e 1 -> cancelar ou manter o seguro
- N e Y -> previsão de cancelar ou manter o seguro

Pode-se, portanto, reescrever a equação de *EV* como aplicando-se os valores de custo e benefício, :

![image](https://user-images.githubusercontent.com/63553829/105252798-ef02f780-5b5c-11eb-8ac5-ae513bbf4d15.png)

Nota-se que, enquanto a retenção possui uma magnitude de $168.9xTP, a campanha de marketing aplicada a clientes que não iriam cancelar o seguro possui uma magnitude de $-37.6xFP. Busca-se, então, altos valores de TP e baixos valores de FP, visando obter um maior lucro esperado, ou seja, maximização da AUC como comentado acima, utilizando, portanto, *ROC-AUC* como métrica de otimização.

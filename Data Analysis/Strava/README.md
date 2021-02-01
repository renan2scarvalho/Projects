# Análise dos dados de atividades do Strava
---
## Objetivo
---
Este repositório teve como objetivo analisar os dados de atividades físicas presentes no aplicativo Strava, no presente caso, corridas e pedaladas.\
Os dados foram baixados diretamente do site do Strava, e como realizar o download por ser encontrado [aqui](https://support.strava.com/hc/pt/articles/216918437-Exportar-os-seus-dados-e-exporta%C3%A7%C3%A3o-em-massa).

## Arquivos
---
Dentre os arquivos existentes no download, foi utilizado somente uma planilha csv com estatísticas gerais das atividades, e alguns arquivos gpx que contêm marcações segundo a segundo das atividades.
O projeto visou analisar as estatísticas gerais através de análise univariadas, relações entre variáveis através de análise bivariadas e, para quando existam outliers, analisar as atividades com maior escrutínio através dos arquivos gpx.
Foram criados três notebooks durante a análise, sendo eles:

1 - Limpeza de dados e Análise Geral - limpar os dados, criar variáveis, e analisar os dados holisticamente i.e. sem distnição de atividades\
2 - Pedaladas - análise das pedaladas somente\
3 - Corridas - análise das corridas somente

Ademais, visando analisar os arquivos gpx utilizados, um arquivo .py chamado *parse_gpx* foi criado para facilidade.

# Projeto TCC - Arquitetura IoT Edge
Projeto para tese de conclusão de curso. 

Arquivos da camada de gateway estão no caminho `gateway/`, e regional em `regional/` (:shipit:). Conferir README.

## WIP/ToDo
- Arrumando dockerfiles de gateway:
    - Ver se é possível criar Dockerfile para os serviços de Mosquitto e Nifi/MiNiFi, para que um gateway possa ser iniciado via build diretamente do compose (e.g.: como os brokers kafka são definidos em um compose)
- Arrumar .env de gateway, e ver se existe necessidade de .env para regional
- Melhorar documentação
- Levantamento bibliográfico:
    - Dados geraods em IoT de agric. de precisão

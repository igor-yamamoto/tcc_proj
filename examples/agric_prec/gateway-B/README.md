# Gateway

Neste dir, se encontram os arquivos referentes à camada de gateway. Este é um processo que se ainda encontra em desenvolvimento. No docker-compose, se encontram os builds das imagens do projeto [IoT-Data-Simulator](https://github.com/IBA-Group-IT/IoT-data-simulator), uma imagem do mosquitto e outra do NiFi (no futuro converter para MiNiFi).

## Configuração
0. Criar uma rede chamada `regional_gateway-network` 
    - ps.: esta rede é criada automaticamente se rodar o compose da camada regional
1. Rodar `docker-compose up -d`
    - ps.: as imagens são relativamente pesadas. beware
2. Acessar o simulador de dados IoT em `localhost:8090` e subir o arquivo [`templates/iot-ds-config.json`](templates/iot-ds-config.json)
3. Dar play na sessão **TCC-TEST**. É possível verificar se o broker está escutando as mensagens pelo próprio terminal built-in da aplicação, ou via comando `docker-compose exec mosquitto mosquitto_sub -h localhost -t "devices/device1"`
4. Para consumir as mensagens no Nifi, acesse `localhost:8081/nifi` e importe o template [`templates/IoT-Stream-Gateway.xml`](templates/IoT-Stream-Gateway.xml). Após importar, coloque o template no painel e execute o processor de consumo MQTT
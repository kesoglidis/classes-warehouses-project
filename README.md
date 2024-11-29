## Preliminaries

### Install docker engine

[Docker docs](https://docs.docker.com/) contains a comprehensive overview of the docker engine and its functionalities. The page [Installation](https://docs.docker.com/engine/install/) contains information for the installation of Docker in different OSs.

### Running the stack from the compose file

Use the command `docker compose up -d` to run the services stack which contains [Zookeeper](https://zookeeper.apache.org/), [Apache Kafka](https://kafka.apache.org/), [PostgreSQL](https://www.postgresql.org/) and [Apache Druid](https://druid.apache.org/).
The compose file includes volumes to permanently store the data in the warehouse even when the docker containers stop.

After running the stack you need to connect the Kafka as an ingestion mechanism to Druid. To do this you need to first start a custom producer that writes data to a Kafka topic and follow the next steps. 

1. Go to the Druid UI `http://localhost:8808/` 
2. `Start a new streaming spec` using the `Load data` and `Streaming` option.
3. Select the `Kafka` option and insert the Kafka broker server (default: `kafka:29092`) and the Kafka topic (**IMPORTANT**: the topic should have already been created and have some data in it).
4. The UI should read and recognize the json data and their columns.
5. In the next step select the time column and follow the next steps of the process.
6. You can select different columns as the dimensions for the cubes.
7. Finally, you can query the data from the `Query` option of the Druid UI.

### Closing and resetting the stack

The stack can be closed using the `docker compose down` command. If you need to reset the stack (i.e. remove the data) you can use the `docker compose down -v` command.

## Creating and debuging the python producer

### Install the python dependencies

First you need to install the dependencies using the command `pip install -r src/requirements.txt`.

### Code

You can make the necessary changes in the data model, the data ingestion and the producer as you see fit. 

The file `data_model.py` contains a template model with a single value as the temperature.

The file `producer.py` contains the login where each second a random value is generated and used in the data model to extract the json message and publish it in the Kafka broker.

It is recommended to find and use a [predefined model](https://doris.apache.org/docs/1.2/benchmark/ssb/) in which case you will need to find a way to translate the given data points to a json format for the message of the broker.

The file `consumer.py` is used to monitor the messages that pass through the Kafka broker.

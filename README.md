# Search Engine


## Preparing the Environment
We will use conda for dependency management. Let's install it:
```sh
$ conda --version
$ conda create --name py39_env=3.9
$ conda activate py39_env
```
Install the packages
```
$ conda install tqdm notebook=7.1.2 
$ pip install openai elasticsearch 
```
Let's put the key to an env variable:
```
export OPENAI_API_KEY="TOKEN"
```
To manage keys, we can use direnv:
```
$ sudo apt update
$ sudo apt install direnv 
$ direnv hook bash >> ~/.bashrc`
```
Create / edit .env in your project directory

```
$ export OPENAI_API_KEY='sk-proj-key'
```
Start a new terminal, and there run jupyter:
```
$ jupyter notebook
```
In another terminal, run elasticsearch with docker:

```
docker run -it \
    --name elasticsearch \
    -p 9200:9200 \
    -p 9300:9300 \
    -e "discovery.type=single-node" \
    -e "xpack.security.enabled=false" \
    docker.elastic.co/elasticsearch/elasticsearch:8.4.3
```
Verify that ES is running

```
$ curl http://localhost:9200
```
You should get something like this:

```
{
  "name" : "63d0133fc451",
  "cluster_name" : "docker-cluster",
  "cluster_uuid" : "AKW1gxdRTuSH8eLuxbqH6A",
  "version" : {
    "number" : "8.4.3",
    "build_flavor" : "default",
    "build_type" : "docker",
    "build_hash" : "42f05b9372a9a4a470db3b52817899b99a76ee73",
    "build_date" : "2022-10-04T07:17:24.662462378Z",
    "build_snapshot" : false,
    "lucene_version" : "9.3.0",
    "minimum_wire_compatibility_version" : "7.17.0",
    "minimum_index_compatibility_version" : "7.0.0"
  },
  "tagline" : "You Know, for Search"
}
```

### License

This project is licensed under the MIT License - see the [LICENSE]() file for details.
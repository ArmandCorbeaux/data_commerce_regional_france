# data_commerce_regional_france
Project to create a complete pipeline to analyze commercial activities in france since 2004

## The goals :
### 1- Extract - Python / Docker :
  - Extracted files stored in a local shared folder

    docker pull jupyter/pyspark-notebook:x86_64-7cce21edff82
    Python 3.11 / Spark 3.5.0 / Ubuntu 22.04
    port 8888
    tips : token is in the console, but can be replaced by password

    local folder mount : -v /some/host/folder/for/work:/home/jovyan/work
    local write fix : sudo chown 1000 /some/host/folder/for/work
    
### 2 - Transform - Pyspark / Docker
  - concatenate stored files in the shared folder

### 3 - Load - Pyspark / Docker to PostGres / Docker
  - create table
  - load dataframe

### 4 - Extract datas from database
  - use the created dataset for another projects

-----

### 5? - Found a free way to perform visual analyzes

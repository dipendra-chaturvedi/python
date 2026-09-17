# What is Big Data?

- Big Data = extremely large or complex amounts of data.
- The data can be too large/fast/varied for simple traditional processing.
- It is commonly explained using the 5 Vs:

```

| V            | Meaning                      | Example                        |
| ------------ | ---------------------------- | ------------------------------ |
| **Volume**   | Huge amount of data          | Billions of transactions       |
| **Velocity** | Data generated quickly       | Live sensor data               |
| **Variety**  | Different data types         | Text, images, JSON, videos     |
| **Veracity** | Data quality/reliability     | Duplicate or incorrect records |
| **Value**    | Useful information from data | Finding customer trends        |


```


## Main differnce
- Think of water bottles.

### List = keep all bottles

```
bottles = [1, 2, 3, 4, 5]

```

```
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number)
```


- "Give me all 5 bottles."
- [1][2][3][4][5]

- Create everything → Process


###  Generator = give me one bottle at a time

``` 
def bottles():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

```
```
def numbers():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

for number in numbers():
    print(number)
```

- "I won't keep all 5. I'll give you one when you ask."

```
Give 1 → use it
Give 2 → use it
Give 3 → use it
Give 4 → use it
Give 5 → use it
```

- Create one → Process → Create next → Process → ...



## Distributed processing

- Simple idea
- Distributed processing = split a large dataset/workload across multiple computers and process it together.

- 1,000,000 records
```
Computer 1
↓
1,000,000 records
```
- we can split the work:
```
Computer 1 → 250,000
Computer 2 → 250,000
Computer 3 → 250,000
Computer 4 → 250,000
```

## Hadoop
- Hadoop is a Big Data framework used to store and process very large datasets across multiple computers.
```
Huge Data
   ↓
Hadoop
   ↓
Multiple Computers
   ↓
Store + Process Data
```
- HDFS → stores large data across multiple machines.
- MapReduce → processes the distributed data.

```
100 GB of data
      ↓
HDFS
 ┌────┬────┬────┬────┐
 PC1  PC2  PC3  PC4
```
- The data is distributed across machines instead of relying on one computer.
- Remember
- HDFS = storage
- MapReduce = processing

## Apache Spark
- Apache Spark is a Big Data processing framework.
```
Huge Dataset
     ↓
   Spark
     ↓
Multiple Computers
     ↓
Fast Processing
```
### Small example
- Suppose:
- 1 billion sales records
- Spark can split the work:

```
Computer 1 → records 1–250M
Computer 2 → records 251–500M
Computer 3 → records 501–750M
Computer 4 → records 751M–1B
```
- and process the partitions in parallel.

- Remember:
```
Hadoop → storage + processing ecosystem
Spark → fast distributed data processing
```
## Data Partitioning
- Partitioning means splitting a large dataset into smaller parts called partitions.
```
1,000,000 records
        ↓
 ┌──────┬──────┬──────┬──────┐
 P1     P2     P3     P4
250K   250K   250K   250K
```
- Each partition can be processed separately, often by different computers/processes.

### Why?
- Large data becomes easier to process.
- Multiple partitions can be processed in parallel.
- Reduces the amount of data handled by each worker.
- Remember:
- Partitioning = divide big data into smaller chunks.


## Data Processing Pipeline
- A data processing pipeline means data goes through multiple steps before we get the final result.
- Example
```Raw Data
   ↓
Collect
   ↓
Clean
   ↓
Transform
   ↓
Analyze
   ↓
Result
```
- Suppose an online store receives:
```
" ₹500 "
" ₹1000 "
" ₹300 "
```
- Pipeline:
```
Raw data
   ↓
Remove ₹ and spaces
   ↓
500, 1000, 300
   ↓
Calculate total
   ↓
₹1800
```
- Pipeline = a sequence of data-processing steps.

## ETL
- ETL is a very common data-processing concept.
```
E → Extract
T → Transform
L → Load
```
- Example:
```
Database
   ↓
EXTRACT
   ↓
Clean / change data
   ↓
TRANSFORM
   ↓
Store in another database
   ↓
LOAD
```
### Suppose we get employee data:
``` 
" Dipendra ", "60000" 
```
- Extract:
``` 
Read the employee data 
```

- Transform:
```
" Dipendra " → "Dipendra"
"60000" → 60000
```
- Load:
- Save the cleaned data into a database
```
Remember

Extract = get data
Transform = change/clean data
Load = store data
```

## Data Lake
- A Data Lake is a storage system where we keep large amounts of raw data in its original form.

- Example:
```
Different Data
     ↓
┌─────────────────┐
│    DATA LAKE    │
├─────────────────┤
│ JSON            │
│ CSV             │
│ Images          │
│ Videos          │
│ Logs            │
└─────────────────┘
```
- Unlike a traditional database, the data doesn't have to be cleaned and structured before storing it.

- Data Lake = store large amounts of raw, different types of data.

## Data Warehouse
- A Data Warehouse stores structured, processed data mainly for reporting and analysis.
```
Data Sources
     ↓
Clean / Transform
     ↓
Data Warehouse
     ↓
Reports / Analysis
```
```
Data Lake = raw data storage
Data Warehouse = organized data for analysis
```




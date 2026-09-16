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






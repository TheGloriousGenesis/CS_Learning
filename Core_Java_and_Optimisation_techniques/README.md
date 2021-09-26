# Java

### Glossary

| Word | Definition|
|:----:|:---------:|

### Current Questions
- Why do we use octal, hexadecimal numbers?

### Data Types
When optimising code, one must always look towards the data that is being used and how it is being stored. The following
table shows a break-down of the primitive types and their storage:

| Type | Storage (bytes) | Range |
|:----:|:---------------:|:-----:|
| int  | 4 |~ -2 billion to +2 billion |
| short| 2 |~ -30 thousand to +30 thousand|
| long | 8 |~ -9 billion billion to +9 billion billion |
| byte | 1 | -128 to 127 |
| float| 4 |~ $-3 x 10^38$ to $+3 x 10^38$ |
|double| 8 |~ -$1.8 x 10^308$ to +$1.8x 10^308$ |

- Short and byte tend to be used for applications that are high performance or when storage space is limited.
- Can use underscores to represent long numbers (similar to python) `int earthHumanPopulation = 8_000_000_000`. The complier
will ignore underscore when rendering the variable.
- Java ensures range for each data type are constant so that programs will compile the same regardless of system.
- 

###

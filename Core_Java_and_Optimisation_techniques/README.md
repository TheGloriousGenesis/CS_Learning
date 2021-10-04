# Java

## Glossary

| Word | Definition|
|:----:|:---------:|

## Current Questions
- Why do we use octal, hexadecimal numbers?
- Why need escape sequence like \u?


## Data Types
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
| char | | |
| boolean| | |

- Short and byte tend to be used for applications that are high performance or when storage space is limited.
- Can use underscores to represent long numbers (similar to python) `int earthHumanPopulation = 8_000_000_000`. The complier
will ignore underscore when rendering the variable.
- Java ensures range for each data type are constant so that programs will compile the same regardless of system.

> *NB: ensure that if you need precise numerical computations, use `BigDecimal` class.*

`BigDecimal` and `BigInteger` used to manipulate large numbers and precision arithmetic. 

## Operators

- `/` operator denotes integer division if both arguments integer, floating point otherwise. 
- Normally, all intermediate computations must be truncated (if not then output would be different dependant on underlying
processors)
- In order to ensure pre-truncated does not occur within method, use the `strictp` on method to use strict 
floating-point computation (might overflow so only use when needed)

## Conversion between numeric types

- byte --> short
- short --> int
- int --> long, double
- float --> double
- char --> int

if values are combined via +, -, x, /, then the operands (values either side of the operator) must be converted to the 
same type before calculations. If either double, long or float they will be converted to the respective type. Else int.

## Bitwise Operators

`^` == or

`~` == not

`>>` == shift bit pattern to the right

`<<` == shift bit pattern to the left

## Read input/output

Use scanner (defined in the java.util package) to read input values from console
`Scanner in = new Scanner(System.in)`.

Use scanner also to read from file input in the following way:
`Scanner in = new Scanner(Paths.get("myFile.txt")`

If you want to read sensitive data from the console you can use `Console` class introduced in java SE 6, which allows 
information like passwords to be hidden when input given:
`Console cons = System.Console()` with `cons.readLine("Read line: ");` and `cons.readPassword("Read password: ");` 
methods. 

`System.out.printf("%8.2f", x)` <-- field width 8 characters and precision 2 characters.

## Control flow

statements/loops can be broken by using loop labels that are defined by:

```java
read_data:
while(. . .)
{
    for(. . .)
    {
        . . .
        break read_data;
    }
}
```

## Arrays

To copy an array use the following statement: `Arrays.copyOf(oldArray, lengthOfNewArray)`.

To sort an array use: `Arrays.sort(a)`. This uses quicksort algorithm.


## Lambdas and comparing 
Can compare data using class that implements either comparable or compartor interface. Preferable use comparable when 
dealing with most cases, and comparator when dealing with 




 
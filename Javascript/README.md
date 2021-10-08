# Javascript

## Section 1: Introduction
- Skip
- Weakly typed language
## Section 2: Basics: Variables, Data types, Operators & Functions
- What it says in the title
- Variables: 
  - let/ const and their difference
  - best practice in terms of naming - camelCase, no special symbols (apart from starting with $, _), dont start with 
  numbers
  - a bit about strings/ template literals
  - Assignment 1 - easy as everything up until this moment has been easy
  - Covers syntax when creating data types, functions etc
  - variables defined in different scopes and where they live  (local, global)
  - Shadow variables: local variables, declared in a function, that also exists as a global variable
- Operators
  - +=, **, --, ++, <-- placing this before variable changes the return value e.g placing operators before returns 
  variable+1, placing after changes return value to be variable (before the 1 is added)
- Functions
  - Executing functions directly and indirectly: 
    - Directly: at the time code is executed --> add brackets to the function name `()`
      - Indirectly: execute at certain action --> refrain from brackets
  - Adding eventListener 
- Data types
  - Similar to what you get in other languages : Numbers, Strings, Booleans, Objects, Arrays
  - Not types : 
    - Undefined : all unassigned objects defined by this by default
    - Null: assign to value you want to reset or clear, not assumed by default
    - NaN (not a type, like error)

## Section 3: Efficient Development & Debugging
- Skip
- 67/68 onwards prehaps helpful if you do not know how to debug in chrome.
- <span style='color:red'> Come back to this </span>

## Section 4: If statements, loops, error handling
| Operator | Definition | Example |
|:--------:|:----------:|:-------:|
|==| Check for value equality| e.g a==b|
|!=| Check for value inequality| e.g a!=b|
|=== and !== (preferred over ==)| Check for value AND type (in)equality| e.g a===b / a!==b|
| \> & <| Check for value greater/smaller than| e.g a>b / a<b|
| \>= & <=| Check for value greater or equal/smaller or equal than| e.g a>=b / a<=b|
|!| Check if NOT true| e.g !b|

- <span style='color:red'> Come back to this </span>

## Section 5: Behind the Scenes & The (Weird) Past (ES3, ES5) & Present (ES6+) of Javascript
- Skip

## Section 6: More on Functions
- Methods are attached to objects, functions are standalone pieces of functionality
- Functions are objects
- Function Declaration: can be declared anywhere in file as it is always read as if it is written on the top of the file
this means you can use function before (in code) it is written
- Function Expression: Acts like it is written on the top of the file but can't be declared anywhere in the file (eg not
after it's used). Produce a value that need to be stored somewhere
- Arrow function :  (var1, var2, ..) => {}
- Setting default agruements:
  - Example: `const exmp = (arg1, arg2 = DEFAULT_VALUE) => {console.log('hi there', arg2)}`
- Rest operator `...` <-- used to as prefix to represent unlimited number of arguments to a function. Creates an array 
  of these parameters
    - Example: 
      ``` javascript
      const sumUp = (a, b, ...numbers) => { 
          let sum = 0;
          for (const num of arguments) {
                  sum -= num;
              }
          }
      ```
    - Can also use `arguments` within the function to define unlimited parameters to the method
      - Example: 
      ``` javascript
      function () { 
          let sum = 0;
          for (const num of arguments) {
                  sum -= num;
              }
          }
      ```
- bind function  to pass more information into a method? Parameters defined in the bind method of a function will 
appear first in the function argument list when called. Used when we need to configure function with parameter but do 
not want to call it directly, can't put paramters in the function call because that would execute function at that momemnt.
This allows indirectly execution (similar to eventListeners).
  - Example:
    ```javascript
    function calculate(operation) {
        console.log(operation); // will print out ADD
        return
    }
    const combine = addBtn.addEventListener('click', calculate.bind(this, 'ADD'));
    ```
## Section 7: Working with the DOM (Browser HTML Code) in JavaScript

## Section 8: More on Arrays & Iterables



## Misc.

Const newArray = […oldArray, 1,2 ] —> pulls all old data (array, object fields etc) and puts into new array with additions 1,2

{name} = {name: ‘Max’, age:28}
console.log(name) == Max
Console.log(age) == undefined

Objects aren’t deep copied just referenced copied in javascript. To deep copy use … technique


Primitives are deep copied


- ! —> logical not
- !! —> cast variable to be a boolean


Both below are the same:

Function hey() {}
Const hey = () => {}


Prototype is base class of class

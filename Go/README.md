# Go Language

- Memory management is managed
- Data Oriented Design (not object orientated)

## Glossary

|      Word       |                                              Definition                                              |
|:---------------:|:----------------------------------------------------------------------------------------------------:|
|    Semantics    |                                          How things behave                                           |
|    Mechanics    |                                        How things are created                                        |
|    Routines     |                                                  -                                                   |
|     Pointer     |                                           Address for data                                           |
|   Data races    |                     * When multiple threads try to mutate data at the same time                      |
|        *        |                                       Access value of Pointer                                        |
|        &        |                               Creating a Pointer for variable or value                               |
| Point semantics | Used when you want to share data through the stack (to different functions) instead of making copies |
| Value semantics |                            When you used copies of data through the stack                            |
|      Heap       |                     Shared storage location where all functions can access data                      |

## Helpful commands

### Go
|           Command           |                             Use                             |
|:---------------------------:|:-----------------------------------------------------------:|
|          `go run`           |                              -                              |
|         `go build`          |          Creates binary file to compile for later           |
|     `goimports -l -w .`     | Print files with incorrect formatting and fix them in place |
|  `go mod init <DIR_PATH>`   |                 Make directory a go module                  |
| `go build -gcflags '-m -l'` |              Show how variables are allocated               |

### Linting (Static check)
More documentation [here](https://staticcheck.dev/docs/running-staticcheck/cli/) regarding uses

|            Command             |                 Use                 |
|:------------------------------:|:-----------------------------------:|
|         `staticcheck`          |            lint go files            |
| `staticcheck -explain <check>` | Explain what given check code means |

## Variables

>[!IMPORTANT]
> - Do not use `var` with pointer semantics or `:=` when assigning (can not assign pointers to variables durin variable declaration)
> - Variable declaration is either via `:=` or `var` NOT both


<details><summary> Declaring </summary>

`var b string`

`var x[3]int`

- Good for zero value initialising. 
- Can also use empty literal construction too: `b := exampleStruct{}`, but that is usually used on return function

```go
var c struct {
    id   int
    name string
}
```
- Good for creating structs on the fly if they are only going to be used in one place (no need to name the struct as that would be pollution)


```go
const(
    dd int
    ee string
    )
```
- Good for declaring or initialising multiple variables/values at once
</details>


<details><summary> Initialise </summary>

`aa := 10`

`var aa int := 10`

`var aa := 10`
- Good for non-zero value initialising

```go
aaa := struct{
    id int
    name string
}{
    id: 1
    name: ana
}
```
- Good for initialising non-zero on the fly struct that is only used in one place
</details>

<details><summary> Literal construction </summary>

```go
type example struct {
    id int
    name string
}
e := example{ id: 1, name: "John"}

// OR

var e example = example{
    id: 1
    name: "John"
}
```
- Good to use for initialising concrete structs

```go
// Array literals
var x = [3]int{10, 20 ,30}
var x = [...]int{10, 20 ,30} // unspecified number
var x = []int{}
```
- Good for initialising arrays 
</details>

<details><summary> Conversion </summary>

Go doesn't have casting, it has conversion. This means you have to create new value to store converted variable.

In fact, no other type can be converted to a bool, implicitly or explicitly. Use `x == 0` or `y == " "` for truthy type values.

> [!WARNING]
> When the type is named (think concrete class), there is no implicit conversion. 
> So with named type struct bob and type struct alice, if they both have the same definition,
> you will not be able to assign a value of bob to a value of alice. But if you have a literal type with the same definition
> of bob (or alice in this case), implicit conversion is possible (example below)

```go
type bob struct{
    id int
    name string
}
type alice struct{
    id int
    name string
}

var e2 struct {
    id int
    name string
}

var b bob
var a alice

b = a // this won't work
b = e2 // this will work
```
</details>

### Constants
- Can come in two kinds: literal and typed

## Types
- Structs are like classes

> [!TIP]
> When optimising for performance, label attributes in struct in order of size from largest 
> to smallest (to optimise memory allocation due to alignment and padding)
> If this is not important, label by readability

- Values are like objects


## Functions

Go routines operate within sandboxed frames on the stack. This means for a given application, 
there will be a slice of the stack and memory  that is sectioned off to implement the application as a whole,
and then further slices of the stack (deeper) that is sectioned off for a function in the app to execute. When that piece is executed,
it then goes up the stack. This is now the active frame, which everything below this frame INVALID and NOT OBTAINABLE.

> [!IMPORTANT]
> Go routines == Executable section of code == Allocated a frame

Each routine gets its own copy of any parameters that is passed to the routine to execute the section of code it needs to.
This means that transformations/mutations are done in isolation (sandbox).

<details><summary> Pass by Value</summary>

```go
func createCount() int{
    var count int
    addCountValue(count, 2)
    return count // this will be 0
}

// The count in this method is a copy of createCount method version. The mutation will not change the above count obj
func addCountValue(count int, value int) int{
    return count + value// this will be 2
}
```
- Good if you want transformations/mutations to be isolated from function to function
</details>

<details><summary> Sharing Data</summary></details>

To share information across routines so that mutations and transformations carry through, use pointer address

```go
func createCount() int{
    var count int
    addCountValue(&count, 2)
    return count // this will be 2
}

// The count in this method is the exact same as createCount version. The mutation will propagate.
func addCountValue(count *int, value int){ //* allows us to undress the pointer and work with value
    *count = *count + value // this will be 2
}
```

## Arrays

> [!IMPORTANT]
> - You must always specify the size of the array if you are going to use it.
> - size of array is considered as PART of the array. This means `var a [3]int` != `var b [4]int`

> [!TIP]
> Use slices instead!


## Slices

 - Use builtin function `make` to create **EMPTY** slice with **NON-ZERO** length e.g `make([]slice, length, capacity)`
 - Slices are defined by their type not by the size of the array
 - You can expand slices! 

> [!IMPORTANT]
> - When expand slices remember they have a return value that should be reassigned to original variable of slice
> - The slice given to append function creates a copy of the slice so remember this 

> [!WARNING]
> There is a difference between declaration of arrays and declaration of slice:
> - `var a []int` == slice
> - `var b [...]int` OR `var b [<number>]int` == array

## Maps

- To create an empty map, use the builtin make: make(map[key-type]val-type).



## For/If-Else loops

There are two ways to define for loop, value semantics and pointers:

```go
var exampleList [2]string{"hey", "ho"}

// pointer loop (mutate exampleList)
for i := range exampleList {
    ...
}

OR

// value loop (list is copied)
for i, v := range exampleList {
    ...
}
```

If conditions do not need to have elses.

```go
if 8%2 == 0 {
   fmt.Println("Divisible by 2") 
}

OR

if 8%2 ==0 {
    fmt.Println("Divisible by 2")
} else if {
    fmt.Println("Not divisible by 2")
}
```

There are also `switch` cases too (similar to Java)

## Packages

Specify the name of current package (script) at the top of the file (before any imports) e.g

```go
package hello

import "fmt"

func SayHello(message string) string {
  fmt.Printf("Hello %s", message)
}
```

## [Naming conventions](http://tinyurl.com/golang-naming-conventions)

- Exported Functions/variables start with uppercase, unexported/private start with lowercase
  - Use camelCase
- Do not use `_` in naming unless using constants and need to seperate the words e.g `INT_MAX`

## Pointer semantics vs Value semantics

- Represent primitive types as values
- Represent slices as value
- Do not use pointer semantics during construction (*)
- With mutations use pointer
- With operations use copies

## Documentation

Write comments on top of the function and it converts to documentation for function (as described [here](https://go.dev/blog/godoc))

## Testing

- `reflect` package contains a function called `DeepEqual` that can compare anything including slices. Good for testing



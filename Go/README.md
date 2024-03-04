# Go Language

- Memory management is managed
- Data Oriented Design (not object orientated)
- [Go playground](https://go.dev/play/)
- Separate state from behaviour
- No inheritance!

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
|      Rune       |                     Similar to other languages concept of character (in string)                      |
| Reference types |                          Maps, Array, Slice, Interface, Functions, Channels                          |

## Helpful commands

### Go code

### Go CLI
|           Command           |                             Use                             |
|:---------------------------:|:-----------------------------------------------------------:|
|          `go run`           |                              -                              |
|         `go build`          |          Creates binary file to compile for later           |
|     `goimports -l -w .`     | Print files with incorrect formatting and fix them in place |
|  `go mod init <DIR_PATH>`   |                 Make directory a go module                  |
| `go build -gcflags '-m -l'` |              Show how variables are allocated               |
|   `go get -u all`           |                                                             |

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

When using structs, you can also validate using the ```` tags:

``go
type Person struct {
  	Name string  `json:"name" validate:"required"`
}
``

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
> to smallest type (to optimise memory allocation due to alignment and padding)
> If this is not important, label by readability

- Values are like objects


## Functions

>[!WARNING]
- Can't use default parameter values
- Can't use optional parameters
- Can't have nullable strings
- 

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

### Method
- Function that has a receiver (parameter) e.g `func (c catlog) GetCatalog(id int) {...}` where the receiver in this case will be the `(c catalog)` bit.


> [!WARNING]
> STICK WITH THE SEMANTICS THAT IS USED ACROSS THE CODE! DO NOT MIX SEMANTICS

> [!IMPORTANT]
> - Receiver should never be more than 3 letters!
> - Receiver is written before the function name!

### Generics

As of Go 1.18, users can use generics. They stated as an additional type parameter list given before the parameter list of a function as shown:

```go
func randomiseValue[T int|float](value T) T { ... }
```

You can also have approximate types that will allow similar types to be used as input (good example given [here](https://sendilkumarn.com/blog/generics-in-go#:~:text=the%20type%20arguments.-,Approximate%20types,-What%20if%20we))

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
> - When expand slices remember they have a return value that should be reassigned to original variable of slice. If not this could cause memory leak as original item no longer directly referenced to
> - The slice given to append function creates a copy of the slice so remember this  (doesn't mutate original slice)

> [!WARNING]
> There is a difference between declaration of arrays and declaration of slice:
> - `var a []int` == slice
> - `var b [...]int` OR `var b [<number>]int` == array
> - Changes to slices of slice will change original slice because underlying backing array is shared among slices (for efficiency)

- Three index slice helps remove side effects when manipulating slices of a slice

- To overcome side effects in general create your own copy using the `copy(a,b)` where `a` is new slice and `b` is old slice.


## Maps

- To create an empty map, use the builtin make: make(map[key-type]val-type). e.g `m := make(map[string]int)`

> [!WARNING]
> A map returns zero value even if the value DOES NOT exist in the map! use comma ok idiom to find if key exists `value, ok := m["key"]`, where `ok` will be false if key doesn't exist in map.

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

if 8%2 == 0 {
    fmt.Println("Divisible by 2")
} else if {
    fmt.Println("Not divisible by 2")
}

OR

if val := 9; num <0 { //Here i have 
  fmt.Println(num)
}
```

In the last example I have assigned a variable that can be used in the subsequent branches of the if/else clause (`val := 9`)

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

### Build and local use of packages

Helpful info on offical website [here](https://go.dev/doc/code#ImportingLocal)

> [!IMPORTANT]
> Build packages to use locally executing `go build` from within package directory root and then use `go list` to list
> available packages as their import paths!

## [Naming conventions](http://tinyurl.com/golang-naming-conventions)

- Exported Functions/variables start with uppercase, unexported/private start with lowercase
  - Use camelCase
- Do not use `_` in naming unless using in a constant string and need to separate the words e.g `INT_MAX`, or make large numbers legible

> [!IMPORTANT]
> Go uses the case of the first letter of the name of a variable/function etc to determine if the item is accessible outside the package!

## Pointer semantics vs Value semantics

- Represent primitive/built-in types USE value semantics (copies of the data)
- Fields in struct? Value semantics (unless struct is being used in relational db)
- Reference type? Value semantics 
  - (can use pointer semantics when decoding/marshaling/encoding)
- Represent slices? as value semantics
- Do not use pointer semantics during construction (&) e.g `b := &person{name: "hello"}` is not good!
- With mutations use pointer
- With operations use copies
- If you want to mutate a reference type, do not use pointer semantics, use value semantics and return new copy of reference from the method
- Does mutation create new object or change original object? think about this if you choose pointer or value semantics (respectively)

## Documentation

Write comments on top of the function, and it converts to documentation for function (as described [here](https://go.dev/blog/godoc))

## Testing

A common way to write tests is using table-driven tests. These are similar to parametrizing your test (like `@pytest.mark.parametrize`).

```go
import (
    "testing"
    "gotest.tools/v3/assert"
)

func TestAddFunction(t *Testing) {
    testCases := []struct{
        number1 int
        number2 int
        result int
    }{
        {1, 2, 3},
        {4, 5, 9},
        {10, 11, 21}  
    }
    for _, tc := range testCases {
        assert.equal(tc.result, AddFunction(tc.number1, tc.number2))
    }
```

- `reflect` package contains a function called `DeepEqual` that can compare anything including slices. Good for testing

## Error handling

- Avoid `else` in error handling! Use switch instead and use negative path (state negative path)
- `nil` will always take on the type it needs

## Interface 

- Describes behaviour (think verb, instead of noun)

> [!IMPORTANT]
> Can group by behaviour but not by noun!
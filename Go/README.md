# Go Language

Memory management is managed

Data Oriented Design (not object orientated)

## Glossary

|    Word    |                                              Definition                                              |
|:----------:|:----------------------------------------------------------------------------------------------------:|
| Semantics  |                                          How things behave                                           |
| Mechanics  |                                        How things are created                                        |
|  Routines  |                                                  -                                                   |
|  Pointer   |                                           Address for data                                           |
| Data races |                     * When multiple threads try to mutate data at the same time                      |
|     *      |                                                  -                                                   |
|     &      | Used when you want to share data through the stack (to different functions) instead of making copies |

## Helpful commands

|         Command          |                             Use                             |
|:------------------------:|:-----------------------------------------------------------:|
|         `go run`         |                              -                              |
|        `go build`        |          Creates binary file to compile for later           |
|   `goimports -l -w .`    | Print files with incorrect formatting and fix them in place |
| `go mod init <DIR_PATH>` |                 Make directory a go module                  |

## Variables

>[!IMPORTANT]
> Do not use pointer semantics during construction
> Use value semantics when assigning for high levels of readability

<details><summary> Declaring </summary>

`var b string`
- Good for zero value initialising. 
- Can also use empty literal construction too: `b := exampleStruct{}`, but that is usually used on return function

```go
var c struct {
    id   int
    name string
}
```
- Good for creating structs on the fly if they are only going to be used in one place (no need to name the struct as that would be pollution)
</details>

```go
```

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
e := example{ id: 1, name: "Hello"}
```
- Good for creating concrete structs 
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
func createCount() {
    var count int
    addCountValue(count, 2)
    return count // this will be 0
}

// The count in this method is a copy of createCount method version. The mutation will not change the above count obj
func addCountValue(count int, value int){
    count := count + value
    return count // this will be 2
}
```
- Good if you want transformations/mutations to be isolated from function to function
</details>

<details><summary> Sharing Data</summary></details>

To share information across routines so that mutations and transformations carry through, use pointer address

```go
func createCount() {
    var count int
    addCountValue(&count, 2)
    return count // this will be 2
}

// The count in this method is the exact same as createCount version. The mutation will propagate.
func addCountValue(count *int, value int){ //* allows us to store address
    *inc++
    return count // this will be 2
}
```


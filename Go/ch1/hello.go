package main

import "fmt"


func CreateCount() int{
    var count int
    AddCountValue(&count, 2)
    return count // this will be 2
}

// The count in this method is the exact same as CreateCount version. The mutation will propagate.
func AddCountValue(count *int, value int){ //* allows us to undress the pointer and work with value
    *count = *count + value // this will be 2
}

type Person struct {
    name string
    age int
}

func AddAge(individual *Person, value int) {
    individual.age = individual.age + value
}

// Test out various forms of declarations and semantics
func testPerson() {
//     pA := &Person{
//         name: "Bob",
//         age: 24,
//     }
//     AddAge(pA, 3)

//     pA := Person{
//         name: "Bob",
//         age: 24,
//     }
//     AddAge(&pA, 3)

    var pA Person = Person{
        name: "Bob",
        age: 24,
    }
    AddAge(&pA, 3)

    fmt.Printf("%+v\n", pA)
}

func main() {
    fmt.Println(CreateCount())
    testPerson()
    var x = [...]int{10, 20 ,30}
    var y = []int{}
    fmt.Printf("Length before append %d\n", len(y))
    y = append(y, 10)
    fmt.Printf("Length after append %d\n", len(y))
    fmt.Println(x)
}
package main

import "fmt"


func CreateCount() int{
    var count int
    AddCountValue(&count, 2)
    return count // this will be 2
}

// The count in this method is the exact same as CreateCount version. The mutation will propagate.
func AddCountValue(c *int, value int){ //* allows us to undress the pointer and work with value
    *c = *c + value // this will be 2
}

type Person struct {
    name string
    age int
}

func (p Person) PrintAge() {
    fmt.Printf("%s is %d years old\n", p.name, p.age)
}

func (p *Person) MethodAddAge(value int) {
    p.age = p.age + value
}

func (p *Person) ChangeName() error {
    p.name = "ChangedName"
    return nil
}

func NonMethodAddAge(p *Person, value int) {
    p.age = p.age + value
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
    NonMethodAddAge(&pA, 3)

    fmt.Printf("%+v\n", pA)
}

func main() {
//     fmt.Println(CreateCount())
//     testPerson()
//     var x = [...]int{10, 20 ,30}
//     var y = []int{}
//     fmt.Printf("Length before append %d\n", len(y))
//     y = append(y, 10)
//     fmt.Printf("Length after append %d\n", len(y))
//     fmt.Println(x)

//     var urlBase []int
//     for i := range "golang" {
//         urlBase = append(urlBase, i)
//     }
//     fmt.Println(urlBase)

//     b := Person{name: "Ana", age: 18}
//     b.MethodAddAge(3)
//     b.PrintAge()

//       var m = map[string]int{}
//       fmt.Println(m["hello"])
//       _, ok := m["hello"]
//       fmt.Println(ok)
//
//       m["hey"] = 1
//
//       for key, value := range m {
//         fmt.Println(key, value)
//       }

    p := Person{
        name: "Ana",
        age: 24,
    }
    if err := p.ChangeName(); err != nil { // Good if function is pointer semantic based and can only return an error
        fmt.Errorf("Error changing name")
    }
    fmt.Println(p)

//     if p.age == 0 || p.age == 1 {
//         fmt.Println("yay it works")
//     }
}
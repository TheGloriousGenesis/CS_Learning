package main

import "fmt"


func createCount() int {
    var count int
    addCountValue(&count, 2)
    return count // this will be 2
}

// The count in this method is the exact same as createCount version. The mutation will propagate.
func addCountValue(count *int, value int) *int{ //* allows us to store address
    return &count + value
//     return *count // this will be 2
}

func main() {
    fmt.Println("Hello, world!")
    fmt.Println(createCount())
}
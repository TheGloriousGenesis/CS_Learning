# React

Everything i've noted down from my journey with react

### React vs Angular
|Angular|React|
|:-----:|:---:|
|App with many users and interactions |App with frequently variable data|
|Two way data binding (child to parent/parent to child)|One way data binding (parent to child)|
|Popular for OOP (has dependancy injection) | Does not have dependancy |
|Heavy framework: has built in routing, Ajax requests, forms, test runner/framework | Lighter framework: Doesn't have anything mentioned with Angular, have to add additional libraries|
|Components defined by classes only |Components defined by functions and classes|
|Stateful service classes can be used to share state across an application| Not sure|
|Custom html elements| Custom html elements|
|Angular CLI| Nothing that is useful|
|||

## Section 29: Optional: React Summary & Core Feature Walkthrough
- Skip 446- 454 general background to React, descriptive, how project is structured, not needed, mentioning html usage and basic
syntax

### Components
- Every UI piece is a component
- Every component function gets given a prop function to work with and has state
- Observable pattern and listens for changes to these components when figuring out whether to rerender or not
- To improve performance, only tshe components that need rerendering are rerendered
- Component can be referenced by a html like tag for example : `<Component />`
- User defined components do not have built in props like `onClick` etcm they have to be configured themselves (all functions)
- Props define what can be passed into the component at a higher(parent) level

[comment]: <> (```javascript)

[comment]: <> (function Model&#40;props&#41; {)

[comment]: <> (    function testFunction&#40;&#41; {)

[comment]: <> (        props.onClick&#40;&#41;;)

[comment]: <> (    })
    
[comment]: <> (    return &#40;)

[comment]: <> (        <div>)
            
[comment]: <> (        </div>)

[comment]: <> (    &#41;)

[comment]: <> (})

[comment]: <> (```)


### State and Props
- Difference between state and props is that state is an internal property controlled from the component and props are 
externally defined
- Props can not be modified. If its been fed into the component thats it. State can be modified using the `this.setState` functionality
- Better example: state is like attributes of a class, props like parameters.
- React uses state in order to change values
- `useState` is popular function. Two outputs (attribute, function) where the function conditionally triggers rerender
of page
- Special types of props determined by prefix ‘on’, is Reacts way of event listening. Instead of object in this case it wants a function.
- React does not rerender when variables change in the class change. You have to manually state this.

### Hooks
- Allow state and lifecycle methods in functional components (functional components being simple functions)
- Allow large functions to be split into smaller understandable pieces
- Hooks must usually be called inside function
- Hooks can be custom or can use inbuilt React ones `useState`: manage state, `useEffect`: manage side effects (edit DOM manually)
- Difference in return type for React components:
  - Render() —> Normal react 
  - Return() —> Hook 
- useState returns array [value, updatingFunction] where first element is current state value, second is the function you need to use to update the state e.g const [title, setTitle]
- Hook can be called multiple times depending on how many instances of the component we have. Each instance is managed independently by react

### Handling Events
- A function defined without the rounded brackets on a html element event handler will bind an action to the method of
choice. Below will print 'Hello' to the DOM.
```javascript
function methodToExecute() {
    console.log('Hello');
}

return (
    <div> 
        <button className='btn' onClick={methodToExecute}> </button>
    </div>
)
```

General React - https://saurabhshah23.medium.com/react-js-architecture-features-folder-structure-design-pattern-70b7b9103f22

- Export all classes to avoid conflicts

Index.js or name of component : default entry point to every react application
/components: shared components amongst features placed here
/assets : static assets (like images) should be kept here
routes.config.ts : containers all the routes of the application defined in one place
/pages : All the features, screens, pages are defined here
- Each screen has index.js that exports the container and makes the screen available as module
- Each
/utils : utility / helper methods can be shared across entire project

/areas
/every directory has a routes file that describe the components that are render in response to config

/hook

Use states :

Asynchronsous call via Apollo

Use… a hook that you have to create

Custom component must start with UpperCase

Instead of *ngIf they use {condition && <html>}

They have a scss.d.ts class to get consts that represent the style associated underneath

Data-cy is how they label there html elements to use for testing (similar to “label’ in angular for testing

Data is set through curly brackets {}

An interface defines variables that must be defined in the

Components in react are just functions with output jsx

Can omit the closing tag for custom react components if there is no content between the opening and closing tags

To pass data through components use props and set values in component tag using the following way: <ExpenseDate date={} /> where ExpenseDate class has date set as a variable

Team uses an interface instead of feeding props into a function. This means when an object extends from props it will have that as its core variables and that input into the object needs to be defined



useLocalStorage() —> caching frontend
useEffect
useCallback

Mounting?

React State


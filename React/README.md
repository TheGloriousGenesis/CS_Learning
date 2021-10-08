# React
Single page application
Jump to Summary in Section 29

## Section 29: Optional: React Summary & Core Feature Walkthrough
- Skip 446- 454 general background to React, descriptive, how project looks, not needed, mentioning html usage and basic
syntax
- 
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

Render —> Normal react
Return —> Hook (different functions to support —>)

useLocalStorage() —> caching frontend
useEffect
useCallback

Mounting?

React State
- Special types of props determined by prefix ‘on’, React way of event listening. Instead of object it wants a function.
- React does not rerender when variables change. You have to manually state this.
- Hooks must usually be called inside function
- useState returns array [value, updatingFunction] where first element is current state value, second the function you need to use to update the state e.g const [title, setTitle]
- Hook can be called multiple times depending on how many instances of the component we have. Each instance is managed independently by react



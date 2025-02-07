## Slicing
We can also use slicing to access and modify multiple elements of a multi-dimensional array at once. We use the slice notation arr[i:j, k:l] to access a subarray that contains rows i through j-1 and columns k through l-1

As with Python sequences, you can specify an “empty” slice to include all possible entries along an axis, 
by default: grades[:, 1] is equivalent to grades[0:n-1, 1] where n is the length of the array


This is because NumPy will automatically insert trailing slices for you if you don’t provide as many indices as there are dimensions for your array. grades[0] was treated as grades[0, :].


### Links

- https://www.freecodecamp.org/news/multi-dimensional-arrays-in-python/
- https://www.pythonlikeyoumeanit.com/Module3_IntroducingNumpy/AccessingDataAlongMultipleDimensions.html#Slice-Indexing
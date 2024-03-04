contex# Fiber

Fiber is GoLangs fastest HTTP engine

Its suppose to be highly performant with zero memory allocation

## Uses

When using fiber, you need to have a context. This context allows api communications.

This context reuse values so do not keep references outside the handler the ctx is being used in.

When new handler is created and ctx is used, old references will be corrputed as the values are being reused

You can create immutable values using `utils.CopyString` in `gofiber/utils`

## Questions

1. Why is zero memory allocation good?
   1. What is the benefit for the user



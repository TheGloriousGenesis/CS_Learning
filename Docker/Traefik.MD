# Traefik

## Glossary
service - Can have a one to many relationship with router
router - 

## Under the hood
Traefik creates for each container a service and a router.

Default service contains 1 server per instance of container (which automatically set port to port of container), and default router contains one rule  (`defaultRule`)

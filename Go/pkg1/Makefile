.DEFAULT_GOAL := build # defines which command (target) run as default if nothing given

fmt:
	go fmt ./...
.PHONY:fmt # ensures no clashing with directories that have fmt name

# golint has been deprecated
lint: fmt # states that fmt target must be run before linting
	golint ./...
.PHONY:lint # ensures no clashing with directories that have lint name

vet: fmt # states that fmt target must be run before vet
	go vet ./...
.PHONY:vet # ensures no clashing with directories that have vet name

build: vet # states that vet target must be run before linting
	go build hello.go
.PHONY:build # ensures no clashing with directories that have build name
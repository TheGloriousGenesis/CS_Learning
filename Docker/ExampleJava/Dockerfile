# syntax=docker/dockerfile:1

# Works for prebuilt jar : SIZE = 326MB
#FROM openjdk:17-alpine
#COPY target/ExampleJava-1.0-SNAPSHOT.jar /ExampleJava.jar
#COPY pom.xml ./
#CMD ["java", "-jar", "/ExampleJava.jar"]

# Works for building jar using dockerfile : SIZE = 326MB
FROM maven:3.8.3-openjdk-17-slim AS build
COPY src ./src
COPY pom.xml .
RUN mvn -f pom.xml clean package

FROM openjdk:17-alpine
COPY --from=build target/ExampleJava-1.0-SNAPSHOT.jar /ExampleJava.jar
CMD ["java", "-jar", "/ExampleJava.jar"]

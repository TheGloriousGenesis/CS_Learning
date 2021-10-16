# syntax=docker/dockerfile:1

FROM openjdk:16-alpine

RUN MKDIR /project
COPY . /project
WORKDIR /project
RUN mvn clean package -DskipTests

RUN apk add dumb-init
RUN mkdir /app
RUN addgroup --system javauser && adduser -S -s /bin/false -G javauser javauser
COPY --from=build /project/target/ExampleJava-1.0-SNAPSHOT.jar /app/ExampleJava.jar
WORKDIR /app

#COPY target/ExampleJava-1.0-SNAPSHOT.jar /ExampleJava.jar

#COPY pom.xml ./

#RUN ./mvnw dependency:go-offline

#COPY src ./src

#CMD ["./mvnw", "spring-boot:run"]
RUN chown -R javauser:javauser /app
USER javauser
CMD "dumb-init" "java" "-jar" "java-application.jar"


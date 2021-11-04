plugins {
    kotlin("jvm") version "1.5.31"
    kotlin("plugin.spring") version "1.5.31"
    kotlin("plugin.jpa") version "1.5.31"
}

group = "per.study"
version = "beta-0.1"

repositories {
    mavenCentral()
}

dependencies {
    implementation("org.jetbrains.kotlin:kotlin-stdlib")
    implementation("org.springframework.data:spring-data-jpa:2.5.6")
    implementation("org.hibernate:hibernate-entitymanager:5.5.6")
    implementation("com.h2database:h2:1.3.148")
}

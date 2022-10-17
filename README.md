# Table of Contents

1. [Python PROLOG Interpreter Library](#python-prolog-interpreter-library)
2. [Introduction](#introduction)
3. [Installation and Usage](#installation-and-usage)
4. [References and Contact](#references-and-contact)
5. [License](#license)

# Python PROLOG Interpreter Library

**PPI** - is a simple Python witten library, that will allow you to use PROLOG syntax
within your Python code and operate on it. 

## Introduction

**Prolog** - is logical programming language that works on **binary boolean logic**. It means
that every statement in Prolog can be either **false** or **true**.

There are 3 whales **Prolog** stands on:
- **Facts** - facts describe objects and relations between them. 
    In order to do that, we use _predicates_ (_relations_) and _arguments_ (_objects_).
    ```
    predicate(arguments)
    ```
    This is very similar to how we describe functions in other programming languages.
    Using **_facts_**, we can build **_Knowledge Databases_**, that will be the main base of items to operate on.
- **Rules** - conditional statements about the existence of dependencies between objects. Here is how rules are described:
  ```
  name_of_rule(arguments) if
                other_rule(arguments) and
                other_rule(arguments) and
                ...
                predicate(arguments).
  ```
- **Requests** - we can request **Prolog** to show objects and how they are related.

## Installation and Usage

## References and Contact

- Developer contact - [mikhail.bahdashych@protonmail.com](mailto:mikhail.bahdashych@protonmail.com)

## License

Licensed by [MIT License](LICENSE).

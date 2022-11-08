# Table of Contents

1. [Python PROLOG Interpreter CLI](#python-prolog-interpreter-cli)
2. [Introduction to PROLOG](#introduction-to-prolog)
   1. [Facts](#facts)
   2. [Rules](#rules)
   3. [Requests](#requests)
3. [Installation](#installation)
4. [Documentation](#documentation)
   1. [Interactive CLI](#interactive-cli)
   2. [Classical Terminal-Based Application](#classical-terminal-based-application)
5. [References and Contact](#references-and-contact)
6. [License](#license)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

---

# Python PROLOG Interpreter CLI

**PPIL** - is a simple `Python` witten library, that will allow you:
- Use `PROLOG` syntax within your Python code and operate on it.
- Use `Python` data objects to write `PROLOG` syntax.
- Read, write and compile `PROLOG` through `Python`. 
- Fetch data from opened sources.
- **And more, more, more...**

Application consists 2 parts:
- **Interactive CLI** and **Classical terminal-based application**
- `Python` library

Documentation and guidelines for every mode will be listed in [Documentation](#documentation) section.

What you see right now, is CLI. In case if you want to use library and use
Prolog syntax within your Python applications see [this](https://github.com/bl4drnnr/python-prolog-interpreter-lib) repository in order
to obtain more information.

---

## Introduction to PROLOG

**Prolog** - is logical programming language that works on **binary boolean logic**. It means
that every statement in Prolog can be either **false** or **true**.

There are 3 whales **Prolog** stands on:

### Facts

- **Facts** - facts describe objects and relations between them. In order to do that, we use _predicates_ (_relations_) and _arguments_ (_objects_).
```
predicate(arguments)
```
This is very similar to how we describe functions in other programming languages.
Using **_facts_**, we can build **_Knowledge Databases_**, that will be the main base of items to operate on.

Here is simple example of what predicates are, and how they work:
```
loves(james, books).
```
Above was described the simples example of what predicate is. **Pay attention, that everything was written in lowercase.**
**This is very important, because uppercase in Prolog means other things.** We will talk about it later.
    
Basically, this statement tell us that _James loves books._ And by using **requests** we can check it. Also, pay
attention, that using PROLOG CLI in order to call predicate, use need to use period at the end.

```
? - loves(james, books).
true.
```

But, if we change something in this statement, name _James_ on other name, of _books_ on something else,
keeping in mind, that in this case out **_Knowledge Databases_** is only one fact, we will get `false`.

```
? - loves(james, fishing).
false.
```

Now, let's discuss, how variables work in PROLOG. First of all, what you should know, is that they are case-sensitive.
Basically, as it was mentioned above, variables are written in uppercase. Let's break down next Knowledge Databases:

```
eat(james, apples)
eat(ann, pie)
eat(janny, apples)
```

It's simple Knowledge Databases of what 3 persons eat. Now, using variables, we can ask PROLOG, about who eat apples.
In order to do that, we need to replace records we want to find with upper-case variables. Here is an example:

```
? - eat(X, apples).
X = james
X = janny
```

As a result, we can see, that there are 2 persons who eat apples, _James_ and _Janny_.

In conclusion, we can say, that **Rules** are basic and fundamental part of `PROLOG` programming languages.
They are used in order to build **_Knowledge Databases_** - facts, describing objects and relations between them.
Facts can be either without arguments or with any quantity of arguments. Expect checking facts on what is `true` or `false`
we can, using uppercase variables, list what records are `true`.

### Rules
- **Rules** - conditional statements about the existence of dependencies between objects. Here is how rules are described:
```
name_of_rule(arguments) if
   other_rule(arguments) and
   other_rule(arguments) or
         ...
   predicate(arguments).
```

Keywords `if`, `and` and `or` can be replaced with `:-`, `,` and `;`. So, the rule above we can rewrite in the next way:

```
name_of_rule(arguments) :-
   other_rule(arguments),
   other_rule(arguments);
         ...
   predicate(arguments).
```

The best way to see how rules work is to show it on an example. Let's take the next knowledge databases,
that is describing parenthood between 2 persons. In this case, as the first argument we have parent, and
on the second place we have a child - this is `parent` predicate. Also, we will have one more predicate,
describing `sex` of this person - `male` of `female`. So, here is how it looks like:

```
parent(zofia, marcin).
parent(andrzej, marcin).
parent(andrzej, kasia).
parent(marcin, ania).
parent(marcin, krzyś).
parent(krzyś, mikołaj).

sex(zofia, female).
sex(kasia, female).
sex(ania, female).
sex(andrzej, male).
sex(marcin, male).
sex(krzyś, male).
sex(mikołaj, male).
```

Therefore, using obtained knowledge how rules should look like and how variables work in predicate, we can
create our own rule. For example, let's create rule, that is going to check if, first person is mother for
another person. Here is how it will look like:

```
mother(X, Y) :- parent(X, Y), sex(X, female).
```

Let's break this down in more human-readable language to understand how it works. Basically, this statement tells us:

The person `X` is mother for `Y` - `mother(X, Y)` - if - `:-` - they are in parenthood relationships - `parent(X, Y)`
and - `,` - the person `X` is `female` - `sex(X, female)`. Let's test it on some examples.

Remember, that in case of rules, rule's arguments from left part are pasted as variables in right part.

```
? - mother(zofia, marcin).
true.
```

Yes, this statement is true, because `zofia` is, as we described, `female` - `sex(zofia, female).` and
she is in parenthood relationships with `marcin`, as we described also - `parent(zofia, marcin).`.

### Requests
- **Requests** - we can request **Prolog** to show objects and how they are related.

They are the easiest part of PROLOG. Their purpose, is to call _predicates_ and _rules_ in order
to show result - `true` or `false`. **Remember, PROLOG is logic language, and it's working
on binary logic - true or false. These are only 2 types of response.**

The easiest way to use PROLOG language is to use `SWI-Prolog` CLI tool. Right after compiling and importing
knowledge database into program, you are able to request _predicates_ and _rules_. After providing
predicate or rule, don't forget about period at the end of the line, before you click `ENTER`.

```
? - loves(james, books).
true.
```

If you have more complicated database, and you are using variables in order to obtain information,
if quantity of outcome records more than 1, you can list them by clicking `;`.

```
? - eat(X, apples).
X = james
X = janny;
```

Also, we can stop this searching by clicking `.` instead of `;`.

In case, if you want to use rule, the situation is very similar to just predicates.
It will be enough to type name of the rule, pass argument and put period at the end, click `ENTER`.

---

## Installation

- For **MacOS** and **Linux**:

Open terminal, paste and execute next command.

```shell
bash <(curl -s -S -L https://raw.githubusercontent.com/bl4drnnr/python-prolog-interpreter-cli/master/install.sh)
```

Right after installation is done, close and restart terminal. Then, open it and type `ppil -h`.
If you see help messages, application has been installed correctly. 

---

## Documentation

As it has been written above, CLI is divided on 2 parts - **interactive CLI** and **classical terminal-based application**.


### Interactive CLI

### Classical terminal-based application

---

## References and Contact

- Developer contact - [mikhail.bahdashych@protonmail.com](mailto:mikhail.bahdashych@protonmail.com)
- [Prolog on wiki](https://en.wikipedia.org/wiki/Prolog) - Official english page of Prolog programming language on Wikipedia
- [Prolog website](https://www.swi-prolog.org/) - Official site and documentation of Prolog
- [Prolog. Programming W. F. Clocksin C. S. Mellish](https://www.amazon.com/Programming-Prolog-Using-ISO-Standard/dp/3540006788/ref=sr_1_1?crid=3SI3X3IWULTLU&keywords=Programming+in+Prolog&qid=1666038671&qu=eyJxc2MiOiIwLjU4IiwicXNhIjoiMC42NSIsInFzcCI6IjAuNzIifQ%3D%3D&s=books&sprefix=%2Cstripbooks-intl-ship%2C234&sr=1-1) - Prolog guidebook

---

## License

Licensed by [MIT License](LICENSE).

# Bibel verse list

## Introduction

This is tool that I have written for myself in Python to support me in learning verses from the Bibel. It is very lightweight, as it only uses functionality from the standard library and does not require any dependencies. I decided against using a database, because with this approach I can fully customize the UI for my needs to increase my productivity and I do not require any infrastructure. Also, since the store is a text file, I can effectively back it up in Git version control. This tool is meant to be executed in a Linux command line.

The reason I have written this, is that it was hard to keep of all the verses that I learned and which I still what to learn by just using paper lists. I wanted to avoid having duplicates in this list. This tool aims to increase productivity while be as simple as possible. There are a few drawbacks however. Since the datastore is just a JSON file, the running time might be inefficient. But since I will probably never learn more than 500-1000 verses in my life, I do not think this will actually matter. The tool is a bit restricted in the sense, that it does not understand dot or dash notation. So you cannot enter a list of verses such as "Mk 2,20-25", you need to enter each verse individually. Also the database in the background will store each verse individually and the tool will not see them as a unit. Furthermore this tool is only meant as a store of bibel locations, not the actual text itself. It is merely an advanced list, you are expected to use a bibel in combination with it.

Note that this tool uses German language and all books are in short notation. If you enter a verse for a book that only has a single chapter, the chapter must be omitted.

## Planned features

I plan to use this tool for the next several years, so I will probably push some updates from time to time. I currently plan the following:
* Implement various statistics about the data store
* Improve the user interface in general, and implement an ncurses-like interface in particular
* Maybe an import function for bulks of verses, to better get you started
* Maybe I will implement the dash notation
* Even more input validation
* Print out random learned verse for control

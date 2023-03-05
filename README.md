# Simple Priority Queue
> Implementation of a simple priority queue to process work items.

## Table of Contents
* [Description](#description)
* [Features](#features)
* [Setup](#setup)
* [Usage](#usage)
* [Room for Improvement](#room-for-improvement)
* [Author](#author)

## Description
#### Problem This Project Is Intended To Solve
- process an incoming stream of work items in order of their priority level
- the incoming stream is a dictionary of work items
- each work item which contains two keys:
  - the command to be executed
  - the priority level
    - an integer value from 0 to 10
- work items of the same priority are processed in the order they are received

## Features
- the raw stream of work items can be validated before being inserted into the priority queue
- while iterating over a list, if the list is modified, there is a known issue that it will break the associate between the index and the element
  - to avoid that issue, the cleanse_stream() function processes the list starting from the back
  - this way, it allows us to delete the element while still maintaining the index-to-element association

## Setup
This project was written in Python 3.9.13

## Usage
See the file `run_example.py` which demonstrates the following example usage:
1. Create the sample stream of work items.
1. Instantiate the SimplePriorityQueue class.
1. Get a clean stream by calling cleanse_steam() on the sample stream.
1. Give the clean stream as an argument to ingest_stream().
1. Start the processing the stream by calling: process_priority_queue().
```
sample_stream = [
    {"priority": 2, "command": "Running command expected order #4"},
    {"priority": 3, "command": "Running command expected order #2"},
    {"priority": 1, "command": "Running command expected order #5"},
    {"priority": 4, "command": "Running command expected order #1"},
    {"prioity": 5, "command": "Running command expected order #0"},
    {"priority": 11, "command": "Running command expected order #0"},
    {"priority": 1, "command": "Running command expected order #6"},
    {"priority": 3, "command": "Running command expected order #3"},
]

my_queue = priority_queue.SimplePriorityQueue()
clean_stream = my_queue.cleanse_stream(sample_stream)
my_queue.ingest_stream(clean_stream)
my_queue.process_priority_queue()
```

## Room for Improvement
1. add test to validate that the command is valid before executing
1. add feature to run command in a subprocess
1. add feature that a valid priority level can be either an integer [8] or a string ["8"]
1. add feature to allow for the insertion of new work items into priority queue while the priority queue is being processed
1. add feature to run the priority queue for a specified number of work items and then stop processing
1. add feature to prompt the user to input new work items

## Author 
Albert Tam
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
- during the ingest of the raw stream of work items, each work item is validated before being inserted into the incoming stream
- provided an optional argument to the move_items_from_stream_to_priority_queue()
  - option to move over a given number of items from the incoming stream
  - option to move all the items from the incoming stream
- provided an optional argument to the process_priority_queue()
  - option to process a given number of items in the priority queue
  - option to process all the items in the priority queue
- provided an example usage folder of scripts which do some simple unit tests

## Environment
This project was written in Python 3.9.13 on Windows 10

## Usage
Please see the included files in the folder named `example_usage`.
Those example scripts demonstrates how to:
1. Create a sample stream of work items.
1. Instantiate the SimplePriorityQueue class.
1. Ingest a sample stream of work items.
1. Move the work items from the incoming stream to the priority stream.
1. Processing the work items in the priority queue.

## Room for Improvement
1. add more work item validations to the cleanse_item() function
1. ability to have a live stream of incoming work items while the priority queue is being processed
1. add test to validate that the command will run without erroring out before executing
1. add feature to run command in a subprocess
1. add feature that a valid priority level can be either an integer [8] or a string ["8"]
1. add feature to prompt the user to input new work items

## Author 
Albert Tam

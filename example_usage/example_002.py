"""
Example of how to run the Simple Priority Queue implementation.
"""

import pprint as pp
import sys
sys.path.insert(0, '..')
from queue_module import priority_queue


if __name__ == "__main__":
    # Create an instance of the SimplePriorityQueue
    # and run it on the sample_stream below.

    # Test cases:
    # -enqueuing 0 items and processing 0 items
    # -enqueuing 5 items (where 4 are invalid) and processing 1 items
    # -enqueuing 0 items and processing 0 items

    sample_stream = []
    print(">>> Raw stream before processing:")
    pp.pprint(sample_stream, indent=4)
    print(">>> The expected output is:")
    print(">>>")
    my_queue = priority_queue.SimplePriorityQueue()

    my_queue.ingest_raw_stream(sample_stream)
    my_queue.move_items_from_stream_to_priority_queue()
    my_queue.process_priority_queue()

    sample_stream = [
        {},
        {"command": "Missing priority, expecting to skip this work item."},
        {"priority": 5},
        {"priority": 5,
         "some unregistered key":
             "Missing command, expecting to skip this work item"},
        {"priority": 5, "command": "Running command expected order #1",
         "extra_key": "extra value"},
    ]
    print(">>> Raw stream before processing:")
    pp.pprint(sample_stream, indent=4)
    print(">>> The expected output is:")
    print("\
>>>     Executing command: Running command expected order #1\n\
    ")
    my_queue.ingest_raw_stream(sample_stream)
    my_queue.move_items_from_stream_to_priority_queue()
    my_queue.process_priority_queue()
    my_queue.process_priority_queue()

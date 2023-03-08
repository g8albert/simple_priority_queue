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
    # -enqueuing 8 items (with 2 invalids) and processing all the items

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
    print(">>> Raw stream before processing:")
    pp.pprint(sample_stream, indent=4)
    print(">>> The expected output is:")
    print("\
>>>     Executing command: Running command expected order #1\n\
>>>     Executing command: Running command expected order #2\n\
>>>     Executing command: Running command expected order #3\n\
>>>     Executing command: Running command expected order #4\n\
>>>     Executing command: Running command expected order #5\n\
>>>     Executing command: Running command expected order #6\n\
        ")
    print(">>> The actual output is:")
    my_queue = priority_queue.SimplePriorityQueue()

    my_queue.ingest_raw_stream(sample_stream)
    my_queue.move_items_from_stream_to_priority_queue(num_items=10)
    my_queue.process_priority_queue(num_items=10)

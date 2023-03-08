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
    # -enqueuing 1 item and processing 1 item
    # -enqueuing 2 item and processing 2 items

    sample_stream = [
        {"priority": 2, "command": "Running command expected order #1"},
        {"priority": 3, "command": "Running command expected order #3"},
        {"priority": 4, "command": "Running command expected order #2"},
    ]
    print(">>> Raw stream before processing:")
    pp.pprint(sample_stream, indent=4)
    print(">>> The expected output is:")
    print("\
>>>     Executing command: Running command expected order #1\n\
>>>     Executing command: Running command expected order #2\n\
>>>     Executing command: Running command expected order #3\n\
    ")
    print(">>> The actual output is:")
    my_queue = priority_queue.SimplePriorityQueue()

    my_queue.ingest_raw_stream(sample_stream)
    my_queue.move_items_from_stream_to_priority_queue(num_items=1)
    my_queue.process_priority_queue(num_items=1)

    my_queue.move_items_from_stream_to_priority_queue(num_items=2)
    my_queue.process_priority_queue(num_items=2)

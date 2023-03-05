"""
Example of how to run the Simple Priority Queue implementation.
"""
import pprint as pp
from queue_module import priority_queue

if __name__ == "__main__":
    # Create an instance of the SimplePriorityQueue
    # and run it on the sample_stream below.

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
    print(">>> List of work items before being processed:")
    pp.pprint(sample_stream, indent=4)
    my_queue = priority_queue.SimplePriorityQueue()
    clean_stream = my_queue.cleanse_stream(sample_stream)
    my_queue.ingest_stream(clean_stream)
    my_queue.process_priority_queue()

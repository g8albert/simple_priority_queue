"""
Implementation of a priority queue.
"""


class SimplePriorityQueue():
    """A simple priority queue to process work items.

    Starting at the most granular level,
    each work item is a dictionary contains two keys:
        priority (int): Priority level from 0 to 10, 10 is highest priority.
        command (str): The command to be executed.

    Example of a work item:
        work_item = {"priority": 1, "command": "dir C:/"}

    The incoming stream is a list of work items, processed from the front.

    Example of the incoming stream:
        incoming_stream = [
            {"priority": 1, "command": "dir C:/one"},
            {"priority": 10, "command": "dir C:/three"},
            {"priority": 1, "command": "dir C:/two"}
        ]

    Now, the priority queue is implemented as a dictionary of 11 lists.
    Each list would hold all the work items for one the priority levels
    from 0 to 10, in the order received, with the earliest item at the front.

    Example of the priority queue:
        priority_queue = {
            0: [],
            1: [
                {"priority": 1, "command": "dir C:/one},
                {"priority": 1, "command": "dir C:/two}
            ],
            ...,
            10: [
                {"priority": 10, "command": "dir C:/three"}
            ]
        }

    To see the simple priority queue in action,
    first, we begin by ingesting a raw stream of work items.
    Second, we cleanse the incoming stream of invalid work items.
    Thirdly, we move work items from the (cleansed) incoming stream to the
    priority queue until the incoming stream is empty.

    Finally, each work item in priority queue is processed, starting at the
    highest priority level.
    When a work item is processed, the command is echoed to the standard
    output.
    """

    def __init__(self):
        self.priority_queue = {}
        self.stream = []

    def initialize_priority_queue(self):
        """Initializes each list in the priority queue to the empty list."""
        for i in range(0, 11):
            self.priority_queue[i] = []

    def ingest_stream(self, stream):
        """Ingest the incoming stream, which is a list of work items.

        Args:
            stream (list of dicts): List of work items.
        """
        self.stream = stream

    def pop_stream(self):
        """Pop the next item from the front of the incoming stream.

        Returns:
            item (dict): A work item as described in the class description.
            Otherwise, return an empty dictionary.
        """
        result = {}
        if len(self.stream) != 0:
            result = self.stream[0]
            del self.stream[0]
        return result

    def push_priority_queue(self, item):
        """Insert an item into the priority queue according
        to its priority level.

        New items of the same priority level are inserted
        at the back of the queue of their priority level.

        Args:
            item (dict): A work item as described in the class description.
        """
        self.priority_queue[item.get("priority")].append(item)

    def pop_priority_queue(self):
        """Pop the highest priority level work item from the priority queue.

        Returns:
            item (dict): A work item (as defined in the class description).
            Otherwise, an empty dictionary.
        """
        for priority_queue_number in reversed(range(0, 11)):
            for item in self.priority_queue.get(priority_queue_number):
                del self.priority_queue[priority_queue_number][0]
                return item

    def execute_work_item(self, item):
        """Execute the command in the work item.

        Args:
            item (dict): A work item as described in the class description.
        """
        if not item:
            return

        command = item.get("command")
        if command:
            print(f">>>     Executing command: {command}")

    def cleanse_stream(self, stream):
        """Remove invalid work items from the stream.

        Args:
            stream (list of dicts)

        Returns:
            A list of dictionaries with valid work items.
            Otherwise, return an empty dictionary.

        Note:
            While iterating over the stream list,
            to prevent breaking the association of the index to the element,
            we process the list starting from the back.
            This allows us to delete the element if it is invalid while still
            maintaining the index to element association as we proceed to the
            front of the list.
        """
        for index in reversed(range(len(stream))):
            item = stream[index]
            if "priority" not in item \
                    or "command" not in item \
                    or item.get("priority") \
                    not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
                del stream[index]
                continue

        return stream

    def process_priority_queue(self):
        """Process each work item in priority queue in order of priority level.
        """
        print(">>>")
        print(">>> Begin processing of Simple Priority Queue.")
        self.initialize_priority_queue()

        # Pop each work item from the incoming stream and
        # push it into the priority queue.
        while len(self.stream) != 0:
            self.push_priority_queue(self.pop_stream())

        # Pop the highest priority level work item from the priority queue and
        # process it.
        next_item = self.pop_priority_queue()
        while next_item:
            self.execute_work_item(next_item)
            next_item = self.pop_priority_queue()

        print(">>> End of Processing Simple Priority Queue.")
        print(">>>")

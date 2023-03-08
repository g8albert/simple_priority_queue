"""
Implementation of a priority queue.
"""


class SimplePriorityQueue():
    """A simple priority queue to process work items.

    Description of Data Structures Used:
        Starting at the most granular level,
        each work item is a dictionary contains two keys:
            priority (int): Priority level from 0 to 10,
                where 10 is the highest priority level.
            command (str): The command to be executed.

        Example of a work item:
            work_item = {"priority": 1, "command": "dir C:/"}

        The incoming stream is a list of work items,
        processed starting from the front.

        Example of the incoming stream:
            incoming_stream = [
                {"priority": 1, "command": "dir C:/one"},
                {"priority": 10, "command": "dir C:/three"},
                {"priority": 1, "command": "dir C:/two"}
            ]

        Now, the priority queue is implemented as a dictionary of 11 lists.
        Each list would hold all the work items for one the priority levels
        from 0 to 10, in the order received, with the earliest item at the
        front.

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

    How The Process Operates:
        To see the simple priority queue in action, we use 3 functions.

        First, we begin by using ingest_raw_stream() to ingest all the work
        items in the given raw stream (list).
        As we ingest each work item, "invalid" work items are removed.

        Secondly, we use move_items_from_stream_to_priority_queue() to move
        either all or a given number of work items from the incoming stream
        to the priority queue, which is sorted by priority
        level.

        Finally, we use process_priority_queue() to process either all or a
        given number of work items in the priority queue.  It starts
        processing with the work item with the highest priority level.

        Items of the same priority level are processed in the order received.
        When a work item is processed, the command is echoed to the standard
        output.
    """

    def __init__(self):
        self.priority_queue = {}
        self.incoming_stream = []
        self.initialize_priority_queue()

    def initialize_priority_queue(self):
        """Initializes each list in the priority queue to the empty list."""
        for index in range(0, 11):
            self.priority_queue[index] = []

    def ingest_raw_stream(self, stream):
        """Copy each item from the front of the given stream argument
            and append it to the back of the incoming stream.

        Args:
            stream (list of dicts): List of work items.
        """
        while len(stream) > 0:
            item = stream.pop(0)
            item = self.cleanse_item(item)
            if item:
                self.incoming_stream.append(item)

    def pop_stream(self):
        """Pop the next item from the front of the incoming stream.

        Returns:
            item (dict): A work item as described in the class description.
            Otherwise, return an empty dictionary.
        """
        result = {}
        if len(self.incoming_stream) != 0:
            result = self.incoming_stream[0]
            del self.incoming_stream[0]
        return result

    def push_priority_queue(self, item):
        """Append the given item to the back of the priority queue according
            to its priority level.

        Args:
            item (dict): A work item as described in the class description.
        """
        self.priority_queue[item.get("priority")].append(item)

    def pop_priority_queue(self):
        """Pop the highest priority level work item from the priority queue.

        Returns:
            item (dict): A work item as defined in the class description.
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

    def cleanse_item(self, item):
        """Return the work item if it is valid,
            otherwise return an empty dictionary.

        A valid work item contains the key "command", "priority",
        and the priority is a number from 0 to 10.

        Args:
            item (dict): A work item as described in the class description.

        Returns:
            The work item if it is valid.
            Otherwise, return an empty dictionary.

        """
        if "priority" not in item \
                or "command" not in item \
                or item.get("priority") \
                not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
            item = {}

        return item

    def move_items_from_stream_to_priority_queue(self, num_items=None):
        """Pop the given number of work items from the incoming stream and
            push it to the priority queue.

        Args:
            num_items (int): Number of work items to process from the
                the incoming stream, where None indicates to process all
                the work items in the incoming stream.
        """
        if num_items is not None and num_items < 1:
            return

        if num_items is None:
            num_items = len(self.incoming_stream)

        while len(self.incoming_stream) != 0 and num_items > 0:
            self.push_priority_queue(self.pop_stream())
            num_items -= 1

    def process_priority_queue(self, num_items=None):
        """Process the given number of work items in priority queue
            starting with the work item with the highest priority level.

        Args:
            num_items (int): Number of work items to process in the
                the priority queue, where None indicates to process all
                the work items in the priority queue.
        """
        if num_items is not None and num_items < 1:
            return

        if num_items is None:
            num_items = len(self.priority_queue)

        next_item = self.pop_priority_queue()
        while next_item and num_items > 0:
            self.execute_work_item(next_item)
            next_item = self.pop_priority_queue()
            num_items -= 1

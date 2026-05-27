class EventBus:
    def __init__(self):
        """
        Central event system
        """
        self.listeners = {}

    # ----------------------------
    # SUBSCRIBE
    # ----------------------------
    def subscribe(self, event_type, listener):
        """
        listener: function or method
        """
        if event_type not in self.listeners:
            self.listeners[event_type] = []

        self.listeners[event_type].append(listener)

    # ----------------------------
    # UNSUBSCRIBE
    # ----------------------------
    def unsubscribe(self, event_type, listener):
        if event_type in self.listeners:
            if listener in self.listeners[event_type]:
                self.listeners[event_type].remove(listener)

    # ----------------------------
    # EMIT
    # ----------------------------
    def emit(self, event_type, data=None):
        """
        Notify all listeners
        """
        if event_type not in self.listeners:
            return

        for listener in self.listeners[event_type]:
            listener(data)

class Window:
    """Candidate window."""

    def __init__(self, size, base_size, offset=0, cursor=1, wrap=False):
        """Constructor.

        Args:
            size (int): Window size.
            base_size (int): Base size (candidate size).
            offset (int): Window offset.
            cursor (int): Cursor position in the window.
            wrap (bool): Wrap or not.
        """
        self._size = size
        self._base_size = base_size
        self._offset = offset
        self._cursor = cursor
        self.wrap = wrap

    @property
    def size(self):
        """int: A window size."""
        return self._size

    @property
    def base_size(self):
        """int: A base size."""
        return self._base_size

    @property
    def offset(self):
        """int: A window offset."""
        return self._offset

    @property
    def cursor(self):
        """int: A cursor in the window."""
        return self._cursor

    @property
    def index(self):
        """int: A selected index.

        Example:
            >>> window = Window(10, 100)
            >>> window.index = 0
            >>> window.index
            0
        """
        return self._offset + self._cursor

    @index.setter
    def index(self, value):
        # Make sure that the value is in [0:base_size-1]
        value = value % self._size if self.wrap else value
        if value < 0:
            value = 0
        elif value > self.base_size:
            value = self.base_size - 1
        # Check if the value is in window or else
        ws = self.offset
        we = self.offset + self.size
        if ws <= value <= we:
            self._cursor = value - self.offset
        elif value < ws:
            self._cursor = 0
            self._offset = value
        elif value > we:
            self._cursor = self.size - 1
            self._offset = value - self.size

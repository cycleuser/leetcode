
"""
The read4 API is already defined for you.

    @param buf, a list of characters
    @return an integer
    def read4(buf):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""

class Solution:
    def __init__(self):
        """
        Initialize an empty queue to store characters.
        """
        self.queue = []

    def read(self, buf, n):
        """
        Read up to n characters from the file and store them into buffer buf.

        :param buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :return: The number of actual characters read (int)
        """
        idx = 0
        while True:
            # Create a temporary buffer with size 4 for read4 API
            buf4 = [""] * 4
            # Read up to 4 characters from the file into buf4
            num_chars_read = read4(buf4)

            # Add these characters to our queue
            self.queue += buf4

            # Calculate the number of characters we can add to buf
            curr = min(num_chars_read, n - idx)
            for i in range(curr):
                # Pop characters from the front of the queue and store them in buf
                buf[idx] = self.queue.pop(0)
                idx += 1

            # If no more characters were added, break out of the loop
            if curr == 0:
                break

        return idx


class File:
    """
    File class represents a file in the file system.
    
    Attributes:
        name (str): The name of the file.
        files (dict): A dictionary to store sub-files under this file.
        content (str): Content of the file.
    """

    def __init__(self, name: str):
        """
        Initialize a File object.

        Args:
            name (str): The name of the file.
        """
        self.name = name
        self.files = {}
        self.content = ''


class FileSystem:
    """
    Represents a file system with operations to manipulate files and directories.
    """

    def __init__(self):
        """
        Initialize a FileSystem object, starting from root directory '/'.
        """
        self.root = File('/')

    def move(self, path: str) -> File:
        """
        Navigate through the paths and return the current file.

        Args:
            path (str): The path to navigate.

        Returns:
            File: The current file at the given path.
        """
        cur = self.root
        if path[1:]:
            for dr in path[1:].split('/'):
                if dr not in cur.files:
                    cur.files[dr] = File(dr)
                cur = cur.files[dr]
        return cur

    def ls(self, path: str) -> List[str]:
        """
        List the names of files and directories under the given path.

        Args:
            path (str): The path to list contents from.

        Returns:
            List[str]: A list containing file/directory names.
        """
        cur = self.move(path)
        return [cur.name] if cur.content else sorted(cur.files.keys())

    def mkdir(self, path: str) -> None:
        """
        Create a directory at the given path.

        Args:
            path (str): The path to create the directory.
        """
        self.move(path)

    def addContentToFile(self, filePath: str, content: str) -> None:
        """
        Add content to a file located at the given path.

        Args:
            filePath (str): The path to the file.
            content (str): Content to be added to the file.
        """
        cur = self.move(filePath)
        cur.content += content

    def readContentFromFile(self, filePath: str) -> str:
        """
        Read and return the content of a file located at the given path.

        Args:
            filePath (str): The path to the file.

        Returns:
            str: The content of the file.
        """
        return self.move(filePath).content

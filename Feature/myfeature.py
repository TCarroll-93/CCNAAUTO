"""
Basic feature module for CCNAAUTO.
"""


class MyFeature:
    """A basic feature class."""

    def __init__(self, name: str):
        """Initialize the feature with a name."""
        self.name = name

    def execute(self) -> str:
        """Execute the feature and return a result."""
        return f"Feature '{self.name}' executed successfully."

    def __str__(self) -> str:
        """Return string representation of the feature."""
        return f"MyFeature(name={self.name})"


def main():
    """Main entry point for the feature."""
    feature = MyFeature("MyFeature")
    print(feature.execute())


if __name__ == "__main__":
    main()


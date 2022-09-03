# Deleted from Song:

# help(Song.__init__)
print(Song.__doc__)
print(Song.__init__.__doc__)
# Methods can have atributes because they are
Song.__init__.__doc__ =         """
        Song init method. (This is little to much, __init__ isn´t standard)
        Args:
            title (str): Initialises the `title` attribute.
            artist (Artist): A Artist object representing the song creator.
            duration (Optional[int]): Initial value for the `duration` attribute.
                Will default to zero if not specified.
        """
help(Song)
class WikipediaPageError(Exception):
    def __init__(self, message="There was an error fetching the page from Wikipedia"):
        self.message = message
        super().__init__(self.message)

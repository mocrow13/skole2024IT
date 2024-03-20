class Bucket_List():
    def __init__(self, name) -> None:
        self.name = name
        self.favoritter = []

    def legg_til(self, tittel):
        self.favoritter.append(tittel)

    def vis(self):
        for i in self.favoritter:
            print(i)


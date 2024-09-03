from abc import ABC, abstractmethod


class DocumentService(ABC):
    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def createDocument(self, documentData):
        pass

    @abstractmethod
    def readDocument(self, documentId):
        pass

class Node:
    def __init__(self, data:str):
        self.data = data;
        self.prev = None;
        self.next = None;

class BrowserHistory:
    currentPage = None;

    def __init__(self, homepage: str):
        self.currentPage = Node(homepage);

    def visit(self, url: str) -> None:
        newNode = Node(url);
        self.currentPage.next = newNode;
        newNode.prev = self.currentPage;
        self.currentPage = self.currentPage.next;
        

    def back(self, steps: int) -> str:
        while steps > 0 and self.currentPage.prev != None:
            self.currentPage =self.currentPage.prev;
            steps -= 1;
        return self.currentPage.data;
        

    def forward(self, steps: int) -> str:
        while steps > 0 and self.currentPage.next != None:
            self.currentPage =self.currentPage.next;
            steps -= 1;
        return self.currentPage.data;

        
# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
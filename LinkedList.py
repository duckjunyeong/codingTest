class ListNode(object):
    def __init__(self, page, next=None, back=None):
        self.page = page
        self.next = next
        self.back = back


class HomePageHistory(object):
    def __init__(self, page):
        new_page = ListNode(page)
        self.current = self.head = new_page

    def visit(self, page):
        new_page = ListNode(page, back=self.current)
        self.current.next = new_page
        self.current = new_page
        return None

    def back(self, step):
        while step > 0 and self.current.back != None:
            step -= 1
            self.current = self.current.back
        return self.current.page

    def forward(self, step):
        while step > 0 and self.current.next != None:
            step -= 1
            self.current = self.current.next
        return self.current.page

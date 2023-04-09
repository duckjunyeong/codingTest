class ListNode(object):
    def __init__(self, page):
        self.page = page


class HomePageHistory(object):
    def __init__(self, page):
        self.current_index = 0
        self.homepage_list = []
        new_page = ListNode(page)
        self.homepage_list.append(new_page)

    def visit(self, page):
        self.current_index += 1
        new_page = ListNode(page)
        self.homepage_list.append(new_page)
        return None

    def back(self, step):
        find_index = self.current_index - step
        if find_index < 0:
            find_index = 0
        self.current_index = find_index
        return print(self.homepage_list[find_index].page)

    def forward(self, step):
        find_index = self.current_index + step
        if find_index > len(self.homepage_list):
            find_index = len(self.homepage_list)
        self.current_index = find_index
        return print(self.homepage_list[find_index].page)

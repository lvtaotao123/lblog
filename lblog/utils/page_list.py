from django.utils.safestring import mark_safe

class Page:
    def __init__(self,data_count,for_page_count,count,current,path='/index'):
        self.data_count = data_count
        self.for_page_count = for_page_count
        self.count = count
        self.current = int(current)
        self.path = path

    @property
    def max_page(self):
        y, v = divmod(self.data_count, self.for_page_count)
        if v:
            y += 1
        return y

    @property
    def start(self):
        starts = self.current - int((self.count - 1)/2)
        if starts < 1:
            starts = 1
        return starts

    @property
    def end(self):
        ends = self.current + int((self.count - 1)/2)
        if ends >self.max_page:
            ends = self.max_page
        return ends

    def page_list(self):
        data_list = []
        if self.current == 1:
            pre = '<li class="page-item disabled"><a class="page-link" href="#" tabindex="-1">Previous</a></li>'
            data_list.append(pre)
        else:
            pre = '<li class="page-item"><a class="page-link" href="{}/?p={}" tabindex="-1">Previous</a></li>'.format(self.path, self.current - 1)
            data_list.append(pre)
        if self.max_page < self.count:
            for i in range(1,self.max_page+1):
                if i == self.current:
                    page = '<li class="page-item active"><a class="page-link" href="{}/?p={}">{} <span class="sr-only">(current)</span></a></li>'.format(self.path, i, i)
                    data_list.append(page)
                else:
                    page = '<li class="page-item"><a class="page-link" href="{}/?p={}">{}</a></li>'.format(self.path,i,i)
                    data_list.append(page)
        else:
            for i in range(self.start, self.end +1):
                if i == self.current:
                    page = '<li class="page-item active"><a class="page-link" href="{}/?p={}">{} <span class="sr-only">(current)</span></a></li>'.format(self.path, i, i)
                    data_list.append(page)
                else:
                    page = '<li class="page-item"><a class="page-link" href="{}/?p={}">{}</a></li>'.format(self.path,i,i)
                    data_list.append(page)
        if self.current == self.max_page:
            next_page = '<li class="page-item disabled"><a class="page-link" href="#" tabindex="-1">Next</a></li>'
        else:
            next_page = '<li class="page-item"><a class="page-link" href="{}/?p={}" tabindex="-1">Next</a></li>'.format(self.path, self.current + 1)
        data_list.append(next_page)
        pagestr = mark_safe("".join(data_list))
        return pagestr
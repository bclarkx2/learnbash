

###############################################################################
# Classes                                                                     #
###############################################################################

class Starter(object):

    def __init__(self, lis):
        self.lis = lis

    def names(self):
        return [c.name for c in self.lis]

    def by_name(self, name):
        for x in self.lis:
            if x.name == name:
                return x
        return None

    def start(self, name, op="start"):
        cls = self.by_name(name)
        if cls:
            obj = cls()
            start = getattr(obj, op)
            start()
            return True
        else:
            return False

# Interface Segregation Principle
class Machine:
    def Print(self, document):
        raise NotImplementedError

    def Scan(self, document):
        raise NotImplementedError

    def Fax(self, document):
        raise NotImplementedError

class MultiFunctionPrinte(Machine):
    def Print(self, document):
        pass

    def Scan(self, document):
        pass

    def Fax(self, document):
        pass

class OldFashionecPrinter(Machine):
    def Print(self, document):
        pass

    def Scan(self, document):
        pass #nooperation
    # this is problemetic because somebody implementing OldFashioned printer is
    # still seeing Scan and Fax methods but they can forget and try to use it
    # doing nothing is onething that can be done and the other thin can be starting
    # complaining such that:

    def Fax(self, document):
        raise  NotImplementedError
    # this may not a problem for small scripts but may be a big problem for bigger projects
    # and apis. You're crashing your application.

# The idea of Interface Segragation Principle is that instead of having this one large
# interface with several members in it, what you want to do is you want to keep things
# granular.
# bir örnek oluşturabilirsin yetenekler class'ı ve oldman'de günümüzde olan ama
# onun zamanında olmayan yetenekler olabilir ya da kişilerin bazıları için geçersiz
# yetenekler. O yüzden işin doğrusu her yetenek için ayrı interface oluşturmak.




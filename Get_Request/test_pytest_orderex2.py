import pytest

class Test2:
    @pytest.mark.order(2)
    def testb(self):
        pass
    @pytest.mark.order(1)
    def testc(self):
        pass
    @pytest.mark.order(4)
    def testd(self):
        pass
    @pytest.mark.order(3)
    def testa(self):
        pass




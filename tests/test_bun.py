from praktikum.bun import Bun

class TestBun1:

    def test_get_correct_name(self):
        bun = Bun('Флюоресцентная булка R2-D3', 988)
        assert bun.get_name() == 'Флюоресцентная булка R2-D3'

    def test_get_correct_price(self):
        bun = Bun('Флюоресцентная булка R2-D3', 988)
        assert bun.get_price() == 988

class TestBun2:

    def test_get_correct_name(self):
        bun = Bun('Краторная булка N-200i', 1255)
        assert bun.get_name() == 'Краторная булка N-200i'

    def test_get_correct_price(self):
        bun = Bun('Краторная булка N-200i', 1255)
        assert bun.get_price() == 1255
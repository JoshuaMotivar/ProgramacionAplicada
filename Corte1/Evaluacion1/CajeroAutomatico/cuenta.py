class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial

    def ver_saldo(self):
        print(f"\n💰 Saldo actual: COP ${self.saldo:,.0f}".replace(",", "."))

    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f"\n✅ Has depositado COP ${monto:,.0f}. Nuevo saldo: COP ${self.saldo:,.0f}".replace(",", "."))
        else:
            print("\n⚠️ El monto a depositar debe ser mayor a cero.")

    def retirar(self, monto):
        if monto <= 0:
            print("\n⚠️ El monto debe ser mayor a cero.")
        elif monto > self.saldo:
            print("\n❌ Fondos insuficientes.")
        else:
            self.saldo -= monto
            print(f"\n💸 Has retirado COP ${monto:,.0f}. Nuevo saldo: COP ${self.saldo:,.0f}".replace(",", "."))
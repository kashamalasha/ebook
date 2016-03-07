# Создайте два новых класса вентилей: NorGate и NandGate.
# Первый работает подобно OrGate, к выходу которого подключено НЕ. Второй - как AndGate с НЕ на выходе.
# Создайте ряд из вентилей, который доказывал бы, что NOT (( A and B) or (C and D)) это то же самое,
# что и NOT( A and B ) and NOT (C and D). Убедитесь, что используете в этой симуляции некоторые из вновь
# созданных вами вентилей.


class LogicGate:

    def __init__(self, n):
        self.name = n
        self.output = None

    def __str__(self):
        return self.name

    def getName(self):
        return self.name

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output


class BinaryGate(LogicGate):

    def __init__(self,n):
        LogicGate.__init__(self,n)

        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA is None:
            return int(input("Enter Pin A input for gate "+self.getName()+"--> "))
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB is None:
            return int(input("Enter Pin B input for gate "+self.getName()+"--> "))
        else:
            return self.pinB.getFrom().getOutput()

    def setNextPin(self,source):
        if self.pinA is None:
            self.pinA = source
        else:
            if self.pinB is None:
                self.pinB = source
            else:
                print("Cannot Connect: NO EMPTY PINS on this gate")


class AndGate(BinaryGate):

    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a == 1 and b == 1:
            return 1
        else:
            return 0


class OrGate(BinaryGate):

    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a == 1 or b == 1:
            return 1
        else:
            return 0


class UnaryGate(LogicGate):

    def __init__(self,n):
        LogicGate.__init__(self,n)

        self.pin = None

    def getPin(self):
        if self.pin is None:
            return int(input("Enter Pin input for gate "+self.getName()+"--> "))
        else:
            return self.pin.getFrom().getOutput()

    def setNextPin(self,source):
        if self.pin is None:
            self.pin = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")


class NotGate(UnaryGate):

    def __init__(self,n):
        UnaryGate.__init__(self,n)

    def performGateLogic(self):
        if self.getPin():
            return 0
        else:
            return 1


class NorGate(BinaryGate):

    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()

        if a != 1 or b != 1:
            return 1
        else:
            return 0


class NandGate(BinaryGate):

    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()

        if a != 1 or b != 1:
            return 1
        else:
            return 0


class Connector:

    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate


def main():

    g1 = AndGate("G1")
    g2 = AndGate("G2")
    g3 = OrGate("G3")
    g4 = NotGate("G4")
    c1 = Connector(g1, g3)
    c2 = Connector(g2, g3)
    c3 = Connector(g3, g4)

    g5 = NandGate("G5")
    c4 = Connector(g1, g5)
    c5 = Connector(g2, g5)

    print(g4.getOutput() == g5.getOutput())

main()


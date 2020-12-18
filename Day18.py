INPUT = open("Day18.txt", "r")

class Calculator():
    def calculate(self, text, order):
        temp = self.parse(text)
        if temp is not []:
            return self._calculate(self.infixToPostfix(temp, order))
        return None

    def infixToPostfix(self, input, level):  # default {"*": 3, "+": 2, "(": 1}
        stack = []
        postfixList = []
        for i in input:
            if i == '(':
                stack.append(i)
            elif i == ')':
                top = stack.pop()
                while top != '(':
                    postfixList.append(top)
                    top = stack.pop()
            elif i not in level and (len(i) > 1 or i[0].isdigit()):
                postfixList.append(i)
            else:
                while len(stack) > 0 and (level.get(stack[-1], 1) >= level.get(i, 1)):
                    postfixList.append(stack.pop())
                stack.append(i)
        while len(stack) > 0:
            postfixList.append(stack.pop())
        return postfixList

    def _calculate(self, postfix):
        stack = []
        for i in postfix:
            try:
                stack.append(int(i))
            except:
                c = 0
                b = stack.pop()
                a = stack.pop()
                if i == '+':
                    c = a + b
                elif i == '*':
                    c = a * b
                stack.append(c)
        return stack[-1]

    def parse(self, text):
        buffer = ""
        out_list = []
        for i in text:
            if i == " ":
                out_list.append(buffer)
                buffer = ""
            elif buffer == "":
                buffer += i;
            elif i in "1234567890":
                if buffer[0].isalnum():
                    buffer += i
                else:
                    out_list.append(buffer)
                    buffer = i
            else:
                out_list.append(buffer)
                buffer = i
        out_list.append(buffer)
        return out_list

equations = INPUT.read().split("\n")
c = Calculator()
equal = {"*": 2, "+": 2, "(": 1}
add_first = {"+": 3, "*": 2, "(": 1}
sums = 0
for i in equations:
    sums += c.calculate(i.strip(), equal)
print("part 1:", sums)

sums = 0
for i in equations:
    sums += c.calculate(i.strip(), add_first)
print("part 2:", sums)
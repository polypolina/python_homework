from flask import Flask, request, jsonify

calc = Flask(__name__)
client = calc.test_client()

# поддерживаемые операции: add (+), sub(-), div(/), mul(*), mod, pow, intdiv

@calc.route('/', methods=['GET'])
def calculation():
    x = request.args.get('x', 'default')
    y = request.args.get('y', 'default')
    mode = request.args.get('mode', 'default')
    if x == 'default' or y == 'default' or mode == 'default':
        return 'Wrong parameters, use x,y: float or int number, mode: add (+), sub(-), div(/), mul(*), mod, pow, intdiv'
    else:
        x = float(x)
        y = float(y)
        if mode == "add":
            res = x + y
            return 'result: ' + str(res)

        elif mode == "sub":
            res = x - y
            return 'result: ' + str(res)

        elif mode == "div":
            if y == 0:
                return 'Division by zero!'
            else:
                res = x / y
                return 'result: ' + str(res)

        elif mode == "mul":
            res = x * y
            return 'result: ' + str(res)

        elif mode == "mod":
            if y == 0:
                return 'Division by zero!'
            else:
                res = int(x % y)
                return 'result: ' + str(res)

        elif mode == "pow":
            res = x ** y
            return 'result: ' + str(res)

        elif mode == "intdiv":
            if y == 0:
                return 'Division by zero!'
            else:
                res = int(x // y)
                return 'result: ' + str(res)


if __name__ == '__main__':
    calc.run()

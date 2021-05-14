class Polynomial:
    def __init__(self, params):
        if isinstance(params, int):
            self.coeffs = [params]
        elif isinstance(params, (list, tuple)):
            if len(params) != 0:
                for coeff in params:
                    if not isinstance(coeff, int):
                        raise Exception('Incorrect polynomial coeffs')
                self.coeffs = list(params)
            else:
                raise Exception('Incorrect polynomial coeffs')
        elif isinstance(params, Polynomial):
            self.coeffs = params.coeffs.copy()
        else:
            raise Exception('Incorrect polynomial coeffs')


    def __add__(self, item):
        if isinstance(item, int):
            coeffs = self.coeffs.copy()
            coeffs[-1] += item
            return Polynomial(coeffs)
        elif isinstance(item, Polynomial):
            coeffs_count = max(len(self.coeffs), len(item.coeffs))
            coeffs = [0] * coeffs_count
            for i in range(len(self.coeffs)):
                coeffs[i + (coeffs_count - len(self.coeffs))] += self.coeffs[i]
            for i in range(len(item.coeffs)):
                coeffs[i + (coeffs_count - len(item.coeffs))] += item.coeffs[i]
            while coeffs[0] == 0 and len(coeffs) > 1:
                del coeffs[0]

            return Polynomial(coeffs)
        else:
            raise Exception('Incorrect arguments')


    def __radd__(self, item):
        if isinstance(item, int):
            return self.__add__(item)
        else:
            raise Exception('Incorrect arguments')


    def __sub__(self, item):
        if isinstance(item, int):
            coeffs = self.coeffs.copy()
            coeffs[-1] -= item
            return Polynomial(coeffs)
        elif isinstance(item, Polynomial):
            coeffs_count = max(len(self.coeffs), len(item.coeffs))
            coeffs = [0] * coeffs_count
            for i in range(len(self.coeffs)):
                coeffs[i + (coeffs_count - len(self.coeffs))] += self.coeffs[i]
            for i in range(len(item.coeffs)):
                coeffs[i + (coeffs_count - len(item.coeffs))] -= item.coeffs[i]
            while coeffs[0] == 0 and len(coeffs) > 1:
                del coeffs[0]

            return Polynomial(coeffs)
        else:
            raise Exception('Incorrect arguments')


    def __rsub__(self, item):
        if isinstance(item, int):
            return Polynomial(item) - self
        else:
            raise Exception('Incorrect arguments')


    def __mul__(self, item):
        if isinstance(item, int):
            if item == 0:
                return Polynomial([0])
            coeffs = self.coeffs.copy()
            for i in range(len(coeffs)):
                coeffs[i] *= item
            return Polynomial(coeffs)
        elif isinstance(item, Polynomial):
            p = Polynomial(0)
            for i in range(len(item.coeffs)):
                coeffs = self.coeffs + [0] * (len(item.coeffs) - (i + 1))
                p = p + (item.coeffs[i] * Polynomial(coeffs))
            return p
        else:
            raise Exception('Incorrect arguments')


    def __rmul__(self, item):
        if isinstance(item, int):
            return self.__mul__(item)
        else:
            raise Exception('Incorrect arguments')


    def __eq__(self, item):
        if isinstance(item, int):
            return len(self.coeffs) == 1 and self.coeffs[0] == item
        elif isinstance(item, Polynomial):
            return self.coeffs == item.coeffs
        else:
            raise Exception('Incorrect arguments')


    def __str__(self):
        result = ''
        for i in range(len(self.coeffs)):
            if self.coeffs[i] < 0:
                result = result + '-'
            elif self.coeffs[i] > 0 and i > 0:
                result = result + '+'
            elif self.coeffs[i] == 0:
                continue

            power = len(self.coeffs) - (i + 1)

            if abs(self.coeffs[i]) == 1 and power != 0:
                pass
            else:
                result = result + str(abs(self.coeffs[i]))                   

            if power > 1:
                result = result + 'x^' + str(power)
            elif power == 1:
                result = result + 'x'

        return result


    def __repr__(self) -> str:
        return 'Polynomial({})'.format(self.coeffs)


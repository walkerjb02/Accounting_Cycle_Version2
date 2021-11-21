
class Operations:
    def shr(self, inp, shift_length):
        new_input = list(inp)
        i = -1
        new_input.pop()
        while i > -1 * shift_length:
            new_input.pop(i)
            i -= 1
        j = 0
        new_input.reverse()
        while j < shift_length:
            new_input.append('0')
            j += 1
        new_input.reverse()
        return(new_input)

    def rotr(self, inp, rotation_length):
        ninp = list(inp)
        ninp.extend(ninp)
        self.output = []
        i = 0
        while i < int((len(ninp) / 2)):
            self.output.append(ninp[i + rotation_length])
            i += 1
        return(self.output)

    def xor(self, x, y, z):
        nx = list(x)
        ny = list(y)
        nz = list(z)
        self.xorr = []
        i = 0
        while i < (len(nx)):
            if nx[i] in ny[i]:
                if nx[i] in nz[i]:
                    self.xorr.append('0')
            elif nx[i] in ny[i] and '1' in nz[i]:
                self.xorr.append('1')
            elif nx[i] not in ny[i] and '0' in nz[i]:
                self.xorr.append('1')
            elif nx[i] not in ny[i] and '1' in nz[i]:
                self.xorr.append('0')
            i += 1
        return(''.join(self.xorr))

    def add(self, x, y):
        binx = list(x)
        biny = list(y)
        xybin = []
        overflow = ['0']
        finalbin = []
        i = 31
        binx.extend(biny)
        while i >= 0:
            if binx[i] in biny[i] and '0' in binx[i]:
                if len(overflow) > 1:
                    xybin.append(overflow[-1])
                    overflow.pop(-1)
                else:
                    xybin.append(binx[i])
            elif binx[i] in biny[i] and '1' in binx[i]:
                if len(overflow) > 1:
                    xybin.append(overflow[-1])
                    overflow.pop(-1)
                else:
                    xybin.append('0')
                    overflow.append(binx[i])
            elif binx[i] not in biny[i]:
                if len(overflow) > 1:
                    xybin.append('0')
                else:
                    if '1' in binx[i]:
                        xybin.append(binx[i])
                    elif '1' in biny[i]:
                        xybin.append(biny[i])
            i -= 1
        for j in xybin[::-1]:
            finalbin.append(j)
        return(''.join(finalbin))


o = Operations()


class Functions:
    def lowersigma(self, x):
        return(o.xor(o.rotr(x, 7), o.rotr(x, 18), o.shr(x, 3)))

    def lowersigmaone(self, x):
        return(o.xor(o.rotr(x, 17), o.rotr(x, 19), o.shr(x, 10)))

    def uppersigma(self, x):
        return(o.xor(o.rotr(x, 2), o.rotr(x, 13), o.rotr(x, 22)))

    def uppersigmaone(self, x):
        return(o.xor(o.rotr(x, 6), o.rotr(x, 11), o.rotr(x, 25)))

    def choice(self, x, y, z):
        binx = list(x)
        biny = list(y)
        binz = list(z)
        choice_final = []
        i = 0
        while i < 32:
            if '1' in binx[i]:
                choice_final.append(biny[i])
            if '0' in binx[i]:
                choice_final.append(binz[i])
            i += 1
        return(''.join(choice_final))

    def majority(self, x, y, z):
        mx = list(x)
        my = list(y)
        mz = list(z)
        self.maj = []
        i = 0
        while i < len(mx):
            if mx[i] in my[i]:
                self.maj.append(mx[i])
            elif mx[i] or my[i] in mz[i]:
                self.maj.append(mz[i])
            i += 1
        return(''.join(self.maj))


F = Functions()


class Assembly:
    def binary_converter(self, text):
        converted_message = []
        binary = {'a': '01100001', 'b': '01100010', 'c': '01100011', 'd': '01100100', 'e': '01100101', 'f': '01100110',
                  'g': '01100111', 'h': '01101000', 'i': '01101001', 'j': '01101010', 'k': '01101011', 'l': '01101100',
                  'm': '01101101', 'n': '01101110', 'o': '01101111', 'p': '01110000', 'q': '01110001', 'r': '01110010',
                  's': '01110011', 't': '01110100', 'u': '01110101', 'v': '01110110', 'w': '01110111', 'x': '01111000',
                  'y': '01111001', 'z': '01111010', '/': '00101111', '.': '00101110', '-': '00101101', '$': '00100100',
                  '(': '00101000', ')': '00101001', '0': '00110000', '1': '00110001', '2': '00110010', '3': '00110011',
                  '4': '00110100', '5': '00110101', '6': '00110110', '7': '00110111', '8': '00111000', '9': '00111001',
                  '=': '00111101', '{': '01111011', '}': '01111101', ':': '00111010', ',': '00101100', ' ': '00100000'}
        for i in text:
            for j in binary:
                if i in j:
                    converted_message.append(binary[i])
        converted_message = ''.join(converted_message)
        return(list(converted_message))

    def message(self, body):
        body = A.binary_converter(body)
        compiler = []
        ilist = []
        i = 0
        while i < (len(body)):
            if i % 488 == 0:
                compiler.append(ilist)
                ilist.clear()
            ilist.append(body[i])
            i += 1
        return(compiler)

    def padding(self, body):
        message = A.message(body)
        message_lengths = []
        i = 0
        for m in message:
            message_lengths.append(str(len(m)))
            size = ((512 - int(len(A.binary_converter(message_lengths[-1])))) - len(m))
            while i < size:
                m.append('0')
                i += 1
            m.extend(A.binary_converter(message_lengths[-1]))
            ''.join(m)
        return(message)


A = Assembly()


class Main:
    def constant(self):
        constants = []
        self.final_constants = []
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 32, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 132, 137, 139, 149,
                  151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 321]
        for i in primes:
            constants.append(A.binary_converter((str(int((pow(i, (1 / 2)) % 1) * pow(2, 32))))))
        h = 0
        j = 0
        prep = []
        while j < 64:
            while h < 32:
                prep.append(constants[j][h])
                h += 1
            j += 1
            self.final_constants.append(prep)
        return(self.final_constants)

    def message_schedule(self, message):
        message = A.padding(message)
        prep = []
        schedule = []
        s = 0
        while s < len(message):
            prep.clear()
            i = 0
            j = 32
            while i < 512:
                prep.append(''.join(message[s][i:j]))
                i += 32
                j += 32
            t = 16
            while t < 64:
                prep.append(o.add(o.add(F.lowersigmaone(prep[t - 2]), prep[t - 7]), o.add(F.lowersigma(prep[t - 15]), prep[t - 16])))
                t += 1
            schedule.append(prep)
            s += 1
        return((schedule))

    def initial_hash_value(self):
        a, b, c, d, e, f, g, h = [], [], [], [], [], [], [], []
        ihv = [a, b, c, d, e, f, g, h]
        i = 0
        while i < 8:
            ihv[i].append(me.constant()[i])
            i += 1
        return((ihv))

    def temporary_word_one(self, message, m, num):
        return((o.add(
            o.add(
            o.add(F.uppersigmaone(me.initial_hash_value()[4][-1]), F.choice(me.initial_hash_value()[4][-1], me.initial_hash_value()[5][-1], me.initial_hash_value()[6][-1])), me.initial_hash_value()[7][-1]),
            o.add(me.constant()[num], me.message_schedule(message)[m][num]))))

    def temporary_word_two(self):
        return((o.add(F.uppersigma(me.initial_hash_value()[0][0]), F.majority(me.initial_hash_value()[0][-1],
                                                                                 me.initial_hash_value()[1][-1],
                                                                                 me.initial_hash_value()[2][-1]))))

    def compression(self, message):
        z = 0
        a = [me.initial_hash_value()[0][0]]
        b = [me.initial_hash_value()[1][0]]
        c = [me.initial_hash_value()[2][0]]
        d = [me.initial_hash_value()[3][0]]
        e = [me.initial_hash_value()[4][0]]
        f = [me.initial_hash_value()[5][0]]
        g = [me.initial_hash_value()[6][0]]
        h = [me.initial_hash_value()[7][0]]
        ai, bi, ci, di, ei, fi, gi, hi = str(a.copy()), str(b.copy()), str(c.copy()), str(d.copy()), str(e.copy()), str(
            f.copy()), str(g.copy()), str(h.copy())
        final = []


        while z < len(me.message_schedule(message)):
            m = 0
            t1 = me.temporary_word_one(message, z, m)
            t2 = o.add(me.temporary_word_one(message, z, m), me.temporary_word_two())
            while m < 64:
                a = o.add(t1, t2)
                b = a
                c = b
                d = c
                e = o.add(d, t1)
                f = e
                g = f
                h = g
                m += 1
                if m == 64:
                    ai, bi, ci, di, ei, fi, gi, hi = o.add(ai, a), o.add(bi, b), o.add(ci, c), o.add(di, d), o.add(ei, e), o.add(fi, f), o.add(gi, g), o.add(hi, h)
            z += 1
            if z == len(me.message_schedule(message)):
                final.append(ai)
                final.append(bi)
                final.append(ci)
                final.append(di)
                final.append(ei)
                final.append(fi)
                final.append(gi)
                final.append(hi)
        return(''.join(final))

    def hash(self, message):
        compression_result = me.compression(message)
        decimal_representation = int(compression_result, 2)
        hexadecimal_string = hex(decimal_representation)
        return((hexadecimal_string))

me = Main()

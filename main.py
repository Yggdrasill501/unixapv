from os import system, chdir, mkdir, path, remove, rename, makedirs

file = 'nova_slozka'


class Homeworks:
    def __init__(self, file):
        self.file = file

    def homework_one(self):
        system('ssh zitnyfil@rodman.fjfi.cvut.cz')
        mkdir(self.file)
        chdir(self.file)

        if path.getsize(self.file) == 0:
            pass
        else:
            # clear()
            pass

        system('∼hudec/hw1/zadani.sh')
        system('./zadani.sh')
        remove('ukol1')
        system('cp -r ukol11src ukol12')
        makedirs('ukol13')
        makedirs('ukol14/ukol14.txt')

        with open('ukol14/ukol14.txt', 'w') as f:
            f.write('Ahoj Unixe')
        rename('ukol15src', 'ukol15')
        remove('ukol16')
        system('./odevzdani.sh')

    def run(self):
        self.homework_one()


if __name__ == '__main__':
    Homeworks(file).run()

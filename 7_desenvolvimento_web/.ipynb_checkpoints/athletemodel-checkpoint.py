import pickle
# from athletelist import AthleteList


class AthleteList(list):
    def __init__(self, a_name, a_dob=None, a_times=[]):
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)
        
    def sanitize(time_string):
        # a função "sanitize" é a mesma do módulo 5
        if '-' in time_string:
            splitter = '-'
        elif ':' in time_string:
            splitter = ':'
        else:
            return(time_string)
        (mins, secs) = time_string.split(splitter)
        return(mins + '.' + secs)
    
    def top3(self):
        return(sorted(set([sanitize(t) for t in self]))[0:3])
    
    def get_coach_data(filename):
        try:
            with open(filename) as f:
                data = f.readline()
            templ = data.strip().split(',')
            return AthleteList(templ.pop(0), templ.pop(0), templ)
        except IOError as ioerr:
            print('File error: '+ str(ioerr))
            return(None)


def get_coach_data(filename):
    try:
            with open(filename) as f:
                data = f.readline()
            templ = data.strip().split(',')
            return AthleteList(templ.pop(0), templ.pop(0), templ)
    except IOError as ioerr:
            print('File error: '+ str(ioerr))
            return(None)

def put_to_store(file_list):
    all_athletes = {}
    for each_file in file_list:
        """
        Pegue cada arquivo e transforme-o em uma instância
        do objeto AthleteList, e adicione os dados do
        atleta ao dicionário
        """
        ath = get_coach_data(each_file)
        """
        O nome de cada atleta é usado como a "chave"
        no dicionário. O "valor" é a instância do objeto AthleteList
        """
        all_athletes[ath.name] = ath
        
    try:
        with open('athletes.pickle', 'wb') as athf:
            """
            Salve o dicionário inteiro de AthleteList em uma conserva(pickle)
            """
            pickle.dump(all_athletes, athf)
    except IOError as ioerr:
        """
        E não se esqueça de usar try/except para proteger o código de E/S do arquivo
        """
        print('File error (put_to_store):' + str(ioerr))
    return(all_athletes)

def get_from_store():
    all_athletes = {}
    
    try:
        with open('athletes.pickle', 'rb') as athf:
            """
            Basta ler a conserva inteira no dicionário.
            O que poderia ser mais fácil?
            """
            all_athletes = pickle.load(athf)
    except IOError as ioerr:
        """
        De novo não se esqueça de usar o try/except
        """
        print('File error (get_from_store):' + str(ioerr))
    return(all_athletes)
        
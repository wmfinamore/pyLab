import pickle
from athletelist import AthleteList


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
        
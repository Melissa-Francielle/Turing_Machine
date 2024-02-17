import json
import csv
import time

class TuringMachine:
    def __init__(self, tape = "", blank_symbol = "", initial = "", final_state = None, transitions = None):
        self.tape = tape
        self.head_position = 0
        self.current_state = initial
        if transitions == None:
            self.transitions = {}
        else:
            self.transitions= transitions
        if final_state == None:
            self.final_state = set()
        else:
            self.final_state = set(final_state)

    def get_tape(self):
        return str(self.tape)
    
    def step(self):
        char_head = self.tape[self.head_position]
        x = (self.current_state, char_head)
        if x in self.transitions:
            y = self.transitions[x]
            self.tape[self.head_position] = y["write"]
            if y["move"] == "R":
                self.head_position += 1
            elif y["move"] == "L":
                self.head_position -= 1
            self.current_state = y["to"]

    def final(self):
        if self.current_state in self.final_state:
            return 1
        else:
            return 0
    
def machine_file(file_path):
    try:
        with open(file_path, 'r') as json_file:
            machine_data = json.load(json_file)
            transitions = {}
            for transition in machine_data['transitions']:
                key = (transition['from'], transition['read'])
                value = {'to': transition['to'], 'write': transition['write'], 'move': transition['move']}
                transitions[key] = value
            return transitions
    except FileNotFoundError:
        print(f"Arquivo {file_path} não encontrado.")
        return None
    except json.JSONDecodeError:
        print(f"Erro ao decodificar o arquivo JSON {file_path}. Verifique o formato.")
        return None
    
def cases(file_path):
    test_cases = []
    try:
        with open(file_path, 'r', newline='') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            next(csv_reader)  # Pula a linha de cabeçalho
            for row in csv_reader:
                input_str = row[0]
                expected_result = int(row[1])
                test_cases.append((input_str, expected_result))
        return test_cases
    except FileNotFoundError:
        print(f"Arquivo {file_path} não encontrado.")
        return []
    except csv.Error:
        print(f"Erro ao ler o arquivo CSV {file_path}. Verifique o formato.")
        return []

def main():
    file_maquina_path = 'arquivo.json'
    file_teste_path = 'entrada.csv'
    file_out_path = 'saida.csv'

    transitions = machine_file(file_maquina_path)
    machine = TuringMachine(machine_file(file_maquina_path))
    case_test = cases(file_teste_path)

    with open(file_out_path, 'w', newline='') as csv_file:
        writing = csv.writer(csv_file, delimiter=';')
        writing.writerow(["Palavra de entrada", "Resultado esperado", "Resultado obtido", "Tempo"])

        for str_in_input, expected_result in case_test:
            start_time = time.perf_counter()
            machine.head_position = 0  # Reinicia a posição da cabeça de leitura/gravação
            result = machine.final()
           # result = ''.join(machine.tape[1:-1])  # Resultado é a fita sem os caracteres brancos adicionais
            end_time = time.perf_counter()

            execution_time = "{:.7f}".format(end_time - start_time)  # Formatação com cinco casas decimais
            writing.writerow([str_in_input, expected_result, result, execution_time])
            csv_file.flush()

if __name__ == "__main__":
    main()

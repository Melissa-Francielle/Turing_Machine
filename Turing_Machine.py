import json
import csv
import time

class TuringMachine:
    def __init__(self, machine_data):
            self.transitions = machine_data["transitions"]
            self.current_state = machine_data["initial"]
            self.tape = []
            self.position = 0
            self.symbol = None
        
    def operation(self, input_str):
        self.current_states = set([0])  # Inicializa com o estado inicial
        for char in input_str:
            self.step(char)
        return 1 if any(state in self.transitions['final'] for state in self.current_states) else 0

    
    def move_machine(self):
        if self.position <(self.tape):
            self.symbol = self.tape[self.position]
        
        else:
            self.symbol = self.machine_data["white"]
        
        transition_found = False
        for trans in self.transitions:
            if trans["from"] == self.current_state and trans["read"] == self.symbol:
                self.current_state = trans["to"]
                self.tape[self.position] = trans["write"]
                self.position += 1 if trans["move"] == "R" else -1 
                transition_found = True
                break

        if not transition_found:
            print ("Não há transição aplicavel")

def machine_file(file_path):
    try:
        with open(file_path, 'r') as json_file:
            machine_data = json.load(json_file)
        return machine_data
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
    file_maq_path = 'arquivo.json'
    file_teste_path = 'entrada.csv'
    file_out_path = 'saida.csv'

    machine = TuringMachine(machine_file (file_maq_path))
    case_test = cases(file_teste_path)

    with open(file_out_path, 'w', newline='') as csv_file:
        writing = csv.writer(csv_file, delimiter=';')
        writing.writerow(["Palavra de entrada", "Resultado esperado", "Resultado obtido", "Tempo"])

    for str_in_input, expected_result in case_test:
        start_time = time.perf_counter()
        result = machine.operation(str_in_input)
        end_time = time.perf_counter()

        while machine.current_state not in machine_file.machine_data["final"]:
            machine.move()

        execution_time = "{:.5f}".format(end_time - start_time)  # Formatação com cinco casas decimais
        writing.writerow([str_in_input, expected_result, result, execution_time])
        csv_file.flush()

if __name__ == "__main__":
    main()

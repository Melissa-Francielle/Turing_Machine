import json 
import time 

def is_comment(line):
    if line[0] == "#":
        return True
    return False

class T_machine:
    def __init__ (self, machine_data):
        self.initial = machine_data["initial"]
        self.final_state = machine_data["final_state"]
        self.blank_symbol = machine_data["blank_symbol"]
        self.transitions = machine_data["transitions"]
    
    def get_action(self, state, symbol):
        for transition in self.transitions:
            if transition["from"] == state and transition["read"] == symbol:
                return (transition["to"], transition["write"], transition["move"])
        return None
    
    def simulate(self, tape):
        current_state = self.initial[0]
        current_index = 0
        tape_list = list(tape)

        while current_state not in self.final_state:
            current_symbol = tape_list[current_index]
        #while current_state not in self.final_state or self.blank_symbol in tape_list:
         #   current_symbol = tape_list[current_index]

            action = self.get_action(current_state, current_symbol)
            if action is None:
                break

            next_state, write_symbol, move_direction = action

            tape_list[current_index] = write_symbol

            if move_direction == "R":
                current_index += 1
            elif move_direction == "L":
                current_index -= 1

            if current_index < 0:
                tape_list.insert(0, self.blank_symbol)
                current_index = 0
            if current_index >= len(tape_list):
                tape_list.append(self.blank_symbol)

            current_state = next_state

            print("Tape:", "".join(tape_list))
        if current_state in self.final_state:
            print("1")  # Indica aceitação
            return 1
        if current_state not in self.final_state:
            print("0")  # Indica rejeição
            return 0 

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

def main():
    file_aut_path = 'arquivo.json'

    machine_data = machine_file(file_aut_path)
    if machine_data is None:
        return

    machine = T_machine(machine_data)

    # Aqui você pode fornecer a entrada da fita que deseja testar
    try:
        with open("entrada.txt", "r") as file:
            input_tape = file.read().strip()  # Lê a fita do arquivo e remove espaços em branco
    except FileNotFoundError:
        print("Arquivo de entrada não encontrado.")
        return

    print("Simulação iniciada:")
    machine.simulate(input_tape)

if __name__ == "__main__":
    main()

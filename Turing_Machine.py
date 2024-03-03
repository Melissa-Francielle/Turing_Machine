import json #importa o arquivo json para que possa ser lido pela máquina

class T_machine:
    def __init__(self, machine_data): #Inicializa a maquina com suas configuracoes
        self.initial = machine_data["initial"] 
        self.final_state = machine_data["final_state"]
        self.blank_symbol = machine_data["blank_symbol"] 
        self.transitions = machine_data["transitions"]
    
    def get_action(self, state, symbol): 
        for transition in self.transitions:  #Funcao escrita com o intuito de ler os "estados" de ação da MT 
            if transition["from"] == state and transition["read"] == symbol:
                return (transition["to"], transition["write"], transition["move"]) #Assim que ele termina de "pegar" as ações da máquia 
            
        return None
    
    def simulate(self, tape): #Inicializa a simulação 
        current_state = self.initial[0] #incializa um estado inicial 
        current_index = 0 
        tape_list = list(tape) #os resultados vão ser armazenados em uma lista 

        while current_state not in self.final_state: #O simbolo branco é adicionado na lista caso não esteja dentro dos limites da fita
            current_symbol = tape_list[current_index]

            action = self.get_action(current_state, current_symbol) #chama a função que le as ações da máquina
            if action is None: #caso não haja ação/estado a simulação da maquina para 
                break 
            
            #Aqui segue o conceito da maquina de turing que é proximo estado, o que escrever, e a direção que deve tomar
            next_state, write_symbol, move_direction = action 

            tape_list[current_index] = write_symbol #E assim escreve o simbolo na lista

            if move_direction == "R": #Condições para tomada de direção dos estados sendo Right ou Left (direita ou esquerda)
                current_index += 1
            elif move_direction == "L":
                current_index -= 1

            if current_index < 0: #Condição responsavel por verificar onde o simbolo branco sera adicionado caso 
                tape_list.insert(0, self.blank_symbol) #escreve o simbolo se estiver fora do limite da fita à esquerda
                current_index = 0
            if current_index >= len(tape_list):
                tape_list.append(self.blank_symbol) #escreve o simbolo se estiver fora do limite da fita à direita

            current_state = next_state

        if current_state in self.final_state: #Por fim indicadores de aceitação e rejeicao e adiciona a lista o resultado da palavra
            print("1") # Indica aceitação
            return "".join(tape_list).strip() 
            
        else:
            print("0") # Indica rejeição
            return "".join(tape_list).strip()  

        
def machine_file(file_path): #Aqui será lido o arquivo json 
    try:
        with open(file_path, 'r') as json_file: #abre o arquivo para leitura 
            machine_data = json.load(json_file)
        return machine_data
    except FileNotFoundError: #Verificaçao de excessões para verificar erros durante a leitura do arquivo 
        print(f"Arquivo {file_path} não encontrado.")
        return None
    except json.JSONDecodeError:
        print(f"Erro ao decodificar o arquivo JSON {file_path}. Verifique o formato.")
        return None

def main(): #Função main 
    file_aut_path = 'arquivo.json' 

    machine_data = machine_file(file_aut_path) #chamada da função para leitura do json
    if machine_data is None:
        return #caso esteja sem ações/vazia retorna nada

    machine = T_machine(machine_data) #incializa a maquina

    # Aqui você pode fornecer o caminho para o arquivo contendo as entradas da fita
    input_file_path = "entrada.txt"

    try: #Leitura do arquivo txt de entrada com as palavras para serem testadas
        with open(input_file_path, "r") as file:
            input_tapes = file.readlines()  # Lê todas as linhas do arquivo
    except FileNotFoundError:
        print("Arquivo de entrada não encontrado.")
        return

    print("Simulação iniciada:") #Mensagem que irá ser printada no terminal para indicar o inicio da simulação
    with open("saida.txt", "w") as output_file: #abre um arquivo txt para escrita
        for tape in input_tapes:
            tape = tape.strip()  # Remove espaços em branco
            result_tape = machine.simulate(tape)
            output_file.write(f"{result_tape}\n")  # Escreve a fita resultante e o resultado no arquivo de saída
    print("Fim da simulação")

if __name__ == "__main__":
    main()

<html>
<body>
 <h1> Implementação de Máquina de Turing </h1>
 <img align="right" alt="imagem_ilustrativa" height="90" width="500" src="https://d18l82el6cdm1i.cloudfront.net/uploads/dfugTjn2WC-tm_palindrome.gif"/> 
 <p> O trabalho é referente a disciplina de Teoria da Computação do curso de Ciência da Computação pela Universidade do Norte do Paraná. </p>
 <p> O desenvolvimento deste trabalho foi implementado em linguagem Python. O trabalho busca simular uma Máquina de Turing originalmente desenvolvida por Alan Turing mais conhecido como pai da computação. </p>
 
<h2> Funcionamento da máquina: </h2>

<p> O simulador deve receber três arquivos: </p>
<ol>
   <li><strong> arquivo.json: </strong> Onde neste arquivo contém as configurações da máquina, ou seja, nele contém estado inicial, estados finais, simbolo branco e transições. </li>
 <li><strong> entrada.txt: </strong> Este arquivo.txt contém as palavras a serem testadas para simulação. </li>
 <li><strong>saida.txt: </strong> Este arquivo será visivel após a simulação ser realizada, nele estará os resultados das palavras do arquivo de entrada.</li>
</ol>
<h3>Formato da entrada.txt</h3>
<p> O arquivo aceita uma entrada simples como desejar, podendo ser várias palavras ou apenas uma para serem testadas. Um exemplo de entrada: </p>
<pre>
  aabb
  bbbbbbbbbbb
  abababa
  aaaabbbb
</pre>
<p> Onde no terminal estará visivel ao usuário os dados de aceitação e rejeição da máquina, quando a máquina devolve 1 significa que o resultado foi aceito, caso seja 0 significa a rejeição.E na saida.txt os resultados dos testes</p>
<h3>Formato de arquivo.json</h3>
<p> O formato do arquivo JSON pode variar dependendo do problema a ser testado pelo simulador, incluindo informações como seu estado inicial, final, simbolo, fita e transição. Um exemplo: </p>
<pre>
  {
            "initial": [0],
            "final_state": [4],
            "blank_symbol": "_",
            "tape": {},
            "transitions": [
                { "from": 0, "to": 1, "read": "a", "write": "A", "move": "R" },
                { "from": 1, "to": 1, "read": "a", "write": "a", "move": "R" },
                // ...
            ]
  }
</pre>
<p>Caso queira testar um arquivo JSON utilize o presente no trabalho como base ou até mesmo para testar. O arquivo em questão deste trabalho é um JSON que trata duplo balanceamento. </p>
<h2> Execução do simulador</h2>
<p>Para executar o simulador, pode ser utilizado o seguinte comando: </p>
<pre> python simulador.py arquivo.json entrada.txt saida.txt </pre>
<p> Importante verificar o python instalado na máquina, pois assim seja necessário alterar o comando "python" para "python3", também pode ser escrito "py" </p>
<ul>
 <li><code>simulador.py</code> é o simulador da máquina de turing, caso seja salvo com outro nome é necessário a modificação do nome quando for ser feita a execução, por exemplo: Maquina_turing.py</li>
 <li><code>arquivo.json</code> é o arquivo que contém as informações de configuração da MT</li>
 <li><code>entrada.txt</code>arquivo com as palavras de entradas para simulaçõa</li>
 <li><code>saida.txt</code> arquivo responsável pela saída dos resultados da simulação que são gravados no final dela</li>
</ul>
<p> É importante certificar de ajustar os nomes dos arquivos com a sua configuração</p>
<h2>Exemplos de configuração </h2>
<p>Os arquivos disponiveis: </p>
<ul>
 <li><a href="https://github.com/Melissa-Francielle/Turing_Machine/blob/main/Turing_Machine.py ">Simulador da Máquina de Turin</a></li>
 <li><a href="https://github.com/Melissa-Francielle/Turing_Machine/blob/main/arquivo.json "> Arquivo JSON (duplo balanceamento)</a></li>
 <li><a href="https://github.com/Melissa-Francielle/Turing_Machine/blob/main/entrada.txt ">Entrada txt</li>
</ul>
 <p> Agora está informado de como utilizar este simulador de Máquina de Turing e pronto para testar.</p>
 <p>Lembrando que os arquivos JSON e TXT apresentados nesse projeto estão testando o problema do duplo balanceamento, caso queira testar outros tipos de problemas utilizando o simulador é necessário alterações nas configurações do JSON e os tipos de entradas que gostaria de testar.</p>
</body>

</html>

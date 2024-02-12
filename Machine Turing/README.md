_Machine Turing_ 

# Máquina: 
* Fita
* Cabeça 
* Registro de estados
* Transições 

## Definição formal 
M = (Q, Sigma, R, s, b, F, delta)

* Q = Um conjunto finito de estados
* Sigma = conjunto finito de simbolos distintos 
* R = conjunto finito de simbolos da fita
* s (pertence a Q) = é o estado inicial
* b (pertence a R) = simbolo branco
* F (contido em Q) = são os simbolos finais 
* delta: Q x R -> Q x R x {E,D} é uma função parcial. E e D indicam o movimento da cabeça, sendo E esquerda e D direita. 


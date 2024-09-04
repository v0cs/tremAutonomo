# Projeto de Controle de Trem Autônomo

## Descrição

Este projeto implementa um sistema de controle para um trem autônomo que opera em um trilho numérico infinito. O sistema é projetado para interpretar e executar comandos de movimento ("ESQUERDA" e "DIREITA"), gerenciando a posição do trem e respeitando certas regras de operação.

## Funcionalidades

- **Controle de Movimento:** O trem se move com base em uma lista de comandos fornecidos. Os comandos são "ESQUERDA" para mover uma posição para a esquerda e "DIREITA" para mover uma posição para a direita.
- **Gestão de Estado:** O sistema rastreia a posição atual do trem e o número de movimentos consecutivos na mesma direção.
- **Validação de Comandos:** O código verifica se os comandos fornecidos são válidos e emite mensagens de erro para comandos desconhecidos ou formatos incorretos.
- **Restrições de Movimento:** O sistema assegura que o trem não ultrapasse uma distância máxima pré-definida e evita um número excessivo de movimentos na mesma direção para preservar o desgaste dos trilhos e componentes.

## Como Funciona

A classe `TremAutonomo` gerencia o estado do trem e a execução dos comandos. Aqui está uma visão geral de como o código opera:

1. **Inicialização:** Quando uma instância de `TremAutonomo` é criada, o trem começa na posição 0. O contador de movimentos consecutivos e a direção anterior são inicializados.

2. **Execução dos Comandos:**
   - **Validação de Comandos:** Cada comando na lista é validado para garantir que seja "ESQUERDA" ou "DIREITA". Caso contrário, é lançada uma exceção.
   - **Atualização do Estado:** O sistema atualiza a posição do trem com base no comando atual e rastreia a direção dos movimentos. Se o trem continua na mesma direção por muitos movimentos consecutivos, é lançada uma exceção.
   - **Verificação de Restrições:** O código verifica se o trem excedeu a distância máxima permitida ou se a quantidade de movimentos consecutivos na mesma direção está dentro dos limites estabelecidos. Exceções são lançadas se as restrições forem violadas.

3. **Retorno da Posição Final:** Após a execução de todos os comandos, a posição final do trem é retornada.

## Cenários de Teste

- **Comandos Inválidos:** Verificação de comandos desconhecidos e formatos incorretos.
- **Restrições de Movimento:** Testes para assegurar que o trem não exceda a distância máxima permitida ou faça movimentos consecutivos excessivos.
- **Condições de Borda:** Testes para cenários próximos aos limites estabelecidos.

## Desenvolvedores

<table align="center">
  <tr>
      <td align="center"><a href="https://github.com/v0cs"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/104214178?v=4" width="100px;" alt=""/><br /><sub><b>Vítor Celestino</b></sub></a><br /><a href="https://rocketseat.com.br/" title="Rocketseat">🚀</a></td>
    <td align="center"><a href="https://github.com/WesllyHn"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/117309594?v=4" width="100px;" alt=""/><br /><sub><b>Weslly Neres</b></sub></a><br /><a href="https://rocketseat.com.br/" title="Rocketseat">👨‍🚀</a></td>
  </tr>

# leilao
Esse trabalho tem como objetivo criar um leilão com as seguintes características:

Fazer o servidor e o cliente para um sistema de leilão. Nesse sistema, novos produtos podem ser cadastrados e listados.
Usuários podem ser cadastrados e podem logar e deslogar no sistema. 
Usuários podem participar de leilões, entrando desde meia hora antes do início do leilão até qualquer momento antes do leilão terminar. 
O número de lances por leilão e por usuário é totalmente livre, assim como o tempo de duração do leilão. 
O leilão termina apenas após transcorrido o tempo máximo sem lances daquele produto. 
Nenhum lance abaixo do lance mínimo deve ser aceito. O usuário pode participar de mais de um leilão ao mesmo tempo.

Uma vez que um lance seja feito, ele deve ser enviado ao servidor, que deve imediatamente repassar o lance e o seu autor para todos os participantes cadastrados para aquele leilão, desde que o lance seja maior que a oferta atual. Durante os períodos sem lances, o servidor deve mandar o valor atual e o autor do lance de 1 em 1 segundo para todos os participantes. Caso ainda não tenham sido feitos lances, o nome do autor deve ser preenchido com a string “Aguardando o envio” e o lance com o valor mínimo. Ao final do leilão, todos os usuários participantes do leilão devem ser notificados de quem ganhou e o valor final do produto. Além disso, os dados de quem comprou devem ser enviados para quem vendeu e os dados de quem vendeu devem ser passados para quem comprou.
Novos usuários podem entrar a qualquer momento no leilão e a saída de um ou mais usuários não deve finalizar o leilão.
O sistema deve listar o histórico de todos os leilões realizados, listando o produto com descrição, preço de venda e data da venda.



Mensagem
Parâmetros
Ação
Pontuação
Lanca_produto
Nome, descrição, lance mínimo, dia, mês, ano, hora, minuto, segundo, tempo máximo sem lances em segundos
Registra o produto e se prepara para o início do leilão no momento especificado.  Responde ao usuário com uma mensagem de ok ou not_ok, caso algum erro tenha acontecido. O usuário emissor dessa mensagem deve ser registrado como dono do produto. Só pode ser feito por usuários cadastrados e logados. Cada leilão deve ter um identificador único gerado pelo sistema.

Lista_leiloes
-
Retorna ao usuário uma mensagem Listagem. Não precisa estar cadastrado ou logado.

Listagem
Descrição
Mensagem enviada em reposta à mensagem Lista_leiloes. A descrição é uma string com um produto por linha, sendo que cada linha contém identificador do leilão, nome do produto, descrição, lance mínimo, dia, mês, ano e hora, minuto de início do leilão, o tempo máximo sem lances para o produto e o dono do produto. Não precisa estar cadastrado ou logado para receber essa mensagem. Só mostra leilões que estão acontecendo ou que ainda vão acontecer.



Adiciona_usuario
Nome, telefone, endereço, e-mail, senha
Registra usuário no servidor. Retorna ok se foi tudo bem ou not_ok se o usuário já existia ou se ocorreu algum problema no registro.

Apaga_usuario
Nome, senha
Se o nome e senha forem compatíveis, o usuário será removido. Só pode ser feito por usuários cadastrados e logados. Retorna ok ou not_ok.

Faz_login
Nome, senha
Verifica se o nome e a senha estão corretos e registra o IP e porta relacionados ao usuário na conexão atual. Só pode ser feito por usuários cadastrados. Retorna ok ou not_ok.

Sair
-
Desloga o usuário. Só pode ser feito pelo próprio usuário ou pelo sistema, caso perceba que a conexão não existe mais.

Entrar_leilao
Identificador do leilão
Entra no leilão identificado. Só pode ser feito por usuários cadastrados e logados.

Sair_leilao
Identificador do leilão
Sai do leilão identificado. Só pode ser feito por usuários cadastrados e logados.

Ok
-
Operação realizada com sucesso.

not_ok
-
Operação não realizada com sucesso.

Enviar_lance
Identificador do leilão, valor
Mensagem do usuário indicando um lance para um determinado produto. Implica no envio imediato das mensagens ok ou not_ok para o usuário que deu o lance e Lance para todos os usuários, incluindo o que deu o lance, caso esteja ok. Só pode ser enviada por usuários cadastrados, logados e participando do leilão.

Lance
Identificador do leilão, nome do usuário, valor, número de usuários no leilão no momento, número de lances que já foram dados.
Mensagem em resposta à Enviar_lance ou para envio periódico durante o leilão. Enviada para todos os usuários participantes do leilão. Ao receber essa mensagem, o cliente deve exibir todos os dados para o usuário.

Fim_leilao
Identificador do leilão, valor de venda, usuário
Enviada no fim do leilão para todos os usuários no leilão, avisando o fim do processo. Deve notificar qual foi o valor de venda e qual usuário comprou.

Contato_vendedor
Identificador do leilão, valor de venda, nome, endereço, telefone, e-mail
Enviada no fim do leilão para o cliente, contendo o identificador do leilão, o valor de venda e todos os dados do vendedor. Caso o comprador não esteja mais logado (não é possível mandar essa mensagem para ele – provavelmente, saiu antes do fim do leilão), ele deve ser marcado como deslogado e, no seu próximo login, a mensagem deve ser enviada automaticamente.

Contato_cliente
Identificador do leilão, valor de venda, nome, endereço, telefone, e-mail
Enviada no fim do leilão para o vendedor, contendo o identificador do leilão, o valor de venda e todos os dados do comprador. Caso o vendedor não esteja mais logado (não é possível mandar essa mensagem para ele), ele deve ser marcado como deslogado e, no seu próximo login, a mensagem deve ser enviada automaticamente.





As mensagens devem ser enviadas com o seguinte formato:
Nome-da-mensagem,parâmetros-também-separados-por-vírgula-e-sem-espaço
A ordem dos parâmetros não pode ser alterada.


É obrigatório:
Requisito
Pontos perdidos caso não seja atendido
- O uso de sockets


-2.0
- A criação de processos ou de threads


-2.0
- A sincronização dos processos e/ou threads com semáforos
-2.0
- O uso de arquivos para armazenar todos os dados do leilão


-1.0
- O uso das mensagens como foram descritas


-1.0
- O tratamento de exceções


-1.5
- O usuário poder entrar em vários leilões ao mesmo tempo
-1.0
- Vários leilões poderem acontecer ao mesmo tempo
-1.0
- O leilão começar na hora certa
-0.5
- Usuários podendo entrar e sair do leilão a qualquer momento sem gerar erros ou interromper o leilão
-1.0
- O leilão terminar na hora certa
-0.5
- O usuário poder entrar e aguardar o início do leilão até meia hora antes de ele começar.
-0.5
- A interface do cliente deve perguntar ao usuário qual o IP e porta do servidor.


-0.5
- Identificar e justificar o uso no código de threads, processos, semáforos e variáveis compartilhadas.
Perde os pontos listados acima. É necessário usar e dizer porque está usando para não perder os pontos.
- Identificar com comentários no código onde cada um dos pontos pedidos no trabalho está sendo feito.


Sem o comentário, não ganha o ponto mesmo que tenha feito o código. Colocar no comentário o nome da mensagem e a lógica que está sendo usada para enviá-la e tomar todas as ações necessárias.

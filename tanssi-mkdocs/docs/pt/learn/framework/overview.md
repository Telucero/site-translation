---
título: Panorama do quadro de desenvolvimento da rede
descrição: Substrate é uma estrutura de desenvolvimento de blockchain construída na linguagem de programação Rust que simplifica e acelera o processo de desenvolvimento de novas redes.
ícone: octicons-home-24
Categorias: Básicos
---

# Visão geral da estrutura de desenvolvimento de rede {: #rede-dev-framework-overview }

## Introdução {: #introdução }

Construir uma rede a partir do zero é uma tarefa muito complexa que requer um conhecimento profundo numa vasta gama de áreas, incluindo (mas não se limitando a):

- **Algoritmos de consenso** - o consenso garante que todos os participantes na rede blockchain concordam com a validade das transacções. Alguns mecanismos de consenso populares incluem Proof of Work (PoW) e Proof of Stake (PoS)

- Criptografia** - a criptografia desempenha um papel crucial na segurança da cadeia de blocos. São necessários algoritmos criptográficos para tarefas como a criação de assinaturas digitais, a verificação de transacções e a encriptação de dados

- Rede distribuída** - uma arquitetura de rede para permitir que os nós comuniquem, validem transacções e sincronizem os dados da cadeia de blocos é fundamental para manter um livro-razão partilhado numa rede descentralizada

- Estruturas de dados** - para além da lista de blocos, em que cada bloco contém um conjunto de transacções juntamente com uma referência ao bloco anterior, é necessária uma estratégia optimizada e de elevado desempenho para armazenar o estado da rede

- Governação** - se a rede for concebida para não ter permissões, é importante um mecanismo de votação para a manter em evolução e refletir a vontade da comunidade

- Capacidade de atualização** - é necessário definir claramente como atualizar, como as modificações são implementadas e como os conflitos são resolvidos na rede

Felizmente, não há necessidade de construir estes componentes da cadeia de blocos a partir do zero, graças a uma excelente estrutura de código aberto chamada [Substrate](https://docs.polkadot.com/develop/parachains/intro-polkadot-sdk/){target=\_blank}. O próprio Tanssi é construído com essa estrutura, aproveitando suas implementações de base abrangentes, modularidade e flexibilidade para alcançar um alto nível de personalização.

## Substrate Framework {: #substrate-framework}

Substrate é uma estrutura extremamente eficiente, flexível, modular e altamente personalizável para a construção de blockchains. Esta estrutura é a base e o motor que alimenta muitos projetos em todo o ecossistema Web3, incluindo a própria rede Tanssi e as redes implantadas através do Tanssi.

Muitas das suas grandes caraterísticas, como o desempenho, a facilidade de utilização e a modularidade, resultam da linguagem de programação escolhida para o seu desenvolvimento. É aqui que a [Linguagem de Programação Rust] (#rust-programming-language) brilha: É rápida, portátil e fornece um modelo maravilhoso para lidar com a memória, entre outras razões detalhadas na [próxima secção](#linguagem-de-programação-ferrugem).

Ao desenvolver uma rede, o Substrate representa um grande avanço ao fornecer um conjunto pronto para uso de implementações dos principais blocos de construção que um projeto precisa:

- **Algoritmos de consenso** - existem vários motores de consenso incorporados, como o Aura (prova de autoridade), o Babe (prova de aposta) e o Grandpa (finalidade do bloco), mas devido ao elevado grau de personalização que o Substrate oferece, as equipas podem sempre optar por desenvolver o seu consenso específico para se adaptarem às necessidades do caso de utilização, como a equipa Moonbeam fez com o [Nimbus Parachain Consensus Framework](https://docs.moonbeam.network/learn/features/consensus){target=\_blank}

- **Módulos de tempo de execução** - muitos módulos incorporados (explicados em pormenor na secção [modules](/learn/framework/modules/){target=\_blank}) podem ser selecionados e configurados na sua rede, tais como contas, saldos, staking, governação, identidade e muito mais

- Rede** - protocolos e bibliotecas integrados para estabelecer conexões, propagar transações e blocos, sincronizar o estado da blockchain e gerenciar interações de rede

- Armazenamento** - mecanismos de armazenamento incorporados para armazenamento e recuperação eficientes de dados

- Fila de transacções** - sistema de fila de transacções incorporado que gere a validação, a priorização e a inclusão de transacções em blocos, garantindo a consistência e a integridade do estado da rede

- APIs RPC** - O substrato fornece APIs de Chamada de Procedimento Remoto (RPC) que permitem que aplicações externas interajam com a rede consultando dados da cadeia de blocos, submetendo transacções e acedendo a várias funcionalidades expostas pelo tempo de execução

Todas as funcionalidades que o Substrate oferece podem ser utilizadas tal como estão, alargadas, personalizadas ou substituídas para satisfazer os requisitos específicos do caso de utilização da rede.

O Substrate simplifica e acelera o processo de desenvolvimento de novas redes. Quando utilizado em conjunto com o Tanssi, que ajuda a lidar com a infraestrutura e a supervisionar a implementação, a tarefa de lançar uma nova rede torna-se significativamente mais simples!

## Linguagem de programação Rust {: #rust-programming-language}

A [Rust](https://www.rust-lang.org){target=\_blank} é uma linguagem de programação com caraterísticas únicas que a tornaram na linguagem mais adorada pelo sétimo ano consecutivo, de acordo com o [inquérito anual a programadores do Stack Overflow](https://survey.stackoverflow.co/2022#section-most-loved-dreaded-and-wanted-programming-scripting-and-markup-languages){target=\blank}.

Para além de proporcionar uma excelente experiência aos programadores, a Rust destaca-se em muitas áreas:

- **Segurança de memória** - O compilador Rust aplica verificações rigorosas em tempo de compilação para evitar erros de programação comuns, como desreferências de ponteiro nulo, estouros de buffer e corridas de dados. Além disso, a memória é gerida através de um novo sistema de propriedade (verificado pelo compilador), o que elimina a necessidade de um coletor de lixo

- Desempenho** - O Rust atinge um desempenho comparável ao do C e do C++, fornecendo controlo de baixo nível sobre os recursos do sistema e minimizando a sobrecarga do tempo de execução. Tem um princípio de abstração de custo zero, semelhante ao "what you don't use, you don't pay for" do C++, o que significa que as abstracções não têm custos adicionais

- Concorrência** - O Rust tem funcionalidades incorporadas que facilitam a escrita de código concorrente e paralelo sem introduzir corridas de dados. Fornece threads leves (tarefas) e um modelo de propriedade poderoso que garante a partilha segura de dados entre threads

- Abstracções expressivas e seguras** - O Rust oferece um conjunto rico de funcionalidades de linguagem modernas, como a correspondência de padrões, tipos de dados algébricos, fechos e inferência de tipos, permitindo aos programadores escrever e ler código expressivo e conciso. O compilador Rust reforça o sistema de tipos fortes, evitando muitos erros de tempo de execução em tempo de compilação

- Compatibilidade entre plataformas** - O Rust foi concebido para funcionar bem numa variedade de plataformas e arquitecturas. Suporta os principais sistemas operativos, como o Windows, macOS e Linux, bem como sistemas incorporados e WebAssembly. Esta versatilidade permite aos programadores escrever código que pode ser implementado em diferentes ambientes

- Ecossistema em crescimento** - O Rust tem um ecossistema em rápido crescimento com uma comunidade vibrante e uma coleção rica de bibliotecas e ferramentas. O gestor de pacotes oficial, Cargo, simplifica a gestão de dependências, a construção e os testes

- Interoperabilidade** - O Rust proporciona uma interoperabilidade perfeita com bases de código existentes escritas em C e C++. Tem uma Foreign Function Interface (FFI) que permite ao código Rust interagir com código escrito noutras linguagens, permitindo aos programadores introduzir gradualmente o Rust em projectos existentes, como o kernel do Linux

Aplicativo para Automação de Coletas em Transportadora usando o sistema SSW: Web Scraping e Atualização em Tempo Real

Este projeto foi criado para uma empresa de transporte que procurava uma solução automatizada para administrar coletas e atualizações de dados em tempo real, aprimorando o processo de trabalho e eliminando a exigência de atualizações manuais em suas planilhas. A seguir, apresento as principais características do aplicativo.

📑 Funções disponíveis 

1- Automação de Entrada e Deslocamento
O Selenium permite que o sistema acesse automaticamente o portal de administração da transportadora, fazendo o login com as credenciais do usuário. Este procedimento inicial é seguido por uma navegação automatizada, direcionada para escolher as informações específicas requeridas para a recolha.

2- Extração de Informações e Scraping na Web
O programa reconhece componentes específicos na interface da empresa de transporte e emprega comandos exatos para obter as informações pretendidas. Este método de scraping na internet permite uma recolha ágil e eficaz de informações atualizadas, que são copiadas e manipuladas em tempo real.

3- Compatibilidade com Planilhas e WhatsApp
As informações obtidas são automaticamente inseridas em uma planilha específica para armazenamento e análise. Posteriormente, a automação emprega o WhatsApp para enviar relatórios das coletas às unidades parceiras, fornecendo informações sobre o estado e atualizações de forma rápida e eficiente.

4- Painel Administrativo para o Usuário
O sistema possui uma interface gráfica (GUI) desenvolvida em Tkinter, que facilita o gerenciamento e o monitoramento de todas as atividades de coleta. Este painel de controle possui botões que possibilitam a realização das tarefas de coleta para diversas unidades, além de um checklist automático.

⭐ Tecnologias Utilizadas
Selenium e PyAutoGUI: Para a automação do navegador e interação com elementos da interface do usuário.
Tkinter: Para a criação da interface gráfica do usuário (GUI), permitindo o controle das operações com um design amigável e intuitivo.
Python: Linguagem principal, escolhida por sua simplicidade e vasta biblioteca para automação.
WhatsApp Web: Integração via web para envio automatizado de relatórios em tempo real.

✅ Resultados e Benefícios
O aplicativo gerou uma grande eficiência para a transportadora, eliminando as atividades manuais e reduzindo o tempo necessário para atualizar as planilhas e comunicar o status das coletas.

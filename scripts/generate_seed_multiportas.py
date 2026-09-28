# -*- coding: utf-8 -*-
"""
Script para gerar o arquivo seed_multiportas.json 100% alinhado ao 
Questionário de Revisão para a Prova 01 de Modelo Multiportas,
removendo bancas de concurso e inserindo casos práticos com nomes de pessoas
e conceitos doutrinários exatos (Carnelutti, Frank Sander, etc.).
"""
import json
from pathlib import Path

questions = [
    # -------------------------------------------------------------
    # TEMA 01: Noção de Conflito de Direito e Conflito Social
    # -------------------------------------------------------------
    {
        "id": "multi_01_a_carnelutti_lide",
        "subject": "Noção de Conflito de Direito e Conflito Social",
        "bank": "Revisão Prova 01",
        "difficulty": "Médio",
        "enunciado": "Mariana e Roberto são vizinhos e divergem sobre a demarcação de um muro divisório, bem da vida considerado escasso entre ambos. Mariana exige que Roberto recue sua cerca em dois metros, mas Roberto recusa terminantemente a pretensão, afirmando ter posse mansa e pacífica. À luz da doutrina processual clássica de Francesco Carnelutti sobre a transposição do conflito social para o plano jurídico, assinale a afirmativa correta:",
        "options": {
            "A": "A situação narrada retrata uma lide, conceituada por Francesco Carnelutti como o conflito de interesses qualificado por uma pretensão resistida, em que Mariana quer subordinar o interesse de Roberto e este resiste.",
            "B": "O conflito entre Mariana e Roberto constitui mero dissabor social sem relevância jurídica, uma vez que a noção de lide prescinde da existência de bens escassos ou de divergência de vontades.",
            "C": "Segundo Carnelutti, a lide se aperfeiçoa unilateralmente, bastando que Mariana manifeste sua pretensão em juízo, sendo desnecessária a resistência ou recusa de Roberto.",
            "D": "O conflito social e a lide jurídica são conceitos idênticos na lição de Francesco Carnelutti, pois qualquer divergência moral ou ética entre vizinhos configura lide perante o ordenamento."
        },
        "gabarito": "A",
        "article": "Doutrina de Francesco Carnelutti (Teoria da Lide)",
        "legal_basis": "A doutrina de Francesco Carnelutti conceitua o conflito de direito como lide: o conflito de interesses qualificado por uma pretensão resistida, quando um sujeito exige que o interesse alheio se subordine ao seu e o outro resiste.",
        "explanation": "Conforme o questionário da Prova 01: o conflito social decorre da divergência sobre bens escassos. No plano jurídico, qualifica-se como lide segundo Francesco Carnelutti: conflito de interesses qualificado por pretensão resistida."
    },
    {
        "id": "multi_01_b_bens_escassos_social",
        "subject": "Noção de Conflito de Direito e Conflito Social",
        "bank": "Revisão Prova 01",
        "difficulty": "Fácil",
        "enunciado": "Ao lecionar sobre a gênese das controvérsias na convivência humana, o Professor de Direito Processual explica aos alunos como os conflitos sociais emergem e quando adquirem relevância para o ordenamento jurídico. De acordo com o conceito fundamental de conflito social e de conflito de direito, assinale a opção correta:",
        "options": {
            "A": "O conflito social é um dado inerente à convivência humana, surgindo sempre que há divergência de interesses, necessidades ou valores sobre bens da vida que são escassos, ganhando relevância jurídica quando qualificado pelo ordenamento.",
            "B": "O conflito social apenas existe quando decorre da prática de um crime expressamente tipificado na legislação penal, inexistindo conflito social em disputas contratuais.",
            "C": "Os bens da vida, por serem infinitos e universais na sociedade moderna, afastam a existência do conflito social, remanescendo apenas disputas de natureza processual formal.",
            "D": "O direito positivo proíbe o surgimento de conflitos sociais, punindo com multa coercitiva todo cidadão que manifestar discordância sobre valores ou necessidades."
        },
        "gabarito": "A",
        "article": "Teoria Geral do Processo - Conflito Social e Jurídico",
        "legal_basis": "O conflito social surge da divergência de interesses sobre bens escassos da vida. Ele se qualifica no plano jurídico quando passa a ter relevância para o ordenamento.",
        "explanation": "O conflito social decorre da escassez de bens e choque de interesses da vida gregária; qualifica-se como conflito de direito ao atrair tutela e relevância na ordem jurídica."
    },
    {
        "id": "multi_01_c_pretensao_subordinacao",
        "subject": "Noção de Conflito de Direito e Conflito Social",
        "bank": "Revisão Prova 01",
        "difficulty": "Médio",
        "enunciado": "Lucas celebrou contrato de compra e venda de um veículo com Felipe. Felipe pagou o preço acordado, mas Lucas recusou-se a entregar os documentos de transferência, alegando despesas supervenientes. Felipe, então, busca a tutela jurisdicional para compelir Lucas a satisfazer a obrigação. Na clássica definição de lide (Carnelutti), o elemento caracterizador da pretensão consiste no ato pelo qual:",
        "options": {
            "A": "Um indivíduo exige que o interesse de outrem se subordine ao seu e esse segundo sujeito resiste à exigência, reclamando a intervenção da ordem jurídica para restabelecer a paz social.",
            "B": "As duas partes abrem mão imediata e espontânea de qualquer direito patrimonial, sem que haja resistência fática ou jurídica de nenhum dos polos.",
            "C": "O Estado impõe compulsoriamente a prisão civil do devedor antes mesmo da citação formal no processo de conhecimento.",
            "D": "O credor busca a conciliação extrajudicial sem formular qualquer exigência ou pretensão patrimonial perante o polo devedor."
        },
        "gabarito": "A",
        "article": "Doutrina de Francesco Carnelutti e Teoria Geral do Conflito",
        "legal_basis": "A pretensão ocorre quando um sujeito exige a subordinação do interesse alheio ao seu; havendo resistência, surge a lide que reclama intervenção jurídica.",
        "explanation": "Conforme o texto da revisão: isso se dá quando um indivíduo exige que o interesse de outrem se subordine ao seu e este segundo sujeito resiste à exigência."
    },
    {
        "id": "multi_01_d_paz_social_relevancia",
        "subject": "Noção de Conflito de Direito e Conflito Social",
        "bank": "Revisão Prova 01",
        "difficulty": "Difícil",
        "enunciado": "Em debate acadêmico, os estudantes Pedro e Amanda discutem a fronteira entre os conflitos puramente sociológicos de foro íntimo e aqueles que demandam intervenção do ordenamento jurídico. Amanda defende acertadamente que o conflito de interesses reclama a intervenção da ordem jurídica quando:",
        "options": {
            "A": "Passa a ter relevância para o ordenamento jurídico ao envolver pretensão resistida sobre bem tutelado, visando restabelecer a paz social e a estabilidade das relações.",
            "B": "Envolve qualquer descontentamento amoroso ou frustração interpessoal privada, independentemente de previsão na ordem jurídica positiva.",
            "C": "O Estado decide aplicar sanções administrativas de ofício sem que nenhuma das partes tenha manifestado resistência ou oposição fática.",
            "D": "As partes já resolveram a lide amigavelmente antes de qualquer choque de interesses ou divergência quanto a bens da vida."
        },
        "gabarito": "A",
        "article": "Teoria Geral do Processo (Conflito e Paz Social)",
        "legal_basis": "No plano jurídico, o conflito se qualifica quando ganha relevância para o ordenamento por meio da lide (pretensão resistida), reclamando a atuação da ordem jurídica para restabelecer a paz social.",
        "explanation": "O conflito no plano jurídico se diferencia do mero choque sociológico por atrair a tutela normativa e exigir solução para a paz social."
    },

    # -------------------------------------------------------------
    # TEMA 02: Enfrentamento dos Conflitos em Contraponto com a Jurisdição
    # -------------------------------------------------------------
    {
        "id": "multi_02_a_monopolio_finalidade",
        "subject": "Enfrentamento dos Conflitos vs. Jurisdição",
        "bank": "Revisão Prova 01",
        "difficulty": "Fácil",
        "enunciado": "Historicamente, o Estado moderno avocou para si o monopólio da função jurisdicional. De acordo com o questionário de revisão, a finalidade primária dessa avocação estatal e as limitações práticas da via judicial tradicional residem em:",
        "options": {
            "A": "Evitar a justiça pelas próprias mãos e garantir segurança jurídica por meio de decisões acobertadas pela coisa julgada, embora a via judicial tradicional trabalhe sob a lógica binária de vencedor e perdedor.",
            "B": "Impedir que qualquer cidadão celebre acordos extrajudiciais espontâneos sobre seus próprios direitos patrimoniais disponíveis.",
            "C": "Garantir que todos os conflitos familiares sejam solucionados no prazo máximo improrrogável de vinte e quatro horas com aplicação de pena pecuniária.",
            "D": "Eliminar a necessidade de fundamentação nas decisões dos magistrados togados, priorizando a celeridade arbitrária da sentença."
        },
        "gabarito": "A",
        "article": "Monopólio da Jurisdição e Limitações do Processo Clássico",
        "legal_basis": "O Estado avocou o monopólio da jurisdição para evitar a justiça com as próprias mãos e dar segurança jurídica pela coisa julgada. Sua limitação é a lógica binária (vencedor/perdedor).",
        "explanation": "Texto exato do questionário: o Estado avocou o monopólio da jurisdição para evitar a justiça pelas próprias mãos e garantir segurança jurídica pela coisa julgada; contudo, trabalha sob a lógica binária de vencedor e perdedor."
    },
    {
        "id": "multi_02_b_logica_binaria_passado",
        "subject": "Enfrentamento dos Conflitos vs. Jurisdição",
        "bank": "Revisão Prova 01",
        "difficulty": "Médio",
        "enunciado": "Carlos e Juliana litigam judicialmente há cinco anos em razão da dissolução de uma união estável conturbada. O magistrado proferiu sentença meritória procedente em parte, transitada em julgado. Contudo, as partes continuam se hostilizando na rotina dos filhos. Esse fenômeno prático evidencia uma das limitações basilares da jurisdição estatal clássica, qual seja:",
        "options": {
            "A": "O processo estatal clássico foca em fatos passados para atribuir culpa ou enquadramento legal, operando na lógica binária (vencedor/perdedor), o que encerra a relação processual formal, mas deixa intocado o conflito sociológico de fundo.",
            "B": "A sentença judicial possui efeito nulo imediato sempre que as partes continuarem residindo no mesmo município após o trânsito em julgado.",
            "C": "O juiz togado atua com desvio de finalidade ao julgar ações de família, competência que a Constituição Federal reservou exclusivamente à arbitragem privada.",
            "D": "A coisa julgada material é incompatível com a proteção dos filhos, impondo a anulação automática da sentença que decretou a dissolução da união estável."
        },
        "gabarito": "A",
        "article": "Limitações da Jurisdição Estatal Clássica",
        "legal_basis": "O processo clássico debruça-se sobre fatos passados para atribuir culpa e enquadramento legal. A sentença formalmente encerra o processo, mas não pacifica a relação sociológica.",
        "explanation": "Na prática forense, a sentença muitas vezes encerra a relação processual formal, mas deixa intocado o conflito sociológico subjacente, demonstrando a necessidade de métodos adequados."
    },
    {
        "id": "multi_02_c_conflito_sociologico_intocado",
        "subject": "Enfrentamento dos Conflitos vs. Jurisdição",
        "bank": "Revisão Prova 01",
        "difficulty": "Médio",
        "enunciado": "A doutrina contemporânea contrapõe a exclusividade da decisão judicial impositiva à adoção de métodos adequados de enfrentamento de litígios. O motivo central dessa contraposição é que:",
        "options": {
            "A": "A via judicial tradicional, ao focar na estrita subsunção normativa de fatos pretéritos, costuma encerrar o processo no papel sem promover a pacificação efetiva das relações humanas.",
            "B": "O Poder Judiciário foi extinto como poder soberano do Estado pelo Código de Processo Civil de 2015, cedendo todo o espaço para os cartórios extrajudiciais.",
            "C": "A decisão impositiva do juiz togado é juridicamente incapaz de produzir coisa julgada formal ou material no ordenamento processual brasileiro.",
            "D": "Os métodos autocompositivos retiram do cidadão o direito fundamental de ser ouvido em juízo, obrigando-o a abrir mão de todos os seus bens."
        },
        "gabarito": "A",
        "article": "Enfrentamento Contemporâneo dos Litígios",
        "legal_basis": "O enfrentamento contemporâneo contrapõe a exclusividade da decisão judicial impositiva à adoção de métodos adequados que buscam a pacificação efetiva das relações.",
        "explanation": "Enquanto a sentença estatal impõe uma solução externa muitas vezes insuficiente para apaziguar os ânimos, os métodos adequados buscam a pacificação material e efetiva da relação."
    },
    {
        "id": "multi_02_d_pacificacao_efetiva",
        "subject": "Enfrentamento dos Conflitos vs. Jurisdição",
        "bank": "Revisão Prova 01",
        "difficulty": "Difícil",
        "enunciado": "Ao analisar a crise da prestação jurisdicional e o modelo de justiça estatal adjudicada, assinale a opção que reflete fielmente o contraponto contemporâneo entre a sentença judicial impositiva e os métodos adequados de resolução de disputas:",
        "options": {
            "A": "Contrapõe-se a exclusividade da decisão judicial impositiva à adoção de métodos adequados que buscam a pacificação efetiva das relações, superando a mera lógica de atribuir culpa e polarizar partes em vencedor e perdedor.",
            "B": "A jurisdição estatal deve proibir qualquer modalidade de diálogo consensual entre os litigantes, pois o acordo entre as partes enfraquece o monopólio soberano do Estado.",
            "C": "O contraponto inexiste na teoria processual brasileira, visto que a única forma legítima de paz social reconhecida pela Constituição é a sentença condenatória transitada em julgado.",
            "D": "A decisão impositiva do juiz togado é sempre superior à autocomposição, porque a vontade das partes não tem qualquer valor normativo no Estado Democrático de Direito."
        },
        "gabarito": "A",
        "article": "Jurisdição vs. Métodos Adequados",
        "legal_basis": "O contraponto contemporâneo combate a exclusividade da sentença adjudicada e propõe métodos adequados que alcancem a pacificação social real.",
        "explanation": "A pacificação efetiva das relações substitui o antigo paradigma focado apenas na sentença formal e no binômio vencedor-perdedor."
    },

    # -------------------------------------------------------------
    # TEMA 03: Construção Legislativa no Enfrentamento de Conflitos
    # -------------------------------------------------------------
    {
        "id": "multi_03_a_marcos_normativos",
        "subject": "Construção Legislativa no Enfrentamento de Conflitos",
        "bank": "Revisão Prova 01",
        "difficulty": "Médio",
        "enunciado": "A evolução legislativa brasileira no tratamento de conflitos demonstra uma transição progressiva do foco exclusivo na sentença estatal para a valorização dos meios consensuais. Assinale a alternativa que apresenta a correta cronologia e os marcos normativos fundamentais dessa construção legislativa:",
        "options": {
            "A": "CF/88 (art. 5º, XXXV e art. 98, I), Lei nº 9.099/1995 (Juizados Especiais), Lei nº 9.307/1996 (Arbitragem), Resolução nº 125/2010 do CNJ (Política Judiciária e CEJUSCs), CPC/2015 (art. 3º) e Lei nº 13.140/2015 (Lei de Mediação).",
            "B": "CPC/1973 que proibiu a conciliação, seguido pela Lei de Arbitragem em 2015 e pela Constituição Federal que baniu os Juizados Especiais em 2020.",
            "C": "Lei nº 13.140/2015 que criou a arbitragem estatal, sucedida pela Resolução do CNJ que revogou o Código de Processo Civil de 2015.",
            "D": "CF/88 que instituiu a autotutela compulsória como regra geral, seguida pela Lei nº 9.099/1995 que vedou transações nos Juizados Cíveis."
        },
        "gabarito": "A",
        "article": "Construção Legislativa (CF/88, Leis 9.099, 9.307, Res. 125 CNJ, CPC/15, Lei 13.140)",
        "legal_basis": "A linha do tempo do questionário destaca: CF/88 (art. 5º, XXXV e art. 98, I); Lei 9.099/95; Lei 9.307/96; Resolução 125/2010 CNJ; CPC/2015 (art. 3º) e Lei 13.140/2015.",
        "explanation": "Esses são exatamente os diplomas normativos detalhados na resposta da questão 03 do Questionário de Revisão."
    },
    {
        "id": "multi_03_b_res125_cnj_cejusc",
        "subject": "Construção Legislativa no Enfrentamento de Conflitos",
        "bank": "Revisão Prova 01",
        "difficulty": "Médio",
        "enunciado": "Em 2010, um ato normativo de fundamental importância para o sistema de justiça brasileiro formalizou a Política Judiciária Nacional de tratamento adequado dos conflitos de interesses. Trata-se da:",
        "options": {
            "A": "Resolução nº 125 do Conselho Nacional de Justiça (CNJ), que impôs a criação dos Centros Judiciários de Solução de Conflitos e Cidadania (CEJUSCs) pelos tribunais.",
            "B": "Súmula Vinculante do Supremo Tribunal Federal que extinguiu a exigência de tentativa de conciliação prévia em ações cíveis e de família.",
            "C": "Emenda Constitucional que privatizou a justiça de primeiro grau e entregou a condução de audiências exclusivamente a cartórios de registro de imóveis.",
            "D": "Portaria do Ministério da Justiça que autorizou os delegados de polícia a proferirem sentenças cíveis condenatórias com força de coisa julgada."
        },
        "gabarito": "A",
        "article": "Resolução CNJ nº 125/2010",
        "legal_basis": "Em 2010, a Resolução nº 125 do CNJ formalizou a Política Judiciária Nacional de tratamento adequado dos conflitos, impondo a criação dos CEJUSCs.",
        "explanation": "A Resolução 125/2010 do CNJ é o marco administrativo estruturante da Política Judiciária Nacional e dos CEJUSCs."
    },
    {
        "id": "multi_03_c_cpc2015_art3_multiportas",
        "subject": "Construção Legislativa no Enfrentamento de Conflitos",
        "bank": "Revisão Prova 01",
        "difficulty": "Fácil",
        "enunciado": "O Código de Processo Civil de 2015 consagrou expressamente o modelo multiportas como norma fundamental do processo civil brasileiro logo em seu artigo 3º. Esse dispositivo e seus parágrafos determinam que:",
        "options": {
            "A": "O Estado promoverá, sempre que possível, a solução consensual dos conflitos, devendo a conciliação, a mediação e outros métodos adequados ser estimulados por juízes, advogados, defensores e promotores.",
            "B": "Apenas a sentença do magistrado togado tem validade jurídica, sendo expressamente proibido a advogados incentivar transações antes da instrução.",
            "C": "A arbitragem é restrita a causas penais hediondas, sendo vedada em litígios civis sobre direitos patrimoniais disponíveis.",
            "D": "O acesso à justiça consiste unicamente no direito de ajuizar petição inicial e aguardar sentença condenatória sem qualquer fase conciliatória."
        },
        "gabarito": "A",
        "article": "Art. 3º, §§ 1º, 2º e 3º do CPC/2015",
        "legal_basis": "O CPC/2015 consolidou o sistema multiportas como norma fundamental no art. 3º, ladeado pela Lei de Mediação (Lei nº 13.140/2015).",
        "explanation": "O art. 3º do CPC/2015 erige a solução consensual e a arbitragem a normas fundamentais da ordem processual brasileira."
    },
    {
        "id": "multi_03_d_constituicao1988_art98",
        "subject": "Construção Legislativa no Enfrentamento de Conflitos",
        "bank": "Revisão Prova 01",
        "difficulty": "Médio",
        "enunciado": "A Constituição da República de 1988 desempenhou papel primordial na virada paradigmática da resolução de disputas no Brasil ao consagrar não apenas o princípio do acesso à justiça (art. 5º, XXXV), mas também prever em seu artigo 98, inciso I:",
        "options": {
            "A": "A criação de Juizados Especiais providos por juízes togados ou togados e leigos, competentes para a conciliação, o julgamento e a execução de causas cíveis de menor complexidade e infrações penais de menor potencial ofensivo.",
            "B": "A exclusão do Poder Judiciário de controvérsias patrimoniais decorrentes de relações de consumo entre fornecedores e consumidores.",
            "C": "A obrigatoriedade de autotutela armada em conflitos fundiários rurais e urbanos como etapa prévia ao processo civil.",
            "D": "O encerramento definitivo das funções jurisdicionais do Estado em matéria cível e comercial em benefício da mediação privada."
        },
        "gabarito": "A",
        "article": "Art. 98, I da Constituição Federal de 1988",
        "legal_basis": "A CF/88 previu no art. 98, I a criação dos Juizados Especiais voltados prioritariamente à conciliação e transação.",
        "explanation": "O art. 98, I da CF/88 é a matriz constitucional dos Juizados Especiais e do estímulo à conciliação e transação."
    },

    # -------------------------------------------------------------
    # TEMA 04: Principais Formas de Resolução de Conflitos
    # -------------------------------------------------------------
    {
        "id": "multi_04_a_triade_classica",
        "subject": "Principais Formas de Resolução de Conflitos",
        "bank": "Revisão Prova 01",
        "difficulty": "Fácil",
        "enunciado": "A Teoria Geral do Processo agrupa os meios de resolução de controvérsias em três grandes categorias fundamentais. Assinale a alternativa que indica corretamente essas três formas e sua premissa conceitual:",
        "options": {
            "A": "Autotutela (imposição pela própria força), autocomposição (os próprios contendores constroem o desfecho) e heterocomposição (terceiro neutro com decisão impositiva e vinculante).",
            "B": "Transação, submissão e desistência da ação, sendo todas modalidades exclusivas de heterocomposição judicial estatal.",
            "C": "Monopólio judicial, desforço possessório e coisa julgada, sendo todas consideradas formas de autotutela ilícita pelo Código Civil.",
            "D": "Arbitragem voluntária, arbitragem legal e arbitragem obrigatória, inexistindo autotutela no ordenamento jurídico nacional."
        },
        "gabarito": "A",
        "article": "Teoria Geral do Processo (Formas de Solução de Conflitos)",
        "legal_basis": "A teoria geral do processo agrupa os meios em: autotutela (própria força), autocomposição (partes constroem o desfecho) e heterocomposição (terceiro impõe a decisão).",
        "explanation": "Essa é a tríade conceitual exata constante da questão 04 do Questionário de Revisão."
    },
    {
        "id": "multi_04_b_autotutela_excecoes",
        "subject": "Principais Formas de Resolução de Conflitos",
        "bank": "Revisão Prova 01",
        "difficulty": "Médio",
        "enunciado": "A autotutela corresponde à imposição da vontade de uma das partes pelo emprego da própria força. No Estado de Direito contemporâneo, a autotutela é tratada como:",
        "options": {
            "A": "Excepcional e, em regra, repudiada pelo direito (tipificada inclusive como crime de exercício arbitrário das próprias razões), ressalvadas hipóteses expressas como a legítima defesa e o desforço possessório imediato.",
            "B": "A via preferencial e obrigatória de solução de todo e qualquer litígio patrimonial, devendo preceder o ajuizamento de qualquer demanda perante o Poder Judiciário.",
            "C": "Um método autocompositivo indireto em que as partes são assessoradas por um mediador togado com poder coercitivo de uso da força policial.",
            "D": "Um instituto exclusivo da arbitragem internacional de comércio, inexistindo qualquer reflexo na legislação civil brasileira."
        },
        "gabarito": "A",
        "article": "Autotutela no Direito Brasileiro (Código Civil e Código Penal)",
        "legal_basis": "A autotutela é excepcional e em regra repudiada pelo direito, ressalvadas hipóteses como a legítima defesa e o desforço possessório imediato.",
        "explanation": "A regra geral é o repúdio à autotutela (art. 345 CP), sendo tolerada apenas excepcionalmente (ex: art. 1.210, § 1º CC e legítima defesa)."
    },
    {
        "id": "multi_04_c_heterocomposicao_agentes",
        "subject": "Principais Formas de Resolução de Conflitos",
        "bank": "Revisão Prova 01",
        "difficulty": "Médio",
        "enunciado": "A heterocomposição opera quando as partes submetem a controvérsia à decisão impositiva e vinculante de um terceiro que se sobrepõe a elas. No sistema jurídico brasileiro, quem pode figurar como terceiro decisor na heterocomposição?",
        "options": {
            "A": "O juiz estatal no exercício da jurisdição togada, ou o árbitro no âmbito da arbitragem privada.",
            "B": "Exclusivamente o delegado de polícia civil nos inquéritos de família.",
            "C": "Apenas o mediador judicial, visto que o juiz togado não possui poderes heterocompositivos no CPC/2015.",
            "D": "O conciliador ou o facilitador comunitário, desde que apliquem sanções penais de prisão simples aos litigantes."
        },
        "gabarito": "A",
        "article": "Heterocomposição (Jurisdição e Arbitragem)",
        "legal_basis": "A heterocomposição opera com a submissão a um terceiro que se sobrepõe às partes: seja o juiz estatal na jurisdição togada, seja o árbitro na arbitragem privada.",
        "explanation": "São as duas vias heterocompositivas do direito brasileiro: a jurisdição estatal togada e a arbitragem privada."
    },
    {
        "id": "multi_04_d_autocomposicao_desfecho",
        "subject": "Principais Formas de Resolução de Conflitos",
        "bank": "Revisão Prova 01",
        "difficulty": "Médio",
        "enunciado": "Diferenciando a autocomposição da heterocomposição, o elemento essencial que consagra a autocomposição é o fato de que:",
        "options": {
            "A": "Os próprios contendores constroem o desfecho do litígio, o que pode ocorrer diretamente entre eles (negociação) ou com a ajuda de um terceiro neutro (mediação ou conciliação).",
            "B": "Um terceiro togado impõe compulsoriamente sua vontade aos sujeitos com base no princípio da autoridade judicial absoluta.",
            "C": "As partes são obrigadas a aceitar qualquer decisão ditada pelo conciliador sob pena de aplicação de multa punitiva por litigância de má-fé.",
            "D": "O conflito é submetido à câmara de arbitragem para julgamento por laudo irrecorrível sem participação dos litigantes."
        },
        "gabarito": "A",
        "article": "Autocomposição - Conceito e Mecânica",
        "legal_basis": "A autocomposição abrange os métodos em que os próprios litigantes constroem a solução, direta ou indiretamente com terceiro neutro.",
        "explanation": "Na autocomposição, o poder de decisão pertence e permanece nas partes envolvidas na controvérsia."
    },

    # -------------------------------------------------------------
    # TEMA 05: Métodos Alternativos e Papel de Cada Condutor
    # -------------------------------------------------------------
    {
        "id": "multi_05_a_mediacao_papel_vedacao",
        "subject": "Métodos Alternativos de Resolução de Conflitos (MASCs/ADRs)",
        "bank": "Revisão Prova 01",
        "difficulty": "Médio",
        "enunciado": "Dra. Renata atua como mediadora em uma disputa de inventário entre irmãos com relações familiares profundamente abaladas. Durante a sessão, Dra. Renata percebe que as partes estão em impasse sobre a partilha de uma fazenda. Nos termos do artigo 165, § 3º, do CPC e do texto de revisão, qual deve ser a conduta e o papel de Dra. Renata como mediadora?",
        "options": {
            "A": "Atuar como facilitadora da comunicação, auxiliando os irmãos a restabelecer o diálogo para que eles próprios construam a solução, sendo-lhe expressamente vedado sugerir propostas ou interferir no mérito.",
            "B": "Apresentar imediatamente um plano obrigatório de partilha de bens elaborado por ela própria e intimar as partes a cumpri-lo em cinco dias.",
            "C": "Impor sanção de perda do quinhão hereditário ao irmão que demonstrar menor disposição para concessões patrimoniais.",
            "D": "Assumir a função de árbitra privada e proferir sentença arbitral sem o consentimento prévio dos herdeiros."
        },
        "gabarito": "A",
        "article": "Art. 165, § 3º do CPC/2015",
        "legal_basis": "Na mediação (preferencial quando há vínculo prévio continuado), o mediador atua como facilitador da comunicação para que as partes construam a solução, sendo expressamente vedado sugerir propostas ou interferir no mérito.",
        "explanation": "Diferença crucial: ao mediador é terminantemente proibido propor soluções (art. 165, § 3º CPC); sua missão é facilitar o diálogo das partes."
    },
    {
        "id": "multi_05_b_conciliacao_propositivo",
        "subject": "Métodos Alternativos de Resolução de Conflitos (MASCs/ADRs)",
        "bank": "Revisão Prova 01",
        "difficulty": "Médio",
        "enunciado": "Rodrigo colidiu seu carro na traseira do veículo de Patrícia em um cruzamento urbano. Nunca haviam se visto antes e não possuem qualquer relação anterior. No CEJUSC, o conciliador Dr. Thiago atua na sessão. À luz do artigo 165, § 2º, do CPC e da teoria multiportas, como deve se dar a atuação de Dr. Thiago na conciliação?",
        "options": {
            "A": "Por se tratar de controvérsia circunstancial e desprovida de laço anterior duradouro, o conciliador pode atuar de forma mais propositiva, sugerindo alternativas factíveis para o acordo, sem criar constrangimento ou coação.",
            "B": "O conciliador deve manter silêncio absoluto durante todo o ato, sendo proibido de fazer qualquer manifestação oral perante as partes.",
            "C": "Dr. Thiago deve julgar o mérito da culpa no acidente de trânsito e expedir ordem judicial de penhora de bens do condutor culpado.",
            "D": "A conciliação é expressamente vedada em acidentes automobilísticos, cabendo unicamente a autotutela material imediata dos condutores."
        },
        "gabarito": "A",
        "article": "Art. 165, § 2º do CPC/2015",
        "legal_basis": "A conciliação destina-se a controvérsias circunstanciais sem vínculo duradouro; o conciliador pode atuar de forma propositiva, sugerindo alternativas, sem constrangimento ou coação.",
        "explanation": "Na conciliação, em litígios pontuais (como consumo e trânsito), o facilitador pode sugerir opções viáveis para o consenso."
    },
    {
        "id": "multi_05_c_negociacao_direta",
        "subject": "Métodos Alternativos de Resolução de Conflitos (MASCs/ADRs)",
        "bank": "Revisão Prova 01",
        "difficulty": "Fácil",
        "enunciado": "A respeito da negociação como método de solução de disputas, é correto afirmar que sua característica precípua reside no fato de que:",
        "options": {
            "A": "Se desenvolve de modo direto entre os próprios interessados, prescindindo de condutor neutro ou intervenção de terceiro.",
            "B": "Exige compulsoriamente a presença de um árbitro togado para validar as tratativas preliminares das partes.",
            "C": "Só pode ser realizada após a prolação de sentença judicial condenatória em segundo grau de jurisdição.",
            "D": "Constitui forma de heterocomposição estatal vinculante regida pelas normas da corregedoria de justiça."
        },
        "gabarito": "A",
        "article": "Negociação Direta (Teoria dos MASCs)",
        "legal_basis": "A negociação se desenvolve de modo direto entre os interessados, prescindindo de condutor neutro.",
        "explanation": "Na negociação, não há terceiro interveniente; as partes comunicam-se e transacionam diretamente."
    },
    {
        "id": "multi_05_d_arbitragem_autoridade_sentenca",
        "subject": "Métodos Alternativos de Resolução de Conflitos (MASCs/ADRs)",
        "bank": "Revisão Prova 01",
        "difficulty": "Médio",
        "enunciado": "Duas grandes companhias de aviação comercial inseriram cláusula compromissória arbitral para dirimir dúvidas sobre o contrato de leasing de turbinas. Iniciado o procedimento, o árbitro Dr. Henrique conduz o ato. Qual a natureza da arbitragem e a autoridade atribuída a Dr. Henrique no desfecho da lide?",
        "options": {
            "A": "Possui natureza heterocompositiva privada sobre direitos patrimoniais disponíveis; o árbitro atua investido de autoridade de fato e de direito e profere sentença arbitral definitiva com eficácia executiva judicial.",
            "B": "Possui natureza autocompositiva direta, cabendo ao árbitro apenas estimular o diálogo, dependendo sua decisão de homologação judicial obrigatória para ter qualquer validade.",
            "C": "Possui natureza de autotutela administrativa, permitindo ao árbitro expropriar bens da companhia aérea sem previsão legal ou contratual.",
            "D": "A arbitragem é ato meramente consultivo e opinativo, não produzindo título executivo nem impedindo rediscussão do mérito pelo juiz togado."
        },
        "gabarito": "A",
        "article": "Lei nº 9.307/1996 (arts. 18 e 31) e Art. 515, VII do CPC",
        "legal_basis": "A arbitragem é heterocomposição privada sobre direitos patrimoniais disponíveis. O árbitro é juiz de fato e de direito e sua sentença tem eficácia de título executivo judicial.",
        "explanation": "O árbitro profere sentença arbitral definitiva, dotada de força de título executivo judicial, dispensando homologação pelo Poder Judiciário."
    },

    # -------------------------------------------------------------
    # TEMA 06: Formas de Autocomposição e Fundamentos
    # -------------------------------------------------------------
    {
        "id": "multi_06_a_participacao_terceiros_direta_indireta",
        "subject": "Formas de Autocomposição e Fundamentos",
        "bank": "Revisão Prova 01",
        "difficulty": "Fácil",
        "enunciado": "Sob o prisma da participação de terceiros na facilitação do ato, a autocomposição divide-se e classifica-se em:",
        "options": {
            "A": "Direta, quando realizada sem intermediários, mediante negociação entre as próprias partes; ou indireta, quando conduzida com a assistência de um mediador ou conciliador.",
            "B": "Judicial coativa ou extrajudicial compulsória, dependendo da aplicação imediata de prisão civil aos participantes.",
            "C": "Heterocompositiva voluntária ou autotutelada coercitiva, a depender da presença de oficiais de justiça na sala de reunião.",
            "D": "Primária estatal ou secundária administrativa, sendo vedada a participação de particulares na autocomposição indireta."
        },
        "gabarito": "A",
        "article": "Classificação da Autocomposição (Direta vs. Indireta)",
        "legal_basis": "Quanto ao modo de condução: direta (sem intermediários, por negociação) ou indireta (conduzida por mediador ou conciliador).",
        "explanation": "A presença ou não do terceiro facilitador define se a autocomposição é direta (negociação pura) ou indireta (mediação/conciliação)."
    },
    {
        "id": "multi_06_b_art487_iii_cpc_modalidades",
        "subject": "Formas de Autocomposição e Fundamentos",
        "bank": "Revisão Prova 01",
        "difficulty": "Médio",
        "enunciado": "No tocante à manifestação de vontade perante o objeto do litígio, o Código de Processo Civil prevê expressamente no artigo 487, inciso III, as formas de autocomposição que geram extinção do processo com resolução de mérito. São elas:",
        "options": {
            "A": "A transação (concessões recíprocas), a renúncia à pretensão formulada na ação (o autor abre mão voluntariamente do direito) e o reconhecimento da procedência do pedido (o réu aceita a pretensão).",
            "B": "A desistência da ação, o abandono da causa pelo autor e a convenção de arbitragem sem resolução de mérito.",
            "C": "A perempção, a litispendência e a coisa julgada material proferida em juízo togado de forma impositiva.",
            "D": "O compromisso arbitral forçado, o laudo pericial compulsório e a revelia com aplicação de confissão ficta."
        },
        "gabarito": "A",
        "article": "Art. 487, III, alíneas 'a', 'b' e 'c' do CPC/2015",
        "legal_basis": "O art. 487, III do CPC prevê a resolução de mérito quando o juiz: a) homologar o reconhecimento da procedência do pedido; b) homologar a transação; c) homologar a renúncia à pretensão formulada.",
        "explanation": "As três formas materiais de autocomposição com resolução de mérito são: transação, renúncia à pretensão e reconhecimento da procedência do pedido."
    },
    {
        "id": "multi_06_c_transacao_concessoes_reciprocas",
        "subject": "Formas de Autocomposição e Fundamentos",
        "bank": "Revisão Prova 01",
        "difficulty": "Médio",
        "enunciado": "Em ação de cobrança de R$ 100.000,00 movida por Lucas contra Mateus, as partes acordam que Mateus pagará R$ 60.000,00 à vista e Lucas dará plena e geral quitação, abrindo mão do restante da quantia e dos juros de mora. Sob o ponto de vista da teoria dos atos de disposição autocompositiva, esse negócio jurídico configura:",
        "options": {
            "A": "Transação, consubstanciada no negócio jurídico bilateral em que ambos os litigantes fazem concessões recíprocas para extinguir a incerteza e pôr fim ao conflito.",
            "B": "Reconhecimento da procedência do pedido, visto que Lucas concordou em receber valor menor do que o exigido na petição inicial.",
            "C": "Renúncia da pretensão praticada exclusivamente por Mateus em benefício integral de Lucas.",
            "D": "Autotutela moderada judicialmente autorizada pela tabela de custas processuais do tribunal."
        },
        "gabarito": "A",
        "article": "Art. 840 do Código Civil e Art. 487, III, 'b' do CPC",
        "legal_basis": "A transação opera quando os sujeitos fazem concessões recíprocas para pôr fim à controvérsia.",
        "explanation": "Houve concessões mútuas: Lucas abriu mão de parte do crédito e Mateus concordou em pagar prontamente sem protelar."
    },
    {
        "id": "multi_06_d_renuncia_vs_reconhecimento",
        "subject": "Formas de Autocomposição e Fundamentos",
        "bank": "Revisão Prova 01",
        "difficulty": "Médio",
        "enunciado": "Gabriel ingressou com ação reivindicatória contra Daniela. Durante o processo, Daniela apresenta manifestação expressa nos autos admitindo que o imóvel pertence com exclusividade a Gabriel e que desocupará o bem sem opor resistência. Esse ato unilateral de autocomposição praticado pelo polo passivo denomina-se:",
        "options": {
            "A": "Reconhecimento da procedência do pedido, ato pelo qual o réu aceita integralmente a pretensão formulada pelo autor, resolvendo o mérito nos moldes do art. 487, III, 'a', do CPC.",
            "B": "Renúncia à pretensão formulada na ação, ato privativo do polo ativo em que o autor desiste voluntariamente do direito.",
            "C": "Desistência unilateral da contestação, mantendo incerto o mérito da causa para julgamento futuro em ação rescisória.",
            "D": "Transação fática extrajudicial preliminar desprovida de homologação judicial pelo magistrado togado."
        },
        "gabarito": "A",
        "article": "Art. 487, III, 'a' do CPC/2015",
        "legal_basis": "O reconhecimento da procedência do pedido é o ato autocompositivo unilateral do réu, que se submete e aceita a pretensão articulada pelo autor.",
        "explanation": "Quando o polo passivo aceita integralmente a procedência do pedido do autor, opera-se o reconhecimento da pretensão (art. 487, III, 'a' CPC)."
    },

    # -------------------------------------------------------------
    # TEMA 07: Formas de Heterocomposição e Fundamentos
    # -------------------------------------------------------------
    {
        "id": "multi_07_a_modalidades_hetero",
        "subject": "Formas de Heterocomposição e Fundamentos",
        "bank": "Revisão Prova 01",
        "difficulty": "Fácil",
        "enunciado": "A heterocomposição ocorre quando as partes transferem a faculdade de decidir a uma terceira pessoa estranha ao conflito. Quais são as duas modalidades de heterocomposição admitidas no ordenamento jurídico brasileiro?",
        "options": {
            "A": "A jurisdição estatal e a arbitragem privada.",
            "B": "A mediação judicial e a negociação assistida.",
            "C": "O desforço possessório e o direito de retenção de bens.",
            "D": "A transação extrajudicial e a renúncia unilateral ao direito."
        },
        "gabarito": "A",
        "article": "Teoria Geral do Processo (Formas de Heterocomposição)",
        "legal_basis": "A heterocomposição manifesta-se na jurisdição estatal e na arbitragem privada.",
        "explanation": "No direito brasileiro, a faculdade impositiva de decidir por terceiro ocorre na via estatal (juiz) ou arbitral (árbitro)."
    },
    {
        "id": "multi_07_b_jurisdicao_estatal_fundamento",
        "subject": "Formas de Heterocomposição e Fundamentos",
        "bank": "Revisão Prova 01",
        "difficulty": "Médio",
        "enunciado": "A heterocomposição estatal é exercida pelo Poder Judiciário por meio de juízes investidos do poder jurisdicional soberano. Seus fundamentos constitucionais expressos e a eficácia de seu provimento final consubstanciam-se:",
        "options": {
            "A": "Nos artigos 5º, inciso XXXV, e artigo 92 da Constituição Federal, resultando em sentença judicial dotada de coercibilidade e apta a fazer coisa julgada material.",
            "B": "Na autonomia irrestrita da vontade privada, inexistindo coercibilidade ou poder de império por parte do magistrado togado.",
            "C": "No Código Comercial de 1850, que autoriza juízes togados a proferirem pareceres não vinculantes sobre a conduta das partes.",
            "D": "Nas resoluções ministeriais locais, sendo a sentença judicial revogável a qualquer tempo por simples requerimento administrativo do perdedor."
        },
        "gabarito": "A",
        "article": "Art. 5º, XXXV e Art. 92 da CF/88",
        "legal_basis": "A heterocomposição estatal baseia-se nos arts. 5º, XXXV e 92 da CF, culminando em sentença judicial com coercibilidade e aptidão para coisa julgada material.",
        "explanation": "O fundamento é a soberania jurisdicional garantida pela Constituição nos artigos 5º, XXXV e 92 da CF/88."
    },
    {
        "id": "multi_07_c_arbitragem_art31_dispensa",
        "subject": "Formas de Heterocomposição e Fundamentos",
        "bank": "Revisão Prova 01",
        "difficulty": "Médio",
        "enunciado": "Em uma arbitragem societária regida pela Lei nº 9.307/1996, o tribunal arbitral proferiu sentença definitiva condenando um dos sócios ao pagamento de indenização. O sócio vencido alegou em juízo comum que a sentença arbitral não teria eficácia executiva por não ter sido homologada por um juiz togado. À luz do artigo 31 da Lei nº 9.307/1996 e do sistema de heterocomposição arbitral, é correto afirmar que:",
        "options": {
            "A": "A alegação do sócio vencido é incorreta, pois a sentença arbitral produz, entre as partes e seus sucessores, os mesmos efeitos da sentença proferida pelos órgãos do Poder Judiciário e, sendo condenatória, constitui título executivo judicial, dispensando qualquer homologação judicial.",
            "B": "A alegação do sócio é procedente, visto que nenhuma decisão privada possui validade no Brasil sem o visto e a chancela prévia de um juiz de direito estadual.",
            "C": "A sentença arbitral é mero parecer opinativo que se extingue se uma das partes manifestar discordância perante o tribunal de justiça.",
            "D": "A arbitragem brasileira só dispensa homologação judicial quando envolver direitos da personalidade e incapazes sob tutela legal."
        },
        "gabarito": "A",
        "article": "Art. 31 da Lei nº 9.307/1996 e Art. 515, VII do CPC",
        "legal_basis": "A decisão final do árbitro possui força de título executivo judicial e dispensa qualquer homologação do Judiciário, consoante o art. 31 da Lei 9.307/96.",
        "explanation": "A revolução da Lei 9.307/96 foi exatamente equiparar a sentença arbitral à judicial e dispensar homologação pelo Judiciário."
    },
    {
        "id": "multi_07_d_requisito_arbitrabilidade",
        "subject": "Formas de Heterocomposição e Fundamentos",
        "bank": "Revisão Prova 01",
        "difficulty": "Difícil",
        "enunciado": "A heterocomposição arbitral assenta-se na autonomia da vontade das partes, mas sua utilização está condicionada a limites objetivos e subjetivos expressos na Lei nº 9.307/1996. Segundo o artigo 1º desse diploma, a arbitragem somente pode ser validamente convencionada:",
        "options": {
            "A": "Por pessoas capazes de contratar, para dirimir litígios relativos a direitos patrimoniais disponíveis.",
            "B": "Por qualquer cidadão, inclusive para definição de guarda de menores e investigação de crimes contra a vida.",
            "C": "Exclusivamente por empresas públicas federais, sendo vedada a participação de pessoas jurídicas de direito privado.",
            "D": "Apenas quando houver ordem impositiva do juiz togado determinando a renúncia forçada à jurisdição estatal."
        },
        "gabarito": "A",
        "article": "Art. 1º da Lei nº 9.307/1996",
        "legal_basis": "A heterocomposição arbitral ampara-se na autonomia da vontade sobre direitos patrimoniais disponíveis entre sujeitos capazes.",
        "explanation": "A arbitrabilidade objetiva recai estritamente sobre direitos patrimoniais disponíveis de sujeitos capazes."
    },

    # -------------------------------------------------------------
    # TEMA 08: Casos Práticos e Adequação dos Métodos
    # -------------------------------------------------------------
    {
        "id": "multi_08_a_autotutela_desforco_imediato",
        "subject": "Casos Práticos e Adequação dos Métodos (Autotutela, Hetero e Auto)",
        "bank": "Revisão Prova 01",
        "difficulty": "Médio",
        "enunciado": "Ricardo é proprietário de uma chácara de lazer. Ao chegar à sua propriedade no sábado de manhã, surpreende um invasor derrubando a cerca divisória e erguendo um barraco em seu quintal. Utilizando seus próprios funcionários e instrumentos moderados logo após a constatação da invasão, Ricardo repele o invasor e restabelece a cerca. À luz das formas de resolução de conflitos, a conduta de Ricardo configura caso adequado de:",
        "options": {
            "A": "Autotutela lícita, consubstanciada no desforço possessório imediato (incontinenti) para defesa imediata da posse amparado no artigo 1.210, § 1º, do Código Civil.",
            "B": "Heterocomposição estatal indireta, pois os funcionários de Ricardo possuem fé pública delegada pelo Poder Judiciário.",
            "C": "Autocomposição por mediação comunitária informal compulsória.",
            "D": "Exercício arbitrário das próprias razões punível com prisão preventiva imediata, sendo vedado qualquer ato de proteção à posse pelo possuidor."
        },
        "gabarito": "A",
        "article": "Art. 1.210, § 1º do Código Civil",
        "legal_basis": "A autotutela tem aplicação adequada na defesa imediata da posse pelo desforço imediato amparado no art. 1.210, § 1º do Código Civil, com moderação logo após o ocorrido.",
        "explanation": "Exemplo expressamente citado no questionário: desforço imediato na defesa da posse contra invasão, feito com moderação logo após o fato."
    },
    {
        "id": "multi_08_b_hetero_estatal_paternidade_revel",
        "subject": "Casos Práticos e Adequação dos Métodos (Autotutela, Hetero e Auto)",
        "bank": "Revisão Prova 01",
        "difficulty": "Médio",
        "enunciado": "Mariana move ação de investigação de paternidade cumulada com fixação de alimentos em face de Lucas, em benefício de seu filho recém-nascido. Lucas foi citado regularmente, mas quedou-se inerte, tornando-se revel e recusando-se expressamente a comparecer a qualquer audiência ou a submeter-se ao exame de DNA. Diante da indisponibilidade do estado de filiação e da recusa contumaz do réu, o caso concreto exige adequadamente a incidência da:",
        "options": {
            "A": "Heterocomposição estatal, indispensável para que o juiz togado, no exercício da jurisdição soberana, profira sentença declaratória e condenatória com força de coisa julgada.",
            "B": "Heterocomposição arbitral, sendo obrigatória a remessa dos autos a uma câmara arbitral privada internacional.",
            "C": "Autotutela física imediata para coagir o réu a comparecer ao laboratório sob pena de perda de seus bens.",
            "D": "Autocomposição por mediação obrigatória, que não permite ao juiz julgar o processo sem o prévio acordo consensual das partes."
        },
        "gabarito": "A",
        "article": "Heterocomposição Estatal no Direito de Família",
        "legal_basis": "A heterocomposição estatal revela-se indispensável em investigação de paternidade cumulada com alimentos na qual o réu é revel e sem disposição conciliatória.",
        "explanation": "Exemplo do questionário: na revelia e matéria indisponível/ausência de consenso, a via togado estatal é imperativa."
    },
    {
        "id": "multi_08_c_hetero_arbitral_infraestrutura",
        "subject": "Casos Práticos e Adequação dos Métodos (Autotutela, Hetero e Auto)",
        "bank": "Revisão Prova 01",
        "difficulty": "Médio",
        "enunciado": "A Construtora Alfa e o Consórcio Energético Beta firmaram contrato bilionário para construção de uma usina hidrelétrica. Surgiu controvérsia de alta complexidade técnica de engenharia sobre atraso no cronograma de concretagem e aplicação de multas milionárias, havendo cláusulas contratuais de segredo industrial e necessidade imperiosa de sigilo negocial. O método mais adequado para dirimir esse litígio é:",
        "options": {
            "A": "Heterocomposição arbitral, face à complexidade técnica das cláusulas de engenharia, à expertise dos árbitros e à necessidade de sigilo do negócio entre as empresas.",
            "B": "Autotutela das máquinas e canteiro de obras pela construtora mediante confronto físico entre seguranças privados.",
            "C": "Conciliação informal com audiência pública de quinze minutos no juizado especial cível estadual.",
            "D": "Mediação comunitária em praça pública conduzida por associação de moradores do entorno da hidrelétrica."
        },
        "gabarito": "A",
        "article": "Heterocomposição Arbitral (Lei nº 9.307/1996)",
        "legal_basis": "A heterocomposição arbitral é ideal para controvérsia contratual entre grandes empresas por atraso na entrega de obras de infraestrutura, com complexidade técnica e sigilo.",
        "explanation": "Exemplo do questionário: disputas societárias e de engenharia complexa entre grandes empresas encontram na arbitragem agilidade, sigilo e expertise."
    },
    {
        "id": "multi_08_d_auto_mediacao_familia_vs_transito",
        "subject": "Casos Práticos e Adequação dos Métodos (Autotutela, Hetero e Auto)",
        "bank": "Revisão Prova 01",
        "difficulty": "Médio",
        "enunciado": "Analise as duas situações práticas a seguir:\n1. Juliana e Marcelo estão se divorciando após 15 anos de casamento; há severo desgaste emocional e mágoas acumuladas, mas necessitam definir a guarda e a convivência dos dois filhos menores.\n2. André e Beatriz sofreram abalroamento de trânsito em um semáforo; não se conheciam e discutem unicamente o pagamento de R$ 3.500,00 pelo conserto do parachoque.\nÀ luz do questionário de revisão, quais métodos autocompositivos são os mais adequados para a Situação 1 e a Situação 2, respectivamente?",
        "options": {
            "A": "Situação 1: Autocomposição por Mediação (relação continuada e necessidade de restabelecer o diálogo familiar); Situação 2: Autocomposição por Conciliação (relação pontual/circunstancial entre condutores sem vínculo anterior).",
            "B": "Situação 1: Autotutela familiar com desforço físico; Situação 2: Heterocomposição arbitral com câmara de Genebra.",
            "C": "Situação 1: Autocomposição por Conciliação com imposição de propostas; Situação 2: Heterocomposição estatal com prisão civil imediata.",
            "D": "Situação 1: Negociação sem intervenção judicial; Situação 2: Mediação profunda de três anos para investigar a árvore genealógica dos motoristas."
        },
        "gabarito": "A",
        "article": "Critérios de Adequação: Mediação vs. Conciliação (Art. 165 CPC)",
        "legal_basis": "A mediação adequa-se à guarda e convivência de filhos em divórcio litigioso com desgaste emocional severo. A conciliação adequa-se a abalroamento de veículos entre condutores que não se conheciam.",
        "explanation": "São exatamente os dois exemplos de autocomposição formulados no item 08 do questionário."
    },

    # -------------------------------------------------------------
    # TEMA 09: Características: Autocomposição vs. Heterocomposição
    # -------------------------------------------------------------
    {
        "id": "multi_09_a_poder_decisorio_contraponto",
        "subject": "Processos Autocompositivos vs. Heterocompositivos",
        "bank": "Revisão Prova 01",
        "difficulty": "Fácil",
        "enunciado": "Ao comparar os procedimentos autocompositivos e heterocompositivos, o contraponto basilar em relação à titularidade do poder decisório consiste em:",
        "options": {
            "A": "Na autocomposição, o poder decisório permanece retido nas partes, que operam sob a lógica cooperativa; na heterocomposição, o poder de ditar o desfecho é transferido ao juiz ou ao árbitro, que impõe o provimento de fora para dentro.",
            "B": "Na autocomposição, o poder é do conciliador que obriga as partes a assinarem o termo; na heterocomposição, o juiz apenas opina sem poder vinculante.",
            "C": "Em ambos os modelos o poder decisório pertence privativamente ao Ministério Público estadual.",
            "D": "A heterocomposição não admite decisões impositivas, dependendo sempre da concordância unânime de todos os parentes dos litigantes."
        },
        "gabarito": "A",
        "article": "Teoria Geral dos Procedimentos de Solução de Conflitos",
        "legal_basis": "Na autocomposição, o poder decisório permanece nas partes sob lógica cooperativa. Na heterocomposição, é transferido ao terceiro que impõe o desfecho de fora para dentro.",
        "explanation": "Texto exato do questionário: na autocomposição as partes retêm a decisão; na heterocomposição o terceiro impõe de fora para dentro."
    },
    {
        "id": "multi_09_b_logica_vencedor_perdedor",
        "subject": "Processos Autocompositivos vs. Heterocompositivos",
        "bank": "Revisão Prova 01",
        "difficulty": "Médio",
        "enunciado": "No tocante à dinâmica relacional e aos resultados esperados, a heterocomposição assenta-se na lógica adversária clássica de vitória de uma parte e derrota da outra (ganha-perde). Em contrapartida, a autocomposição caracteriza-se pela:",
        "options": {
            "A": "Lógica cooperativa em busca de um consenso mutualmente satisfatório (ganha-ganha), priorizando a preservação da comunicação e o futuro das relações entre os participantes.",
            "B": "Submissão involuntária da parte economicamente mais fraca ao poder bélico da parte mais forte.",
            "C": "Imposição de perda patrimonial integral a ambas as partes pelo mediador judicial.",
            "D": "Necessidade de condenação criminal por perjúrio do polo que manifestar intenção conciliatória prévia."
        },
        "gabarito": "A",
        "article": "Diferenças Estruturais: Auto vs. Heterocomposição",
        "legal_basis": "A autocomposição opera sob a lógica cooperativa e busca o consenso mútuo; a heterocomposição assenta-se na lógica adversária de vencedor e perdedor.",
        "explanation": "Enquanto a heterocomposição polariza o conflito em vitória de um e derrota de outro, a autocomposição busca a satisfação convergente dos interesses."
    },
    {
        "id": "multi_09_c_forma_estrita_vs_flexibilidade",
        "subject": "Processos Autocompositivos vs. Heterocompositivos",
        "bank": "Revisão Prova 01",
        "difficulty": "Médio",
        "enunciado": "Quanto às formalidades procedimentais e ao objeto de análise temporal, assinale a opção que descreve com rigor técnico o contraste entre autocomposição e heterocomposição:",
        "options": {
            "A": "O procedimento autocompositivo é informal e flexível, priorizando a comunicação e o futuro das relações; o processo heterocompositivo submete-se à estrita forma legal, focando em fatos pretéritos, instrução probatória e aplicação cogente da norma.",
            "B": "A autocomposição é rígida e exige prazos preclusivos fatais de vinte e quatro horas; a heterocomposição dispensa qualquer rito processual formal.",
            "C": "A heterocomposição analisa exclusivamente o futuro amoroso das famílias; a autocomposição preocupa-se unicamente em atribuir culpas pretéritas.",
            "D": "Ambos os procedimentos seguem o rito solene do Tribunal do Júri com quesitação obrigatória aos jurados sorteados."
        },
        "gabarito": "A",
        "article": "Procedimentos: Forma e Objeto Temporal",
        "legal_basis": "Autocomposição: informal e flexível, foca na comunicação e no futuro. Heterocomposição: estrita forma legal, foca em fatos pretéritos e aplicação cogente da lei.",
        "explanation": "Contraste nítido do item 09: flexibilidade/futuro vs. estrita forma/fatos pretéritos e instrução probatória."
    },
    {
        "id": "multi_09_d_resumo_principios_opostos",
        "subject": "Processos Autocompositivos vs. Heterocompositivos",
        "bank": "Revisão Prova 01",
        "difficulty": "Difícil",
        "enunciado": "Em síntese doutrinária sobre o contraponto entre os modelos autocompositivo e heterocompositivo, é correto afirmar que:",
        "options": {
            "A": "Eles assentam-se em princípios e dinâmicas procedimentais opostas: enquanto um busca a pacificação pela autonomia e consenso espontâneo, o outro busca a pacificação pela imposição da autoridade e subsunção normativa do passado.",
            "B": "A autocomposição visa exclusivamente substituir as leis substantivas civis pelas decisões unipessoais dos mediadores leigos.",
            "C": "A heterocomposição estatal tornou-se inconstitucional no direito brasileiro após a promulgação da Lei de Mediação em 2015.",
            "D": "Os dois modelos são idênticos em todas as suas fases, possuindo os mesmos ritos, princípios e instrumentos decisórios vinculantes."
        },
        "gabarito": "A",
        "article": "Teoria Geral dos Meios de Resolução de Conflitos",
        "legal_basis": "Os procedimentos autocompositivos e heterocompositivos assentam-se em princípios e dinâmicas procedimentais opostas.",
        "explanation": "Afirmação de abertura da questão 09 do questionário: dinâmica procedimental oposta entre consenso e imposição externa."
    },

    # -------------------------------------------------------------
    # TEMA 10: Princípios, Acesso à Justiça, Celeridade e Efetividade
    # -------------------------------------------------------------
    {
        "id": "multi_10_a_principios_bussola",
        "subject": "Princípios da Resolução de Conflitos e Acesso à Justiça",
        "bank": "Revisão Prova 01",
        "difficulty": "Médio",
        "enunciado": "Os princípios reitores da solução de disputas — a exemplo da confidencialidade, autonomia da vontade, oralidade e cooperação — desempenham papel crucial na ordem jurídica contemporânea, atuando como:",
        "options": {
            "A": "Bússola interpretativa para aplicar o direito processual e integrar lacunas do sistema jurídico na busca pela pacificação.",
            "B": "Meras recomendações morais desprovidas de qualquer força normativa ou utilidade prática no processo civil.",
            "C": "Instrumentos para impedir que o cidadão tenha assistência jurídica de advogados e defensores públicos.",
            "D": "Justificativa legal para a quebra de sigilo fiscal e bancário de todos os envolvidos em conciliação cível."
        },
        "gabarito": "A",
        "article": "Art. 166 do CPC/2015 e Teoria Geral dos Princípios",
        "legal_basis": "Os princípios reitores da solução de disputas atuam como bússola interpretativa para aplicar o direito processual e integrar lacunas do sistema.",
        "explanation": "Texto da questão 10: atuam como bússola interpretativa e integrativa para aplicação das normas e colmatação de lacunas."
    },
    {
        "id": "multi_10_b_acesso_justica_ordem_justa",
        "subject": "Princípios da Resolução de Conflitos e Acesso à Justiça",
        "bank": "Revisão Prova 01",
        "difficulty": "Fácil",
        "enunciado": "Sob a ótica do modelo multiportas e da moderna teoria processual, o princípio constitucional do acesso à justiça (art. 5º, XXXV, CF) é ressignificado, deixando de ser compreendido como mero direito formal de provocar a máquina judiciária para significar:",
        "options": {
            "A": "O acesso à ordem jurídica justa, incumbindo ao Estado oferecer o mecanismo mais apropriado à pacificação do caso concreto.",
            "B": "A obrigatoriedade de obter uma sentença meritória condenatória proferida por juiz togado em todos os conflitos da sociedade.",
            "C": "O encerramento do protocolo de petições nas varas cíveis para impor a arbitragem internacional compulsória.",
            "D": "O acesso gratuito e ilimitado a recursos judiciais extraordinários perante os tribunais superiores sem pagamento de preparo."
        },
        "gabarito": "A",
        "article": "Art. 5º, XXXV da CF/88 e Doutrina de Acesso à Ordem Jurídica Justa",
        "legal_basis": "O acesso à justiça deixa de ser compreendido como mero direito formal de provocar a máquina judiciária e passa a significar o acesso à ordem jurídica justa, incumbindo ao Estado oferecer o mecanismo mais apropriado.",
        "explanation": "Definição literal do questionário: acesso à ordem jurídica justa mediante o método mais adequado a cada situação."
    },
    {
        "id": "multi_10_c_celeridade_efetividade_cumprimento",
        "subject": "Princípios da Resolução de Conflitos e Acesso à Justiça",
        "bank": "Revisão Prova 01",
        "difficulty": "Médio",
        "enunciado": "Como os princípios da celeridade processual e da efetividade da prestação jurisdicional encontram pleno cumprimento na atuação consensual e arbitral segundo o questionário de revisão?",
        "options": {
            "A": "A simplificação do procedimento encurta o tempo de desfecho da lide e os acordos construídos pelas próprias partes possuem índices mínimos de descumprimento, desonerando a fase executiva.",
            "B": "Pela eliminação de todas as garantias do contraditório e da ampla defesa, proferindo-se sentenças sem ouvir os réus.",
            "C": "Pelo aumento do número de recursos judiciais cabíveis contra qualquer manifestação dos mediadores em audiência.",
            "D": "Pela transferência da cobrança de honorários advocatícios para os cartórios de protesto de títulos de crédito."
        },
        "gabarito": "A",
        "article": "Celeridade e Efetividade Jurisdicional nos Métodos Adequados",
        "legal_basis": "A celeridade e efetividade realizam-se porque a simplificação procedimental encurta o tempo e os acordos construídos pelas próprias partes têm índice mínimo de descumprimento, desonerando a execução.",
        "explanation": "Quando as partes constroem o acordo, o cumprimento espontâneo é altíssimo, evitando anos de execução forçada."
    },
    {
        "id": "multi_10_d_confidencialidade_autonomia_integracao",
        "subject": "Princípios da Resolução de Conflitos e Acesso à Justiça",
        "bank": "Revisão Prova 01",
        "difficulty": "Médio",
        "enunciado": "Durante uma sessão de mediação judicial entre dois sócios de uma clínica médica, foram discutidas informações estratégicas sobre faturamento e proposta de aquisição de cotas. Posteriormente, não havendo acordo, um dos sócios requereu que o mediador prestasse depoimento como testemunha em juízo para relatar as propostas da outra parte. À luz do princípio da confidencialidade (art. 166 do CPC), o juiz deve:",
        "options": {
            "A": "Indeferir o depoimento do mediador, haja vista que as informações reveladas na sessão autocompositiva são estritamente confidenciais e não podem ser utilizadas como prova no processo.",
            "B": "Determinar que o mediador junte cópia de todas as anotações sob pena de prisão em flagrante por desobediência.",
            "C": "Anular a sessão de mediação e julgar antecipadamente a lide em favor do sócio que requereu a prova testemunhal.",
            "D": "Autorizar a quebra de sigilo por se tratar de direito patrimonial societário com fins lucrativos privados."
        },
        "gabarito": "A",
        "article": "Art. 166, §§ 1º e 2º do CPC/2015",
        "legal_basis": "O princípio da confidencialidade protege as informações prestadas durante a mediação, sendo vedado ao mediador depor como testemunha ou divulgar o teor das tratativas.",
        "explanation": "A confidencialidade é garantia estrutural dos métodos consensuais para assegurar que as partes negociem sem medo de prejuízo futuro."
    },

    # -------------------------------------------------------------
    # TEMA 11: Evolução Histórica dos Métodos Consensuais
    # -------------------------------------------------------------
    {
        "id": "multi_11_a_conferencia_pound_1976",
        "subject": "Evolução Histórica dos Métodos Consensuais",
        "bank": "Revisão Prova 01",
        "difficulty": "Médio",
        "enunciado": "No cenário internacional, a crise do modelo tradicional de jurisdição contenciosa culminou no surgimento do movimento ADR (Alternative Dispute Resolution) nos Estados Unidos durante a década de 1970. O divisor de águas histórico e ponto de virada desse movimento foi:",
        "options": {
            "A": "A Conferência Pound, realizada em 1976, na qual se discutiu a insatisfação popular com a administração da justiça e se lançaram as bases do modelo multiportas.",
            "B": "A Convenção de Viena de 1969, que proibiu os tribunais estatais de julgarem controvérsias comerciais privadas.",
            "C": "O julgamento do caso Marbury v. Madison pela Suprema Corte norte-americana no início do século XIX.",
            "D": "A edição do Código de Hamurabi na Babilônia antiga consagrando a conciliação comercial obrigatória."
        },
        "gabarito": "A",
        "article": "Evolução Histórica das ADRs (Conferência Pound de 1976)",
        "legal_basis": "No cenário internacional, a crise do modelo tradicional culminou no movimento ADR nos EUA nos anos 1970, cujo ponto de virada foi a Conferência Pound de 1976.",
        "explanation": "A Conferência Pound de 1976 é mundialmente consagrada como o marco de nascimento do movimento ADR e do modelo multiportas."
    },
    {
        "id": "multi_11_b_constituicao_imperio_1824",
        "subject": "Evolução Histórica dos Métodos Consensuais",
        "bank": "Revisão Prova 01",
        "difficulty": "Médio",
        "enunciado": "No Brasil, a conciliação possui raízes constitucionais profundas. Na história do direito pátrio, qual diploma fundamental já previa a tentativa de conciliação como etapa obrigatória antes de se litigar em juízo contencioso?",
        "options": {
            "A": "A Constituição do Império de 1824, em seus artigos 161 e 162, estabelecendo que nenhuma ação começaria sem que se tentasse a reconciliação perante o juiz de paz.",
            "B": "A Constituição da República de 1891, que proibiu qualquer intervenção estatal nos conflitos de particulares.",
            "C": "O Código Civil de 1916, que vedou a conciliação prévia em virtude do princípio da imutabilidade processual.",
            "D": "O Código de Processo Penal de 1941, que estendeu a conciliação forçada a todos os crimes dolosos contra a vida."
        },
        "gabarito": "A",
        "article": "Constituição Imperial de 1824 (arts. 161 e 162)",
        "legal_basis": "No Brasil, a conciliação estava prevista na Constituição do Império de 1824 como etapa obrigatória antes de se litigar em juízo.",
        "explanation": "O texto da questão 11 destaca expressamente a Constituição do Império de 1824 como antecedente histórico fundamental."
    },
    {
        "id": "multi_11_c_cultura_demandista_reversao",
        "subject": "Evolução Histórica dos Métodos Consensuais",
        "bank": "Revisão Prova 01",
        "difficulty": "Médio",
        "enunciado": "Apesar dos antecedentes históricos favoráveis, o século XX no Brasil assistiu ao enraizamento de uma cultura fortemente demandista e litigiosa. A reversão prática dessa tendência teve início a partir:",
        "options": {
            "A": "Da década de 1990, com as leis de Juizados Especiais (Lei nº 9.099/1995) e de Arbitragem (Lei nº 9.307/1996), culminando na unificação principiológica advinda da Resolução nº 125/2010 do CNJ e do CPC/2015.",
            "B": "Da proclamação da República, que fechou os tribunais estaduais de primeira instância até a década de 1970.",
            "C": "Da edição da Lei de Segurança Nacional durante o regime militar, que proibiu os juízes de proferirem sentenças cíveis.",
            "D": "Da criação do Supremo Tribunal Federal pelo Tratado de Tordesilhas no século XV."
        },
        "gabarito": "A",
        "article": "Histórico Brasileiro: Anos 1990 e Virada Paradigmática",
        "legal_basis": "A reversão da cultura demandista iniciou-se na década de 1990 com as leis de Juizados e Arbitragem, culminando na Resolução 125/2010 do CNJ e no CPC/2015.",
        "explanation": "A virada legislativa consolidou-se na década de 1990 e alcançou maturidade com o CNJ e o CPC/2015."
    },
    {
        "id": "multi_11_d_crise_monopolio_sobrecarga",
        "subject": "Evolução Histórica dos Métodos Consensuais",
        "bank": "Revisão Prova 01",
        "difficulty": "Fácil",
        "enunciado": "A principal razão histórica que motivou a eclosão do movimento pelas vias consensuais e alternativas de resolução de litígios no mundo e no Brasil foi:",
        "options": {
            "A": "A sobrecarga generalizada da jurisdição contenciosa após a substituição histórica da autotutela pelo monopólio judiciário dos Estados modernos.",
            "B": "A extinção definitiva das faculdades de direito e a carência de magistrados em escala planetária.",
            "C": "O desinteresse da sociedade civil pelo direito à ampla defesa e ao contraditório nos processos formais.",
            "D": "A proibição internacional do comércio eletrônico e das transações bancárias virtuais."
        },
        "gabarito": "A",
        "article": "Crise da Jurisdição Estatal e Movimento ADR",
        "legal_basis": "Após a substituição histórica da autotutela pelo monopólio judiciário promovido pelos Estados modernos, a jurisdição contenciosa passou a apresentar sobrecarga generalizada.",
        "explanation": "A sobrecarga generalizada do Judiciário e a morosidade da jurisdição contenciosa deflagraram a busca por vias adequadas."
    },

    # -------------------------------------------------------------
    # TEMA 12: Objetivos do Modelo Multiportas
    # -------------------------------------------------------------
    {
        "id": "multi_12_a_frank_sander_origem",
        "subject": "Objetivos do Modelo Multiportas",
        "bank": "Revisão Prova 01",
        "difficulty": "Fácil",
        "enunciado": "O modelo multiportas (Multi-door Courthouse System) foi idealizado por qual jurista e em qual contexto acadêmico internacional?",
        "options": {
            "A": "Por Frank Sander, professor da Universidade de Harvard, durante a Conferência Pound de 1976.",
            "B": "Por Francesco Carnelutti, na Universidade de Roma, durante a redação do Código de Processo Civil Italiano de 1940.",
            "C": "Por Hans Kelsen, no Tribunal Constitucional da Áustria, em 1920.",
            "D": "Por Pontes de Miranda, no Supremo Tribunal Federal do Brasil, na década de 1950."
        },
        "gabarito": "A",
        "article": "Histórico do Multi-door Courthouse (Frank Sander / 1976)",
        "legal_basis": "Idealizado por Frank Sander na Conferência Pound de 1976, o modelo multiportas visa estruturar o fórum como um centro de resolução com múltiplas portas de encaminhamento.",
        "explanation": "Frank Sander na Conferência Pound de 1976 é a referência nominal e histórica obrigatória do Modelo Multiportas."
    },
    {
        "id": "multi_12_b_conceito_centro_resolucao",
        "subject": "Objetivos do Modelo Multiportas",
        "bank": "Revisão Prova 01",
        "difficulty": "Médio",
        "enunciado": "A metáfora do 'Tribunal Multiportas' concebida por Frank Sander propõe uma alteração estrutural no papel do Poder Judiciário. Essa proposta consiste em estruturar o fórum não como:",
        "options": {
            "A": "Um tribunal de porta única para o processo judicial formal, mas como um centro de resolução com múltiplas alternativas de encaminhamento de controvérsias.",
            "B": "Um local de atendimento médico de emergência para as vítimas de acidentes automobilísticos urbanos.",
            "C": "Uma repartição arrecadadora de tributos fiscais para custeio do funcionalismo público federal.",
            "D": "Um centro de triagem de processos com envio compulsório de todos os cidadãos à penitenciária pública."
        },
        "gabarito": "A",
        "article": "Conceito de Tribunal Multiportas (Frank Sander)",
        "legal_basis": "O modelo visa estruturar o fórum não como um tribunal de porta única para o processo judicial formal, mas como um centro de resolução com múltiplas alternativas de encaminhamento.",
        "explanation": "Supera-se o tribunal de porta única (sentença formal) para oferecer múltiplas portas de tratamento qualificado."
    },
    {
        "id": "multi_12_c_quatro_objetivos_basilares",
        "subject": "Objetivos do Modelo Multiportas",
        "bank": "Revisão Prova 01",
        "difficulty": "Médio",
        "enunciado": "De acordo com o questionário de revisão para a prova, os objetivos basilares do modelo multiportas consistem em:",
        "options": {
            "A": "1) Garantir adequação procedimental; 2) Restaurar o protagonismo dos cidadãos; 3) Desafogar a sobrecarga do Judiciário; 4) Assegurar a pacificação material do conflito, superando a mera extinção formal.",
            "B": "1) Privatizar os fóruns estaduais; 2) Extinguir os honorários advocatícios; 3) Aumentar as custas judiciais; 4) Suprimir o contraditório.",
            "C": "1) Proibir a atuação de juízes togados; 2) Tornar a mediação compulsória para crimes hediondos; 3) Revogar o CPC/2015; 4) Incentivar a autotutela armada.",
            "D": "1) Manter o foco exclusivo na sentença estatal; 2) Retirar das partes o poder decisório; 3) Ampliar os recursos processuais; 4) Congelar pautas de audiência."
        },
        "gabarito": "A",
        "article": "Objetivos Centrais do Modelo Multiportas",
        "legal_basis": "Objetivos: garantir adequação procedimental, restaurar o protagonismo dos cidadãos, desafogar a sobrecarga de demandas do Judiciário e assegurar pacificação material.",
        "explanation": "Os quatro objetivos essenciais explicados no texto da questão 12 do questionário."
    },
    {
        "id": "multi_12_d_adequacao_protagonismo",
        "subject": "Objetivos do Modelo Multiportas",
        "bank": "Revisão Prova 01",
        "difficulty": "Médio",
        "enunciado": "No modelo multiportas, a 'adequação procedimental' significa que o sistema de justiça deve:",
        "options": {
            "A": "Destinar cada litígio concreto ao meio condizente com a sua natureza e com o tipo de relação existente entre as partes (ex: mediação para famílias e arbitragem para complexidade empresarial).",
            "B": "Uniformizar todos os procedimentos num rito único e inflexível, aplicando rigorosamente as mesmas regras probatórias para todas as causas.",
            "C": "Obrigar os litigantes a desistirem de suas ações patrimoniais sob pena de litigância de má-fé.",
            "D": "Encaminhar todos os processos cíveis diretamente ao Supremo Tribunal Federal em grau de recurso de ofício."
        },
        "gabarito": "A",
        "article": "Adequação Procedimental no Sistema Multiportas",
        "legal_basis": "Adequação procedimental consiste em destinar cada litígio ao meio condizente com a sua natureza e com a relação das partes.",
        "explanation": "A premissa da adequação (Fitting the Forum to the Fuss) é conectar a disputa à porta metodológica correta."
    },

    # -------------------------------------------------------------
    # TEMA 13: Evolução Histórica e Legislativa dos Juizados Especiais
    # -------------------------------------------------------------
    {
        "id": "multi_13_a_origem_rs_pequenas_causas",
        "subject": "Evolução Histórica e Legislativa dos Juizados Especiais",
        "bank": "Revisão Prova 01",
        "difficulty": "Médio",
        "enunciado": "O surgimento prático dos Juizados Especiais no Brasil remonta às experiências pioneiras ocorridas no início da década de 1980. Qual foi o marco empírico originário dessa trajetória e sua inspiração internacional?",
        "options": {
            "A": "Os Juizados Informais de Conciliação criados no Rio Grande do Sul no início dos anos 1980, inspirados nos tribunais de pequenas causas (Small Claims Courts) norte-americanos, que culminaram na Lei nº 7.244/1984.",
            "B": "A criação dos tribunais feudais ingleses no século XII durante o reinado do Rei João Sem Terra.",
            "C": "A Lei das Doze Tábuas em Roma, que instituiu a conciliação cartorária nos litígios entre patrícios e plebeus.",
            "D": "O Código Civil Francês de Napoleão Bonaparte de 1804, que aboliu os tribunais de primeira instância na Europa."
        },
        "gabarito": "A",
        "article": "Juizados Especiais - Origem no RS e Lei nº 7.244/1984",
        "legal_basis": "O surgimento remonta aos Juizados Informais de Conciliação no RS no início dos anos 80, inspirados nas pequenas causas dos EUA, culminando na Lei 7.244/1984.",
        "explanation": "A experiência empírica dos Juizados Informais de Conciliação do Rio Grande do Sul gerou a Lei 7.244/84 e a inclusão no art. 98, I da CF/88."
    },
    {
        "id": "multi_13_b_principios_norteadores_lei9099",
        "subject": "Evolução Histórica e Legislativa dos Juizados Especiais",
        "bank": "Revisão Prova 01",
        "difficulty": "Fácil",
        "enunciado": "A concretização definitiva dos Juizados Especiais Cíveis e Criminais em âmbito estadual ocorreu com a Lei nº 9.099/1995. Quais são os princípios expressos no artigo 2º desse diploma que orientam todo o procedimento?",
        "options": {
            "A": "Simplicidade, oralidade, informalidade, economia processual e celeridade.",
            "B": "Rigor formal, solenidade cartorária, sigilo obrigatório, onerosidade e presunção de culpa.",
            "C": "Taxatividade recursal, colegialidade plena, litisconsórcio passivo universal e lentidão moderada.",
            "D": "Autotutela punitiva, segredo de justiça absoluto, preclusão formal imediata e mediação internacional."
        },
        "gabarito": "A",
        "article": "Art. 2º da Lei nº 9.099/1995",
        "legal_basis": "A Lei nº 9.099/1995 é orientada pelos princípios da simplicidade, oralidade, informalidade, economia processual e celeridade.",
        "explanation": "O quinteto principiológico básico do art. 2º da Lei 9.099/95: oralidade, simplicidade, informalidade, economia processual e celeridade."
    },
    {
        "id": "multi_13_c_juizes_togados_leigos_constituicao",
        "subject": "Evolução Histórica e Legislativa dos Juizados Especiais",
        "bank": "Revisão Prova 01",
        "difficulty": "Médio",
        "enunciado": "O artigo 98, inciso I, da Constituição Federal de 1988 inovou na organização judiciária brasileira ao dispor que os Juizados Especiais serão providos por:",
        "options": {
            "A": "Juízes togados, ou togados e leigos, competentes para a conciliação, o julgamento e a execução de causas cíveis de menor complexidade e infrações penais de menor potencial ofensivo.",
            "B": "Apenas juízes leigos voluntários, sendo terminantemente proibida a intervenção de magistrados togados de carreira.",
            "C": "Oficiais do exército nacional investidos de poder de polícia civil judiciária.",
            "D": "Árbitros privados contratados pelas partes para atuar exclusivamente mediante pagamento antecipado de custas."
        },
        "gabarito": "A",
        "article": "Art. 98, I da Constituição Federal de 1988",
        "legal_basis": "A CF/88 determinou a instituição de juizados providos por juízes togados ou togados e leigos para conciliação e julgamento de causas cíveis de menor complexidade e infrações de menor potencial ofensivo.",
        "explanation": "Previsão expressa do art. 98, I da Carta Maior, combinando juízes togados e juízes leigos/conciliadores."
    },
    {
        "id": "multi_13_d_consolidacao_federal_fazenda",
        "subject": "Evolução Histórica e Legislativa dos Juizados Especiais",
        "bank": "Revisão Prova 01",
        "difficulty": "Médio",
        "enunciado": "Após a consolidação dos Juizados Especiais estaduais pela Lei nº 9.099/1995, o microssistema dos juizados foi ampliado no Brasil para abranger demandas contra entes públicos federais, estaduais e municipais por meio da edição de quais diplomas legais?",
        "options": {
            "A": "Lei nº 10.259/2001 (Juizados Especiais Federais) e Lei nº 12.153/2009 (Juizados Especiais da Fazenda Pública).",
            "B": "Código Comercial de 1850 e Lei de Falências de 1945.",
            "C": "Lei do Mandado de Segurança de 2009 e Consolidação das Leis do Trabalho de 1943.",
            "D": "Estatuto do Desarmamento e Lei de Responsabilidade Fiscal de 2000."
        },
        "gabarito": "A",
        "article": "Leis nº 10.259/2001 e nº 12.153/2009",
        "legal_basis": "Posteriormente, o microssistema foi consolidado com a edição da Lei nº 10.259/2001 para a Justiça Federal e da Lei nº 12.153/2009 para os Juizados da Fazenda Pública.",
        "explanation": "O microssistema dos Juizados Especiais se compõe da Lei 9.099/95, Lei 10.259/01 (Federal) e Lei 12.153/09 (Fazenda Pública)."
    },

    # -------------------------------------------------------------
    # TEMA 14: Evolução Histórica e Legislativa da Arbitragem no Brasil
    # -------------------------------------------------------------
    {
        "id": "multi_14_a_inoperancia_cc1916_cpc1973",
        "subject": "Evolução Histórica e Legislativa da Arbitragem no Brasil",
        "bank": "Revisão Prova 01",
        "difficulty": "Médio",
        "enunciado": "A arbitragem sempre teve raízes no direito brasileiro, constando das Ordenações Filipinas e da Constituição Imperial de 1824. Contudo, sob a vigência do Código Civil de 1916 e do Código de Processo Civil de 1973, o instituto revelou-se praticamente inoperante na prática brasileira. Quais eram os dois entraves técnicos que causavam essa inoperância?",
        "options": {
            "A": "A decisão do árbitro dependia de posterior homologação judicial para produzir efeitos (laudo homologando) e a cláusula compromissória era considerada mero pré-contrato sem força executiva imediata.",
            "B": "A arbitragem exigia autorização prévia por referendo popular e as custas eram repassadas integralmente ao Ministério Público.",
            "C": "A lei impunha pena de prisão civil imediata a qualquer cidadão que contratasse câmara arbitral privada.",
            "D": "O tribunal arbitral só podia julgar controvérsias criminais e desapropriações de terras indígenas."
        },
        "gabarito": "A",
        "article": "Histórico da Arbitragem no Brasil (CC/1916 e CPC/1973)",
        "legal_basis": "Sob o CC/16 e CPC/73, a arbitragem era inoperante porque a decisão do árbitro dependia de posterior homologação judicial e a cláusula compromissória era tida como mero pré-contrato sem força executiva direta.",
        "explanation": "A dependência de homologação e a fragilidade da cláusula esvaziavam a arbitragem antes da Lei 9.307/96."
    },
    {
        "id": "multi_14_b_lei9307_eficacia_efeito_negativo",
        "subject": "Evolução Histórica e Legislativa da Arbitragem no Brasil",
        "bank": "Revisão Prova 01",
        "difficulty": "Médio",
        "enunciado": "Esse cenário de inoperância da arbitragem foi superado de forma definitiva com a promulgação da Lei nº 9.307/1996 (Lei de Arbitragem). Esse diploma revolucionou a matéria ao:",
        "options": {
            "A": "Conferir eficácia executiva direta à sentença arbitral (dispensando homologação judicial) e dotar a convenção arbitral de efeito vinculante negativo (afastando a jurisdição estatal).",
            "B": "Subordinar todas as sentenças arbitrais a recurso ordinário automático perante os juizados especiais cíveis estaduais.",
            "C": "Extinguir as câmaras arbitrais privadas no país, transferindo sua estrutura para as delegacias de polícia civil.",
            "D": "Proibir que empresas multinacionais utilizem cláusulas compromissórias em contratos celebrados no território brasileiro."
        },
        "gabarito": "A",
        "article": "Lei nº 9.307/1996 (arts. 18, 31 e 485, VII do CPC)",
        "legal_basis": "A Lei nº 9.307/1996 superou os entraves ao conferir eficácia executiva direta à sentença arbitral e dotar a convenção arbitral de efeito vinculante negativo.",
        "explanation": "A sentença arbitral virou título executivo judicial direto e a convenção impede o julgamento pelo juiz togado."
    },
    {
        "id": "multi_14_c_stf_sec5206_constitucionalidade",
        "subject": "Evolução Histórica e Legislativa da Arbitragem no Brasil",
        "bank": "Revisão Prova 01",
        "difficulty": "Difícil",
        "enunciado": "A segurança jurídica definitiva da arbitragem no Brasil foi fixada pelo Supremo Tribunal Federal em paradigmático julgamento concluído no ano de 2001. Trata-se do precedente firmado na:",
        "options": {
            "A": "Sentença Estrangeira Contestada (SEC) nº 5.206, na qual o STF declarou a plena constitucionalidade da Lei nº 9.307/1996 e a legitimidade da renúncia convencional à jurisdição estatal.",
            "B": "Ação Direta de Inconstitucionalidade que anulou a Lei nº 9.099/1995 por violação ao princípio do devido processo legal formal.",
            "C": "Arguição de Descumprimento de Preceito Fundamental que proibiu a celebração de acordos consensuais em matéria cível.",
            "D": "Súmula Vinculante que impôs a revisão obrigatória de todas as sentenças arbitrais pelo Ministério Público da União."
        },
        "gabarito": "A",
        "article": "STF - SEC nº 5.206/Espanha (Pleno, 2001)",
        "legal_basis": "A segurança jurídica definitiva foi fixada em 2001 pelo STF na SEC nº 5.206, que declarou a plena constitucionalidade da lei.",
        "explanation": "O STF, no julgamento da SEC 5.206, pacificou que a cláusula compromissória e a sentença arbitral sem homologação judicial respeitam o art. 5º, XXXV da CF/88."
    },
    {
        "id": "multi_14_d_lei13129_administracao_publica",
        "subject": "Evolução Histórica e Legislativa da Arbitragem no Brasil",
        "bank": "Revisão Prova 01",
        "difficulty": "Médio",
        "enunciado": "Mais recentemente, a Lei nº 13.129/2015 modernizou o diploma arbitral brasileiro (Lei nº 9.307/1996). Entre as principais inovações expressamente destacadas na revisão da matéria, inclui-se:",
        "options": {
            "A": "A admissão formal e expressa da arbitragem na Administração Pública (direta e indireta) para dirimir litígios sobre direitos patrimoniais disponíveis, bem como a regulamentação das tutelas de urgência cautelares no âmbito arbitral.",
            "B": "A determinação de que as sessões arbitrais passem a ser transmitidas obrigatoriamente em televisão aberta de âmbito nacional.",
            "C": "A exigência de que os árbitros sejam aprovados em concurso público de provas e títulos organizado pelo Conselho Nacional do Ministério Público.",
            "D": "A proibição de aplicação de normas do Código de Defesa do Consumidor nos contratos administrativos de concessão de serviços."
        },
        "gabarito": "A",
        "article": "Lei nº 13.129/2015 (Alterações na Lei nº 9.307/1996)",
        "legal_basis": "A Lei nº 13.129/2015 modernizou a arbitragem para admitir formalmente sua realização pela Administração Pública e regulamentar as tutelas de urgência.",
        "explanation": "A reforma de 2015 consagrou a arbitrabilidade na Administração Pública e estabeleceu a cooperação judicial nas cartas arbitrais e tutelas de urgência."
    }
]

def main():
    target_path = Path(__file__).resolve().parent.parent / "database" / "seed_multiportas.json"
    data = {
        "module": "multiportas",
        "version": "3.0.0",
        "description": "56 questões inéditas e alinhadas 100% ao Questionário de Revisão para a Prova 01 de Modelo Multiportas (4 questões para cada um dos 14 temas com nomes de pessoas e casos práticos)",
        "questions": questions
    }
    
    with open(target_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Sucesso! Geradas {len(questions)} questões no arquivo {target_path}")

if __name__ == "__main__":
    main()

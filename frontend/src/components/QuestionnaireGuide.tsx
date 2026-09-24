import React, { useState } from 'react';
import { BookOpen, ChevronDown, ChevronUp, Search, PlayCircle, Scale } from 'lucide-react';

interface QuestionnaireItem {
  id: number;
  subject: string;
  question: string;
  legalBasis: string;
  summary: string;
  explanation: string;
  examples?: string;
}

const QUESTIONNAIRE_ITEMS: QuestionnaireItem[] = [
  {
    id: 1,
    subject: "Escada Ponteana e Planos do Negócio Jurídico",
    question: "O que é a Escada Ponteana e quais são os planos do negócio jurídico?",
    legalBasis: "Doutrina de Pontes de Miranda; Arts. 104, 166, 171 do Código Civil",
    summary: "Estrutura tridimensional concebida por Pontes de Miranda dividida em: Existência, Validade e Eficácia.",
    explanation: `A Escada Ponteana divide a análise do negócio jurídico em 3 degraus sucessivos:
1. Plano da Existência (substantivos): Pressupostos para que o negócio venha a existir no mundo jurídico: partes/sujeito, vontade/consentimento, objeto e forma. Se faltar algum destes, o negócio é INEXISTENTE.
2. Plano da Validade (adjetivos qualificadores - art. 104 CC): Agente capaz; vontade livre e de boa-fé; objeto lícito, possível, determinado ou determinável; forma prescrita ou não defesa em lei. A inobservância gera NULIDADE ABSOLUTA (art. 166) ou ANULABILIDADE (art. 171).
3. Plano da Eficácia: Produção concreta de efeitos sociais e jurídicos. É influenciado pelos elementos acidentais (condição - evento futuro e incerto; termo - evento futuro e certo; encargo/modo - ônus) e consequências do adimplemento ou inadimplemento.`,
    examples: "Exemplo: Um contrato de compra e venda celebrado por menor de 15 anos sem representação: EXISTE (degrau 1), mas é NULO de pleno direito por incapacidade absoluta do agente (degrau 2, art. 166, I)."
  },
  {
    id: 2,
    subject: "Requisitos de Validade do Negócio Jurídico (Art. 104 CC)",
    question: "Quais são os requisitos subjetivos, objetivos e formais de validade do negócio jurídico?",
    legalBasis: "Art. 104, 107, 108 do Código Civil",
    summary: "Requisitos do art. 104: Agente capaz (subjetivo), Objeto lícito, possível, determinado/determinável (objetivo) e Forma prescrita ou não defesa em lei (formal).",
    explanation: `Para que o negócio seja válido, exige-se a observância concorrente de:
- Requisitos Subjetivos: Capacidade civil plena das partes e legitimação negocial (ex.: outorga uxória para alienação de imóveis, salvo separação absoluta).
- Requisitos Objetivos: O objeto da prestação deve ser: (a) lícito (não proibido pelo ordenamento nem atentatório à moral); (b) possível física e juridicamente; (c) determinado ou ao menos determinável (gênero e quantidade, art. 243).
- Requisitos Formais: Regra geral da liberdade de formas (art. 107 CC: consensualismo). Excepcionalmente, exige-se forma solene/ad solemnitatem (ex.: escritura pública para imóveis com valor superior a 30 salários mínimos, art. 108 CC).`,
    examples: "Exemplo: Doação verbal de imóvel no valor de R$ 500.000,00 é nula por desrespeito à solenidade essencial de escritura pública (art. 108 e 541 do CC)."
  },
  {
    id: 3,
    subject: "Princípios Contratuais Fundamentais",
    question: "Quais são os princípios contratuais modernos e como se equilibram?",
    legalBasis: "Arts. 421, 421-A e 422 do Código Civil",
    summary: "Autonomia Privada, Força Obrigatória (Pacta Sunt Servanda), Relatividade dos Efeitos, Função Social do Contrato e Boa-Fé Objetiva.",
    explanation: `O Direito Contratual contemporâneo é regido pela síntese entre princípios individuais e princípios sociais:
- Autonomia Privada (Liberdade Contratual): Liberdade de contratar (escolha do parceiro) e liberdade contratual (conteúdo e cláusulas), hoje exercida nos limites da função social (art. 421 CC, redação da Lei da Liberdade Econômica).
- Força Obrigatória (Pacta Sunt Servanda): O contrato faz lei entre as partes, mitigado pela cláusula rebus sic stantibus e teoria da imprevisão (art. 478 CC).
- Função Social do Contrato (Art. 421 CC): Princípio de ordem pública que tutela a eficácia interna (justiça contratual e equilíbrio) e a eficácia externa (tutela de terceiros contra efeitos nocivos do contrato e vedação ao aliciamento de contratantes).
- Boa-fé Objetiva (Art. 422 CC): Padrão ético de lealdade, confiança e mútua colaboração.`,
    examples: "Exemplo: Contrato de empréstimo com juros abusivos de agiotagem afronta diretamente a função social e os bons costumes, ensejando intervenção corretiva judicial."
  },
  {
    id: 4,
    subject: "Funções da Boa-Fé Objetiva",
    question: "Quais são as três funções fundamentais da Boa-Fé Objetiva?",
    legalBasis: "Arts. 113, 187 e 422 do Código Civil",
    summary: "1. Função Interpretativa (art. 113); 2. Função Limitadora de Direitos / Controle (art. 187); 3. Função Integrativa / Fonte de Deveres Anexos (art. 422).",
    explanation: `A Boa-fé Objetiva desdobra-se em três vertentes essenciais:
1. Função Interpretativa-Integrativa dos Negócios (Art. 113 CC): Os negócios jurídicos devem ser interpretados conforme a boa-fé e os usos do lugar de celebração.
2. Função de Controle / Limitadora do Exercício de Direitos Subjetivos (Art. 187 CC): Comete ato ilícito aquele que, titular de um direito, ao exercê-lo, excede manifestamente os limites impostos pelo seu fim econômico ou social, pela boa-fé ou pelos bons costumes (abuso de direito, de responsabilidade objetiva).
3. Função Integrativa / Criadora de Deveres Anexos ou Laterais (Art. 422 CC): Impõe aos contratantes deveres de conduta éticos independentes de cláusula expressa, tais como: dever de informação/esclarecimento, dever de proteção e incolumidade, dever de lealdade e sigilo. O descumprimento de dever anexo configura violação positiva do contrato (responsabilidade objetiva).`,
    examples: "Exemplo: Concessionária que vende veículo usado com histórico de sinistro grave sem avisar o comprador viola o dever anexo de informação (função integrativa do art. 422)."
  },
  {
    id: 5,
    subject: "Figuras Parcelares da Boa-Fé Objetiva",
    question: "Quais são as figuras parcelares da boa-fé objetiva (conceitos doutrinários)?",
    legalBasis: "Doutrina civilista contemporânea; Enunciados 362 e 169 das Jornadas de Direito Civil",
    summary: "Venire contra factum proprium, Supressio, Surrectio, Tu quoque e Duty to mitigate the loss.",
    explanation: `Constituem desdobramentos operacionais da boa-fé objetiva:
- Venire contra factum proprium: Proibição de comportamento contraditório. Veda que uma parte pratique conduta incoerente com ato anterior juridicamente relevante sobre o qual gerou legítima expectativa na outra parte.
- Supressio (Verwirkung): Perda ou enfraquecimento de um direito subjetivo em razão do seu não exercício continuado e reiterado por longo tempo, gerando na contraparte a confiança de que não mais seria exigido.
- Surrectio (Erwirkung): Surgimento de uma nova posição jurídica/direito em favor de uma parte, como contraface da supressio, advindo da prática reiterada e habitual aceita pela outra.
- Tu quoque ('até tu?'): Vedação a que alguém exija da contraparte o cumprimento de uma regra ou obrigação que ele próprio descumpriu ou violou anteriormente.
- Duty to mitigate the loss (Enunciado 169 CJF): Dever do credor de mitigar o próprio prejuízo, evitando o agravamento culposo do dano causado pelo devedor.`,
    examples: "Exemplo: Locador que durante 3 anos aceitou o pagamento do aluguel todo dia 15 sem jamais cobrar juros ou multa, não pode repentinamente cobrar retroativamente encargos de atraso em relação ao vencimento do dia 5 (Supressio e Venire contra factum proprium)."
  },
  {
    id: 6,
    subject: "Regras de Interpretação dos Contratos",
    question: "Quais são as regras legais de interpretação dos contratos nos artigos 112, 113, 114 e 423 do CC?",
    legalBasis: "Arts. 112, 113, 114 e 423 do Código Civil",
    summary: "Art. 112 (vontade real prevalece sobre literal); Art. 113 (boa-fé e usos locais); Art. 114 (interpretação estrita de renúncias/benesses); Art. 423 (contra proferentem em contratos de adesão).",
    explanation: `O Código Civil estabelece cânones interpretativos vinculantes:
1. Art. 112 CC (Prevalência da Vontade Real): Nas declarações de vontade se atenderá mais à intenção nelas consubstanciada do que ao sentido literal da linguagem.
2. Art. 113 CC (Interpretação Conforme Boa-fé e Usos): Devem ser interpretados conforme a boa-fé e os usos do lugar. Os incisos do § 1º (incluídos pela Lei 13.874/19) determinam observar hábitos das partes, racionalidade econômica e comportamento posterior.
3. Art. 114 CC (Interpretação Restritiva): Os negócios jurídicos benéficos (gratuitos, como doação e fiança) e a renúncia interpretam-se estritamente, vedada interpretação extensiva.
4. Art. 423 CC (Interpretação Contra Proferentem em Adesão): Havendo no contrato de adesão cláusulas ambíguas ou contraditórias, dever-se-á adotar a interpretação mais favorável ao aderente (regra protetiva).`,
    examples: "Exemplo Art. 423: Em contrato de seguro residencial redigido pela seguradora, havendo ambiguidade sobre a cobertura de vendavais ou tempestades, o juiz interpreta a cláusula da forma mais favorável ao segurado aderente."
  },
  {
    id: 7,
    subject: "Classificação Geral dos Contratos",
    question: "Como se classificam os contratos e quais as principais espécies com exemplos?",
    legalBasis: "Doutrina e Código Civil (Arts. 421 a 480)",
    summary: "Unilaterais vs. Bilaterais; Gratuitos vs. Onerosos; Comutativos vs. Aleatórios; Consensuais vs. Reais; Solenes vs. Não solenes; Paritários vs. Adesão; Execução Instantânea vs. Continuada.",
    explanation: `Critérios classificatórios clássicos:
1. Quanto aos efeitos obrigacionais:
   - Unilaterais: Apenas uma das partes assume obrigações (ex: doação pura, mútuo, mandato gratuito).
   - Bilaterais (Sinalagmáticos): Ambas as partes possuem prestações recíprocas e interdependentes (ex: compra e venda, locação). Aplica-se a exceção do contrato não cumprido (art. 476).
2. Quanto às vantagens patrimoniais:
   - Onerosos: Ambas as partes obtêm vantagem com sacrifício patrimonial correspectivo (ex: locação).
   - Gratuitos (Benéficos): Uma parte usufrui do benefício e a outra suporta o ônus (ex: comodato, doação pura).
3. Quanto ao risco e determinação das prestações:
   - Comutativos: Prestações certas, determinadas e equivalentes subjetivamente desde a celebração.
   - Aleatórios: A prestação de uma das partes depende de álea/evento futuro e incerto (ex: seguro, compra de safra futura).
4. Quanto ao momento de aperfeiçoamento:
   - Consensuais: Aperfeiçoam-se pelo mero consenso/acordo de vontades (ex: compra e venda).
   - Reais: Exigem a efetiva tradição/entrega da coisa para se formarem (ex: comodato, mútuo, depósito, penhor).
5. Quanto à forma:
   - Solenes/Formais: A lei exige solenidade essencial para validade (ex: compra de imóvel > 30 salários mínimos, art. 108).
   - Não Solenes/Consensualistas: Forma livre (regra geral, art. 107).
6. Quanto à paridade na estipulação:
   - Paritários: As partes discutem e negociam as cláusulas em pé de igualdade.
   - De Adesão: Uma parte estipula previamente todas as condições sem possibilidade de alteração substancial pela outra.`,
    examples: "Exemplo: Contrato de Compra e Venda de Carro à vista: Bilateral, Oneroso, Comutativo, Consensual, Não solene, Paritário e de Execução Imediata."
  },
  {
    id: 8,
    subject: "Fases de Formação do Contrato",
    question: "Quais são as etapas de formação contratual: negociações, proposta e aceitação?",
    legalBasis: "Arts. 427 a 435 do Código Civil",
    summary: "1. Fase Preliminar (Puntuação/Tratativas); 2. Proposta (Policitação/Oblação); 3. Aceitação (Conclusão do pacto).",
    explanation: `O iter formativo compreende:
1. Fase de Negociações Preliminares (Puntuação/Tratativas): Não vincula as partes ao contrato definitivo em regra, mas impõe respeito à boa-fé objetiva (art. 422). A ruptura injustificada e abrupta que cause danos em virtude de legítima expectativa frustrada enseja responsabilidade civil pré-contratual (interesse negativo).
2. Fase da Proposta (Policitação ou Oferta): Declaração unilateral de vontade receptícia, séria, completa e inequívoca de contratar. Vincula o proponente nos termos do art. 427 do CC.
3. Fase da Aceitação (Oblação): Manifestação de assentimento integral à proposta. Se feita fora do prazo ou com adições, modificações ou restrições, importa NOVA PROPOSTA (contraproposta, art. 431 CC).`,
    examples: "Exemplo de responsabilidade pré-contratual: Empresa que convence agrônomo a rescindir contrato de trabalho e mudar de cidade para nova fábrica e desiste repentinamente da contratação na véspera sem motivo plausível."
  },
  {
    id: 9,
    subject: "Obrigatoriedade e Desoneração da Proposta (Arts. 427 e 428 CC)",
    question: "Quando a proposta é obrigatória e em quais hipóteses ela deixa de ser vinculante?",
    legalBasis: "Arts. 427 e 428 do Código Civil",
    summary: "Regra: proposta obriga o proponente. Exceções: se o contrário resultar dos termos, da natureza do negócio ou das circunstâncias do caso (art. 428, incisos I a IV).",
    explanation: `Regra geral (Art. 427 CC): A proposta de contrato obriga o proponente se o contrário não resultar dos termos dela, da natureza do negócio, ou das circunstâncias do caso.
Hipóteses de desoneração (Art. 428 CC):
- Inciso I (Entre presentes sem prazo): Se feita sem prazo a pessoa presente e não for imediatamente aceita (inclui conversas telefônicas ou mensageiros instantâneos em tempo real).
- Inciso II (Entre ausentes com prazo): Se feita com prazo a pessoa ausente e tiver decorrido o prazo sem resposta.
- Inciso III (Entre ausentes sem prazo): Se feita sem prazo a pessoa ausente e tiver decorrido tempo suficiente para chegar a resposta ao conhecimento do proponente (prazo moral).
- Inciso IV (Retratação prévia ou simultânea): Se antes dela, ou simultaneamente a ela, chegar ao conhecimento da outra parte a retratação do proponente.`,
    examples: "Exemplo Art. 428, IV: Proponente envia carta propondo vender imóvel, mas logo em seguida envia mensagem por WhatsApp cancelando a proposta antes que a carta seja aberta pelo destinatário. A proposta deixa de ser obrigatória."
  },
  {
    id: 10,
    subject: "Momento da Conclusão do Contrato entre Presentes e Ausentes",
    question: "Qual o momento em que se considera concluído o contrato entre presentes e entre ausentes?",
    legalBasis: "Arts. 428, I e 434 do Código Civil",
    summary: "Entre presentes: no instante da aceitação imediata. Entre ausentes: teoria da expedição (recepção mitigada) no momento em que a aceitação é expedida (art. 434).",
    explanation: `Critério temporal de aperfeiçoamento:
- Entre Presentes (inter praesentes): Considera-se concluído no momento em que o oblato emite a sua aceitação imediata. Abrange comunicação verbal presencial, telefone, vídeochamada e chat síncrono.
- Entre Ausentes (inter absentes): O Brasil adotou a Teoria da Expedição (mitigada pela teoria da recepção), positivada no art. 434 do CC: Os contratos entre ausentes tornam-se perfeitos desde que a aceitação é EXPEDIDA.
Exceções do art. 434 (o contrato NÃO se conclui na expedição se):
1. Antes dela ou com ela chegar ao proponente a retratação do aceitante (art. 434, I).
2. Se o proponente se houver comprometido a esperar resposta (art. 434, II).
3. Se ela não chegar no prazo convencionado (art. 434, III).`,
    examples: "Exemplo: Se B envia e-mail aceitando a proposta às 14h, o contrato está aperfeiçoado às 14h (expedição), a menos que B envie mensagem de retratação simultânea que chegue antes ou ao mesmo tempo."
  },
  {
    id: 11,
    subject: "Lugar de Formação do Contrato (Art. 435 CC e Art. 9º LINDB)",
    question: "Qual o lugar da celebração do contrato no Código Civil e no Direito Internacional Privado?",
    legalBasis: "Art. 435 do Código Civil e Art. 9º da Lei de Introdução às Normas do Direito Brasileiro (LINDB)",
    summary: "No direito interno: onde foi proposto (art. 435 CC). No direito internacional: aplica-se a lei do país em que constituída a obrigação / residência do proponente (art. 9º LINDB).",
    explanation: `Regras de competência territorial e direito aplicável:
- Art. 435 do Código Civil (Direito Interno): Reputar-se-á celebrado o contrato no lugar em que foi PROPOSTO. Portanto, mesmo que o aceitante esteja em Salvador e o proponente em Curitiba, o contrato considera-se formado em Curitiba.
- Art. 9º da LINDB (Direito Internacional Privado): Para qualificar e reger as obrigações, aplicar-se-á a lei do país em que se constituírem. O § 2º estabelece que a obrigação resultante do contrato reputa-se constituída no lugar em que residir o proponente.`,
    examples: "Exemplo: Proposta enviada por empresário sediado em São Paulo a fornecedor em Paris. O contrato considera-se celebrado em São Paulo, aplicando-se a lei brasileira quanto à sua constituição conforme o art. 435 do CC e art. 9º, § 2º da LINDB."
  },
  {
    id: 12,
    subject: "Estipulação em Favor de Terceiro",
    question: "O que é estipulação em favor de terceiro, quais são as partes envolvidas e seus efeitos?",
    legalBasis: "Arts. 436 a 438 do Código Civil",
    summary: "Negócio triangular onde o estipulante convenciona com o promitente que este realizará prestação em proveito de terceiro (beneficiário).",
    explanation: `Trata-se de exceção legítima ao princípio da relatividade dos efeitos contratuais.
Partes envolvidas:
- Estipulante: Aquele que contrata e exige a vantagem em favor de outrem. Pode exigir o cumprimento da obrigação (art. 436) ou exonerar o devedor (se não reservou o direito ao terceiro, art. 437).
- Promitente: O devedor que se compromete a realizar a prestação em favor do terceiro.
- Terceiro Beneficiário: Quem recebe a vantagem patrimonial sem ter participado originariamente da formação do pacto. Pode exigir o cumprimento da obrigação se anuir à estipulação e se o estipulante não o houver exonerado (art. 436, parágrafo único).
Revogação/Substituição (Art. 438 CC): O estipulante pode substituir o terceiro a qualquer momento por ato entre vivos ou disposição de última vontade, independentemente de anuência do promitente ou do terceiro.`,
    examples: "Exemplo clássico: Seguro de vida contratado pelo pai (estipulante) com a seguradora (promitente) em favor de seu filho (terceiro beneficiário)."
  },
  {
    id: 13,
    subject: "Promessa de Fato de Terceiro",
    question: "O que é a promessa de fato de terceiro, qual a responsabilidade do promitente e suas exceções?",
    legalBasis: "Arts. 439 e 440 do Código Civil",
    summary: "Contrato em que alguém promete que terceiro praticará determinado ato. Se o terceiro recusar, o promitente responde por perdas e danos.",
    explanation: `Conceito e responsabilidade:
- Art. 439 CC: Aquele que tiver prometido fato de terceiro responderá por perdas e danos quando este o não executar. Trata-se de obrigação de garantia/resultado assumida pelo promitente.
- Art. 440 CC: Nenhuma responsabilidade terá o promitente se o terceiro, tempestivamente, anuir à promessa e assumir a obrigação em seu próprio nome (ocorre liberação do promitente).
Exceções à responsabilidade do promitente (Art. 439, parágrafo único): Não haverá responsabilidade se o terceiro for o cônjuge do promitente, dependendo a sua anuência do regime de bens que determine a perda de bens do casal, ou quando decorrer de caso fortuito ou força maior.`,
    examples: "Exemplo: Empresário artístico que promete que cantor famoso fará show beneficente em clube. Se o cantor se recusar a comparecer, o empresário promitente responde pessoalmente por perdas e danos perante o contratante (art. 439 CC)."
  },
  {
    id: 14,
    subject: "Contrato com Pessoa a Declarar",
    question: "O que é o contrato com pessoa a declarar, como funciona a electio amici e seus efeitos?",
    legalBasis: "Arts. 467 a 471 do Código Civil",
    summary: "Negócio com cláusula pro amico eligendo, na qual um contratante reserva a faculdade de indicar ulteriormente quem assumirá a posição contratual.",
    explanation: `Mecanismo de substituição contratual:
- Art. 467 CC: No momento da conclusão do contrato, pode uma das partes reservar-se a faculdade de indicar a pessoa que deve adquirir os direitos e assumir as obrigações dele decorrentes.
- Indicação (Electio Amici - Art. 468 CC): A indicação deve ser comunicada à outra parte no prazo de 5 (cinco) dias da conclusão do contrato, se outro não tiver sido estipulado entre os contratantes.
- Forma e Aceitação: A aceitação da pessoa nomeada deve revestir a mesma forma que as partes usaram para o contrato (art. 468, parágrafo único).
Efeitos da Nomeação Válida (Art. 469 CC): A pessoa nomeada adquire os direitos e assume as obrigações com eficácia retroativa (ex tunc), desde o momento da celebração original.
Subsistência do Promitente Originário (Art. 470 CC): O contrato produzirá seus efeitos exclusivamente entre os contratantes originários se: (I) não houver indicação no prazo legal/convencional; (II) o nomeado recusar a indicação ou for incapaz/insolvente no momento da nomeação.`,
    examples: "Exemplo: Investidor imobiliário compra terreno em seu nome mas insere cláusula com pessoa a declarar para poder indicar a construtora compradora final em 30 dias sem incidir dupla tributação de ITBI."
  },
  {
    id: 15,
    subject: "Distinção: Pessoa a Declarar vs. Cessão de Contrato, Representação e Estipulação",
    question: "Qual a diferença entre Contrato com Pessoa a Declarar, Cessão de Contrato, Representação e Estipulação em Favor de Terceiro?",
    legalBasis: "Doutrina e Arts. 115, 436, 467 CC",
    summary: "Pessoa a declarar opera retroativamente desde o início; Cessão opera para o futuro (ex nunc); Representação age em nome alheio; Estipulação cria direito puro a terceiro.",
    explanation: `Quadro distintivo conceitual:
1. Contrato com Pessoa a Declarar vs. Representação: Na representação (art. 115), o representante age desde o início em nome e por conta do representado. Na pessoa a declarar, o contratante age em nome próprio, reservando a substituição posterior com efeitos retroativos.
2. Contrato com Pessoa a Declarar vs. Cessão de Posição Contratual: A cessão opera transferência ex nunc (para o futuro) de um contrato já em execução e exige anuência expressa da contraparte no momento da cessão. A electio amici opera retroativamente (ex tunc) e o consentimento da contraparte já foi dado na gênese do contrato.
3. Contrato com Pessoa a Declarar vs. Estipulação em Favor de Terceiro: Na estipulação, o terceiro recebe apenas uma vantagem/benefício (não assume dívidas nem vira parte contratual). Na pessoa a declarar, o nomeado assume a integralidade da posição jurídica (direitos e obrigações).`,
    examples: "Exemplo: Se o estipulante contrata seguro de vida para o filho, o filho nunca responderá pelas mensalidades (estipulação). Se o nomeado assume contrato com pessoa a declarar, assume também a obrigação de pagar o preço total (art. 469 CC)."
  },
  {
    id: 16,
    subject: "Contrato Preliminar (Arts. 462 a 466 CC)",
    question: "Quais são os requisitos, a eficácia e a tutela específica do Contrato Preliminar?",
    legalBasis: "Arts. 462 a 466 do Código Civil e Art. 501 do CPC",
    summary: "Negócio autônomo preparatório que vincula as partes à celebração do contrato definitivo. Deve conter todos os requisitos essenciais, exceto a forma (art. 462).",
    explanation: `Regramento do pré-contrato / promessa de contratar:
- Requisitos (Art. 462 CC): O contrato preliminar, exceto quanto à forma, deve conter todos os requisitos essenciais ao contrato a ser celebrado (partes, objeto, preço, condições). Por isso, promessa de compra e venda de imóvel pode ser feita por instrumento particular, mesmo que o definitivo exija escritura pública.
- Eficácia e Exigibilidade (Art. 463 CC): Concluído o preliminar com observância dos requisitos e sem cláusula de arrependimento, qualquer das partes tem o direito de exigir a celebração do definitivo.
- Tutela Específica / Execução Forçada (Art. 464 CC e Art. 501 CPC): Esgotado o prazo, poderá o juiz, a pedido do interessado, suprir a vontade da parte inadimplente, conferindo caráter definitivo ao contrato preliminar (adjudicação compulsória). Se a natureza da obrigação a isso se opuser, resolver-se-á em perdas e danos (art. 465).`,
    examples: "Exemplo: 'Promessa de Compra e Venda' quitada de imóvel com recusa injustificada do promitente vendedor em outorgar a escritura definitiva enseja ação de adjudicação compulsória para que a sentença judicial sirva de título para registro no Cartório de Imóveis."
  },
  {
    id: 17,
    subject: "Contratos Aleatórios: Conceito e Distinção",
    question: "O que são contratos aleatórios e como se diferenciam dos comutativos?",
    legalBasis: "Arts. 458 a 461 do Código Civil",
    summary: "Contratos bilaterais onerosos em que a prestação de uma das partes depende de um evento futuro e incerto (álea).",
    explanation: `Diferenciação dogmática:
- Contratos Comutativos: As partes conhecem de antemão suas prestações e vantagens patrimoniais, que guardam relação de equivalência subjetiva pré-fixada (ex: compra e venda pura e simples). Aplicam-se vícios redibitórios e lesão.
- Contratos Aleatórios (de alea = sorte, risco): A contraprestação ou a extensão da vantagem depende de um fator de incerteza (sorte ou risco assumido). Uma das partes assume o risco de receber menos ou até nada, sem que isso configure enriquecimento sem causa da outra.
Classificam-se em acidentalmente aleatórios (venda de safra futura, art. 458/459) e tipicamente aleatórios (seguro, jogo, aposta).`,
    examples: "Exemplo: Compra de bilhete de loteria oficial ou seguro automóvel: contrato tipicamente aleatório onde o pagamento da indenização depende do evento sinistro."
  },
  {
    id: 18,
    subject: "Espécies de Contratos Aleatórios: Emptio Spei vs. Emptio Rei Speratae",
    question: "Qual a diferença fundamental entre Emptio Spei (art. 458) e Emptio Rei Speratae (art. 459)?",
    legalBasis: "Arts. 458 e 459 do Código Civil",
    summary: "Emptio Spei = venda da esperança (risco da existência da coisa). Emptio Rei Speratae = venda da coisa esperada (risco da quantidade da coisa).",
    explanation: `Distinção clássica dos contratos aleatórios futuros:
1. Emptio Spei (Venda da Esperança - Art. 458 CC): O adquirente assume o risco de as coisas futuras virem a NÃO EXISTIR em qualquer quantidade. O alienante terá direito a receber todo o preço estipulado, desde que não tenha havido dolo ou culpa de sua parte.
2. Emptio Rei Speratae (Venda da Coisa Esperada - Art. 459 CC): O adquirente assume o risco de as coisas futuras virem a existir em QUANTIDADE MENOR do que a esperada. O alienante terá direito a todo o preço caso alguma quantidade venha a existir. Todavia, se nada vier a existir (existência zero), o contrato fica sem efeito e o alienante deve restituir integralmente o preço recebido.`,
    examples: "Exemplo Emptio Spei: Pagar R$ 1.000 pelo lance da rede de um pescador. Mesmo que não venha peixe algum, o pescador tem direito ao preço total (assumiu o risco da existência). Exemplo Emptio Rei Speratae: Comprar a colheita de milho de uma fazenda estipulada em 1.000 sacas com risco de quantidade: se colher apenas 50 sacas, paga o valor integral acordado; mas se uma geada destruir 100% da lavoura (zero sacas), o comprador não paga nada."
  },
  {
    id: 19,
    subject: "Contratos Aleatórios sobre Coisas Expostas a Risco (Arts. 460 e 461 CC)",
    question: "Como funcionam os contratos aleatórios sobre coisas já existentes expostas a risco e quais os efeitos da má-fé?",
    legalBasis: "Arts. 460 e 461 do Código Civil",
    summary: "Venda de coisa existente sujeita a perigo; o adquirente assume o risco de ela estar danificada ou destruída (art. 460), salvo má-fé do alienante que anula o pacto (art. 461).",
    explanation: `Regramento legal:
- Art. 460 CC: Se for aleatório o contrato, por se referir a coisas existentes, mas expostas a risco, assumido pelo adquirente, terá igualmente direito o alienante a todo o preço, posto que a coisa já não existisse, em parte, ou de todo, no dia do contrato.
- Art. 461 CC (Má-fé do Alienante): A alienação aleatória a que se refere o artigo antecedente poderá ser ANULADA como dolosa pelo prejudicado, se provar que o outro contratante não ignorava a consumação do risco (ou seja, se o alienante já sabia no momento da celebração que a coisa havia perecido ou se danificado).`,
    examples: "Exemplo: Compra de carga de café transportada por navio em alto-mar durante tempestade severa. O comprador assume o risco da perda da carga (art. 460). Se o vendedor já sabia por rádio que o navio havia naufragado 2 horas antes de assinar a venda, o negócio é anulado por dolo (art. 461 CC)."
  },
  {
    id: 20,
    subject: "Vícios Redibitórios: Conceito e Requisitos",
    question: "O que são vícios redibitórios e quais são seus requisitos cumulativos?",
    legalBasis: "Art. 441 do Código Civil",
    summary: "Defeitos ocultos em coisa recebida em contrato comutativo que a tornem imprópria ao uso a que é destinada ou lhe diminuam o valor.",
    explanation: `Conceito e requisitos cumulativos:
- Conceito (Art. 441 CC): A coisa recebida em virtude de contrato comutativo pode ser enjeitada por vícios ou defeitos ocultos, que a tornem imprópria ao uso a que é destinada, ou lhe diminuam o valor. Aplica-se também às doações onerosas (art. 441, parágrafo único).
Requisitos Obrigatórios Cumulativos:
1. Contrato bilateral comutativo ou doação com encargo.
2. Vício ou defeito oculto (não perceptível de pronto por um homem médio em exame diligente ordinário).
3. Preexistência do vício à celebração/tradição do contrato.
4. Gravidade do defeito (tornar a coisa inaproveitável ou diminuir sensivelmente sua utilidade ou valor).`,
    examples: "Exemplo: Comprador adquire veículo usado aparentemente perfeito cuja caixa de transmissão interna quebra após 10 dias em virtude de desgaste interno oculto pré-existente à venda."
  },
  {
    id: 21,
    subject: "Efeitos da Boa/Má-Fé do Alienante e Ações Edilícias (Art. 443 CC)",
    question: "Quais os efeitos da boa-fé ou má-fé do alienante e quais são as ações edilícias cabíveis?",
    legalBasis: "Arts. 442, 443 e 444 do Código Civil",
    summary: "Se o alienante conhecia o vício (má-fé): restitui o valor + despesas + perdas e danos. Se desconhecia (boa-fé): restitui valor + despesas. Ações: Redibitória (rescisão) ou Quanti Minoris (abatimento).",
    explanation: `Regramento de responsabilização e opções do adquirente:
- Art. 442 CC (Ações Edilícias): O adquirente tem direito potestativo de escolha alternada entre:
  1. Ação Redibitória: Rejeitar a coisa, rescindindo o contrato e recebendo de volta o preço pago.
  2. Ação Estimatória (Quanti Minoris): Ficar com a coisa e pleitear o abatimento proporcional do preço.
- Art. 443 CC (Distinção pelo elemento anímico):
  - Alienante de Má-fé (conhecia o vício oculto): Restitui o que recebeu com perdas e danos.
  - Alienante de Boa-fé (não conhecia o vício oculto): Restitui tão-somente o valor recebido, mais as despesas do contrato (sem perdas e danos).
- Art. 444 CC: A responsabilidade subsiste ainda que a coisa pereça em poder do adquirente se o perecimento decorrer do próprio vício oculto.`,
    examples: "Exemplo: Se o vendedor do cavalo sabia que o animal tinha anemia infecciosa incurável e ocultou do comprador, pagará de volta o valor do cavalo mais perdas e danos (custas veterinárias e lucros cessantes de competições canceladas - art. 443)."
  },
  {
    id: 22,
    subject: "Prazos Decadenciais e Distinção de Vício, Erro e Aliud Pro Alio",
    question: "Quais os prazos decadenciais dos vícios redibitórios e como distinguir vício oculto de erro e aliud pro alio?",
    legalBasis: "Arts. 445 do Código Civil e Art. 501 do CPC",
    summary: "Bens móveis: 30 dias (ou 180 dias se vício só puder ser conhecido mais tarde). Bens imóveis: 1 ano (ou 1 ano se vício só puder ser conhecido mais tarde). Aliud pro alio = inadimplemento absoluto.",
    explanation: `Prazos e distinções de fronteira:
1. Prazos Decadenciais do Art. 445 CC:
   - Bem Móvel: 30 dias contados da entrega efetiva. Se o vício, por sua natureza, só puder ser conhecido mais tarde, o prazo será de 30 dias contados da ciência, até o limite máximo de 180 dias.
   - Bem Imóvel: 1 ano contado da posse efetiva. Se já estava na posse, conta-se da alienação, reduzido à metade. Se o vício só puder ser conhecido mais tarde, o prazo será de 1 ano da ciência, até o prazo máximo de 1 ano.
2. Distinção essencial:
   - Vício Redibitório: A coisa entregue é a mesma combinada, mas contém imperfeição oculta que reduz seu valor ou uso. Rege-se por ações edilícias e prazos curtos decadenciais do art. 445 CC.
   - Erro Substancial (Vício do Consentimento, art. 138): O defeito está na mente do declarante (falsa representação da realidade sobre o objeto ou suas qualidades). Prazo decadencial de 4 anos para anular (art. 178, II).
   - Inadimplemento Absoluto (Aliud Pro Alio): Entrega-se coisa inteiramente diferente da acordada (ex: compra cobre e recebe chumbo; compra touro reprodutor e recebe touro estéril congênito). É inadimplemento da obrigação de dar, sujeito a prazo prescricional geral decenal (art. 205 CC), e não vício redibitório!`,
    examples: "Exemplo de Aliud Pro Alio: Comprar lote nº 14 da quadra B e receber o lote nº 15 da quadra C. Não é vício redibitório, mas sim inadimplemento total, ensejando cumprimento forçado ou perdas e danos."
  }
];

interface QuestionnaireGuideProps {
  onTrainSubject: (subject: string) => void;
}

export const QuestionnaireGuide: React.FC<QuestionnaireGuideProps> = ({ onTrainSubject }) => {
  const [searchTerm, setSearchTerm] = useState<string>('');
  const [expandedId, setExpandedId] = useState<number | null>(1);

  const filtered = QUESTIONNAIRE_ITEMS.filter(item =>
    item.question.toLowerCase().includes(searchTerm.toLowerCase()) ||
    item.subject.toLowerCase().includes(searchTerm.toLowerCase()) ||
    item.explanation.toLowerCase().includes(searchTerm.toLowerCase()) ||
    item.legalBasis.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <div className="max-w-4xl mx-auto space-y-6 pb-24 animate-fade-in">
      {/* Header Banner */}
      <div className="p-6 rounded-2xl bg-gradient-to-r from-indigo-950/70 via-slate-900 to-slate-900 border border-indigo-500/30 shadow-xl">
        <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
          <div className="flex items-center gap-3.5">
            <div className="p-3 bg-indigo-600 text-white rounded-xl shadow-lg shadow-indigo-600/30">
              <Scale size={26} />
            </div>
            <div>
              <div className="flex items-center gap-2">
                <h2 className="text-xl font-black text-white">Gabarito Oficial do Questionário</h2>
                <span className="text-[10px] font-extrabold uppercase px-2 py-0.5 rounded-full bg-emerald-500/20 text-emerald-400 border border-emerald-500/30">
                  Prova Quarta-Feira
                </span>
              </div>
              <p className="text-xs text-slate-400 mt-1">
                22 Questões dissertativas comentadas ponto a ponto com fundamentação e exemplos práticos (Evicção excluída).
              </p>
            </div>
          </div>

          <div className="text-right shrink-0">
            <span className="text-2xl font-black text-indigo-400">22</span>
            <span className="text-xs text-slate-500 block font-bold">TEMAS CHAVE</span>
          </div>
        </div>

        {/* Barra de Busca */}
        <div className="mt-5 relative">
          <Search className="absolute left-3.5 top-3 text-slate-400" size={18} />
          <input
            type="text"
            value={searchTerm}
            onChange={e => setSearchTerm(e.target.value)}
            placeholder="Buscar por conceito, artigo (ex: 445, 113) ou termo (ex: Emptio Spei, Supressio)..."
            className="w-full bg-slate-950/80 border border-slate-800 rounded-xl pl-10 pr-4 py-2.5 text-sm text-white placeholder-slate-500 focus:outline-none focus:border-indigo-500"
          />
        </div>
      </div>

      {/* Lista de Questões */}
      <div className="space-y-3">
        {filtered.map(item => {
          const isExpanded = expandedId === item.id;
          return (
            <div
              key={item.id}
              className={`rounded-2xl border transition-all ${
                isExpanded
                  ? 'bg-slate-900 border-indigo-500/40 shadow-lg'
                  : 'bg-slate-900/60 border-slate-800 hover:border-slate-700'
              }`}
            >
              {/* Topo do Accordion */}
              <button
                onClick={() => setExpandedId(isExpanded ? null : item.id)}
                className="w-full p-4 md:p-5 flex items-start justify-between text-left gap-4"
              >
                <div className="flex items-start gap-3">
                  <div className={`p-2 rounded-xl text-xs font-black shrink-0 ${
                    isExpanded ? 'bg-indigo-600 text-white' : 'bg-slate-800 text-slate-400'
                  }`}>
                    {String(item.id).padStart(2, '0')}
                  </div>
                  <div>
                    <span className="text-[11px] font-bold text-indigo-400 uppercase tracking-wider block">
                      {item.subject}
                    </span>
                    <h3 className="text-sm md:text-base font-bold text-white mt-0.5 leading-snug">
                      {item.question}
                    </h3>
                    <p className="text-xs text-slate-400 mt-1 line-clamp-1">
                      {item.summary}
                    </p>
                  </div>
                </div>

                <div className="p-1 text-slate-400 hover:text-white shrink-0 mt-1">
                  {isExpanded ? <ChevronUp size={20} /> : <ChevronDown size={20} />}
                </div>
              </button>

              {/* Conteúdo Expandido */}
              {isExpanded && (
                <div className="px-5 pb-5 pt-1 border-t border-slate-800/80 space-y-4 text-xs md:text-sm animate-fade-in">
                  {/* Fundamentação Legal */}
                  <div className="p-3 bg-indigo-950/20 border border-indigo-500/20 rounded-xl flex items-center gap-2.5 text-indigo-300">
                    <BookOpen size={16} className="shrink-0 text-indigo-400" />
                    <div>
                      <span className="font-bold text-[11px] uppercase tracking-wider text-indigo-400 block">Base Normativa & Doutrinária:</span>
                      <span className="font-semibold text-xs">{item.legalBasis}</span>
                    </div>
                  </div>

                  {/* Resposta Completa */}
                  <div className="space-y-2">
                    <h4 className="text-xs font-bold uppercase tracking-wider text-slate-400">Resposta Padrão para Prova:</h4>
                    <div className="text-slate-300 leading-relaxed whitespace-pre-line bg-slate-950/60 p-4 rounded-xl border border-slate-850">
                      {item.explanation}
                    </div>
                  </div>

                  {/* Exemplo Prático */}
                  {item.examples && (
                    <div className="p-3.5 bg-amber-500/10 border border-amber-500/20 rounded-xl text-amber-200/90 text-xs leading-relaxed">
                      <span className="font-bold text-amber-400 block mb-1">💡 Exemplo Prático de Fixação:</span>
                      {item.examples}
                    </div>
                  )}

                  {/* Ação: Treinar Este Ponto */}
                  <div className="pt-2 flex justify-end">
                    <button
                      onClick={() => onTrainSubject(item.subject)}
                      className="flex items-center gap-2 px-4 py-2 bg-indigo-600 hover:bg-indigo-500 text-white rounded-xl text-xs font-bold transition-all shadow-md shadow-indigo-600/20"
                    >
                      <PlayCircle size={15} />
                      Treinar Questões Deste Ponto
                    </button>
                  </div>
                </div>
              )}
            </div>
          );
        })}
      </div>
    </div>
  );
};

from typing import List, Dict, Any

# Banco de dados estático dos principais artigos do Código Civil brasileiro (arts. 304 a 420)
ARTICLES_DATA: List[Dict[str, Any]] = [
    {
        "id": "art_304",
        "number": 304,
        "subject": "Quem deve pagar",
        "text": "Art. 304. Qualquer interessado na extinção da dívida pode pagá-la, usando, se o credor se opuser, dos meios conducentes à exoneração do devedor. Parágrafo único. Igual direito cabe ao terceiro não interessado, se o fizer em nome e por conta do devedor, salvo oposição deste.",
        "summary": "Qualquer interessado (como fiador) pode pagar. Terceiro não interessado também pode pagar se o fizer em nome do devedor.",
        "tips": "O terceiro interessado tem direito de sub-rogação. O terceiro não interessado pode pagar, mas se pagar em seu próprio nome terá apenas direito de reembolso.",
        "common_errors": "Confundir terceiro interessado (que se sub-roga) com terceiro não interessado (que só reembolsa)."
    },
    {
        "id": "art_305",
        "number": 305,
        "subject": "Quem deve pagar",
        "text": "Art. 305. O terceiro não interessado, que paga a dívida em seu próprio nome, tem direito a reembolsar-se do que pagar; mas não se sub-roga nos direitos do credor. Parágrafo único. Se pagar antes de vencida a dívida, só terá direito ao reembolso no vencimento.",
        "summary": "Terceiro não interessado que paga em seu nome: tem direito de reembolso, mas não de sub-rogação. Reembolso só no vencimento se pago antes.",
        "tips": "Bancas cobram muito o parágrafo único: o reembolso antecipado é vedado; deve-se aguardar o prazo de vencimento original da obrigação.",
        "common_errors": "Achar que o terceiro não interessado se sub-roga nas garantias (hipoteca, fiança) do credor original."
    },
    {
        "id": "art_306",
        "number": 306,
        "subject": "Quem deve pagar",
        "text": "Art. 306. O pagamento feito por terceiro, com desconhecimento ou oposição do devedor, não obriga a reembolso, se este tinha meios para ilidir a ação.",
        "summary": "Pagamento contra a vontade do devedor não gera reembolso se o devedor provar que tinha como impedir a cobrança (ex: dívida prescrita ou compensada).",
        "tips": "O devedor deve provar que tinha meios para ilidir (anular, extinguir) a obrigação na data do pagamento.",
        "common_errors": "Achar que qualquer pagamento feito por terceiro com desconhecimento do devedor é nulo."
    },
    {
        "id": "art_308",
        "number": 308,
        "subject": "A quem se deve pagar",
        "text": "Art. 308. O pagamento deve ser feito ao credor ou a quem de direito o represente, sob pena de só valer depois de por ele ratificado, ou tanto quanto reverter em seu proveito.",
        "summary": "O pagamento deve ser feito ao credor ou seu representante. Se pago a terceiro, só é válido se o credor ratificar ou se o dinheiro reverter em seu favor.",
        "tips": "Origem da regra clássica 'quem paga mal, paga duas vezes'. A ratificação valida o pagamento retroativamente.",
        "common_errors": "Considerar que o pagamento feito a um terceiro de forma errada é nulo de forma absoluta e irrecuperável."
    },
    {
        "id": "art_309",
        "number": 309,
        "subject": "A quem se deve pagar",
        "text": "Art. 309. O pagamento feito de boa-fé ao credor putativo é válido, ainda provado depois que não era credor.",
        "summary": "Teoria da Aparência: Pagamento feito a quem parecia ser o credor de forma convincente (e com boa-fé do devedor) é válido.",
        "tips": "O credor putativo deve aparentar de forma inequívoca ser o verdadeiro credor. O credor real deve cobrar o valor do credor putativo, não do devedor exonerado.",
        "common_errors": "Exigir que o pagamento ao credor putativo seja homologado pelo juiz para ter validade."
    },
    {
        "id": "art_313",
        "number": 313,
        "subject": "Objeto do pagamento e sua prova",
        "text": "Art. 313. O credor não pode ser obrigado a receber prestação diversa da que lhe é devida, ainda que mais valiosa.",
        "summary": "Princípio da Identidade do Objeto: O credor tem direito ao objeto exato contratado e pode rejeitar substitutos, mesmo que mais valiosos.",
        "tips": "Este artigo é a base que contrasta com a Dação em Pagamento, que exige o consentimento expresso do credor.",
        "common_errors": "Acreditar que se o devedor oferecer um bem de valor muito maior o credor é obrigado a aceitar."
    },
    {
        "id": "art_327",
        "number": 327,
        "subject": "Lugar do pagamento",
        "text": "Art. 327. Efetuar-se-á o pagamento no domicílio do devedor, salvo se as partes convencionarem diversamente, ou se o contrário dispuserem a lei, a natureza da obrigação ou as circunstâncias. Parágrafo único. Designados dois ou mais lugares, cabe ao credor escolher entre eles.",
        "summary": "Regra geral: Pagamento no domicílio do devedor (obrigação querível). Exceção: Domicílio do credor (portável).",
        "tips": "Na prova, a regra geral é o domicílio do DEVEDOR. Se houver pluralidade de locais, a escolha cabe ao CREDOR.",
        "common_errors": "Achar que a escolha do local em caso de multiplicidade cabe ao devedor."
    },
    {
        "id": "art_330",
        "number": 330,
        "subject": "Lugar do pagamento",
        "text": "Art. 330. O pagamento reiteradamente feito em outro local faz presumir renúncia do credor relativamente ao previsto no contrato.",
        "summary": "Surrectio e Supressio no adimplemento: Pagamento feito reiteradamente em local diferente altera tacitamente o contrato.",
        "tips": "Representa a aplicação direta do princípio da boa-fé objetiva e proibição de comportamento contraditório.",
        "common_errors": "Achar que qualquer alteração de local exige aditivo por escrito sob pena de nulidade."
    },
    {
        "id": "art_331",
        "number": 331,
        "subject": "Tempo do pagamento",
        "text": "Art. 331. Salvo disposição especial deste Código, as obrigacões puras e simples, sem prazo assinalado, são exigíveis imediatamente.",
        "summary": "Obrigações sem prazo vencem imediatamente.",
        "tips": "O credor pode cobrar logo após a constituição do vínculo, dispensando prazo moratório.",
        "common_errors": "Achar que a ausência de prazo torna a obrigação nula."
    },
    {
        "id": "art_335",
        "number": 335,
        "subject": "Consignação em pagamento",
        "text": "Art. 335. A consignação tem lugar: I - se o credor não puder, ou, sem justa causa, recusar receber o pagamento, ou dar quitação na devida forma; II - se o credor não for nem mandar receber a coisa no lugar, tempo e condição devidos; III - se o credor for incapaz de receber, for desconhecido, declarado ausente, ou residir em lugar incerto ou de acesso perigoso ou difícil; IV - se ocorrer dúvida sobre quem deva legitimamente receber; V - se pender litígio sobre o objeto do pagamento.",
        "summary": "Relação de hipóteses legais que autorizam o devedor a efetuar depósito consignado para extinguir a dívida.",
        "tips": "Decorre da mora do credor ou de situações de incerteza jurídica. É um rol exemplificativo, embora muito explorado em provas.",
        "common_errors": "Acreditar que a consignação só serve quando o credor se recusa a receber."
    },
    {
        "id": "art_346",
        "number": 346,
        "subject": "Pagamento com sub-rogação",
        "text": "Art. 346. A sub-rogação opera-se, de pleno direito, em favor: I - do credor que paga a dívida do devedor comum; II - do adquirente do imóvel hipotecado, que paga ao credor o débito que onera o imóvel; III - do terceiro interessado, que paga a dívida pela qual era ou podia ser obrigado, no todo ou em parte.",
        "summary": "Hipóteses de sub-rogação legal (automática), transferindo todos os direitos do credor original ao que pagou a dívida.",
        "tips": "Muito comum em provas o item III: o fiador que paga a dívida assume todos os privilégios e garantias do credor perante o devedor principal.",
        "common_errors": "Achar que a sub-rogação do terceiro interessado depende de contrato escrito."
    },
    {
        "id": "art_354",
        "number": 354,
        "subject": "Imputação do pagamento",
        "text": "Art. 354. Havendo capital e juros, o pagamento imputar-se-á primeiro nos juros vencidos, e depois no capital, salvo estipulação em contrário, ou se o credor passar quitação por conta do capital.",
        "summary": "Regra de imputação financeira: Qualquer pagamento quita primeiro os juros vencidos acumulados, e depois abate o saldo principal.",
        "tips": "Esta regra é de extrema relevância prática e cai com frequência em questões de múltipla escolha.",
        "common_errors": "Achar que o devedor pode exigir que o pagamento parcial abata apenas o capital principal."
    },
    {
        "id": "art_356",
        "number": 356,
        "subject": "Dação em pagamento",
        "text": "Art. 356. O credor pode consentir em receber prestação diversa da que lhe é devida.",
        "summary": "Dação em Pagamento: Extinção da obrigação mediante a entrega de prestação de natureza diferente, condicionado ao acordo bilateral.",
        "tips": "Exige o consentimento do credor (animus solvendi com objeto diverso). Se o credor aceitar, a obrigação é quitada.",
        "common_errors": "Confundir com novação objetiva (que cria nova dívida) ou achar que a dação é ato unilateral."
    },
    {
        "id": "art_359",
        "number": 359,
        "subject": "Dação em pagamento",
        "text": "Art. 359. Se o credor for evicto da coisa recebida em pagamento, restabelecer-se-á a obrigação primitiva, ficando sem efeito a quitação dada, ressalvados os direitos de terceiros de boa-fé.",
        "summary": "Se o credor perder o bem recebido em dação em decisão judicial (evicção), a dívida original em dinheiro renasce.",
        "tips": "Bancas adoram esse artigo. A perda do bem anula a dação e restaura a obrigação como se nunca tivesse ocorrido, protegendo terceiros.",
        "common_errors": "Pensar que o credor evicto só tem direito a perdas e danos pelo valor do bem perdido, sem o renascimento da dívida original."
    },
    {
        "id": "art_360",
        "number": 360,
        "subject": "Novação",
        "text": "Art. 360. Dá-se a novação: I - quando o devedor contrai com o credor nova obrigação para extinguir e substituir a anterior; II - quando novo devedor substitui o antigo, ficando este quitado com o credor; III - quando, em virtude de nova obrigação, um novo credor é substituído ao antigo, ficando o devedor livre com este.",
        "summary": "Novação: Extinção de dívida pela criação de outra. Pode ser objetiva (mudança do objeto) ou subjetiva (mudança do devedor ou credor).",
        "tips": "Requer intenção de novar (animus novandi). Se não houver, a nova obrigação apenas confirma a primeira.",
        "common_errors": "Confundir novação passiva por expromissão (sem consentimento do devedor) com a delegação (com consentimento)."
    },
    {
        "id": "art_368",
        "number": 368,
        "subject": "Compensação",
        "text": "Art. 368. Se duas pessoas forem ao mesmo tempo credor e devedor uma da outra, as duas obrigações extinguem-se, até onde se compensarem.",
        "summary": "Compensação: Extinção recíproca de débitos paralelos e opostos.",
        "tips": "A compensação legal ocorre de forma automática por força da lei uma vez preenchidos os requisitos. A convencional decorre de acordo.",
        "common_errors": "Achar que a compensação legal exige homologação judicial para produzir efeitos."
    },
    {
        "id": "art_381",
        "number": 381,
        "subject": "Confusão",
        "text": "Art. 381. Extingue-se a obrigação, desde que na mesma pessoa se reunam as qualidades de credor e devedor.",
        "summary": "Confusão: Aglutinação de credor e devedor em um único sujeito (geralmente por sucessão hereditária ou fusão empresarial).",
        "tips": "Cessando a confusão por motivo superveniente, restabelece-se imediatamente a obrigação original com todos os acessórios.",
        "common_errors": "Acreditar que a confusão sempre extingue a dívida de forma irreversível."
    },
    {
        "id": "art_385",
        "number": 385,
        "subject": "Remissão das dívidas",
        "text": "Art. 385. A remissão da dívida, aceita pelo devedor, extingue a obrigação, mas sem prejuízo de terceiro.",
        "summary": "Remissão: Perdão da dívida. Exige concordância do devedor e não pode prejudicar direitos de terceiros.",
        "tips": "A aceitação pode ser tácita (ex: devolução voluntária do título físico do débito).",
        "common_errors": "Achar que a remissão é ato unilateral irrecusável pelo devedor."
    },
    {
        "id": "art_389",
        "number": 389,
        "subject": "Inadimplemento - Disposições gerais",
        "text": "Art. 389. Não cumprida a obrigação, responde o devedor por perdas e danos, mais juros e atualização monetária segundo índices oficiais regularmente estabelecidos, e honorários de advogado.",
        "summary": "Regra geral de inadimplemento: O devedor responde pela recomposição integral do prejuízo causado pelo descumprimento.",
        "tips": "Base da responsabilidade civil contratual no Brasil.",
        "common_errors": "Acreditar que honorários contratuais de advogado estão excluídos das perdas e danos."
    },
    {
        "id": "art_394",
        "number": 394,
        "subject": "Mora - Geral",
        "text": "Art. 394. Considera-se em mora o devedor que não efetuar o pagamento e o credor que o não quiser receber no tempo, lugar e forma que a lei ou a convenção estabelecer.",
        "summary": "Mora: Atraso culposo ou descumprimento imperfeito quanto ao tempo, lugar ou forma.",
        "tips": "Existe mora do devedor (solvendi) e mora do credor (accipiendi).",
        "common_errors": "Achar que mora se resume apenas ao atraso temporal do devedor."
    },
    {
        "id": "art_397",
        "number": 397,
        "subject": "Mora - Geral",
        "text": "Art. 397. O inadimplemento da obrigação, positiva e líquida, no seu termo, constitui de pleno direito em mora o devedor. Parágrafo único. Não havendo termo, a mora se constitui mediante interpelação judicial ou extrajudicial.",
        "summary": "Mora ex re (vencimento automático se há prazo e liquidez) e Mora ex persona (exige notificação se não há prazo).",
        "tips": "Regra dies interpellat pro homine (o dia do vencimento interpela pelo homem). Cai massivamente em exames.",
        "common_errors": "Exigir notificação prévia para dívida com prazo e valor líquido expressos."
    },
    {
        "id": "art_399",
        "number": 399,
        "subject": "Mora do devedor",
        "text": "Art. 399. O devedor em mora responde pela impossibilidade da prestação, embora essa impossibilidade resulte de caso fortuito ou de força maior, se estes ocorrerem durante o atraso; salvo se provar que a isenção de culpa se deu por não ter havido atraso, ou que o dano sobreviria ainda que a obrigação tivesse sido oportunamente desempenhada.",
        "summary": "Perpetuação da obrigação: O devedor em mora assume o risco total, inclusive por eventos inevitáveis.",
        "tips": "Só se exime provando que o dano ocorreria mesmo se ele tivesse entregue no prazo (ex: inundação da cidade inteira).",
        "common_errors": "Achar que caso fortuito sempre exclui a responsabilidade civil do devedor atrasado."
    },
    {
        "id": "art_402",
        "number": 402,
        "subject": "Perdas e danos",
        "text": "Art. 402. Salvo as exceções expressamente previstas em lei, as perdas e danos devidas ao credor abrangem, além do que ele efetivamente perdeu, o que razoavelmente deixou de lucrar.",
        "summary": "Composição de Perdas e Danos = Dano Emergente + Lucro Cessante.",
        "tips": "O lucro cessante deve ser razoável e provável, não mero dano hipotético ou fantasioso.",
        "common_errors": "Excluir os lucros cessantes da condenação civil por falta de previsão contratual."
    },
    {
        "id": "art_406",
        "number": 406,
        "subject": "Juros legais",
        "text": "Art. 406. Quando os juros moratórios não forem convencionados, ou o forem sem taxa estipulada, ou provierem de determinação da lei, serão fixados segundo a taxa que estiver em vigor para a mora do pagamento de impostos devidos à Fazenda Nacional.",
        "summary": "Fixação de juros de mora legais na ausência de taxa em contrato (aplicação da taxa Selic de acordo com o entendimento do STJ).",
        "tips": "Importante para atualização de cálculos de liquidação cível.",
        "common_errors": "Achar que a taxa legal de juros de mora é fixada em 1% ao ano de forma imutável."
    },
    {
        "id": "art_412",
        "number": 412,
        "subject": "Cláusula penal",
        "text": "Art. 412. O valor da cominação imposta na cláusula penal não pode exceder o da obrigação principal.",
        "summary": "Teto da Cláusula Penal: A multa contratual compensatória ou moratória é limitada ao valor total do contrato.",
        "tips": "Se exceder, a cláusula penal é reduzida judicialmente, não sendo a cláusula inteira nula.",
        "common_errors": "Pensar que o excesso da multa contratual anula todo o contrato de forma absoluta."
    },
    {
        "id": "art_413",
        "number": 413,
        "subject": "Cláusula penal",
        "text": "Art. 413. A penalidade deve ser reduzida equitativamente pelo juiz se a obrigação principal tiver sido cumprida em parte, ou se o montante da penalidade for manifestamente excessivo, tendo-se em vista a natureza e a finalidade do negócio.",
        "summary": "Redução equitativa da multa: O juiz deve (de ofício) reduzir a cláusula penal se houver adimplemento parcial ou valor absurdo.",
        "tips": "Norma cogente (ordem pública). Não cabe às partes afastarem a incidência deste artigo contratualmente.",
        "common_errors": "Achar que a redução depende obrigatoriamente de provocação do réu em contestação."
    },
    {
        "id": "art_418",
        "number": 418,
        "subject": "Arras ou sinal",
        "text": "Art. 418. Se a parte que deu as arras der causa à inexecução do contrato, poderá a outra retê-las, prendendo-as como indenização; se a inexecução for da parte que recebeu as arras, poderá quem as deu haver o contrato por desfeito, e exigir a devolução das arras, mais o equivalente, com atualização monetária segundo índices oficiais regularmente estabelecidos, juros e honorários de advogado.",
        "summary": "Arras confirmatórias: Se quem deu descumprir, perde o sinal. Se quem recebeu descumprir, devolve o sinal em dobro (devolve + equivalente).",
        "tips": "Se quem recebeu descumprir, a devolução em dobro do sinal visa equilibrar a penalização das partes.",
        "common_errors": "Achar que a devolução de arras por inexecução de quem recebeu é apenas o valor simples pago originalmente."
    },
    {
        "id": "art_420",
        "number": 420,
        "subject": "Arras ou sinal",
        "text": "Art. 420. Se no contrato for estipulado o direito de arrependimento, as arras ou sinal terão função unicamente indenizatória. Neste caso, quem as deu perdê-las-á em benefício da outra parte; e quem as recebeu devolvê-las-á mais o equivalente. Em ambos os casos não haverá direito a indenização suplementar.",
        "summary": "Arras Penitenciais: Contratos com cláusula de arrependimento. As arras servem de teto indenizatório máximo, proibindo cobranças suplementares.",
        "tips": "Diferença essencial das arras confirmatórias: nas penitenciais é proibido pedir indenização complementar pelas perdas.",
        "common_errors": "Permitir indenização suplementar mesmo havendo cláusula expressa de arrependimento regulada por arras."
    }
]

# -*- coding: utf-8 -*-
"""
Módulo de geração offline e guia de estudos para Processo Penal (1º Bimestre).
Alinhado 100% ao Questionário do Professor Felipe Velozo e à jurisprudência
vinculante atualizada do STF (ADIs 6.298, 6.299, 6.300 e 6.305) e STJ.
"""
import random
import uuid
from typing import Dict, Any, List

PROCESSO_PENAL_SUBJECTS = [
    "Juiz das Garantias - Criação e Campo de Atuação",
    "Aplicação Imediata da Norma Processual Penal e Efeito Jurídico",
    "Notitia Criminis e Atuação da Autoridade Policial",
    "Inquérito Policial e Vedação ao Arquivamento pelo Delegado",
    "Devolução do Inquérito Policial ao Delegado pelo MP",
    "Arquivamento do Inquérito e Realização de Novas Diligências",
    "Espécies de Ação Penal e suas Subdivisões",
    "Retratação da Representação na Ação Penal Pública Condicionada",
    "Peças Inaugurais da Ação Penal: Denúncia e Queixa-Crime",
    "Prazos para Oferecimento da Denúncia",
    "Prazos para Oferecimento da Queixa-Crime e Consequência Jurídica",
    "Hipóteses de Rejeição Liminar da Denúncia ou Queixa",
    "Inépcia da Denúncia e Consequência Jurídica",
    "Efeitos da Sentença Penal Absolutória na Esfera Cível",
    "Extinção da Punibilidade e Independência da Ação Civil",
    "Conceito e Fundamentos do Flagrante Delito",
    "Modalidades Legais e Doutrinárias de Flagrante"
]

PROCESSO_PENAL_BANKS = ["Revisão 1º Bimestre", "Estudo de Caso", "Doutrina", "Processo Penal"]

PROCESSO_PENAL_STUDY_GUIDE: Dict[str, Dict[str, str]] = {
    "Juiz das Garantias - Criação e Campo de Atuação": {
        "articles": "Art. 3º-B e 3º-C do CPP (Lei 13.964/2019) e ADIs 6.298, 6.299, 6.300 e 6.305 do STF",
        "key_concept": "Criado para assegurar a higidez do sistema acusatório e a imparcialidade do juiz da instrução. Pela interpretação conforme do STF, sua competência cessa com o OFERECIMENTO da denúncia/queixa, cabendo ao juiz da instrução receber a exordial e manter cautelares.",
        "trap": "A competência NÃO vai até o recebimento da denúncia (o texto original previa isso, mas o STF fixou o término no OFERECIMENTO da peça acusatória)."
    },
    "Aplicação Imediata da Norma Processual Penal e Efeito Jurídico": {
        "articles": "Art. 2º do CPP e Art. 5º, XL da CF/88",
        "key_concept": "Princípio da aplicação imediata (tempus regit actum): atinge imediatamente os atos futuros dos processos em curso, preservando os atos praticados. Normas mistas/híbridas obedecem à irretroatividade penal maléfica.",
        "trap": "Normas puramente processuais aplicam-se imediatamente mesmo que tornem o procedimento mais gravoso para o réu; apenas normas de conteúdo material submetem-se ao art. 5º, XL da CF."
    },
    "Notitia Criminis e Atuação da Autoridade Policial": {
        "articles": "Art. 5º, incisos I e II, §§ 4º e 5º do CPP",
        "key_concept": "Pública incondicionada: instauração de ofício (portaria). Pública condicionada: depende de representação da vítima ou requisição do Ministro da Justiça. Privada: depende de requerimento expresso de quem tem legitimidade.",
        "trap": "O delegado NÃO pode instaurar inquérito de ofício em crime de ação penal pública condicionada sem representação válida."
    },
    "Inquérito Policial e Vedação ao Arquivamento pelo Delegado": {
        "articles": "Art. 17 do CPP",
        "key_concept": "A autoridade policial NUNCA pode mandar arquivar autos de inquérito policial. Trata-se de competência exclusiva do titular da ação penal (Ministério Público).",
        "trap": "Mesmo diante da comprovação cabal de excludente de ilicitude, o delegado deve relatar as diligências, cabendo ao MP promover o arquivamento."
    },
    "Devolução do Inquérito Policial ao Delegado pelo MP": {
        "articles": "Art. 16 do CPP",
        "key_concept": "A devolução dos autos à delegacia só é admitida para a realização de diligências novas comprovadamente imprescindíveis ao oferecimento da denúncia. Vedada a devolução para diligências genéricas ou protelatórias.",
        "trap": "O MP não pode devolver inquérito apenas para cumprir formalidades dispensáveis ou protelar prazo decadencial."
    },
    "Arquivamento do Inquérito e Realização de Novas Diligências": {
        "articles": "Art. 18 do CPP e Súmula 524 do STF",
        "key_concept": "O arquivamento por falta de justa causa ou fragilidade probatória gera coisa julgada meramente formal. A autoridade policial pode realizar novas diligências se de outras provas tiver notícia (Súmula 524 do STF).",
        "trap": "O arquivamento fundado em atipicidade da conduta gera coisa julgada material e impede a reabertura mesmo com prova nova."
    },
    "Espécies de Ação Penal e suas Subdivisões": {
        "articles": "Art. 129, I e Art. 5º, LIX da CF/88; Arts. 24 a 32 do CPP",
        "key_concept": "Pública (incondicionada ou condicionada à representação/requisição). Privada: exclusivamente privada, personalíssima (art. 236 CP) e privada subsidiária da pública (por inércia do MP).",
        "trap": "A ação privada subsidiária só cabe diante da inércia do MP no prazo legal; se o MP pediu arquivamento ou diligências tempestivamente, ela não cabe."
    },
    "Retratação da Representação na Ação Penal Pública Condicionada": {
        "articles": "Art. 25 do CPP, Art. 102 do CP e Art. 16 da Lei 11.340/2006",
        "key_concept": "Regra geral: retratação é válida até o OFERECIMENTO da denúncia. Lei Maria da Penha (violência doméstica contra mulher): só cabe em audiência especial perante o juiz antes do RECEBIMENTO da denúncia.",
        "trap": "Na regra geral do CPP a retratação é até o oferecimento; na Lei Maria da Penha é perante o juiz antes do recebimento."
    },
    "Peças Inaugurais da Ação Penal: Denúncia e Queixa-Crime": {
        "articles": "Arts. 24, 30, 41 e 44 do CPP",
        "key_concept": "Ação pública: Denúncia (peça privativa do Ministério Público). Ação privada: Queixa-crime (peça do ofendido subscrita por advogado com procuração com poderes especiais).",
        "trap": "A petição da vítima em crime de ação pública não é queixa, é mera notitia criminis ou representação."
    },
    "Prazos para Oferecimento da Denúncia": {
        "articles": "Art. 46 do CPP",
        "key_concept": "Regra geral do CPP: 5 dias se o réu estiver preso cautelarmente; 15 dias se o réu estiver solto ou sob fiança, contados do recebimento dos autos pelo MP.",
        "trap": "O prazo de réu preso conta-se a partir do recebimento dos autos no órgão do MP e não da data da prisão."
    },
    "Prazos para Oferecimento da Queixa-Crime e Consequência Jurídica": {
        "articles": "Art. 38 do CPP, Art. 103 e Art. 107, IV do Código Penal",
        "key_concept": "Prazo decadencial de 6 meses a contar do conhecimento da autoria (ou do esgotamento do prazo ministerial na subsidiária). O não oferecimento no prazo acarreta a DECADÊNCIA e a EXTINÇÃO DA PUNIBILIDADE.",
        "trap": "O prazo decadencial não se prorroga nem se suspende por férias forenses ou domingos."
    },
    "Hipóteses de Rejeição Liminar da Denúncia ou Queixa": {
        "articles": "Art. 395, incisos I, II e III do CPP",
        "key_concept": "A denúncia/queixa é rejeitada quando: I - manifestamente inepta; II - faltar pressuposto processual ou condição da ação; III - faltar justa causa (lastro probatório mínimo de materialidade e autoria).",
        "trap": "Falta de justa causa gera rejeição do art. 395, III, e não absolvição sumária do art. 397."
    },
    "Inépcia da Denúncia e Consequência Jurídica": {
        "articles": "Art. 41 e Art. 395, I do CPP",
        "key_concept": "Inépcia decorre da ausência de descrição individualizada e clara do fato criminoso e suas circunstâncias, impedindo o exercício da ampla defesa. Consequência jurídica: rejeição liminar (art. 395, I).",
        "trap": "Denúncia genérica que não individualiza a conduta em crimes multitudinários ou societários pode ser trancada por inépcia."
    },
    "Efeitos da Sentença Penal Absolutória na Esfera Cível": {
        "articles": "Arts. 65, 66 e 386 do CPP; Art. 935 do Código Civil",
        "key_concept": "Faz coisa julgada no cível: inexistência material do fato (art. 386, I), negativa categórica de autoria (art. 386, IV) e excludentes de ilicitude reais (art. 65). NÃO faz coisa julgada no cível: falta de provas (art. 386, II, V, VII) e atipicidade penal (art. 386, III).",
        "trap": "Absolvição por falta de provas (in dubio pro reo) não impede ação civil de ressarcimento patrimonial."
    },
    "Extinção da Punibilidade e Independência da Ação Civil": {
        "articles": "Art. 67, inciso II do CPP",
        "key_concept": "A extinção da punibilidade (prescrição, decadência, anistia, indulto) NÃO impede a propositura da ação civil indenizatória ex delicto. Apenas extingue o poder punitivo estatal.",
        "trap": "A prescrição penal não extingue automaticamente a pretensão indenizatória civil, que segue seus próprios prazos civis."
    },
    "Conceito e Fundamentos do Flagrante Delito": {
        "articles": "Art. 5º, LXI da CF/88 e Arts. 301 a 310 do CPP",
        "key_concept": "Medida cautelar pré-processual restritiva de liberdade, autoexecutável, que prescinde de ordem judicial prévia diante da certeza visual do delito. Qualquer do povo pode e autoridades devem prender em flagrante.",
        "trap": "O flagrante é medida precária: em até 24 horas deve ser realizada a audiência de custódia para conversão em preventiva, concessão de liberdade ou relaxamento."
    },
    "Modalidades Legais e Doutrinárias de Flagrante": {
        "articles": "Art. 302 do CPP e Súmula 145 do STF",
        "key_concept": "Legais: Próprio (cometendo ou acaba de cometer - I e II); Impróprio/quase-flagrante (perseguido logo após - III); Presumido/ficto (encontrado logo depois com objetos/armas - IV). Doutrinárias: Preparado (inválido, crime impossível, Súmula 145 STF); Forjado (crime de denunciação caluniosa); Esperado (válido, mera campana sem induzimento).",
        "trap": "No flagrante presumido NÃO há perseguição física; o agente é localizado logo depois com os instrumentos ou produtos do crime."
    }
}

NOMES_PENAL = ["Carlos", "Mariana", "Lucas", "Roberto", "Fernanda", "Eduardo", "Juliana", "Guilherme", "Patrícia", "Thiago", "Beatriz", "Marcelo", "Camila", "Rodrigo"]

def generate_processo_penal_question_offline(subject: str, bank: str = "Revisão 1º Bimestre", difficulty: str = "Médio") -> Dict[str, Any]:
    """Gera proceduralmente questões técnicas sobre os 17 temas de Processo Penal"""
    if subject not in PROCESSO_PENAL_SUBJECTS:
        subject = random.choice(PROCESSO_PENAL_SUBJECTS)
    guide = PROCESSO_PENAL_STUDY_GUIDE.get(subject, {})
    p1 = random.choice(NOMES_PENAL)
    p2 = random.choice([n for n in NOMES_PENAL if n != p1])
    
    enunciado = (
        f"Em determinado inquérito penal envolvendo {p1} e {p2}, questiona-se a aplicação das regras fundamentais "
        f"referentes ao tema '{subject}'. Considerando a disciplina do Código de Processo Penal e a jurisprudência "
        f"do STF e STJ, assinale a opção correta:"
    )
    
    options = {
        "A": guide.get("key_concept", "Conceito correto sobre a matéria."),
        "B": f"A conduta é regulada de modo oposto, sendo vedada a observância das regras de {subject}.",
        "C": f"A legislação determina que a matéria de {subject} foi revogada compulsoriamente no direito brasileiro.",
        "D": guide.get("trap", "Alternativa que contém a pegadinha clássica sobre o tema.")
    }
    
    return {
        "id": f"proc_penal_{uuid.uuid4().hex[:8]}",
        "subject": subject,
        "bank": bank,
        "difficulty": difficulty,
        "enunciado": enunciado,
        "options": options,
        "gabarito": "A",
        "article": guide.get("articles", "Código de Processo Penal"),
        "legal_basis": guide.get("key_concept", ""),
        "explanation": f"Correta a alternativa A: {guide.get('key_concept', '')} Atenção à pegadinha: {guide.get('trap', '')}"
    }

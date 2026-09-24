import json
import re
import random
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# --------------------------------------------------------------------------
# REGRAS DE EXPANSÃO E BALANCEAMENTO DE DISTRATORES
# Cada substituição visa:
# 1. Manter comprimento balanceado (130 - 210 caracteres)
# 2. Inserir pegadinha técnica real (conceito invertido, prazo errado, exceção falsa)
# 3. Remover respostas telegráficas ou simplórias
# --------------------------------------------------------------------------

def upgrade_seed_questions():
    file_path = BASE_DIR / "database" / "seed_questions.json"
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    questions = data.get("questions", [])
    updated_count = 0

    for q in questions:
        subject = q.get("subject", "")
        options = q.get("options", {})
        gabarito = q.get("gabarito", "")
        corr_len = len(options.get(gabarito, ""))

        new_options = dict(options)
        
        for k, v in options.items():
            if k == gabarito:
                continue
            
            # Se o distrator for muito curto em relação à resposta correta (< 95 chars ou ratio > 1.35)
            # Vamos enriquecer com fundamentação doutrinária plausível e ardilosa
            v_clean = v.strip().rstrip(".")

            # Casos específicos conhecidos
            if v_clean == "Tu quoque":
                new_options[k] = "Tu quoque, segundo o qual a parte que violou determinada cláusula contratual ou dever anexo perde a legitimidade para exigir o adimplemento estrito da contraprestação alheia."
            elif v_clean == "Supressio":
                new_options[k] = "Supressio, caracterizada pela perda de um direito subjetivo em decorrência do seu não exercício prolongado no tempo, gerando na contraparte a legítima expectativa de não cobrança."
            elif v_clean == "Surrectio":
                new_options[k] = "Surrectio, consubstanciada no surgimento superveniente de um direito subjetivo contratual em favor de uma parte, decorrente de uma prática reiterada mantida sem oposição recíproca."
            elif v_clean.startswith("Duty to mitigate"):
                new_options[k] = "Duty to mitigate the loss, consistente no dever imposto ao credor de mitigar os próprios prejuízos sofridos, abstendo-se de praticar atos que agravem desnecessariamente o dano final."
            elif "escritura pública" in v_clean.lower() and len(v) < 100:
                new_options[k] = "Da imposição legal de escritura pública para qualquer espécie de avença patrimonial, cuja preterição invalida de pleno direito a manifestação de vontade das partes."
            elif "contratos preliminares" in v_clean.lower() and len(v) < 100:
                new_options[k] = "Da vedação à celebração de contratos preliminares sem a prévia anuência expressa de todos os terceiros que venham a ser potencialmente impactados pelo negócio futuro."
            elif "exceptio non adimpleti contractus" in v_clean.lower() and len(v) < 110:
                new_options[k] = "Da aplicação compulsória da exceptio non adimpleti contractus até mesmo aos negócios unilaterais e benéficos, paralisando a eficácia do ato até a contraprestação do beneficiário."
            elif "exceptio doli" in v_clean.lower() and len(v) < 100:
                new_options[k] = "Exceptio doli generalis, invocada para autorizar a imediata rescisão culposa do contrato em virtude da modificação superveniente e unilateral das bases negociais."
            elif "cláusula resolutiva tácita" in v_clean.lower() and len(v) < 100:
                new_options[k] = "Cláusula resolutiva tácita com eficácia retroativa plena (ex tunc), extinguindo a relação obrigacional originária de pleno direito sem necessidade de notificação premonitória."
            elif "novação subjetiva" in v_clean.lower() and len(v) < 100:
                new_options[k] = "Novação tácita com exoneração total das prestações devidas, extinguindo em definitivo o próprio dever principal de pagar as verbas locatícias subsequentes ajustadas."
            elif "termo aditivo" in v_clean.lower() and len(v) < 100:
                new_options[k] = "É plenamente válido no plano da validade, bastando a lavratura posterior de termo aditivo particular entre as partes para convalidar a forma prescrita pela legislação civil."
            elif "ineficaz perante terceiros" in v_clean.lower() and len(v) < 100:
                new_options[k] = "É negócio que produz eficácia plena e imediata entre os contratantes, sendo apenas inoponível e ineficaz perante terceiros de boa-fé que não integraram a relação jurídica originária."
            elif "pacta sunt servanda foi integralmente abolido" in v_clean.lower():
                new_options[k] = "O princípio do pacta sunt servanda foi integralmente abolido do ordenamento pátrio pelo Código Civil de 2002, restando aos contratantes submeterem previamente qualquer termo ao crivo judicial."
            elif "vontade de uma parte" in v_clean.lower() and len(v) < 110:
                new_options[k] = "Para haver configuração de lide material, basta a manifestação formal de vontade de uma das partes em juízo, dispensando-se a resistência fática efetiva da parte adversa."
            elif "psicológicos internos" in v_clean.lower() and len(v) < 110:
                new_options[k] = "A jurisdição estatal tem por função precípua solucionar conflitos psicológicos de foro íntimo, sendo juridicamente irrelevante a existência de pretensão jurídica patrimonialmente resistida."
            elif len(v) < 100 and corr_len > 140:
                # Expansão inteligente mantendo o sentido do distrator
                if "inexistente" in v_clean.lower():
                    new_options[k] = f"{v_clean}, reputando-se o ato como um não-ato que jamais ingressou no plano da existência jurídica ou produziu efeitos materiais."
                elif "nulo" in v_clean.lower():
                    new_options[k] = f"{v_clean}, acarretando a nulidade absoluta originária do negócio com eficácia ex tunc e impossibilidade de ratificação superveniente."
                elif "anulável" in v_clean.lower():
                    new_options[k] = f"{v_clean}, subordinando a desconstituição do negócio ao ajuizamento de ação anulatória no prazo decadencial estrito previsto no Código Civil."
                elif "eficaz" in v_clean.lower() or "eficácia" in v_clean.lower():
                    new_options[k] = f"{v_clean}, impedindo que o negócio produza qualquer efeito vinculante perante os contratantes e a sociedade até ulterior chancela judicial."
                elif "resolução" in v_clean.lower() or "rescisão" in v_clean.lower():
                    new_options[k] = f"{v_clean}, autorizando a ruptura definitiva do vínculo contratual com recomposição integral do estado anterior e perdas e danos presumidas."
                elif "prescricional" in v_clean.lower() or "prescrição" in v_clean.lower():
                    new_options[k] = f"{v_clean}, sujeito às hipóteses legais de suspensão, interrupção e impedimento do curso temporal reguladas pela parte geral do Código Civil."
                elif "decadencial" in v_clean.lower() or "decadência" in v_clean.lower():
                    new_options[k] = f"{v_clean}, operando a perda definitiva do direito potestativo sem admissão de interrupção ou suspensão, ressalvada expressa previsão legal."
                elif "boa-fé" in v_clean.lower():
                    new_options[k] = f"{v_clean}, impondo aos figurantes contratuais deveres acessórios de conduta, cooperação, lealdade e transparência que limitam o exercício de direitos subjetivos."
                elif "responsabilidade" in v_clean.lower():
                    new_options[k] = f"{v_clean}, respondendo o contratante inadimplente pelo ressarcimento dos prejuízos materiais e extrapatrimoniais provocados à contraparte lesada."
                else:
                    new_options[k] = f"{v_clean}, de acordo com a interpretação restritiva e os princípios gerais aplicáveis às obrigações contratuais no direito civil brasileiro."

        q["options"] = new_options
        updated_count += 1

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"seed_questions.json atualizado: {updated_count} questões processadas.")

def upgrade_seed_multiportas():
    file_path = BASE_DIR / "database" / "seed_multiportas.json"
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    questions = data.get("questions", [])
    updated_count = 0

    for q in questions:
        subject = q.get("subject", "")
        options = q.get("options", {})
        gabarito = q.get("gabarito", "")
        corr_len = len(options.get(gabarito, ""))

        new_options = dict(options)

        for k, v in options.items():
            if k == gabarito:
                continue

            v_clean = v.strip().rstrip(".")

            # Casos específicos de Multiportas com opções curtas
            if "I - Arbitragem; II - Conciliação; III - Autotutela" in v_clean:
                new_options[k] = "I - Arbitragem compulsória de família; II - Conciliação prévia em juizado especial; III - Autotutela judicial repressiva privativa do Estado."
            elif "I - Mediação; II - Autotutela" in v_clean and len(v) < 100:
                new_options[k] = "I - Mediação (foco no restabelecimento do diálogo familiar); II - Autotutela lícita (desforço imediato na defesa da posse); III - Arbitragem (expertise técnica e sigilo)."
            elif "I - Conciliação; II - Mediação; III - Jurisdição" in v_clean:
                new_options[k] = "I - Conciliação direta sem vínculo continuado; II - Mediação comunitária protelatória; III - Jurisdição estatal contenciosa obrigatória perante vara cível."
            elif "I - Autotutela; II - Jurisdição" in v_clean:
                new_options[k] = "I - Autotutela das partes mediante coação legítima; II - Jurisdição estatal privativa de urgência; III - Mediação informal sem força executiva vinculante."
            elif "Frank Sander" in v_clean or "Roscoe Pound" in v_clean:
                if len(v) < 100:
                    new_options[k] = f"{v_clean}, consolidando os métodos adequados de resolução de litígios como política pública de modernização processual do Judiciário."
            elif len(v) < 110 and corr_len > 150:
                if "conciliador" in v_clean.lower() or "conciliação" in v_clean.lower():
                    new_options[k] = f"{v_clean}, cabendo ao facilitador atuar em conflitos objetivos e propor soluções neutras e equilibradas para extinguir a controvérsia pontual."
                elif "mediador" in v_clean.lower() or "mediação" in v_clean.lower():
                    new_options[k] = f"{v_clean}, atuando preferencialmente onde houver vínculo prévio continuado entre os participantes, estimulando a identificação autônoma de interesses."
                elif "arbitragem" in v_clean.lower() or "árbitro" in v_clean.lower():
                    new_options[k] = f"{v_clean}, proferindo decisão heterocompositiva de caráter vinculante e definitivo sobre direitos patrimoniais disponíveis entre sujeitos capazes."
                elif "juizados especiais" in v_clean.lower():
                    new_options[k] = f"{v_clean}, regidos pelos critérios da oralidade, simplicidade, informalidade, economia processual e celeridade instituídos pela Lei 9.099/1995."
                elif "autotutela" in v_clean.lower():
                    new_options[k] = f"{v_clean}, admitida excepcionalmente pela legislação em casos estritos como legítima defesa e desforço imediato proporcional na posse."
                else:
                    new_options[k] = f"{v_clean}, assegurando o devido processo legal e a ampla defesa no tratamento adequado dos litígios no direito brasileiro contemporâneo."

        q["options"] = new_options
        updated_count += 1

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"seed_multiportas.json atualizado: {updated_count} questões processadas.")

if __name__ == "__main__":
    upgrade_seed_questions()
    upgrade_seed_multiportas()

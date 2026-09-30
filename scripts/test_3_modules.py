from database.connection import SessionLocal
from services.adaptive import AdaptiveEngine
from ai.manager import AIProviderManager

db = SessionLocal()
m1 = AdaptiveEngine.get_dashboard_data(db, 'session_test', module='multiportas')
m2 = AdaptiveEngine.get_dashboard_data(db, 'session_test', module='processo_penal')
m3 = AdaptiveEngine.get_dashboard_data(db, 'session_test', module='contratos')

print(f"Multiportas: {len(m1['subjects'])} temas")
print(f"Processo Penal: {len(m2['subjects'])} temas")
print(f"Contratos: {len(m3['subjects'])} temas")

q1 = AIProviderManager.generate_question("Noção de Conflito de Direito e Conflito Social", "Revisão Prova 01", "Médio", db, "session_test", module="multiportas")
q2 = AIProviderManager.generate_question("Juiz das Garantias - Criação e Campo de Atuação", "Revisão 1º Bimestre", "Médio", db, "session_test", module="processo_penal")
q3 = AIProviderManager.generate_question("Exceção do Contrato Não Cumprido e Onerosidade Excessiva", "Revisão Oficial - Contratos", "Médio", db, "session_test", module="contratos")

print("Multiportas Q:", q1["id"], "| Gabarito:", q1["gabarito"], "| Banco:", q1["bank"])
print("Processo Penal Q:", q2["id"], "| Gabarito:", q2["gabarito"], "| Banco:", q2["bank"])
print("Contratos Q:", q3["id"], "| Gabarito:", q3["gabarito"], "| Banco:", q3["bank"])
db.close()

import streamlit as st 
import time

st.set_page_config(page_title="Simulado ENCCEJA - Matemática", layout="centered")

# Lista inicial de questões
questions = [
    {
        "question": "Um trabalhador recebe um salário bruto de R$ 2.800,00 e é descontado em 11% de INSS. Qual o valor do desconto?",
        "options": ["A) R$ 308,00", "B) R$ 280,00", "C) R$ 252,00", "D) R$ 308,88"],
        "answer": "A) R$ 308,00"
    },
    {
        "question": "A loja oferece um desconto de 20% sobre o preço de uma jaqueta de R$ 250,00. Qual o valor a ser pago?",
        "options": ["A) R$ 230,00", "B) R$ 225,00", "C) R$ 200,00", "D) R$ 175,00"],
        "answer": "C) R$ 200,00"
    },
    {
        "question": "Qual é a raiz quadrada exata de 196?",
        "options": ["A) 12", "B) 13", "C) 14", "D) 15"],
        "answer": "C) 14"
    },
    {
        "question": "João percorre 4 km por dia indo e voltando da escola. Em 5 dias, ele percorre:",
        "options": ["A) 10 km", "B) 20 km", "C) 25 km", "D) 40 km"],
        "answer": "D) 40 km"
    },
    {
        "question": "Uma piscina em forma de paralelepípedo tem 10 m de comprimento, 4 m de largura e 2 m de profundidade. Qual o seu volume?",
        "options": ["A) 80 m³", "B) 40 m³", "C) 60 m³", "D) 100 m³"],
        "answer": "A) 80 m³"
    },
    {
        "question": "Se um carro percorre 12 km por litro de gasolina, quantos litros serão necessários para percorrer 300 km?",
        "options": ["A) 20 L", "B) 25 L", "C) 30 L", "D) 35 L"],
        "answer": "B) 25 L"
    },
    {
        "question": "Na sequência aritmética 3, 6, 9, ..., qual é o 10º termo?",
        "options": ["A) 27", "B) 30", "C) 33", "D) 36"],
        "answer": "B) 30"
    },
    {
        "question": "Se um produto custa R$ 600,00 e sofre um aumento de 15%, qual será o novo valor?",
        "options": ["A) R$ 690,00", "B) R$ 660,00", "C) R$ 720,00", "D) R$ 750,00"],
        "answer": "A) R$ 690,00"
    },
    {
        "question": "Qual é o valor da expressão: 2² + 3² + 4²?",
        "options": ["A) 25", "B) 29", "C) 30", "D) 35"],
        "answer": "B) 29"
    },
    {
        "question": "Em uma pesquisa, 3 em cada 5 pessoas preferem filmes de ação. Em um grupo de 120 pessoas, quantas preferem ação?",
        "options": ["A) 60", "B) 72", "C) 80", "D) 90"],
        "answer": "B) 72"
    },
]
questions += [
    {
        "question": (
            "Uma gráfica recebeu um pedido para imprimir 2.000 panfletos em papel A4. Cada resma tem 500 folhas, e a impressora utiliza uma folha a cada dois panfletos (frente e verso). "
            "Durante a impressão, 8% das folhas apresentaram falhas e foram descartadas. Quantas resmas a gráfica deve comprar para atender ao pedido com segurança?"
        ),
        "options": ["A) 4", "B) 5", "C) 6", "D) 7"],
        "answer": "C) 6"
    },
    {
        "question": (
            "Um agricultor planta milho em uma área retangular de 120 m por 80 m. Ele quer dividir essa área em lotes quadrados de maior tamanho possível, sem sobras. "
            "Cada lote deve ser cercado por arame. Qual será o comprimento total de arame necessário para cercar todos os lotes individualmente?"
        ),
        "options": ["A) 4.000 m", "B) 4.800 m", "C) 6.400 m", "D) 7.200 m"],
        "answer": "C) 6.400 m"
    },
    {
        "question": (
            "Em uma pesquisa de consumo de água, uma residência apresentou as seguintes leituras mensais do hidrômetro: 12.340, 12.590, 12.810 e 13.070. "
            "Sabendo que o valor da tarifa por metro cúbico é de R$ 4,80 até 20 m³ e R$ 6,40 acima disso, qual o valor total pago em três meses?"
        ),
        "options": ["A) R$ 345,60", "B) R$ 355,20", "C) R$ 360,80", "D) R$ 374,40"],
        "answer": "B) R$ 355,20"
    },
    {
        "question": (
            "Uma loja oferece desconto progressivo: 10% na primeira peça, 20% na segunda e 30% na terceira. Um cliente compra três peças, cada uma por R$ 100,00. "
            "Qual foi o valor total pago por ele considerando os descontos?"
        ),
        "options": ["A) R$ 240,00", "B) R$ 250,00", "C) R$ 260,00", "D) R$ 270,00"],
        "answer": "C) R$ 260,00"
    },
    {
        "question": (
            "Uma empresa reduziu o consumo de energia elétrica em 12% no primeiro mês, e mais 15% sobre o novo valor no mês seguinte. Se a conta original era de R$ 1.000,00, "
            "qual o valor da conta no segundo mês após os dois descontos?"
        ),
        "options": ["A) R$ 730,00", "B) R$ 748,00", "C) R$ 765,00", "D) R$ 772,00"],
        "answer": "B) R$ 748,00"
    },
    {
        "question": (
            "Uma indústria produz 3.000 parafusos por dia, mas 2,5% são descartados no controle de qualidade. "
            "Após uma modernização, a produção aumentou 20% e os descartes caíram para 1,5%. Quantos parafusos em média passaram no controle após a modernização?"
        ),
        "options": ["A) 3.528", "B) 3.534", "C) 3.540", "D) 3.546"],
        "answer": "A) 3.528"
    },
    {
        "question": (
            "O gráfico de uma função do 2º grau representa o lucro de uma empresa em função do número de unidades vendidas. A função é dada por L(x) = -2x² + 120x - 1.600. "
            "Qual o número de unidades vendidas para obter o lucro máximo e qual o valor desse lucro?"
        ),
        "options": ["A) 30 unidades e R$ 1600", "B) 25 unidades e R$ 1000", "C) 40 unidades e R$ 800", "D) 30 unidades e R$ 400"],
        "answer": "A) 30 unidades e R$ 1600"
    },
    {
        "question": (
            "O dono de uma padaria mistura farinha nacional com farinha importada em uma proporção de 3:2 para preparar um tipo especial de pão. "
            "Se ele deseja produzir 50 kg de mistura, quantos quilos de farinha importada deverá utilizar?"
        ),
        "options": ["A) 20 kg", "B) 25 kg", "C) 30 kg", "D) 35 kg"],
        "answer": "A) 20 kg"
    },
    {
        "question": (
            "Um estudante preenche um tanque com capacidade de 40 litros usando uma torneira que despeja 2,5 litros por minuto. "
            "Ao mesmo tempo, há um vazamento que retira 0,5 litro por minuto. Quanto tempo levará para o tanque encher totalmente?"
        ),
        "options": ["A) 10 min", "B) 12 min", "C) 16 min", "D) 20 min"],
        "answer": "C) 16 min"
    },
    {
        "question": (
            "Um lote de produtos é embalado em caixas com 8 itens cada. Um erro no empacotamento causou uma diferença de 2 itens a menos em 25% das caixas. "
            "Se foram empacotadas 80 caixas, quantos itens, de fato, foram distribuídos?"
        ),
        "options": ["A) 600", "B) 620", "C) 640", "D) 660"],
        "answer": "B) 620"
    },
]
questions += [
    {
        "question": (
            "Durante uma liquidação, uma loja oferece dois tipos de desconto: 25% à vista ou 10% parcelado em 3 vezes sem juros. "
            "Se um produto custa R$ 480,00, quanto o cliente economiza optando pelo pagamento à vista em vez de parcelar?"
        ),
        "options": ["A) R$ 48,00", "B) R$ 72,00", "C) R$ 96,00", "D) R$ 120,00"],
        "answer": "C) R$ 96,00"
    },
    {
        "question": (
            "Um motorista percorre 240 km em 3 horas, mantendo velocidade constante. Em outro dia, no mesmo trajeto, ele gasta 4 horas devido ao trânsito. "
            "Qual a variação percentual na velocidade média entre os dois dias?"
        ),
        "options": ["A) 20%", "B) 25%", "C) 30%", "D) 33,3%"],
        "answer": "D) 33,3%"
    },
    {
        "question": (
            "Um gráfico de barras mostra a população de cinco bairros. No bairro A, há 8.000 habitantes; no B, 6.500; no C, 7.200; no D, 5.800 e no E, 7.500. "
            "Qual a média populacional desses bairros?"
        ),
        "options": ["A) 7.000", "B) 7.200", "C) 7.400", "D) 7.600"],
        "answer": "B) 7.200"
    },
    {
        "question": (
            "O salário de um trabalhador aumentou de R$ 1.500,00 para R$ 1.800,00. Posteriormente, foi aplicado um desconto de 10% no novo valor. "
            "Qual é o valor final recebido após o aumento e o desconto?"
        ),
        "options": ["A) R$ 1.620,00", "B) R$ 1.650,00", "C) R$ 1.700,00", "D) R$ 1.740,00"],
        "answer": "A) R$ 1.620,00"
    },
    {
        "question": (
            "Para calcular o piso de uma sala em formato de L, um pedreiro desenhou o espaço em duas partes retangulares: uma com 4 m x 3 m e outra com 2 m x 3 m. "
            "Sabendo que cada caixa de cerâmica cobre 2 m², quantas caixas ele deve comprar considerando 10% de sobra?"
        ),
        "options": ["A) 9", "B) 10", "C) 11", "D) 12"],
        "answer": "C) 11"
    },
    {
        "question": (
            "Uma estudante faz uma pesquisa e registra a temperatura de uma cidade por 7 dias consecutivos. As temperaturas (em °C) foram: 22, 23, 24, 24, 25, 26, 29. "
            "Qual é a mediana e a média dessas temperaturas, respectivamente?"
        ),
        "options": ["A) 24 e 24,7", "B) 24 e 24,6", "C) 24 e 24", "D) 25 e 24,7"],
        "answer": "A) 24 e 24,7"
    },
    {
        "question": (
            "Uma parede retangular de 2,7 m de altura por 3,5 m de largura será revestida com azulejos de 30 cm por 40 cm. "
            "Quantos azulejos são necessários, desprezando perdas e recortes?"
        ),
        "options": ["A) 72", "B) 75", "C) 78", "D) 81"],
        "answer": "D) 81"
    },
    {
        "question": (
            "Ao aplicar uma sequência de descontos sucessivos de 20% e depois 10% sobre um produto de R$ 500,00, o valor final é:"
        ),
        "options": ["A) R$ 350,00", "B) R$ 360,00", "C) R$ 370,00", "D) R$ 375,00"],
        "answer": "B) R$ 360,00"
    },
    {
        "question": (
            "Uma empresa possui um plano de metas que aumenta a bonificação mensal em função da produtividade. "
            "Se a bonificação segue a fórmula B(n) = 200 + 15n, onde n é o número de dias úteis trabalhados no mês, qual o valor da bonificação para um mês com 22 dias úteis?"
        ),
        "options": ["A) R$ 500", "B) R$ 530", "C) R$ 540", "D) R$ 560"],
        "answer": "B) R$ 530"
    },
    {
        "question": (
            "Um professor distribui R$ 1.200,00 em prêmios para os três melhores alunos, de forma proporcional às notas obtidas: 9, 8 e 7. "
            "Qual valor recebeu o aluno com nota 9?"
        ),
        "options": ["A) R$ 400", "B) R$ 450", "C) R$ 480", "D) R$ 500"],
        "answer": "C) R$ 480"
    },
]
questions += [
    {
        "question": "Qual é o valor de 7 × 8?",
        "options": ["A) 54", "B) 56", "C) 58", "D) 60"],
        "answer": "B) 56"
    },
    {
        "question": "Se João tem R$ 50,00 e gasta R$ 18,00, quanto sobra?",
        "options": ["A) R$ 32,00", "B) R$ 33,00", "C) R$ 34,00", "D) R$ 35,00"],
        "answer": "A) R$ 32,00"
    },
    {
        "question": "Qual é a fração equivalente a 1/2?",
        "options": ["A) 2/4", "B) 3/5", "C) 2/3", "D) 3/6"],
        "answer": "A) 2/4"
    },
    {
        "question": "Qual é o número que, somado com 25, resulta em 80?",
        "options": ["A) 45", "B) 50", "C) 55", "D) 60"],
        "answer": "C) 55"
    },
    {
        "question": "Se um produto custa R$ 90,00 e está com 10% de desconto, qual é o valor final?",
        "options": ["A) R$ 80,00", "B) R$ 81,00", "C) R$ 82,00", "D) R$ 83,00"],
        "answer": "B) R$ 81,00"
    },
    {
        "question": "Quantos metros há em 2,5 km?",
        "options": ["A) 2.500", "B) 250", "C) 25.000", "D) 250.000"],
        "answer": "A) 2.500"
    },
    {
        "question": "Qual é a média aritmética dos números 4, 6 e 10?",
        "options": ["A) 6", "B) 7", "C) 8", "D) 9"],
        "answer": "B) 7"
    },
    {
        "question": "Quantos lados tem um hexágono?",
        "options": ["A) 5", "B) 6", "C) 7", "D) 8"],
        "answer": "B) 6"
    },
    {
        "question": "Qual o valor da expressão 3² + 2²?",
        "options": ["A) 11", "B) 12", "C) 13", "D) 14"],
        "answer": "C) 13"
    },
    {
        "question": "Qual o número que é 25% de 200?",
        "options": ["A) 40", "B) 45", "C) 50", "D) 55"],
        "answer": "C) 50"
    },
]
questions += [
    {
        "question": "Qual é o valor de 7 × 8?",
        "options": ["A) 54", "B) 56", "C) 58", "D) 60"],
        "answer": "B) 56"
    },
    {
        "question": "Se João tem R$ 50,00 e gasta R$ 18,00, quanto sobra?",
        "options": ["A) R$ 32,00", "B) R$ 33,00", "C) R$ 34,00", "D) R$ 35,00"],
        "answer": "A) R$ 32,00"
    },
    {
        "question": "Qual é a fração equivalente a 1/2?",
        "options": ["A) 2/4", "B) 3/5", "C) 2/3", "D) 3/6"],
        "answer": "A) 2/4"
    },
    {
        "question": "Qual é o número que, somado com 25, resulta em 80?",
        "options": ["A) 45", "B) 50", "C) 55", "D) 60"],
        "answer": "C) 55"
    },
    {
        "question": "Se um produto custa R$ 90,00 e está com 10% de desconto, qual é o valor final?",
        "options": ["A) R$ 80,00", "B) R$ 81,00", "C) R$ 82,00", "D) R$ 83,00"],
        "answer": "B) R$ 81,00"
    },
    {
        "question": "Quantos metros há em 2,5 km?",
        "options": ["A) 2.500", "B) 250", "C) 25.000", "D) 250.000"],
        "answer": "A) 2.500"
    },
    {
        "question": "Qual é a média aritmética dos números 4, 6 e 10?",
        "options": ["A) 6", "B) 7", "C) 8", "D) 9"],
        "answer": "B) 7"
    },
    {
        "question": "Quantos lados tem um hexágono?",
        "options": ["A) 5", "B) 6", "C) 7", "D) 8"],
        "answer": "B) 6"
    },
    {
        "question": "Qual o valor da expressão 3² + 2²?",
        "options": ["A) 11", "B) 12", "C) 13", "D) 14"],
        "answer": "C) 13"
    },
    {
        "question": "Qual o número que é 25% de 200?",
        "options": ["A) 40", "B) 45", "C) 50", "D) 55"],
        "answer": "C) 50"
    },
]

questions += [
    {
        "question": "Se 40% de um número é 120, qual é esse número?",
        "options": ["A) 280", "B) 300", "C) 320", "D) 360"],
        "answer": "B) 300"
    },
    {
        "question": "O gráfico de uma função do 1º grau intercepta o eixo y no ponto (0, 2) e passa pelo ponto (2, 6). Qual é a equação dessa função?",
        "options": ["A) y = 2x + 2", "B) y = 3x", "C) y = 2x + 4", "D) y = x + 4"],
        "answer": "A) y = 2x + 2"
    },
    {
        "question": "Quantos lados tem um polígono regular cuja soma dos ângulos internos é 1.260°?",
        "options": ["A) 7", "B) 8", "C) 9", "D) 10"],
        "answer": "C) 9"
    },
    {
        "question": "Qual é o menor número inteiro que satisfaz a desigualdade 3x - 5 > 10?",
        "options": ["A) 4", "B) 5", "C) 6", "D) 7"],
        "answer": "C) 6"
    },
    {
        "question": "Em uma loja, um produto foi reajustado de R$ 200,00 para R$ 250,00. Qual foi o percentual de aumento?",
        "options": ["A) 20%", "B) 25%", "C) 30%", "D) 35%"],
        "answer": "B) 25%"
    },
    {
        "question": "Qual é o próximo número da sequência: 1, 1, 2, 3, 5, 8, ...?",
        "options": ["A) 11", "B) 12", "C) 13", "D) 14"],
        "answer": "C) 13"
    },
    {
        "question": "Um tanque com capacidade de 2.000 litros está cheio. Retira-se 15% do total. Quantos litros ainda restam?",
        "options": ["A) 1.500", "B) 1.600", "C) 1.700", "D) 1.800"],
        "answer": "C) 1.700"
    },
    {
        "question": "Um terreno retangular tem 20 metros de frente e 30 metros de profundidade. Qual é sua área?",
        "options": ["A) 500 m²", "B) 600 m²", "C) 700 m²", "D) 800 m²"],
        "answer": "B) 600 m²"
    },
    {
        "question": "Se a média aritmética entre dois números é 18 e um deles é 12, qual é o outro?",
        "options": ["A) 24", "B) 20", "C) 18", "D) 16"],
        "answer": "A) 24"
    },
    {
        "question": "Um automóvel gasta 8 litros para percorrer 100 km. Quantos litros são necessários para percorrer 350 km?",
        "options": ["A) 28", "B) 30", "C) 32", "D) 35"],
        "answer": "A) 28"
    },
]
questions += [
    {
        "question": "Qual é a solução da equação 2x – 5 = 3x + 4?",
        "options": ["A) x = -9", "B) x = -1", "C) x = 1", "D) x = 9"],
        "answer": "A) x = -9"
    },
    {
        "question": "O gráfico de barras de uma pesquisa mostra que 60% dos entrevistados preferem o produto A. Se participaram 150 pessoas, quantas preferem o produto A?",
        "options": ["A) 90", "B) 100", "C) 110", "D) 120"],
        "answer": "A) 90"
    },
    {
        "question": "Qual é o valor de x na equação: (x - 3)(x + 2) = 0?",
        "options": ["A) x = -3 ou x = 2", "B) x = 3 ou x = -2", "C) x = 3", "D) x = -3"],
        "answer": "B) x = 3 ou x = -2"
    },
    {
        "question": "Qual o valor aproximado de π × 4²?",
        "options": ["A) 12,56", "B) 25,12", "C) 50,24", "D) 16,00"],
        "answer": "C) 50,24"
    },
    {
        "question": "Uma loja oferece um celular por R$ 1.200,00 à vista ou em 10 parcelas de R$ 135,00. Qual é o valor pago a mais no parcelamento?",
        "options": ["A) R$ 100,00", "B) R$ 150,00", "C) R$ 200,00", "D) R$ 300,00"],
        "answer": "B) R$ 150,00"
    },
    {
        "question": "Se em uma sala há 12 meninas e 18 meninos, qual a razão entre o número de meninas e o total de alunos?",
        "options": ["A) 2/3", "B) 3/5", "C) 2/5", "D) 2/6"],
        "answer": "C) 2/5"
    },
    {
        "question": "Qual é o valor de 5³ - 2³?",
        "options": ["A) 117", "B) 98", "C) 125", "D) 97"],
        "answer": "B) 98"
    },
    {
        "question": "Em uma pesquisa, 40% dos entrevistados são mulheres. Se foram entrevistadas 250 pessoas, quantas são homens?",
        "options": ["A) 100", "B) 150", "C) 200", "D) 250"],
        "answer": "B) 150"
    },
    {
        "question": "Se o perímetro de um triângulo equilátero é 72 cm, qual é a medida de cada lado?",
        "options": ["A) 24 cm", "B) 18 cm", "C) 36 cm", "D) 20 cm"],
        "answer": "A) 24 cm"
    },
    {
        "question": "Um gráfico mostra o consumo mensal de energia elétrica em kWh. Se uma casa consumiu 180 kWh em abril e 210 kWh em maio, qual foi a variação percentual de abril para maio?",
        "options": ["A) 15%", "B) 16,7%", "C) 20%", "D) 30%"],
        "answer": "B) 16,7%"
    },
]
import time  # necessário para o timer

if "current_q" not in st.session_state:
    st.session_state.current_q = 0
    st.session_state.correct = 0
    st.session_state.answers = []
    st.session_state.start_time = time.time()



st.title("🧮 Simulado ENCCEJA - Matemática (Ensino Médio)")

# Exibir uma pergunta por vez
if st.session_state.current_q < len(questions):
    q_num = st.session_state.current_q + 1
    total = len(questions)
    st.subheader(f"📘 Questão {q_num} de {total}")

    # Barra de progresso
    progress = q_num / total
    st.progress(progress)

    # Timer simples
    tempo_decorrido = int(time.time() - st.session_state.start_time)
    minutos = tempo_decorrido // 60
    segundos = tempo_decorrido % 60
    st.caption(f"⏱️ Tempo decorrido: {minutos:02d}:{segundos:02d}")
    q = questions[st.session_state.current_q]
    user_answer = st.radio(q["question"], q["options"], key=st.session_state.current_q)

    if st.button("Responder"):
        st.session_state.answers.append(user_answer)

        if user_answer == q["answer"]:
            st.session_state.correct += 1

        st.session_state.current_q += 1
        st.rerun()
else:
    st.subheader("✅ Simulado finalizado!")
    st.write(f"Você acertou **{st.session_state.correct}** de **{len(questions)}** questões.")
    st.write(f"🎯 Aproveitamento: **{round((st.session_state.correct / len(questions)) * 100)}%**")

    # Tempo total
    tempo_total = int(time.time() - st.session_state.start_time)
    minutos = tempo_total // 60
    segundos = tempo_total % 60
    st.write(f"⏱️ Tempo total: **{minutos:02d}:{segundos:02d}**")

    # Mostrar gabarito após o simulado
    with st.expander("📋 Ver gabarito e suas respostas"):
        for i, q in enumerate(questions):
            if i < len(st.session_state.answers):
                correta = "✅" if st.session_state.answers[i] == q["answer"] else "❌"
                st.markdown(f"**Q{i+1}** - {correta} Sua: `{st.session_state.answers[i]}` | Correta: `{q['answer']}`")
            else:
                st.markdown(f"**Q{i+1}** - ❌ Não respondida | Correta: `{q['answer']}`")

    # Botão para reiniciar
    if st.button("🔄 Refazer Simulado"):
        st.session_state.current_q = 0
        st.session_state.correct = 0
        st.session_state.answers = []
        st.session_state.start_time = time.time()  # reinicia o timer
        st.rerun()

      


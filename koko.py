import streamlit as st
import random

st.set_page_config(layout="wide")
st.title("Program Sistem Bilangan")

# =========================
# SIDEBAR MENU
# =========================

menu = st.sidebar.selectbox(
    "Pilih Fitur",
    ["Konversi", "Calculator", "BCD", "Komplemen", "Mini Game"]
)

# mapping basis
base_map = {
    "Biner": 2,
    "Desimal": 10,
    "Oktal": 8,
    "Hexa": 16,
    "Hexadesimal": 16
}

# =========================
# 1 KONVERSI
# =========================
if menu == "Konversi":

    st.subheader("Konversi Sistem Bilangan")

    jenis = st.selectbox(
        "Jenis Bilangan Input",
        ["Biner", "Desimal", "Oktal", "Hexadesimal"]
    )

    bil = st.text_input("Masukkan bilangan")

    if st.button("Konversi"):

        try:
            desimal = int(bil, base_map[jenis])

            st.divider()

            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.write("Biner")
                st.success(format(desimal, 'b'))

            with col2:
                st.write("Desimal")
                st.success(desimal)

            with col3:
                st.write("Oktal")
                st.success(format(desimal, 'o'))

            with col4:
                st.write("Hexa")
                st.success(format(desimal, 'X'))

        except:
            st.error("Input tidak sesuai dengan jenis bilangan")

# =========================
# 2 CALCULATOR
# =========================
elif menu == "Calculator":

    st.subheader("Calculator Sistem Bilangan")

    col1, col2 = st.columns(2)

    with col1:
        jenis1 = st.selectbox(
            "Jenis Bilangan 1",
            ["Biner", "Desimal", "Oktal", "Hexa"]
        )
        bil1 = st.text_input("Bilangan 1")

    with col2:
        jenis2 = st.selectbox(
            "Jenis Bilangan 2",
            ["Biner", "Desimal", "Oktal", "Hexa"]
        )
        bil2 = st.text_input("Bilangan 2")

    operasi = st.selectbox("Operasi", ["+", "-", "*", "/"])

    hasil_basis = st.selectbox(
        "Tampilkan hasil dalam",
        ["Biner", "Desimal", "Oktal", "Hexa"]
    )

    if st.button("Hitung"):

        try:
            a = int(bil1, base_map[jenis1])
            b = int(bil2, base_map[jenis2])

            if operasi == "+":
                hasil = a + b
            elif operasi == "-":
                hasil = a - b
            elif operasi == "*":
                hasil = a * b
            else:
                hasil = a / b

            st.divider()
            st.subheader("Hasil")

            if hasil_basis == "Biner":
                st.success(format(int(hasil), 'b'))

            elif hasil_basis == "Desimal":
                st.success(hasil)

            elif hasil_basis == "Oktal":
                st.success(format(int(hasil), 'o'))

            else:
                st.success(format(int(hasil), 'X'))

        except:
            st.error("Input tidak valid")

# =========================
# 3 BCD
# =========================
elif menu == "BCD":

    st.subheader("Konversi Code Digital")

    jenis = st.selectbox(
        "Jenis Bilangan Input",
        ["Desimal", "Biner", "Oktal", "Hexa"]
    )

    bil = st.text_input("Masukkan bilangan")

    if st.button("Konversi"):

        try:

            desimal = int(bil, base_map[jenis])

            if jenis != "Desimal":
                st.info(f"Input {jenis} dikonversi dulu ke Desimal")

            des_str = str(desimal)

            code8421 = " ".join(format(int(i), '04b') for i in des_str)

            tabel2421 = {
                "0":"0000","1":"0001","2":"0010","3":"0011","4":"0100",
                "5":"1011","6":"1100","7":"1101","8":"1110","9":"1111"
            }

            code2421 = " ".join(tabel2421[i] for i in des_str)

            excess3 = " ".join(format(int(i)+3,'04b') for i in des_str)

            biner = format(desimal,'b')
            gray = biner[0]

            for i in range(1,len(biner)):
                gray += str(int(biner[i-1]) ^ int(biner[i]))

            st.divider()

            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.write("8421 Code")
                st.success(code8421)

            with col2:
                st.write("2421 Code")
                st.success(code2421)

            with col3:
                st.write("Excess-3")
                st.success(excess3)

            with col4:
                st.write("Gray Code")
                st.success(gray)

        except:
            st.error("Input tidak valid")

# =========================
# 4 KOMPLEMEN
# =========================
elif menu == "Komplemen":

    st.subheader("Komplemen Biner")

    biner = st.text_input("Masukkan bilangan biner")

    if st.button("Hitung"):

        if set(biner) - {"0", "1"}:
            st.error("Masukkan hanya angka 0 dan 1")

        else:

            k1 = "".join("1" if i=="0" else "0" for i in biner)
            k2 = format(int(k1,2)+1,'b')

            st.divider()

            col1, col2 = st.columns(2)

            with col1:
                st.write("Komplemen 1")
                st.success(k1)

            with col2:
                st.write("Komplemen 2")
                st.success(k2)

# =========================
# MINI GAME
# =========================
elif menu == "Mini Game":

    st.subheader("Mini Game Sistem Bilangan 🎮")

    difficulty = st.selectbox(
        "Difficulty",
        ["Easy", "Medium", "Hard"]
    )

    mini_menu = st.selectbox(
        "Pilih Game",
        ["Conversion Challenge", "Binary Operation"]
    )

    # =========================
    # SESSION STATE
    # =========================

    if "score" not in st.session_state:
        st.session_state.score = 0

    if "correct" not in st.session_state:
        st.session_state.correct = 0

    if "wrong" not in st.session_state:
        st.session_state.wrong = 0

    if "question_conv" not in st.session_state:
        st.session_state.question_conv = None

    if "question_bin" not in st.session_state:
        st.session_state.question_bin = None

    # =========================
    # RESET
    # =========================

    if st.button("Reset Score"):
        st.session_state.score = 0
        st.session_state.correct = 0
        st.session_state.wrong = 0
        st.session_state.question_conv = None
        st.session_state.question_bin = None

    # =========================
    # LEVEL SYSTEM
    # =========================

    level = "Beginner"

    if st.session_state.score >= 5:
        level = "Binary Explorer"

    if st.session_state.score >= 10:
        level = "Binary Master"

    if st.session_state.score >= 20:
        level = "Binary Legend"

    st.info(f"Level : **{level}**")

    # =========================
    # GAME 1
    # =========================

    if mini_menu == "Conversion Challenge":

        if st.session_state.question_conv is None:

            if difficulty == "Easy":
                num = random.randint(1,50)
            elif difficulty == "Medium":
                num = random.randint(1,200)
            else:
                num = random.randint(1,500)

            bases = ["Biner","Desimal","Oktal","Hexa"]

            from_base = random.choice(bases)
            to_base = random.choice(bases)

            while from_base == to_base:
                to_base = random.choice(bases)

            value = num

            if from_base == "Biner":
                value = format(num,'b')

            elif from_base == "Oktal":
                value = format(num,'o')

            elif from_base == "Hexa":
                value = format(num,'X')

            st.session_state.question_conv = (num,value,from_base,to_base)

        num,value,from_base,to_base = st.session_state.question_conv

        st.info(f"Convert **{value} ({from_base}) → {to_base}**")

        ans = st.text_input("Jawaban")

        if st.button("Submit Answer"):

            correct = num

            if to_base == "Biner":
                correct = format(num,'b')

            elif to_base == "Oktal":
                correct = format(num,'o')

            elif to_base == "Hexa":
                correct = format(num,'X')

            if str(ans).upper() == str(correct):

                st.success("Benar!")
                st.session_state.score += 1
                st.session_state.correct += 1

            else:

                st.error(f"Salah! Jawaban: {correct}")
                st.session_state.wrong += 1

            st.session_state.question_conv = None

        if st.button("Next Question"):
            st.session_state.question_conv = None

    # =========================
    # GAME 2
    # =========================

    elif mini_menu == "Binary Operation":

        if st.session_state.question_bin is None:

            a = random.randint(1,15)
            b = random.randint(1,15)

            op = random.choice(["AND","OR","XOR"])

            st.session_state.question_bin = (a,b,op)

        a,b,op = st.session_state.question_bin

        bin_a = format(a,'b')
        bin_b = format(b,'b')

        st.info(f"{bin_a} {op} {bin_b} = ?")

        ans = st.text_input("Jawaban biner")

        if st.button("Submit Answer"):

            if op == "AND":
                correct = format(a & b,'b')

            elif op == "OR":
                correct = format(a | b,'b')

            else:
                correct = format(a ^ b,'b')

            if ans == correct:

                st.success("Benar!")
                st.session_state.score += 1
                st.session_state.correct += 1

            else:

                st.error(f"Salah! Jawaban: {correct}")
                st.session_state.wrong += 1

            st.session_state.question_bin = None

        if st.button("Next Question"):
            st.session_state.question_bin = None

    # =========================
    # SCOREBOARD
    # =========================

    col1,col2,col3 = st.columns(3)

    with col1:
        st.metric("Score",st.session_state.score)

    with col2:
        st.metric("Benar",st.session_state.correct)

    with col3:
        st.metric("Salah",st.session_state.wrong)
st.divider() 
st.caption("Number System Calculator • Kelompok 4")
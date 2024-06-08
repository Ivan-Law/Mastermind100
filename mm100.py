### Mastermind 100 ###
# A player tries to guess the color ball pattern by placing different combinations of four color balls
# out of six color balls. Feedback from the system regarding how many of the color balls are in the correct
# color and position (black ball) or correct color but incorrect position (white ball). A player wins by
# guessing the pattern within 8 rows of guesses.
#
# Created by Ivan Law (ivan.law@gmail.com)
# Last Update: June 7th, 2024
# Version: 1.0

import random
import streamlit as st

@st.cache_data
def genNum():
    a1 = random.randint(1, 6)
    a2 = random.randint(1, 6)
    a3 = random.randint(1, 6)
    a4 = random.randint(1, 6)
    a = str(a1) + str(a2) + str(a3) + str(a4)
    return a

def replaceFirstAppear(orglist, replaceThis, symbol):
    newlist = []
    first = 0
    for x in orglist:
        if x != replaceThis:
            newlist.append(x)
        else:
            if first == 0:
                newlist.append(symbol)
                first = 1
            else:
                newlist.append(x)
    s = ''.join(newlist)
    return s

def noBlack(myGus1, myRes1, black):
    s = []
    t = []
    for x in range(len(myGus1)):
        if myGus1[x] == myRes1[x]:
            s.append('-')
            t.append('=')
        else:
            s.append(myGus1[x])
            t.append(myRes1[x])
        for y in range(len(myRes1)):
            if x == y and myGus1[x] == myRes1[y]:
                black += 1
    myGus1 = s
    myRes1 = t
    return black, myGus1, myRes1

def noWhite(myGusX, myResX, white):
    myResTmp = myResX
    for x in range(len(myGusX)):
        if myGusX[x] in myResTmp:
            if myGusX[x] != myResTmp[x]:
                white += 1
                myResTmp = replaceFirstAppear(myResTmp, myGusX[x], '=')
    return white

def myGuess(guessNum, resNum):
    black = 0
    white = 0
    myGus1 = guessNum
    myRes1 = resNum
    black, myGus1, myRes1 = noBlack(myGus1, myRes1, black)
    white = noWhite(myGus1, myRes1, white)
    return black, white

def game():
    st.markdown("""
            <style>
                .block-container {
                        padding-top: 3rem;
                        padding-bottom: 0rem;
                        padding-left: 1rem;
                        padding-right: 0rem;
                    }
                .stApp {
                        background-color: black;
                    }
            </style>
            """, unsafe_allow_html=True)

    st.write(r"""$\textsf{\Huge Mastermind💯}$<br>🔴🟠🟡🟢🔵🟣 By Ivan Law""", unsafe_allow_html=True)
    st.caption("""Rule 1: Choose 4 color balls (can be repeated).  \n"""
               """Rule 2: You will get feedback of black ball"""
               """ (correct color and position) or white ball"""
               """ (correct color but incorrect position).  \n"""
               """Rule 3: You have 8 chances to guess. Good Luck!""", unsafe_allow_html=True)

    if "allResult" not in st.session_state:
        st.session_state['allResult'] = 'Your guess        Checking\n'
    if "color" not in st.session_state:
        st.session_state['color'] = ''
    if "check" not in st.session_state:
        st.session_state['check'] = ''
    if "number" not in st.session_state:
        st.session_state['number'] = ''
    if "sum" not in st.session_state:
        st.session_state.sum = 0
    if "guess" not in st.session_state:
        st.session_state.guess = 0

    myRes = genNum()

    def ResBalls(myRes):
        resultballs = ''
        for x in range(len(myRes)):
            if myRes[x] == '1':
                resultballs += "🔴"
            if myRes[x] == '2':
                resultballs += "🟠"
            if myRes[x] == '3':
                resultballs += "🟡"
            if myRes[x] == '4':
                resultballs += "🟢"
            if myRes[x] == '5':
                resultballs += "🔵"
            if myRes[x] == '6':
                resultballs += "🟣"
        return resultballs

    def BlackCheck():
        st.session_state['check'] += "⚫"

    def WhiteCheck():
        st.session_state['check'] += "⚪"

    def Red():
        st.session_state['color'] += "🔴"
        st.session_state['number'] += "1"
        st.session_state.sum += 1

    def Orange():
        st.session_state['color'] += "🟠"
        st.session_state['number'] += "2"
        st.session_state.sum += 1

    def Yellow():
        st.session_state['color'] += "🟡"
        st.session_state['number'] += "3"
        st.session_state.sum += 1

    def Green():
        st.session_state['color'] += "🟢"
        st.session_state['number'] += "4"
        st.session_state.sum += 1

    def Blue():
        st.session_state['color'] += "🔵"
        st.session_state['number'] += "5"
        st.session_state.sum += 1

    def Purple():
        st.session_state['color'] += "🟣"
        st.session_state['number'] += "6"
        st.session_state.sum += 1

    def removeLast(a):
        b = list(a)
        b = b[:-1]
        b = "".join(b)
        b = str(b)
        return b

    def Back():
        st.session_state['color'] = removeLast(st.session_state['color'])
        st.session_state['number'] = removeLast(st.session_state['number'])
        if st.session_state.sum <= 0:
            st.session_state.sum = 0
        else:
            st.session_state.sum -= 1

    def disable(b):
        st.session_state["disabled"] = b

    def clear_cache():
        st.session_state.guess = 0
        st.cache_data.clear()
        st.session_state['allResult'] = 'Your guess        Checking\n'
        disable(False)

    with st.container(height=200):
         st.text(st.session_state['allResult'])
    st.write("Chosen color:", st.session_state['color'])
    st.write("Remaining guess:", 8 - st.session_state.guess)
    # st.write("My number:", st.session_state['number'])
    # st.write("Sum:", st.session_state.sum)
    # st.write("myRes", myRes)

    if st.session_state.sum % 4 == 0 and st.session_state.sum != 0:
        if st.button("🔙Back", on_click=Back, disabled=st.session_state.get("disabled", False)):
            pass
        if st.button("✅Confirm", on_click=disable, args=(True,), disabled=st.session_state.get("disabled", False)):

            st.session_state['check'] += st.session_state['color']
            st.session_state['check'] += "         "

            black, white = myGuess(st.session_state['number'], myRes)
            if black > 0:
                for i in range(1, black+1):
                    BlackCheck()
            if white > 0:
                for j in range(1, white+1):
                    WhiteCheck()

            st.session_state['allResult'] += st.session_state['check']
            st.session_state['allResult'] += "  \n"

            thisResult = "Checking result:  \n" + st.session_state['check']
            st.text(thisResult)
            del st.session_state['color']
            del st.session_state['number']
            del st.session_state['check']
            st.session_state.sum = 0
            st.session_state.guess += 1

            if black == 4:
                st.balloons()
                st.write(r"$\textsf{\Huge You Win!💯🎉}$")
                st.text(st.session_state['allResult'])
                if st.button("Let's play again!😎👍", on_click=clear_cache):
                    game()
            else:
                if st.session_state.guess % 8 != 0:
                    st.button("Let's continue to guess!🤔", on_click=disable, args=(False,))

            if st.session_state.guess % 8 == 0 and st.session_state.guess != 0 and black != 4:
                st.write(r"$\textsf{\Huge You Lose!😮‍💨}$")
                st.write("The balls should be:")
                st.write("ResultBalls", ResBalls(myRes))
                if st.button("Let's play again!🆗", on_click=clear_cache):
                    game()
    else:
        st.write('''<style>
        [data-testid="column"] {
            width: calc(33.3333% - 1rem) !important;
            flex: 1 1 calc(33.3333% - 1rem) !important;
            min-width: calc(33% - 1rem) !important;
        }
        </style>''', unsafe_allow_html=True)
        col = st.columns(3)
        with col[0]:
            st.button(r"$\textsf{\Huge🔴}$", on_click=Red)
            st.button(r"$\textsf{\Huge🟠}$", on_click=Orange)
        with col[1]:
            st.button(r"$\textsf{\Huge🟡}$", on_click=Yellow)
            st.button(r"$\textsf{\Huge🟢}$", on_click=Green)
        with col[2]:
            st.button(r"$\textsf{\Huge🔵}$", on_click=Blue)
            st.button(r"$\textsf{\Huge🟣}$", on_click=Purple)
            st.button("️️◀️◀️Back", on_click=Back)

if __name__ == "__main__":
    game()

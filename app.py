from ast import Num
from os import POSIX_SPAWN_CLOSE
import streamlit as st
import pyperclip
import random

class pwGenerator:
    def __init__(self):
        self.numLower = 0
        self.charList = []
        self.pwString = []
        for i in range(97, 123, 1):
            self.charList.append(chr(i))

    def renderGUI(self) -> None:
        st.slider("Number of Characters", min_value=6, max_value=20, value=8, key="numChars")

    def passwordString(self):
        for i in range(self.numLower):
            self.pwString.append(random.choice(self.charList))
        return self.pwString
    
    
    def generate(self, num):
        self.numLower = num
        random.shuffle(self.passwordString())
        my_password = ''.join(self.pwString)
        return my_password

class strongGenerator(pwGenerator):

    def __init__(self):
        super().__init__()
        self.numUpper = 0
        self.upperList = []
        for i in range(65, 91, 1):
            self.upperList.append(chr(i))

    
    def renderGUI(self):
        st.slider("Number of Characters", min_value=6, max_value=20, value=8, key="numChars")
        st.slider("number of uppercase characters", min_value=0, max_value=10, value=3, key="numUpper")


    def passwordString(self, upper):
        super().passwordString()
        for i in range(upper):
            self.pwString.append(random.choice(self.upperList))
    

    def generate(self, num, numUpper):
        if ((num - numUpper) > 0):            
            self.numUpper = numUpper
            self.numLower = num - numUpper

            self.passwordString(numUpper)

            random.shuffle(self.pwString)
            return ''.join(self.pwString)
        else:
            return "!number of upper case characters can't exceed number of characters!"
    

class extremeGenerator(strongGenerator):
    def __init__(self):
        super().__init__()
        self.numSpecial = 0
        self.specialList = []
        for i in range(33, 48, 1):
            self.specialList.append(chr(i))

    def renderGUI(self):
        st.slider("Number of Characters", min_value=6, max_value=20, value=8, key="numChars")
        st.slider("number of uppercase characters", min_value=0, max_value=10, value=3, key="numUpper")
        st.slider("number of special characters", min_value=0, max_value=10, value=0, key="numSpecial")

    def passwordString(self, upper, special):
        super().passwordString(upper)

        for i in range(special):
            self.pwString.append(random.choice(self.specialList))


    def generate(self, num, upperNo, special):

        self.numLower = num - upperNo - special
        if self.numLower > 0:
            # self.numUpper = upperNo
            # self.numSpecial = special

            self.passwordString(upperNo, special)
            random.shuffle(self.pwString)
            return ''.join(self.pwString)            
        else: 
            return "sum of upper and special characters can't exceed number of characters"

st.subheader("Password Generator")


selected = st.selectbox("Select your password model: ", 
                        ["------------------------",
                        "Simple Password", 
                        "Strong Password", 
                        "Very Strong Password"])
if (selected) == "Simple Password":
    pw = pwGenerator()
    pw.renderGUI()
    if (st.button("GENERATE", key="btnGenerate")):        
        my_password = pw.generate(st.session_state.numChars)
        st.text_input("generated password", value=my_password, key="my_password")


elif (selected) == "Strong Password":
    pw = strongGenerator()
    pw.renderGUI()
    if (st.button("GENERATE", key="btnGenerate")):        
        my_password = pw.generate(st.session_state.numChars, st.session_state.numUpper)
        st.text_input("generated password", value=my_password, key="my_password") 

        
elif (selected) == "Very Strong Password":
    pw = extremeGenerator()
    pw.renderGUI()
    if (st.button("GENERATE", key="btnGenerate")):
        my_password = pw.generate(st.session_state.numChars, st.session_state.numUpper, st.session_state.numSpecial)
        st.text_input("generated password", value=my_password, key="my_password")


else:
    st.write("please select available model")

# st.slider("number of characters:", min_value=8, max_value=20, value=10, key="numChars")
# st.slider("number of uppercase characters", min_value=0, max_value=10, value=3, key="numUpper")
# st.slider("number of numbers", min_value=0, max_value=10, value=3, key="numNumber")
# st.slider("number of special characters", min_value=0, max_value=10, value=3, key="numSpecial")

# if (st.button("GENERATE", key="btnGenerate")):
#     # password = st.session_state.numChars
#     my_password = pw.generate(st.session_state.numChars, st.session_state.numUpper, st.session_state.numSpecial)
#     st.text_input("generated password", value=my_password)





if (st.button("COPY")):
    pyperclip.copy(st.session_state.my_password)




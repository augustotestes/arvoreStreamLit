# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 19:19:34 2022

@author: mirkos
"""

import streamlit as st
import pickle
from sklearn.tree import DecisionTreeClassifier

#carregar o modelo da arvore

arquivo = open('arvore.pkl','rb')
arvore = pickle.load(arquivo)

individuo = []

st.text_input('Digite o sexo do paciente (masculino/feminino)',key='sexo')
if st.session_state.sexo.lower() == 'masculino':
    individuo.append(0)
else:
    individuo.append(1)
    
st.text_input('Qual a idade do paciente?',key='idade')
idade = int(st.session_state.idade)
if 59<idade<70:
    individuo.append(0)
else:
  if 2<idade<5:
    individuo.append(1)
  else:
    if 49<idade<60:
      individuo.append(2)
    else:
      if 4<idade<10:
        individuo.append(3)
      else:
          if 29<idade<40:
            individuo.append(4)
          else:
              if 69<idade<80:
                individuo.append(5)
              else:
                  if 9<idade<15:
                    individuo.append(6)
                  else:
                      if idade<2:
                        individuo.append(7)
                      else:
                          if 19<idade<30:
                            individuo.append(8)
                          else:
                              if 14<idade<20:
                                individuo.append(9)
                              else:
                                  if 39<idade<40:
                                    individuo.append(10)
                                  else:
                                        individuo.append(11)
st.text_input('O paciente está hospitalizado? (s/n)',key='hospitalizado')
if st.session_state.hospitalizado.lower()=='s':
    individuo.append(0)
else:
    individuo.append(1)
    
st.text_input('O paciente tem febre? (s/n)',key='febre')
if st.session_state.febre == 's':
    individuo.append(0)
else:
    individuo.append(1)
    
st.text_input("O indivíduo tem tosse? sim | nao:",key='tosse')
if st.session_state.tosse == 'n':
    individuo.append(0)
else:
    individuo.append(1)
    
st.text_input("O indivíduo tem dor de garganta? sim | nao",key='garganta')
if st.session_state.garganta == 'sim':
    individuo.append(0)
else:
    individuo.append(1)
#-------------------dispneia
st.text_input("O indivíduo tem dispneia? sim | nao | nao informado",key='dispneia')
if st.session_state.dispneia == 'sim':
    individuo.append(0)
else:
    if st.session_state.dispneia == 'nao info':
        individuo.append(1)
    else:
        if st.session_state.dispneia =='nao':
            individuo.append(2)
            
st.text_input("O indivíduo é gestante? sim | nao",key='gestante')
if st.session_state.gestante == 'sim':
    individuo.append(0)
else:
    individuo.append(1)
    
st.text_input("O indivíduo se identifica com qual raça/cor? nao informa | preta | parda | indigena | branca | amarela",key='raca')

if st.session_state.raca == 'nao informa':
    individuo.append(0)
else:
    if  st.session_state.raca == 'preta':
        individuo.append(1)
    else:
        if  st.session_state.raca == 'parda':
            individuo.append(2)
        else:
            if  st.session_state.raca == 'indigena':
                individuo.append(3)
            else:
                if st.session_state.raca == 'branca':
                    individuo.append(4)
                else:
                    if  st.session_state.raca == 'amarela':
                        individuo.append(5)
st.text_input("O indivíduo desenvolveu Sindrome Respiratória Aguda Grave (SRAG)? sim | nao",key='srag')

if st.session_state.srag == 'sim':
    individuo.append(0)
else:
    individuo.append(1)

resultado = arvore.predict([individuo])
st.write(resultado)




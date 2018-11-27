# coding=utf-8
# python 2.7
# 
# Alunos:
# - Leonardo Ortiz
# - Daniel Welter
# Apresentação
# https://docs.google.com/presentation/d/1RIf1WofLys628svTFFoB0JdE_Jk12tWN61XM38ulXi8/edit?usp=sharing

def print_obj(obj):
    attrs = vars(obj)
    print ', '.join("%s: %s" % item for item in attrs.items())
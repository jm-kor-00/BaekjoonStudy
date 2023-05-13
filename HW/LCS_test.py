from LCS_memo import lcs_memo
from LCS_table import lcs_dp
from LCS_traceback import lcs_dp_traceback

X = "DATA STRUCTURE"
Y = "PYTHON ALGORITHM"
memo = {}
print("======================================================")
print("비교할 문자열\n")
print("X :",X)
print("Y :",Y)
print("======================================================")
print("메모지에이션을 통한 구현(Top-Down) : ",end='')
print(lcs_memo(X, Y, len(X), len(Y), memo))
print("======================================================")
print("테뷸레이션을 통한 구현(Bottom-Up) : ",end='')
L,res = lcs_dp(X,Y)
print(res)
print("======================================================")
print("LCS추적결과 :",lcs_dp_traceback(X,Y,L))
def function(parameter):
    #parameter를 사용해서 행동을 함
    print(parameter)
    result = parameter * 2
    result += parameter
    result //= 2
    return result
    #return에는 모든 자료형이 올 수 있다.
    #리스트, 정수, 실수, True/False, 튜플 등등

#사용할 때, 반환값이 있는 함수라면?
A = function()

#반환값이 필요없다면? 그냥 사용가능
function()
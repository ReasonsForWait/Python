# 왼쪽 오른쪽

# 문제 설명
# 문자열 리스트 str_list에는 "u", "d", "l", "r" 네 개의 문자열이 여러 개 저장되어 있습니다. 
# str_list에서 "l"과 "r" 중 먼저 나오는 문자열이 "l"이라면 해당 문자열을 기준으로 왼쪽에 있는 문자열들을 순서대로 담은 리스트를, 
# 먼저 나오는 문자열이 "r"이라면 해당 문자열을 기준으로 오른쪽에 있는 문자열들을 순서대로 담은 리스트를 return하도록 solution 함수를 완성해주세요. "l"이나 "r"이 없다면 빈 리스트를 return합니다.

# 제한사항
# 1 ≤ str_list의 길이 ≤ 20
# str_list는 "u", "d", "l", "r" 네 개의 문자열로 이루어져 있습니다.

# str_list = ["u", "u", "r", "r"]

def solution1(str_list):
    for i, v in enumerate(str_list):
        if v == "l":
            return str_list[:i]
        
        if v == "r":
            return str_list[i + 1:]
        
    return []


# s(str_list)

#---------------------------------------------------------------------------------------------------------------------------------------

# 숨어있는 숫자의 덧셈 (2)

# 문제 설명
# 문자열 my_string이 매개변수로 주어집니다. my_string은 소문자, 대문자, 자연수로만 구성되어있습니다. 
# my_string안의 자연수들의 합을 return하도록 solution 함수를 완성해주세요.

# 제한사항
# 1 ≤ my_string의 길이 ≤ 1,000
# 1 ≤ my_string 안의 자연수 ≤ 1000
# 연속된 수는 하나의 숫자로 간주합니다.
# 000123과 같이 0이 선행하는 경우는 없습니다.
# 문자열에 자연수가 없는 경우 0을 return 해주세요.

# TODO 못푼 문제

#-------------------------

# 최솟값 만들기

# 문제 설명
# 길이가 같은 배열 A, B 두개가 있습니다. 각 배열은 자연수로 이루어져 있습니다.
# 배열 A, B에서 각각 한 개의 숫자를 뽑아 두 수를 곱합니다. 이러한 과정을 배열의 길이만큼 반복하며, 두 수를 곱한 값을 누적하여 더합니다. 이때 최종적으로 누적된 값이 최소가 되도록 만드는 것이 목표입니다. (단, 각 배열에서 k번째 숫자를 뽑았다면 다음에 k번째 숫자는 다시 뽑을 수 없습니다.)

# 예를 들어 A = [1, 4, 2] , B = [5, 4, 4] 라면

# A에서 첫번째 숫자인 1, B에서 첫번째 숫자인 5를 뽑아 곱하여 더합니다. (누적된 값 : 0 + 5(1x5) = 5)
# A에서 두번째 숫자인 4, B에서 세번째 숫자인 4를 뽑아 곱하여 더합니다. (누적된 값 : 5 + 16(4x4) = 21)
# A에서 세번째 숫자인 2, B에서 두번째 숫자인 4를 뽑아 곱하여 더합니다. (누적된 값 : 21 + 8(2x4) = 29)
# 즉, 이 경우가 최소가 되므로 29를 return 합니다.

# 배열 A, B가 주어질 때 최종적으로 누적된 최솟값을 return 하는 solution 함수를 완성해 주세요.

def solution2(A, B):
    A = sorted(A)
    B = sorted(B)[::-1]
    
    min_value = 0
    for i in range(len(A)):
        min_value += A[i] * B[i]

    return min_value

# s([1,2,3,2], [1,3,6,5])

def solution3(operations):
    queue = []
    for i in operations:
        word, num = list(i.split())

        if word == "I":
            queue.append(int(num))
        else:
            if len(queue) != 0:
                if num == "1":
                    queue.remove(max(queue))
                else:
                    queue.remove(min(queue))
                
    if len(queue) == 0:
        return [0,0]
    else:
        return [max(queue), min(queue)]
    
# solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"])

#----------------------------------------------------------------------------------------------------------------

# 조건에 맞게 수열 변환하기 2

# 문제 설명
# 정수 배열 arr가 주어집니다. arr의 각 원소에 대해 값이 50보다 크거나 같은 짝수라면 2로 나누고, 50보다 작은 홀수라면 2를 곱하고 다시 1을 더합니다.

# 이러한 작업을 x번 반복한 결과인 배열을 arr(x)라고 표현했을 때, arr(x) = arr(x + 1)인 x가 항상 존재합니다. 이러한 x 중 가장 작은 값을 return 하는 solution 함수를 완성해 주세요.

# 단, 두 배열에 대한 "="는 두 배열의 크기가 서로 같으며, 같은 인덱스의 원소가 각각 서로 같음을 의미합니다.

# 제한사항
# 1 ≤ arr의 길이 ≤ 1,000,000
# 1 ≤ arr의 원소의 값 ≤ 100

def solution4(arr):
    chk = True
    count = 0
    while(chk):
        new_arr = []
        for v in arr:
            if v >= 50 and v % 2 == 0:
                new_arr.append(int(v / 2))
            elif v < 50 and v % 2 == 1:
                new_arr.append(v * 2 + 1)
            else:
                new_arr.append(v)
            
        count += 1
        n = len(arr)
        for i in range(len(arr)):
            if arr[i] == new_arr[i]:
                n -= 1

            if n == 0:
                chk = False
                
        arr = new_arr
        
    return count - 1

#----------------------------------------------------------------------------------------------------------------------------------------------------------------

# 잘라서 배열로 저장하기

# 문제 설명
# 문자열 my_str과 n이 매개변수로 주어질 때, my_str을 길이 n씩 잘라서 저장한 배열을 return하도록 solution 함수를 완성해주세요.

# 제한사항
# 1 ≤ my_str의 길이 ≤ 100
# 1 ≤ n ≤ my_str의 길이
# my_str은 알파벳 소문자, 대문자, 숫자로 이루어져 있습니다.

def solution5(my_str, n):
    result = []
    while(len(my_str) != 0):
        result.append(my_str[:n])
        my_str = my_str[n:]
        
    return result

#------------------------------------------------------------------------------------------------------------------------------------------------------------

# 다항식 더하기

# 문제 설명
# 한 개 이상의 항의 합으로 이루어진 식을 다항식이라고 합니다. 다항식을 계산할 때는 동류항끼리 계산해 정리합니다. 
# 덧셈으로 이루어진 다항식 polynomial이 매개변수로 주어질 때, 동류항끼리 더한 결괏값을 문자열로 return 하도록 solution 함수를 완성해보세요. 
# 같은 식이라면 가장 짧은 수식을 return 합니다.

# TODO 실패작 고치기

def solution6(polynomial):
    x = 0
    num = 0
    arr = polynomial.split()[::2]
    for i in arr:
        if "x" in i:
            print(i)
            if i[0] == "x":
                x += 1
            elif i[0] == "-":
                x -= int(i[1:len(i) - 1])
            else:
                x += int(i[:len(i) - 1])
        else:
            print(i)
            if i[0] == "-":
                num -= int(i[1:])
            else:
                num += int(i)
        
    if num != 0:
        return str(x) + "x + " + str(num)
    else:
        return str(x) + "x"

# print(solution4("-3x + -7 + x"))

# JS로 구현성공

# function solution(polynomial) {
#     let arr = polynomial.split(" ");
#     let x = 0;
#     let num = 0;
#     for (let i = 0; i < arr.length; i += 2) {
#         if (arr[i].includes("x")) {
#             if(arr[i].length == 1){
#                 x += 1
#             } else {
#                 x += +arr[i].slice(0, -1);
#             }
#         } else {
#                 num += +arr[i];
#             }
#         }
    
#     if (x != 0 && num != 0) {
#         return x == 1 ? `x + ${num}` : `${x}x + ${num}`;
#     } else if (x != 0 && num == 0) {
#         return x == 1 ? `x` : `${x}x`
#     } else if (x == 0 && num != 0) {
#         return `${num}`
#     }
# }

#----------------------------------------------------------------------------------------

# 뒤에서 5등까지
# TODO 문제 1
# https://school.programmers.co.kr/learn/courses/30/lessons/181853
# 문제

# 문제 설명
# 정수로 이루어진 리스트 num_list가 주어집니다. num_list에서 가장 작은 5개의 수를 오름차순으로 담은 리스트를 return하도록 solution 함수를 완성해주세요.

# 제한사항
# 6 ≤ num_list의 길이 ≤ 30
# 1 ≤ num_list의 원소 ≤ 100

def solution7(num_list):
    return sorted(num_list)[:5]

solution7([1,34,5,77,9,12])

#----------------------------------------------------------------------------------------------------------------------------------------------

# 안전지대

# 문제 설명
# 다음 그림과 같이 지뢰가 있는 지역과 지뢰에 인접한 위, 아래, 좌, 우 대각선 칸을 모두 위험지역으로 분류합니다.

# 지뢰는 2차원 배열 board에 1로 표시되어 있고 board에는 지뢰가 매설 된 지역 1과, 지뢰가 없는 지역 0만 존재합니다.
# 지뢰가 매설된 지역의 지도 board가 매개변수로 주어질 때, 안전한 지역의 칸 수를 return하도록 solution 함수를 완성해주세요.

# 제한사항
# board는 n * n 배열입니다.
# 1 ≤ n ≤ 100
# 지뢰는 1로 표시되어 있습니다.
# board에는 지뢰가 있는 지역 1과 지뢰가 없는 지역 0만 존재합니다.

# TODO 좀더 간단히 고쳐보기

def solution8(board):
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                if i != 0 and j != 0: 
                    if board[i-1][j-1] != 1:
                        board[i-1][j-1] = 2
                if i != 0:
                    if board[i-1][j] != 1:
                        board[i-1][j] = 2
                if i != 0 and j != n-1:
                    if board[i-1][j+1] != 1:
                        board[i-1][j+1] = 2
                if j != 0:
                    if board[i][j-1] != 1:
                        board[i][j-1] = 2
                if j != n-1:
                    if board[i][j+1] != 1:
                        board[i][j+1] = 2
                if i != n-1 and j != 0:
                    if board[i+1][j-1] != 1:
                        board[i+1][j-1] = 2
                if i != n-1:
                    if board[i+1][j] != 1:
                        board[i+1][j] = 2
                if i != n-1 and j != n-1:
                    if board[i+1][j+1] != 1:
                        board[i+1][j+1] = 2
    
    count = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                count += 1
                
    return count

#---------------------------------------------------------------------------------------------------------------

# 문자열이 몇번 등장하는지 세기

# 문제 설명
# 문자열 myString과 pat이 주어집니다. myString에서 pat이 등장하는 횟수를 return 하는 solution 함수를 완성해 주세요.

# 제한사항
# 1 ≤ myString ≤ 1000
# 1 ≤ pat ≤ 10

def solution9(myString, pat):
    result = 0
    for i in range(len(myString) - len(pat) + 1):
        if myString[i:len(pat) + i] == pat:
            result += 1
            
    return result

#------------------------------------------------------------------------------------------------------------------------

# 전국 대회 선발 고사

# 문제 설명
# 0번부터 n - 1번까지 n명의 학생 중 3명을 선발하는 전국 대회 선발 고사를 보았습니다. 등수가 높은 3명을 선발해야 하지만, 개인 사정으로 전국 대회에 참여하지 못하는 학생들이 있어 참여가 가능한 학생 중 등수가 높은 3명을 선발하기로 했습니다.

# 각 학생들의 선발 고사 등수를 담은 정수 배열 rank와 전국 대회 참여 가능 여부가 담긴 boolean 배열 attendance가 매개변수로 주어집니다. 전국 대회에 선발된 학생 번호들을 등수가 높은 순서대로 각각 a, b, c번이라고 할 때 10000 × a + 100 × b + c를 return 하는 solution 함수를 작성해 주세요.

# 제한사항
# 3 ≤ rank의 길이 = attendance의 길이 ≤ 100
# rank[i]는 i번 학생의 선발 고사 등수를 의미합니다.
# rank의 원소는 1부터 n까지의 정수로 모두 서로 다릅니다.
# attendance[i]는 i번 학생의 전국 대회 참석 가능 여부를 나타냅니다.
# attendance[i]가 true라면 참석 가능, false면 참석 불가능을 의미합니다.
# attendance의 원소 중 적어도 3개는 true입니다.

def solution10(rank, attendance):
    rank_dic = {}
    rank_arr = []
    for i, v in enumerate(attendance):
        if v:
            rank_dic[rank[i]] = i
            rank_arr.append(rank[i])
            
    a = sorted(rank_arr)[0]
    b = sorted(rank_arr)[1]
    c = sorted(rank_arr)[2]
    
    return 10000 * rank_dic[a] + 100 * rank_dic[b] + rank_dic[c]

#------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 구명보트

# 문제 설명
# 무인도에 갇힌 사람들을 구명보트를 이용하여 구출하려고 합니다. 구명보트는 작아서 한 번에 최대 2명씩 밖에 탈 수 없고, 무게 제한도 있습니다.

# 예를 들어, 사람들의 몸무게가 [70kg, 50kg, 80kg, 50kg]이고 구명보트의 무게 제한이 100kg이라면 2번째 사람과 4번째 사람은 같이 탈 수 있지만 1번째 사람과 3번째 사람의 무게의 합은 150kg이므로 구명보트의 무게 제한을 초과하여 같이 탈 수 없습니다.

# 구명보트를 최대한 적게 사용하여 모든 사람을 구출하려고 합니다.

# 사람들의 몸무게를 담은 배열 people과 구명보트의 무게 제한 limit가 매개변수로 주어질 때, 모든 사람을 구출하기 위해 필요한 구명보트 개수의 최솟값을 return 하도록 solution 함수를 작성해주세요.

# 제한사항
# 무인도에 갇힌 사람은 1명 이상 50,000명 이하입니다.
# 각 사람의 몸무게는 40kg 이상 240kg 이하입니다.
# 구명보트의 무게 제한은 40kg 이상 240kg 이하입니다.
# 구명보트의 무게 제한은 항상 사람들의 몸무게 중 최댓값보다 크게 주어지므로 사람들을 구출할 수 없는 경우는 없습니다.

# TODO 고치기

def solution11(people, limit):
    count = 0
    while(len(people) != 0):
        weight = people.pop()
        print(weight)
        while(weight < limit):
            if weight + people.pop() > limit:
                break
            else:
                weight += people.pop()

            print(weight)
            
        count += 1
    
    print(count)
    return count

solution11([70, 50, 80, 50], 100)

#--------------------------------------------------------------------------------------------------------------------------------------

# PCCE 모의고사 1회 10번

# 문제 설명
# 애너그램(Anagram) 이란 주어진 단어를 이루는 문자의 위치를 뒤바꾸어 새로운 단어를 만드는 것을 말합니다. 애너그램을 이용해 암호화, 복호화를 하려고합니다.

# 암, 복호화할 단어와 애너그램 테이블이 주어집니다. 애너그램 테이블은 단어를 암호화한 후의 문자들의 위치가 저장되어 있습니다.

# 예를들어 문자열 "Hello"를 암호화  할 때, 애너그램 테이블이 [4, 2, 0, 1, 3]이면, 문자열의 0번째 값인 'H'는 애너그램 테이블의 0번째 값에 해당하는 4에 의해 4번째로 이동하고 같은 방식으로 'e'는 2번째로, 'l'은 0번째로, 'l'은 1번째로, 'o'는 3번째로 이동하여 "lleoH"가 됩니다.

# 위의 방법으로 만들어진 애너그램 암호문을 복호화하려면 애너그램 테이블의 인덱스와 값의 반대 방향으로 문자열의 순서를 바꿔주면 됩니다.

# 예를들어 암호화된 문자열이 "lleoH"이고 애너그램 테이블이 [4, 2, 0, 1, 3]이면, 애너그램 테이블의 0번째 값인 4에 해당하는 문자인 'H'는 해당 인덱스인 0번째로 이동하고 같은 방식으로 'e'는 1번째로, 'l'은 2번째로, 'l'은 3번째로, 'o'는 4번째로 이동하여 "Hello"가 됩니다.

# 암호화할 문자열 text와 애너그램 테이블 anagram, 암호화를 할지 복호화를 할지가 저장된 변수 sw가 주어질 때 암호화 또는 복호화된 문자열을 return하도록 solution함수를 완성해 보세요.

# 제한 사항
# 5 ≤ text의 길이 = anagram의 길이 ≤ 50
# text는 대문자와 소문자 알파벳으로 이루어진 문자열 입니다.
# 0 ≤ anagram의 원소 < text의 길이
# anagram의 원소는 중복되지 않습니다.
# sw는 True또는 False입니다.
# sw가 True이면 암호화, False이면 복호화를 해야합니다.

def solution12(text, anagram, sw):
    result = [""] * len(text)
    if sw:
        for i, v in enumerate(anagram):
            result[v] = text[i]
    else:
        for i, v in enumerate(anagram):
            result[i] = text[v]
            
    return "".join(v for v in result)

#---------------------------------------------------------------------------------------------------------------------------------------

# [PCCP 모의고사 #1] 외톨이 알파벳
# 문제 설명
# 알파벳 소문자로만 이루어진 어떤 문자열에서, 2회 이상 나타난 알파벳이 2개 이상의 부분으로 나뉘어 있으면 외톨이 알파벳이라고 정의합니다.

# 문자열 "edeaaabbccd"를 예시로 들어보면,

# a는 2회 이상 나타나지만, 하나의 덩어리로 뭉쳐있으므로 외톨이 알파벳이 아닙니다.
# "ede(aaa)bbccd"
# b, c도 a와 같은 이유로 외톨이 알파벳이 아닙니다.
# d는 2회 나타나면서, 2개의 부분으로 나뉘어 있으므로 외톨이 알파벳입니다.
# "e(d)eaaabbcc(d)"
# e도 d와 같은 이유로 외톨이 알파벳입니다.
# 문자열 "eeddee"를 예시로 들어보면,

# e는 4회 나타나면서, 2개의 부분으로 나뉘어 있으므로 외톨이 알파벳입니다.
# "(ee)dd(ee)"
# d는 2회 나타나지만, 하나의 덩어리로 뭉쳐있으므로 외톨이 알파벳이 아닙니다.
# "ee(dd)ee"
# 문자열 input_string이 주어졌을 때, 외톨이 알파벳들을 알파벳순으로 이어 붙인 문자열을 return 하도록 solution 함수를 완성해주세요. 만약, 외톨이 알파벳이 없다면 문자열 "N"을 return 합니다.

# 제한사항
# 1 ≤ input_string의 길이 ≤ 2,600
# input_string은 알파벳 소문자로만 구성되어 있습니다.

def solution13(input_string):
    result = []
    result_dic = {}
    for i, v in enumerate(input_string):
        if v not in result_dic:
            result_dic[v] = 1
        else:
            result_dic[v] += 1
        
        if i == 0:
            continue
            
        if result_dic[v] > 1 and input_string[i] != input_string[i-1]:
            result.append(v)
            
    if len(result) == 0:
        return "N"
    else:
        return "".join(i for i in set(sorted(result)))

#----------------------------------------------------------------------------------------------------------------------------------

# 특정 문자열로 끝나는 가장 긴 부분 문자열 찾기

# 문제 설명
# 문자열 myString과 pat가 주어집니다. myString의 부분 문자열중 pat로 끝나는 가장 긴 부분 문자열을 찾아서 return 하는 solution 함수를 완성해 주세요.

# 제한사항
# 5 ≤ myString ≤ 20
# 1 ≤ pat ≤ 5
# pat은 반드시 myString의 부분 문자열로 주어집니다.
# myString과 pat에 등장하는 알파벳은 대문자와 소문자를 구분합니다.

def solution14(myString, pat):
    result = ""
    for i in range(0, len(myString) - len(pat) + 1):
        if myString[i:i + len(pat)] == pat:
            result = myString[:i + len(pat)]
    
    return result

#------------------------------------------------------------------------------------------------------------------------------------------------

# 누워서 읽는 알고리즘 p64 문제 1

# 99개의 값을 저장할 수 있는 배열 item[0], item[1], ... item[98]이 있다.
# 1부터 100까지의 값이 들어 있는 집합 {1, 2, ... 100}에서 무작위로 수를 꺼내서 저장했다.

# 집합에 들어있는 원소의 수는 100개 인데 반해 배열은 99개의 값을 저장할 수 있으므로 집합안에 하나의 숫자가 남았다.

# 남은것이 어느 수 인지 확인하는 프로그램을 작성하라.


def solution15():
    item = [0] * 99
    for i in range(99):
        item[i] = i + 1

    total = 5050

    for i in item:
        total -= item[i]

    return total


#--------------------------------------------------------------------------------------------------

# 누워서 읽는 알고리즘 p64 문제 2

# 앞에서 읽으나 뒤에서 읽으나 똑같은 단어를 희문이라고 한다.
# 희문인지 아닌지 여부를 판단하는 함수를 작성하라.

# 입력한 문장이 희문이면 True 아니면 False를 return하라

def solution16(str):
    if str == str[::-1]:
        return True
    else:
        return False
    
print(solution16("adaa"))

#------------------------------------------------------------------------------------------------------------------------------

# 누워서 읽는 알고리즘 p64 문제 3

# 2199년 7월 2일은 무슨 요일인가?

def solution17():
    return

#------------------------------------------------------------------------------------------------------

# 외계어 사전

# 문제 설명
# PROGRAMMERS-962 행성에 불시착한 우주비행사 머쓱이는 외계행성의 언어를 공부하려고 합니다. 알파벳이 담긴 배열 spell과 외계어 사전 dic이 매개변수로 주어집니다. spell에 담긴 알파벳을 한번씩만 모두 사용한 단어가 dic에 존재한다면 1, 존재하지 않는다면 2를 return하도록 solution 함수를 완성해주세요.

# 제한사항
# spell과 dic의 원소는 알파벳 소문자로만 이루어져있습니다.
# 2 ≤ spell의 크기 ≤ 10
# spell의 원소의 길이는 1입니다.
# 1 ≤ dic의 크기 ≤ 10
# 1 ≤ dic의 원소의 길이 ≤ 10
# spell의 원소를 모두 사용해 단어를 만들어야 합니다.
# spell의 원소를 모두 사용해 만들 수 있는 단어는 dic에 두 개 이상 존재하지 않습니다.
# dic과 spell 모두 중복된 원소를 갖지 않습니다.

from itertools import permutations

def solution18(spell, dic):
    
    for permutation in permutations(spell):
        str1 = ''.join(permutation)
        for i in dic:
            if i == str1:
                return 1
            
    return 2

#------------------------------------------------------------------------------------------------------------------------------------------------

# 문자열 밀기

# 문제 설명
# 문자열 "hello"에서 각 문자를 오른쪽으로 한 칸씩 밀고 마지막 문자는 맨 앞으로 이동시키면 "ohell"이 됩니다. 이것을 문자열을 민다고 정의한다면 문자열 A와 B가 매개변수로 주어질 때, A를 밀어서 B가 될 수 있다면 밀어야 하는 최소 횟수를 return하고 밀어서 B가 될 수 없으면 -1을 return 하도록 solution 함수를 완성해보세요.

# 제한사항
# 0 < A의 길이 = B의 길이 < 100
# A, B는 알파벳 소문자로 이루어져 있습니다.

def solution19(A, B):
    count = 0
    for i in range(len(A)):
        if (A[len(A) - i:] + A[:len(A) - i]) == B:
            return count
        
        count += 1
        
    return -1

#------------------------------------------------------------------------------------------------------------------------------

# 치킨 쿠폰

# 문제 설명
# 프로그래머스 치킨은 치킨을 시켜먹으면 한 마리당 쿠폰을 한 장 발급합니다. 쿠폰을 열 장 모으면 치킨을 한 마리 서비스로 받을 수 있고, 서비스 치킨에도 쿠폰이 발급됩니다. 시켜먹은 치킨의 수 chicken이 매개변수로 주어질 때 받을 수 있는 최대 서비스 치킨의 수를 return하도록 solution 함수를 완성해주세요.

# 제한사항
# chicken은 정수입니다.
# 0 ≤ chicken ≤ 1,000,000

def solution20(chicken):
    result = 0
    ticket = 0
    while(chicken >= 10):
        result += chicken // 10
        ticket += chicken % 10
        chicken = (chicken // 10)

    ticket += chicken
    while(ticket >= 10):
        result += ticket // 10
        ticket = (ticket % 10) + (ticket // 10)
        
    return result

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 특별한 이차원 배열 1

# 문제 설명
# 정수 n이 매개변수로 주어질 때, 다음과 같은 n × n 크기의 이차원 배열 arr를 return 하는 solution 함수를 작성해 주세요.

# arr[i][j] (0 ≤ i, j < n)의 값은 i = j라면 1, 아니라면 0입니다.
# 제한사항
# 1 ≤ n ≤ 100

def solution21(n):
    result = []
    for i in range(n):
        arr = [0] * n
        arr[i] = 1
        result.append(arr)
        
    return result

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 등수 매기기

# 문제 설명
# 영어 점수와 수학 점수의 평균 점수를 기준으로 학생들의 등수를 매기려고 합니다. 영어 점수와 수학 점수를 담은 2차원 정수 배열 score가 주어질 때, 영어 점수와 수학 점수의 평균을 기준으로 매긴 등수를 담은 배열을 return하도록 solution 함수를 완성해주세요.

# 제한사항

# 0 ≤ score[0], score[1] ≤ 100
# 1 ≤ score의 길이 ≤ 10
# score의 원소 길이는 2입니다.
# score는 중복된 원소를 갖지 않습니다.

def solution22(score):
    result = []
    obj = {}
    rank = []
    for i in score:
        result.append((i[0] + i[1]) / 2)
    
    
    for i, v in enumerate(sorted(result)[::-1]):
        j = 1
        if v not in obj:
            obj[v] = i + j
        else:
            j += 1

    for i in result:
        rank.append(obj[i])
        
    return rank

#------------------------------------------------------------------------------------------------------------------------------

# 특이한 정렬

# 문제 설명
# 정수 n을 기준으로 n과 가까운 수부터 정렬하려고 합니다. 이때 n으로부터의 거리가 같다면 더 큰 수를 앞에 오도록 배치합니다. 정수가 담긴 배열 numlist와 정수 n이 주어질 때 numlist의 원소를 n으로부터 가까운 순서대로 정렬한 배열을 return하도록 solution 함수를 완성해주세요.

# 제한사항

# 1 ≤ n ≤ 10,000
# 1 ≤ numlist의 원소 ≤ 10,000
# 1 ≤ numlist의 길이 ≤ 100
# numlist는 중복된 원소를 갖지 않습니다.

def solution23(numlist, n):
    arr1 = []
    result = []
    for i in numlist:
        arr1.append(i - n)
        
    arr2 = list(map(abs, arr1))
    
    for i in sorted(arr2):
        if n + i in numlist:
            result.append(n + i)
            numlist.remove(n + i)
        else:
            result.append(n - i)
            numlist.remove(n - i)
            
    return result

#------------------------------------------------------------------------------------------------------------------------------

# 연속된 수의 합

# 문제 설명
# 연속된 세 개의 정수를 더해 12가 되는 경우는 3, 4, 5입니다. 두 정수 num과 total이 주어집니다. 
# 연속된 수 num개를 더한 값이 total이 될 때, 정수 배열을 오름차순으로 담아 return하도록 solution함수를 완성해보세요.

# 2중 반복문 때문에 별로 좋지않음 바꿔보기

def solution24(num, total):
    for j in range(-100, 100):
        result = []
        for i in range(j, j + num):
            result.append(i)
            
        if sum(result) == total:
            return result
        
#--------------------------------------------------------------------------------------------------

# 겹치는 선분의 길이

# 문제 설명
# 선분 3개가 평행하게 놓여 있습니다. 
# 세 선분의 시작과 끝 좌표가 [[start, end], [start, end], [start, end]] 형태로 들어있는 2차원 배열 lines가 매개변수로 주어질 때, 
# 두 개 이상의 선분이 겹치는 부분의 길이를 return 하도록 solution 함수를 완성해보세요.

def solution25(lines):
    result = [0] * 200
    count = 0
    for i in lines:
        for j in range(i[0] + 100, i[1] + 100):
            result[j] += 1
    
    for i in result:
        if i >= 2:
            count += 1
            
    return count

#-----------------------------------------------------------------------------

# 저주의 숫자 3

# 문제 설명
# 3x 마을 사람들은 3을 저주의 숫자라고 생각하기 때문에 3의 배수와 숫자 3을 사용하지 않습니다. 3x 마을 사람들의 숫자는 다음과 같습니다.

# 정수 n이 매개변수로 주어질 때, n을 3x 마을에서 사용하는 숫자로 바꿔 return하도록 solution 함수를 완성해주세요.

# 고치기

def solution26(i):
    for n in range(1, 20):
        print(n)
        answer = n + (n // 3)
        if answer % 3 == 0:
            answer += 1

        def isInThree(i):
            for n in str(i):
                if n == "3":
                    return True

            return False
        print(f"전 answer = {answer}")

        while(isInThree(answer)):
            answer += 1
        
        print(f"후 answer = {answer}")
        
    return answer


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
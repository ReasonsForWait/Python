# 개수 세기

# 문제
# 총 N개의 정수가 주어졌을 때, 정수 v가 몇 개인지 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 정수의 개수 N(1 ≤ N ≤ 100)이 주어진다. 둘째 줄에는 정수가 공백으로 구분되어져있다. 
# 셋째 줄에는 찾으려고 하는 정수 v가 주어진다. 입력으로 주어지는 정수와 v는 -100보다 크거나 같으며, 100보다 작거나 같다.

n = int(input())

numbers = list(map(int, input().split()))
target = int(input())
result = 0

for i in numbers:
    if i == target:
        result += 1
  
print(result)

#-------------------------------------------------------------------------------------

# X보다 작은 수

# 문제
# 정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N과 X가 주어진다. (1 ≤ N, X ≤ 10,000)

# 둘째 줄에 수열 A를 이루는 정수 N개가 주어진다. 주어지는 정수는 모두 1보다 크거나 같고, 10,000보다 작거나 같은 정수이다.

n, x = list(map(int, input().split()))
numbers = list(map(int, input().split()))
result = []

for i in numbers:
    if i < x:
        result.append(i)

result1 = " ".join(str(e) for e in result)
print(result1)

#--------------------------------------------------------------

# 최소, 최대

# 문제
# N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 정수의 개수 N (1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄에는 N개의 정수를 공백으로 구분해서 주어진다. 
# 모든 정수는 -1,000,000보다 크거나 같고, 1,000,000보다 작거나 같은 정수이다.

n = int(input())
numbers = list(map(int, input().split()))

print(f"{min(numbers)} {max(numbers)}")

#----------------------------------------------------------------------------

# 최댓값

# 문제
# 9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.

# 예를 들어, 서로 다른 9개의 자연수

# 3, 29, 38, 12, 57, 74, 40, 85, 61

# 이 주어지면, 이들 중 최댓값은 85이고, 이 값은 8번째 수이다.

# 입력
# 첫째 줄부터 아홉 번째 줄까지 한 줄에 하나의 자연수가 주어진다. 주어지는 자연수는 100 보다 작다.

numbers = []

for i in range(0, 9):
    numbers.append(int(input()))

print(max(numbers))
print(numbers.index(max(numbers)) + 1)
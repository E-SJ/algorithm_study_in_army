n,m,k = map(int, input().split())
nums = list(map(int,input().split()))
nums.sort(reverse=True)
max=nums[0]
min=nums[1]

full_num=m//(k+1) #반복되는 max*k + min 합의 반복 횟수
rest_num=m%(k+1) #나머지 합의 반복 횟수

result = (max*k+min)*full_num + max*rest_num

print(result)

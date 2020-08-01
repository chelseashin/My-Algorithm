user_input = "[(-))]"
user_input = list(user_input)
N = len(user_input)
S = []
for i in range(N):
    if len(S) == 0:
        S.append(user_input[i])
    else:
        if user_input[i] == '-':
            user_input[i] = user_input[i-1]
        elif user_input[i] == '+':
            for j in range(i+1, N):
                if user_input[j] != '+':
                    user_input[i] = user_input[j]
                    break
        if S[-1] == '(':
            if user_input[i] == ')':
                S.pop()
            else:
                S.append(user_input[i])
        elif S[-1] == '{':
            if user_input[i] == '}':
                S.pop()
            else:
                S.append(user_input[i])
        elif S[-1] == '[':
            if user_input[i] == ']':
                S.pop()
            else:
                S.append(user_input[i])
        else:
            S.append(user_input[i])
if len(S):
    print(False)
else:
    print(True)
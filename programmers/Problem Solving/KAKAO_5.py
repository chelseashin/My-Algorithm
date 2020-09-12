play_time = "02:03:55"
adv_time = "00:14:15"
logs = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]

def solution(play_time, adv_time, logs):
    answer = ''
    hour, minute, second = map(int, play_time.split(":"))
    print(hour, minute, second)
    visited = [[[0] * 60, [0] * 60] for _ in range(hour+2)]
    print(visited)
    for log in logs:
        start, end = log.split("-")
        sh, sm, ss = map(int, start.split(":"))
        eh, em, es = map(int, end.split(":"))
        
        print(sh, sm, ss, eh, em, es)
    return answer

print(solution(play_time, adv_time, logs))
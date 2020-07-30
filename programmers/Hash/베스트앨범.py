genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

def solution(genres, plays):
    genre_dic = {}
    genre_total_play = {}

    for i in range(len(genres)):
        # 새로운 장르 추가
        if genres[i] not in genre_dic.keys():
            genre_dic[genres[i]] = [(plays[i], i)]
            genre_total_play[genres[i]] = plays[i]
        # 기존에 있다면
        else:
            genre_dic[genres[i]].append((plays[i], i))
            genre_total_play[genres[i]] += plays[i]
    # print(genre_dic)
    # print(genre_total_play)
    sorted_total_play = sorted(genre_total_play.items(), key=lambda x: x[1], reverse=True)
    # print(sorted_total_play)
    answer = []
    for key, value in sorted_total_play:
        play_list = genre_dic[key]
        play_list = sorted(play_list, key=lambda x: (-x[0], x[1]))
        for i in range(len(play_list)):
            if i == 2:
                break
            answer.append(play_list[i][1])
    # print(play_list)
    return answer
print(solution(genres, plays))
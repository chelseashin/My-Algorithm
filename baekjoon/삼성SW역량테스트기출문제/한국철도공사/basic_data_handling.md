```R
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
# Lecture: Basic Data Analysis                           #
#                                                        #
# Author : Chaewon Shin                                  #
# Date : October 06th, 2020                              #
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#



# 패키지 설치 및 로딩하기
install.packages("ggplot2") # 실행하지 않아도 코드에 넣기
install.packages("RColorBrewer")
install.packages("prettyR")
install.packages("e1071")
install.packages("psych")
install.packages("dplyr")
install.packages("funModeling")
install.packages("writexl")
install.packages("data.table")
library(ggplot2)
library(RColorBrewer)
library(prettyR)
library(e1071)
library(psych)
library(dplyr)
library(funModeling)
library(writexl)
library(data.table)


# 작업공간
setwd("c:/R/FastCampus/")


# 데이터 불러오기
# ggplot2::diamonds


# 질적 자료: cut, color, clarity
# 양적 자료: carat, depth, table, price, x, y, z



# 1. 일변량(Uni-variate): 질적 자료의 분석 ----
# 1.1 표 = 빈도표(Frequency Table) ----
# (1) 빈도(Frequency) ----
# table(data$variable) : 해당된 데이터 자료의 개수 = 빈도
table(diamonds$cut)
table(diamonds$color)
table(diamonds$clarity)
# 실전에서는 가장 많은 것부터 차례대로 = 내림차순
sort(table(diamonds$cut) , decreasing = TRUE )
sort(table(diamonds$color) , decreasing = TRUE)
sort(table(diamonds$clarity) , decreasing = TRUE)

for(i in 2:4){
  print(sort(table(diamonds[ , i]) , decreasing = TRUE))
}



# (2) 백분율(Percent) = (빈도/합계) * 100(%) ----
# prop.table(frequency)*100
prop.table(table(diamonds$cut)) *100
# 비율은 0-1
sort(prop.table(table(diamonds$cut)) *100 , decreasing = TRUE )
# 백분율은 관례로 소수점을 하나까지만 표현 = round( , digit = )
round(sort(prop.table(table(diamonds$cut)) *100 , decreasing = TRUE ), digits = 1)


# 문제1. 각 질적 자료에 대해서 빈도와 백분율을 구하라. (for문 이용)

for(i in c("cut", "color", "clarity")){
  print(sort(table(diamonds[ , i]) , decreasing = TRUE))
  print(round(sort(prop.table(table(diamonds[ , i])) *100 , decreasing = TRUE ), digits = 1))
}


# 1.2 그래프(Graph) ----
# (1) 막대그래프(Bar Chart) ----
#barplot(frequency or percent)
barplot(sort(table(diamonds$cut) , decreasing = TRUE))

# 막대 색: col = "color"
barplot(sort(table(diamonds$cut) , decreasing = TRUE), 
        col = "pink")

barplot(sort(table(diamonds$cut) , decreasing = TRUE), 
        col = "aquamarine")

barplot(sort(table(diamonds$cut) , decreasing = TRUE), 
        col = c("aquamarine", "pink", "red", "tan1", "black"))

# 패키지 이용 그라데이션으로 바꾸기
color.palatte <- RColorBrewer::brewer.pal(n = 5, name = "BuGn")
barplot(sort(table(diamonds$cut) , decreasing = TRUE), 
        col = color.palatte)

# 차트 제목: main = "title"
barplot(sort(table(diamonds$cut) , decreasing = TRUE), 
        col  = "aquamarine",
        main = "Cut of Diamonds")

# y축 제목: ylab = "y's axis title" -> 차트 제목은 안 달아도, y축 제목은 필수
# ylab    : y label의 약자
barplot(sort(table(diamonds$cut) , decreasing = TRUE), 
        col  = "aquamarine",
        main = "Cut of Diamonds",
        ylab = "Frequency")

# y축 눈금: ylim = c(min, max) -> min은 0으로
# ylim    : y limit의 약자
barplot(sort(table(diamonds$cut) , decreasing = TRUE), 
        col  = "aquamarine",
        main = "Cut of Diamonds",
        ylab = "Frequency",
        ylim = c(0, 25000))

# 가로 막대 그래프: horiz = TRUE
# horiz           : horizontal의 약자
barplot(sort(table(diamonds$cut) , decreasing = FALSE), 
        col   = "aquamarine",
        main  = "Cut of Diamonds",
        xlab  = "Frequency",
        xlim  = c(0, 25000),
        horiz = TRUE)

# 문제2. for문으로 3개의 질적 자료에 대한 가로 막대 그래프 작성

for(i in 2:4){
  barplot(sort(table(diamonds[ , i]) , decreasing = FALSE), 
          col   = "aquamarine",
          main  = "Cut of Diamonds",
          xlab  = "Frequency",
          xlim  = c(0, 25000),
          horiz = TRUE)
}

# 하나로 묶기 -> 결과는 character
paste("Love", "is", "choice.") # 기본적으로 사이에 space 있음
paste(1, 1, 1)

paste("Love", "is", "choice.", sep = "-")

# 문제3. paste를 이용하여 Var1, Var2, ... , Var100 완성
paste("Var", 1:100, sep = "")
# 변수명 혹은 이름을 지을 때, 상당히 유용


# 그래프의 제목을 그에 맞게 바꾸고 싶다면
paste(colnames(diamonds)[i], "of Diamonds")


for(i in 2:4){
  barplot(sort(table(diamonds[ , i]) , decreasing = FALSE), 
          col   = "aquamarine",
          main  = paste(colnames(diamonds)[i], "of Diamonds"),
          xlab  = "Frequency",
          xlim  = c(0, 25000),
          horiz = TRUE)
}

# 
v1 <- "Love is choice."
toupper(v1) # 대문자
tolower(v1) # 소문자
casefold(v1, upper = TRUE)


# 그래프 화면 분할하기
# 기본적으로 하나의 그래픽 화면에 하나의 그래프만 출력
# par(mfrow = c(nrow, ncol)) : 행부터 그래프를 채움
# par(mfcol = c(nrow, ncol)) : 열부터 그래프를 채움

par(mfrow = c(3, 1))
for(i in 2:4){
  barplot(sort(table(diamonds[ , i]) , decreasing = FALSE), 
          col   = "aquamarine",
          main  = paste(colnames(diamonds)[i], "of Diamonds"),
          xlab  = "Frequency",
          xlim  = c(0, 25000),
          horiz = TRUE)
}

# 그래프 화면 원상태로 돌리기
# par(mfrow = c(1,1))
par(mfrow = c(1, 1))



# (2) 원그래프(Pie Chart) ----
# pie(frequency or percent)
pie(sort(table(diamonds$cut) , decreasing = TRUE))

# 반지름: radius = 0.8
pie(sort(table(diamonds$cut) , decreasing = TRUE),
    radius = 1)

# 시계방향: clockwise = TRUE
pie(sort(table(diamonds$cut) , decreasing = TRUE),
    radius = 1,
    clockwise = TRUE)

# 첫째 조각의 시작 각도 
# init.angle = 0  : 반시계방향
# init.angle = 90 : 시계방향
pie(sort(table(diamonds$cut) , decreasing = TRUE),
    radius = 1,
    clockwise = TRUE,
    init.angle = 0)


# 문제4. 그래픽 화면을 3행 2열로 분할하고, 
# 각 행에 각 질적 자료의 막대그래프, 원그래프가 출력 되도록 해라
par(mfrow = c(3, 2))

for(i in 2:4){
  barplot(sort(table(diamonds[ , i]) , decreasing = TRUE), 
          col   = "aquamarine",
          main  = paste(colnames(diamonds)[i], "of Diamonds"),
          ylab  = "Frequency",
          ylim  = c(0, 25000))
  
  pie(sort(table(diamonds[ ,i]) , decreasing = TRUE),
      radius = 1,
      clockwise = TRUE,
      init.angle = 0,
      main  = paste(colnames(diamonds)[i], "of Diamonds"))
}

par(mfrow = c(1, 1))


# pdf 파일에 그래프 저장하기
# pdf(file = "directory/filename.pdf") : 저장 시작
# 그래프 작업
# dev.off() : 저장 끝
# dev : graphic device의 약자

pdf(file = "graphics.pdf")

for(i in 2:4){
  barplot(sort(table(diamonds[ , i]) , decreasing = TRUE), 
          col   = "aquamarine",
          main  = paste(colnames(diamonds)[i], "of Diamonds"),
          ylab  = "Frequency",
          ylim  = c(0, 25000))
  
  pie(sort(table(diamonds[ ,i]) , decreasing = TRUE),
      radius = 1,
      clockwise = TRUE,
      init.angle = 0,
      main  = paste(colnames(diamonds)[i], "of Diamonds"))
}

dev.off()

# 한 페이지에 여러 그래프

pdf(file = "graphics2.pdf")
par(mfrow = c(3, 2))
for(i in 2:4){
  barplot(sort(table(diamonds[ , i]) , decreasing = TRUE), 
          col   = "aquamarine",
          main  = paste(colnames(diamonds)[i], "of Diamonds"),
          ylab  = "Frequency",
          ylim  = c(0, 25000))
  
  pie(sort(table(diamonds[ ,i]) , decreasing = TRUE),
      radius = 1,
      clockwise = TRUE,
      init.angle = 0,
      main  = paste(colnames(diamonds)[i], "of Diamonds"))
}
dev.off()




# 2. 일변량 양적 자료 분석 ----
# 2.1 표 = 빈도표 : 구간의 빈도, 백분율 ----
# 성별은 두개의 값으로 나뉘지만, 키는 사람마다 다르기 때문에 구간을 만들어야 함
# 양적 자료 -> 질적 자료는 cut, 그러면 factor로 변해서 그걸로 구간 명명
diamonds$price.group <- cut(diamonds$price,
                            breaks = seq(from = 0, to = 20000, by = 5000),
                            right = FALSE)

table(diamonds$price.group)
sort(table(diamonds$price.group), decreasing = TRUE)

prop.table(table(diamonds$price.group)) * 100
sort(prop.table(table(diamonds$price.group)) * 100, decreasing = TRUE)
round(sort(prop.table(table(diamonds$price.group)) * 100, decreasing = TRUE), 1)


# 범위
# diff(range(data$variable))
# 문제5. carat에 대한 빈도/백분율 구하기


head(diamonds$carat)

interval.count <- 1 + 3.3 * log10(length(diamonds$carat)) #구간 개수
carat.range <- diff(range(diamonds$carat)) # 범위
interval.width <- carat.range / interval.count

min(diamonds$carat)
max(diamonds$carat)

diamonds$carat.group <- cut(diamonds$carat,
                            breaks = seq(from = 0, to = 5.1, by = 0.3),
                            right = FALSE)

table(diamonds$carat.group)
sort(table(diamonds$carat.group), decreasing = TRUE)

prop.table(table(diamonds$carat.group)) *100 # 백분율
sort(prop.table(table(diamonds$carat.group)) *100, decreasing = TRUE)
round(sort(prop.table(table(diamonds$carat.group)) *100, decreasing = TRUE), digits = 1)


# 2.2 그래프 ----
# (1) 히스토그램(Histogram) ----
# hist(data$variable, breaks = )
hist(diamonds$price,
     xlim = c(0, 20000))
# hist()안에, 1 + 3.3 * log10(n)이란 알고리즘이 들어사서 자동으로 1000단위로 나뉨. 
# - 기본값: Sturge's formular

hist(diamonds$price,
     xlim = c(0, 20000),
     breaks = seq(from = 0, to = 20000, by = 500))

hist(diamonds$price,
     xlim = c(0, 20000),
     breaks = 20) # 20개 근처로 구간을 만들어라 = 구간의 개수


# (2) 상자그림(Boxplot) ----
# 목적: 양적 자료의 이상치 파악
# boxplot(data$variable, range = 1.5, horizontal = ) : range 1.5가 기본값
boxplot(diamonds$price)
boxplot(diamonds$price, horizontal = TRUE)

age <- c(30, 28, 25, 24, 25, 24, 24, 24, 25, 23)
boxplot(age)

# 집단별로 상자그림 그리기
# boxplot(data$variable ~ data$variable)
# boxplot(양적 자료 ~ 질적 자료)
boxplot(diamonds$price ~ diamonds$cut) # cut의 price값
boxplot(diamonds$price ~ diamonds$color) 
boxplot(diamonds$price ~ diamonds$clarity)

par(mfrow = c(3,1))
for(i in c("cut", "color", "clarity")){
  boxplot(as.formula(paste0("price ~ ", i)), data = diamonds)
}
# paste0은 공백이 없음
par(mfrow = c(1,1))


# 참고: IQR(Inter Quartile Range) = 사분위 범위

price.boxplot <- boxplot(diamonds$price)
price.boxplot
# $status가 min, 사분위수, max; $out이 이상치
length(price.boxplot$out) #이상치 개수
min(price.boxplot$out)
max(price.boxplot$out)
str(price.boxplot)

# 참고
# List의 Slicing
# (1) list[index]
# (2) list[[index]]
# (3) list$variable


# quantile(data$variable): 사분위수
quantile(diamonds$price)
quantile(diamonds$price)[2] # Q1
quantile(diamonds$price)[4] # Q3

quantile(diamonds$price)[2] - 1.5*IQR(diamonds$price) # 마이너스의 이상치 기준
quantile(diamonds$price)[4] + 1.5*IQR(diamonds$price) # 큰 쪽의 이상치 기준



# 2.3 기술통계량 = 요약통계량 ----
# (1) 중심 = 대표값 ----
# 특징: 원본과 샘플이 비슷해야 함
# 평균, 절사평균, 중위수(중앙값), 최빈수(최빈값)
# 양적인 자료의 값들을 대표해 주는 값을 구해야 함

# i. 평균 = 전체값의 합 / 자유도(df = degree of freedom) ----
# 1, 2, 8, 9, = > 평균 = 5
# 1, 2, 8, 89 = > 평균 = 25
# R에서는 모든 데이터를 다 보지 못한 채 대표값을 구하기 때문에, 이를 통해 전체 데이터를 봐야함. 
# 1, 2, 8, 989 => 평균 = 250
# 실제 데이터랑 차이가 많이 남, 평균은 대표값으로의 역할을 잘 못함
# 평균은 아주 작은 값과 아주 큰 값에 영향을 많이 받음 = outlier

# mean(data$variable, na.rm = TRUE)
mean(diamonds$carat)
# outlier가 없다는 가정 하에, 
# 대부분의 데이터가 0.8과 비슷하지 않을까? 라고 추측 가능

# missing value를 처리하는 방법: 
# 1. 제거 2. imputation(대체) : 평균 or 중위수
# - 예측력 or 분류를 더 높여준다면 그게 맞는 방법
# - 항상 그 방법이 통하리란 법은 없음, 그에 맞는 가장 좋은 방법 찾기!
age <- c(10, NA, 20, 30)
mean(age)                 # 결과: NA
mean(age, na.rm = TRUE)   # 결과: 20 (NA를 빼고 3으로 나눔)

# ii. 5% 절사평균(5% Trimmed Mean) = 절단된 평균 ----
# Min ---------- Max로 정렬한 후,
# Min과 Max 값을 잠시 뺌 (outlier 처리)
# 나머지 데이터에서 평균을 구한 것을 절사(절삭) 평균이라 함
# 가장 많이 쓰이는 것이 5% 절사평균 (가장 작은 쪽 5%, 가장 큰 쪽 5%를 뺀 값)
# 평균이 outlier에 영향을 많이 받으니까 채택한 방법

# 만약 평균이 200, 5% 절사평균이 20일 경우, 
# 알 수 있는 것 : outlier가 큰 쪽에 존재한다.
#               : 평균은 쓰지 않고, 절사 평균을 대표값으로 사용
#               : 원본 데이터는 절사평균과 비슷 할 것
# "경영자 마인드"로 이를 활용하여 어떻게 하면 기업에 더 도움이 될까,
#                                 돈을 많이 벌거나, 절약하는 방법 생각하기
# 만약 평균이 200, 5%절이 198이라면,
# outlier가 없는 것으로 존재하며, 별 차이 없으니 평균을 쓴다. 
# 그렇다면, '내가 보지 못한 데이터'는 200과 비슷하지 않을까를 추론할 수 있음

# mean(data$variable, trim = 0.05, na.rm = TRUE)
mean(diamonds$carat, trim = 0.05)
# 그냥 평균 0.8, 절사평균 0.76 => 이상치가 없는 것으로 판단
# 평균을 데이터의 대표값으로 설정, 다이아몬드의 carat은 0.8과 비슷할 것
# gaslighterfe?? : 내가 본 것이 다 인 줄 아는 착각
# 일부의 데이터만 보고 전체를 판단하는 선입견, 항상 주의해야 함


# iii. 중위수(Median) ----
# 1, 1, 3, 7, 10 => 중위수 = 3
# 1, 2, 8, 9     => 중위수 = 5
# 1, 2, 8, 89    => 중위수 = 5
# 특징. 평균보다 이상치의 영향을 덜 받음

# median(data$variable, na.rm = TRUE)
median(diamonds$carat)
# 평균, 중앙값, 중위수 모두 비슷한 값. 
# 중위수는 이상치에 영향을 더 받기 때문에, 현재로썬 0.76사용이 현명할 듯


# iv. 최빈수(Mode) ----
# 1, 1, 2, 2, 2, 3, 4
# 1: 2개, 2: 3개, 3: 1개, 4: 1개
# 그래서 우리가 보지 못한 데이터는 2와 비슷하지 않을까? 라는 생각
# 1, 1, 1, 2, 2, 2, 2, 3, 4
# 최빈값 : 1과 2
# 1, 2, 3, 4
# 최빈값 없음. 최빈수는 두 개 이상이 존재할 때만 존재. 

# which.max(table(data$variable))
# prettyR::Mode(data$variable)

money <- c(30, 50, 30, 50, 100, 30, 200, 40, 40)
table(money)

which.max(c(10, 20, 200, 50))
which.max(table(money)) # names와 위치를 알려줌

which.max(table(diamonds$carat))
prettyR::Mode(diamonds$carat)


# (2) 퍼짐 = 산포 = 다름 ----
# 데이터 분석에서 가장 중요한 것은 "다름"
# - 데이터를 보고 생각해야 할 3가지
# 내가 관심있는 데이터, 집단에 "다름"이 얼마나 있을까?를 수량화 해야함
# 이 "다름"은 무시해도 될만한가? 아님 의미를 둬야 하나?
# 이 "다름"은 왜 발생했는가? ***

# i. 범위(Range) : 최대값 - 최소값 ----
#           중심 |  평균  중위수  최빈수 | 범위
# A : 1, 2, 8, 9 |   5      5      x     |  8
# B : 3, 4, 6, 7 |   5      5      x     |  4
# C : 5, 5, 5, 5 |   5      5      5     |  0
# 범위가 작을 수록, 데이터가 비슷함
# 가장 비슷한 것: C
# 가장 다른 것: A (범위가 가장 많이 차이나서)

#     Q1  중 Q3                   사분위범위(IQR)
#   |  |  |  |  |    범위   중위수
# A : 1, 2, 8, 9   |  8   |  6
# B : 3, 4, 6, 89  |  88  |  6
# C : 5, 5, 5, 989 |  988 |  6
# 범위는 이상치에 영향을 상당히 많이 받음
# 범위와 사분위범위와 비슷하다면, 이상치가 없다는 것, 
# 범위가 데이터에서 작다고 느껴지면 데이터에 다름이 별로 없다는 것,
# 크다고 느껴진다면, 데이터에 다름이 크다는 것.

# diff(range(data$variable))
range(diamonds$carat)     # numeric vector
range(diamonds$carat)[1]  # 최소값
range(diamonds$carat)[2]  # 최대값

diff(c(0.2, 5.01))
# 시계열 데이터에서 중요
diff(range(diamonds$carat))

# ii. 사분위범위 = 사분위수범위 = IQR(Inter Quartile Range) ----
# IQR(data$variable)
IQR(diamonds$carat)
# 범위와 IQR의 차이가 많이 나기 때문에, 이상치가 있다고 판단

# iii. (표본)분산(Variance) ----
# var(data$variable)
var(diamonds$carat)
# 단위가 있어서 해석이 어려움

# iv. (표본)표준편차(SD: Standard Deviation) ----
# sd(data$variable)
sd(diamonds$carat)
# 평균 8과 0.47정도 차이 남

# v. 중위수 절대편차(MAD: Median Absolute Deviation) ----
# mad(data$variable)
mad(diamonds$carat)
# 중위수와 표준편차가 별로 차이가 안나기 때문에, 이상치가 없다고 판단


# (3) 분포의 모양 ----
# i. 왜도(Skweness)
# 대칭 여부를 알려줌
# e1071::skewness(data$variable)
e1071::skweness(diamonds$carat)

# ii. 첨도(Kurtosis)
# 중심이 얼마나 뾰족한가
# e1071::kurtosis(data$variable)
e1071::kurtosis(diamonds$carat)

hist(diamonds$carat)


# (4) 기타 ----
# i. 최소값(Min)
# min(data$variable)
min(diamonds$carat)

# ii. 최대값(Max)
# max(data$variable)
max(diamonds$carat)

# 강을 건너고 싶은 군대가 있다면, 
# 강은 최대수심(max), 군대는 키가 가장 작은 사람(min)을 구해야 함. 



# 2.4 기술통계량을 구해주는 유용한 함수들 ----
# (1) summary(data$variable)
summary(diamonds$carat)
# 평균을 제외한 5개의 값: 다섯수치요약(Five Numbers summary)
# Min, Q1, Median, Q3, Max

# (2) by(data$variable, data$variable, functionName)
# by(양적 자료, 질적 자료, functionName)
# 집단 별로 양적 자료에 대해 처리할 때 사용함
by(diamonds$carat, diamonds$cut, mean)
by(diamonds$carat, diamonds$cut, sd)
by(diamonds$carat, diamonds$cut, summary)
by(diamonds$carat, diamonds$cut, hist)

# (3) psych::describe(), describeBy()
# psych::describe(data$variable)
# psych::describe(data) -> 양적 자료만 slicing해서
psych::describe(diamonds$carat)              # 10% 절사평균
psych::describe(diamonds$carat, trim = 0.05) # 5% 절사평균
psych::describe(diamonds[ , c(1, 5:10)])

# psych::describeBy(data$variable, data$variable)
# psych::describeBy(양적 자료, 질적 자료)
psych::describeBy(diamonds$carat, diamonds$cut)
psych::describeBy(diamonds[ , c(1, 5:10)], diamonds$cut)

# (4) dplyr::summarise()
diamonds %>% 
  dplyr::select(carat) %>% 
  dplyr::summarise(N = n(),
                   Mean = mean(carat),
                   SD   = sd(carat))

diamonds %>% 
  dplyr::select(carat, cut) %>% 
  dplyr::group_by(cut) %>% 
  dplyr::summarise(N = n(),
                   Mean = mean(carat),
                   SD   = sd(carat))
# summarise는 groupby의 뒤에 와야 함

diamonds %>% 
  dplyr::select(carat, cut) %>% 
  dplyr::group_by(cut) %>% 
  dplyr::summarise(N = n(),
                   Mean = mean(carat),
                   SD   = sd(carat)) %>% 
  dplyr::arrange(desc(Mean))
# Mean 내림차순

diamonds %>% 
  dplyr::select(carat, cut) %>% 
  dplyr::group_by(cut) %>% 
  dplyr::summarise(N = n(),
                   Mean = mean(carat),
                   SD   = sd(carat)) %>% 
  dplyr::arrange(desc(Mean)) %>% 
  head(n = 3)
# 위 3번째 줄까지만 자르기


# 문제1. carat이 4.0 이상, price는 10000 이상인 데이터의 depth에 대해서 clarity별로 n, Mean, SD를 구한 결과의 평균을 기준으로 top3를 알아내라. 

diamonds %>% 
  dplyr::filter(carat >= 4.0 & price >= 10000) %>% 
  dplyr::select(depth, clarity) %>% 
  dplyr::group_by(clarity) %>% 
  dplyr::summarise(N = n(),
                   Mean = mean(depth),
                   SD = sd(depth)) %>% 
  dplyr::arrange(desc(Mean)) %>% 
  head(n = 3)

# 열 추가하기
diamonds <- dplyr::mutate(diamonds, xyz.mean = (x + y + z)/3)
View(diamonds)



# dplyr 패키지 정리 ----
# filter    : 행 추출
# select    : 열 추출
# mutate    : 새로운 변수 생성
# summarise : 기술통계량
# group_by  : 집단으로 구분
# arrange   : 정렬
# %>%       : pipe operator 


# (5) funModeling 패키지 ----
funModeling::df_status(diamonds)
funModeling::plot_num(diamonds)
funModeling::profiling_num(diamonds)
funModeling::freq(diamonds$cut)




# 문제1. cut이 "Ideal"인 데이터의 clarity에 대한 빈도, 백분율, 막대 그래프, 원그래프 작성.
# 방법 1
diamonds2 <- diamonds %>% 
  dplyr::filter(cut == "Ideal") %>% 
  dplyr::select(clarity)

sort(table(diamonds2$clarity), decreasing = TRUE) #빈도
round(sort(prop.table(table(diamonds2$clarity))* 100, decreasing = TRUE), digits = 1) #백분율

barplot(sort(table(diamonds2$clarity), decreasing = TRUE))
pie(sort(table(diamonds2$clarity), decreasing = TRUE))

# 방법 2
diamonds3 <- diamonds %>% 
  dplyr::filter(cut == "Ideal") %>% 
  dplyr::select(clarity) %>% 
  table() %>% 
  sort(decreasing = TRUE)

round(prop.table(diamonds3)* 100, digits = 1)
barplot(diamonds3)
pie(diamonds3)



# 분석한 결과를 엑셀로 저장하기
# 엑셀로 저장하기 위해서는 항상 2차원 구조를 가져야함
diamonds3 <- diamonds %>% 
  dplyr::filter(cut == "Ideal") %>% 
  dplyr::select(clarity) %>% 
  table() %>% 
  sort(decreasing = TRUE)


diamonds3 <- as.data.frame(diamonds3)
writexl::write_xlsx(diamonds3,
                    path = "dia3result.xlsx")


result2 <- psych::describe(diamonds[ , c(1, 5:10)])
result2 <- as.data.frame(result2)
writexl::write_xlsx(result2,
                    path = "dia3result2.xlsx")



result3 <- psych::describeBy(diamonds[ , c(1, 5:10)], diamonds$cut)
str(result3)

result3 <- data.table::rbindlist(result3)
str(result3)

writexl::write_xlsx(result3,
                    path = "dia3result3.xlsx")

```



import pandas as pd
from scipy.stats import shapiro, ttest_ind

# CSV 불러오기
df = pd.read_csv("gender_scores.csv")

# 성별에 따라 점수 나누기
female = df[df['성별'] == '여학생']['점수']
male = df[df['성별'] == '남학생']['점수']

# 정규성 검정
print("🔍 Shapiro-Wilk 정규성 검정")
stat_f, p_f = shapiro(female)
stat_m, p_m = shapiro(male)
print("여학생: 통계량 =", stat_f, ", p =", p_f)
print("남학생: 통계량 =", stat_m, ", p =", p_m)

# T-test (양측 검정)
t_stat, p_val_two_tailed = ttest_ind(male, female)

# 단측 검정: 남학생 평균이 더 클 경우만 유의
if t_stat > 0:
    p_val_one_tailed = p_val_two_tailed / 2
else:
    p_val_one_tailed = 1 - (p_val_two_tailed / 2)

print("\n📊 T-test (단측 검정: 남 > 여)")
print("t =", t_stat)
print("p (one-tailed) =", p_val_one_tailed)

# 결과 해석
alpha = 0.05
if p_val_one_tailed < alpha:
    print("→ 귀무가설 기각: 남학생 평균 점수가 여학생보다 유의하게 높다.")
else:
    print("→ 귀무가설 채택: 남학생 평균 점수가 여학생보다 높다고 보기 어렵다.")

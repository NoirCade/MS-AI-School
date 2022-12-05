import numpy as np
# 실행마다 결과 동일하도록 Seed값 부여
np.random.seed(7777)
print(np.random.randint(0, 10, (2, 3)))
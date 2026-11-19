kakao = []
kakao.append("Friend1")
kakao.append("Friend2")
kakao.append("Friend3")
kakao.append("Friend4")
kakao.append("Friend5")
print(kakao)
kakao.append(kakao[4])
print(kakao)
kakao[4] = kakao[3]
print(kakao)
kakao[3] = kakao[2]
print(kakao)